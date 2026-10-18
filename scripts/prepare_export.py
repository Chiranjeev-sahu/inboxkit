"""Apply mechanical list gates to an agent-researched lead CSV.

Research and evidence judgment stay with the agent. This script only normalizes,
deduplicates, suppresses, and separates clear-valid rows for a later import.
"""

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


REQUIRED = (
    "name", "title", "company", "domain", "linkedin_url", "email",
    "verification_status", "qualification_status", "signal", "signal_source",
    "fit_source", "first_line", "first_line_source",
)
EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
STATUSES = {"valid", "catch_all", "unknown", "invalid"}
QUALIFICATIONS = {"qualified", "uncertain", "rejected"}


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"No CSV header: {path}")
        return reader.fieldnames, list(reader)


def write_csv(path: Path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def normalize_accept_all(fields, rows):
    """Accept older provider-style headers; export one documented field name."""
    if "is_accept_all" not in fields:
        return fields, rows
    canonical = "verification_accept_all"
    fields = [canonical if field == "is_accept_all" else field for field in fields]
    fields = list(dict.fromkeys(fields))
    for row in rows:
        alias = row.pop("is_accept_all", "").strip().lower()
        current = row.get(canonical, "").strip().lower()
        if alias and current and alias != current:
            raise ValueError("Conflicting accept-all fields; resolve the source record before export")
        row[canonical] = current or alias
    return fields, rows


def norm_domain(value):
    value = value.strip().lower()
    if "://" in value:
        value = urlparse(value).hostname or ""
    return value.removeprefix("www.").rstrip("/")


def norm_company(value):
    """Match public partner/customer names despite case and punctuation."""
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def is_url(value):
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def send_review_reason(row):
    """Evidence is judged by the agent; require its decision and proof links."""
    hold = row.get("send_ready_hold_reason", "").strip()
    if hold:
        return hold
    if row["verification_status"] != "valid":
        return "verification_" + row["verification_status"]
    if row["email"].split("@", 1)[1] != row["domain"]:
        sources = row.get("email_domain_ownership_sources", "").split("|")
        if (row.get("email_domain_ownership_status", "").strip() != "proven"
                or not any(source.strip() for source in sources)
                or not all(is_url(source.strip()) for source in sources if source.strip())):
            return "alternate_email_domain_ownership_unproven"
    return ""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Agent-researched leads.csv")
    parser.add_argument("--suppression", type=Path, default=Path("data/suppression.csv"))
    parser.add_argument("--output-dir", type=Path, help="Defaults to the input file's directory")
    parser.add_argument("--presentation", action="store_true",
                        help="Keep ready/review CSVs at output root; write audit/research/exclusions in evidence/")
    args = parser.parse_args()
    if args.presentation and args.output_dir is None:
        parser.error("--presentation requires --output-dir pointing to the run folder")

    fields, rows = read_csv(args.input)
    fields, rows = normalize_accept_all(fields, rows)
    missing_columns = [field for field in REQUIRED if field not in fields]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    suppressed_emails, suppressed_domains, suppressed_companies = set(), set(), set()
    if args.suppression.exists():
        suppression_fields, suppression_rows = read_csv(args.suppression)
        if not {"type", "value"}.issubset(suppression_fields):
            raise ValueError("Suppression CSV needs type,value columns")
        for item in suppression_rows:
            kind = item["type"].strip().lower()
            value = item["value"].strip().lower()
            if not value:
                continue
            if kind == "email":
                suppressed_emails.add(value)
            elif kind == "domain":
                suppressed_domains.add(norm_domain(value))
            elif kind == "company":
                suppressed_companies.add(norm_company(value))
            else:
                raise ValueError(f"Unknown suppression type: {kind}")

    qualified, ready, parked, rejected = [], [], [], []
    seen_emails, seen_domains = set(), set()
    reasons = Counter()
    for row in rows:
        row = dict(row)
        row["email"] = row["email"].strip().lower()
        row["domain"] = norm_domain(row["domain"])
        row["verification_status"] = row["verification_status"].strip().lower()
        row["qualification_status"] = row["qualification_status"].strip().lower()

        reason = ""
        if row["qualification_status"] not in QUALIFICATIONS:
            reason = "bad_qualification_status"
        elif row["qualification_status"] != "qualified":
            reason = "qualification_" + row["qualification_status"]
        elif row["verification_status"] not in STATUSES:
            reason = "bad_verification_status"
        elif row["verification_status"] == "invalid":
            reason = "invalid_email"
        elif any(not row[field].strip() for field in REQUIRED):
            reason = "missing_required_field"
        elif not EMAIL.fullmatch(row["email"]):
            reason = "malformed_email"
        elif (row["email"].split("@", 1)[1] != row["domain"]
              and not row.get("email_source", "").strip()):
            reason = "alternate_email_domain_without_source"
        elif any(not is_url(row[field]) for field in ("linkedin_url", "signal_source", "fit_source", "first_line_source")):
            reason = "missing_source_url"
        elif (row["email"] in suppressed_emails or row["domain"] in suppressed_domains
              or row["email"].split("@", 1)[1] in suppressed_domains
              or norm_company(row["company"]) in suppressed_companies):
            reason = "suppressed"
        elif row["email"] in seen_emails:
            reason = "duplicate_email"
        elif row["domain"] in seen_domains:
            reason = "duplicate_domain"

        if reason:
            row["exclusion_reason"] = reason
            rejected.append(row)
            reasons[reason] += 1
            continue

        seen_emails.add(row["email"])
        seen_domains.add(row["domain"])
        qualified.append(row)
        review_reason = send_review_reason(row)
        if not review_reason:
            ready.append(row)
        else:
            parked.append({**row, "review_reason": review_reason})

    destination = args.output_dir or args.input.parent
    destination.mkdir(parents=True, exist_ok=True)
    evidence = destination / "evidence" if args.presentation else destination
    evidence.mkdir(parents=True, exist_ok=True)
    write_csv(evidence / "qualified.csv", fields, qualified)
    write_csv(destination / "send-ready.csv", fields, ready)
    write_csv(destination / "review-parked.csv", [*fields, "review_reason"], parked)
    write_csv(evidence / "excluded.csv", [*fields, "exclusion_reason"], rejected)
    audit = {
        "input_rows": len(rows),
        "qualified_rows": len(qualified),
        "send_ready_rows": len(ready),
        "review_parked_rows": len(parked),
        "research_reconciles": len(qualified) == len(ready) + len(parked),
        "alternate_email_domain_rows": sum(
            row["email"].split("@", 1)[1] != row["domain"] for row in qualified
        ),
        "alternate_email_domain_review_rows": sum(
            row["email"].split("@", 1)[1] != row["domain"] for row in parked
        ),
        "review_reasons": dict(Counter(row["review_reason"] for row in parked)),
        "verification_statuses": dict(Counter(row["verification_status"] for row in qualified)),
        "excluded_reasons": dict(reasons),
    }
    (evidence / "audit.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
