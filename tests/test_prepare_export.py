"""One integration check for the assignment's list-hygiene requirements."""

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "name", "title", "company", "domain", "linkedin_url", "email",
    "verification_status", "qualification_status", "signal", "signal_source",
    "fit_source", "first_line", "first_line_source",
    "email_source",
    "email_domain_ownership_status", "email_domain_ownership_sources",
    "send_ready_hold_reason", "verification_accept_all",
]


class ExportGateTest(unittest.TestCase):
    def test_bad_emails_duplicates_and_suppression(self):
        def lead(name, domain, email, status="valid", qualification="qualified"):
            return {
                "name": name, "title": "Founder", "company": name,
                "domain": domain, "linkedin_url": "https://linkedin.com/in/example",
                "email": email, "verification_status": status,
                "qualification_status": qualification, "signal": "dated case",
                "signal_source": "https://example.com/case",
                "fit_source": "https://example.com/service",
                "first_line": "I saw your client case.",
                "first_line_source": "https://example.com/case",
                "email_source": "",
            }

        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            folder = Path(directory)
            leads = folder / "leads.csv"
            suppression = folder / "suppression.csv"
            with leads.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS)
                writer.writeheader()
                rows = [
                    lead("Keep", "keep.com", "a@keep.com"),
                    lead("Duplicate email", "keep.com", "A@KEEP.COM"),
                    lead("Duplicate domain", "keep.com", "b@keep.com"),
                    lead("Suppressed email", "other.com", "c@other.com"),
                    lead("Suppressed domain", "blocked.com", "d@blocked.com"),
                    lead("Public Partner", "alternate-domain.com", "p@alternate-domain.com"),
                    lead("Invalid", "invalid.com", "e@invalid.com", "invalid"),
                    lead("Catch-all", "review.com", "f@review.com", "catch_all"),
                    lead("Uncertain signal", "uncertain.com", "g@uncertain.com", qualification="uncertain"),
                    lead("Unattributed alternate", "site.example", "h@other.example"),
                ]
                alternate = lead("Attributed alternate", "website.example", "i@sending.example")
                alternate["email_source"] = "Named finder lookup using website.example"
                rows.append(alternate)
                proven = lead("Proven alternate", "group.example", "j@subsidiary.example")
                proven.update(email_source="Named finder lookup", email_domain_ownership_status="proven",
                              email_domain_ownership_sources="https://group.example/about", verification_accept_all="true")
                rows.append(proven)
                no_proof = lead("Claim without proof", "claim.example", "k@alias.example")
                no_proof.update(email_source="Named finder lookup", email_domain_ownership_status="proven")
                rows.append(no_proof)
                bad_proof = lead("Bad proof URL", "badproof.example", "l@alias2.example")
                bad_proof.update(email_source="Named finder lookup", email_domain_ownership_status="proven",
                                 email_domain_ownership_sources="not a URL")
                rows.append(bad_proof)
                held = lead("Identity hold", "hold.example", "m@hold.example")
                held["send_ready_hold_reason"] = "Exact address not corroborated"
                rows.append(held)
                suppressed_alias = lead("Suppressed alias", "public.example", "n@blocked.com")
                suppressed_alias.update(email_source="Named finder lookup", email_domain_ownership_status="proven",
                                        email_domain_ownership_sources="https://public.example/about")
                rows.append(suppressed_alias)
                writer.writerows(rows)
            with suppression.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["type", "value", "reason"])
                writer.writeheader()
                writer.writerows([
                    {"type": "email", "value": "c@other.com", "reason": "opted out"},
                    {"type": "domain", "value": "blocked.com", "reason": "account suppression"},
                    {"type": "company", "value": "Public-Partner", "reason": "public partner"},
                ])

            subprocess.run(
                [sys.executable, str(ROOT / "scripts/prepare_export.py"), str(leads),
                 "--suppression", str(suppression)],
                check=True, capture_output=True, text=True,
            )
            audit = json.loads((folder / "audit.json").read_text(encoding="utf-8"))
            self.assertEqual(audit["qualified_rows"], 7)
            self.assertEqual(audit["send_ready_rows"], 2)
            self.assertEqual(audit["review_parked_rows"], 5)
            self.assertTrue(audit["research_reconciles"])
            self.assertEqual(audit["alternate_email_domain_rows"], 4)
            self.assertEqual(audit["alternate_email_domain_review_rows"], 3)
            self.assertEqual(audit["excluded_reasons"], {
                "duplicate_email": 1, "duplicate_domain": 1, "suppressed": 4,
                "invalid_email": 1, "qualification_uncertain": 1,
                "alternate_email_domain_without_source": 1,
            })
            with (folder / "send-ready.csv").open(newline="", encoding="utf-8") as handle:
                self.assertEqual([row["email"] for row in csv.DictReader(handle)],
                                 ["a@keep.com", "j@subsidiary.example"])
            with (folder / "review-parked.csv").open(newline="", encoding="utf-8") as handle:
                parked = list(csv.DictReader(handle))
            self.assertEqual(len(parked), 5)
            self.assertEqual(set(row["review_reason"] for row in parked), {
                "verification_catch_all", "alternate_email_domain_ownership_unproven",
                "Exact address not corroborated",
            })

            # Presentation mode must change paths only, never filtering decisions.
            presentation = folder / "presentation"
            subprocess.run(
                [sys.executable, str(ROOT / "scripts/prepare_export.py"), str(leads),
                 "--suppression", str(suppression), "--output-dir", str(presentation),
                 "--presentation"],
                check=True, capture_output=True, text=True,
            )
            for filename in ("send-ready.csv", "review-parked.csv"):
                self.assertEqual((presentation / filename).read_bytes(), (folder / filename).read_bytes())
            for filename in ("qualified.csv", "excluded.csv", "audit.json"):
                self.assertEqual((presentation / "evidence" / filename).read_bytes(),
                                 (folder / filename).read_bytes())
                self.assertFalse((presentation / filename).exists())


if __name__ == "__main__":
    unittest.main()
