"""Check the staged assignment offline without rewriting its source files."""

import argparse
import csv
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        raw = list(csv.reader(handle))
    if not raw or len(set(raw[0])) != len(raw[0]):
        raise ValueError("Missing or duplicate CSV headers: " + str(path))
    if any(len(row) != len(raw[0]) for row in raw[1:]):
        raise ValueError("CSV row width differs from header: " + str(path))
    return [dict(zip(raw[0], row)) for row in raw[1:]]


def merge_issues(rows):
    issues = []
    for row in rows:
        label = row.get("company", "unnamed row")
        if not row.get("first_name", "").strip():
            issues.append(label + ": missing explicit greeting name")
        if row.get("email_variant") not in {"A", "B"}:
            issues.append(label + ": missing agency email variant A/B")
        if row.get("verification_accept_all", "") not in {"", "true", "false", "unknown"}:
            issues.append(label + ": invalid accept-all flag")
    return issues


def validate(root=ROOT):
    errors = []
    deliverables = root / "deliverables"
    canonical = root / "runs/2026-10-15-second-pass"
    research = read_rows(deliverables / "lead-sheet.csv")
    ready = read_rows(deliverables / "send-ready.csv")
    parked = read_rows(deliverables / "review-parked.csv")
    audit = json.loads((canonical / "audit.json").read_text(encoding="utf-8"))

    def check(condition, message):
        if not condition:
            errors.append(message)

    check(len(research) >= 100, "Assignment requires at least 100 research rows")
    check(len({row["domain"] for row in research}) == len(research), "Research has duplicate companies")
    check(len({row["email"] for row in research}) == len(research), "Research has duplicate emails")
    ready_emails = {row["email"] for row in ready}
    parked_emails = {row["email"] for row in parked}
    check(not ready_emails & parked_emails, "Ready and parked subsets overlap")
    check(ready_emails | parked_emails == {row["email"] for row in research}, "Research subsets lose or add rows")
    check(all(row["verification_status"] == "valid" for row in ready), "Non-valid contact promoted")
    check(audit["qualified_rows"] == len(research) and audit["send_ready_rows"] == len(ready)
          and audit["review_parked_rows"] == len(parked), "Saved audit counts differ from deliverables")
    errors.extend(merge_issues(research))
    for row in research:
        check(not re.search("[\u2013\u2014]", row.get("first_line", "")),
              row["company"] + ": first line contains an em/en dash")
        for field in ("linkedin_url", "signal_source", "fit_source", "first_line_source"):
            parsed = urlparse(row.get(field, ""))
            check(parsed.scheme in {"http", "https"} and bool(parsed.netloc),
                  row["company"] + ": missing source/profile URL in " + field)

    pairs = [("lead-sheet.csv", "qualified.csv"), ("send-ready.csv", "send-ready.csv"),
             ("review-parked.csv", "review-parked.csv")]
    for destination, source in pairs:
        check((deliverables / destination).read_bytes() == (canonical / source).read_bytes(),
              "Stale deliverable snapshot: " + destination)
    temporary_base = root / "tmp"
    temporary_base.resolve().relative_to(root.resolve())
    temporary_base.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="submission-check-", dir=temporary_base) as temporary:
        result = subprocess.run(
            [sys.executable, str(root / "scripts/prepare_export.py"), str(canonical / "leads.csv"),
             "--suppression", str(root / "data/suppression.csv"), "--output-dir", temporary],
            capture_output=True, text=True,
        )
        check(result.returncode == 0, "Canonical export failed: " + result.stderr.strip())
        if result.returncode == 0:
            for filename in ("qualified.csv", "send-ready.csv", "review-parked.csv", "excluded.csv", "audit.json"):
                actual = Path(temporary) / filename
                saved = canonical / filename
                # Git checkout newline conventions vary across Windows/Linux.
                if filename.endswith(".csv"):
                    matches = read_rows(actual) == read_rows(saved)
                else:
                    matches = json.loads(actual.read_text(encoding="utf-8")) == json.loads(saved.read_text(encoding="utf-8"))
                check(matches, "Stale canonical generated file: " + filename)

    first_lines = read_rows(deliverables / "ten-first-lines.csv")
    check(len(first_lines) == 10, "Ten first-line examples are required")
    identities = {(row["name"], row["company"], row["first_line"]) for row in research}
    check(all((row["name"], row["company"], row["first_line"]) in identities for row in first_lines),
          "First-line examples differ from the research sheet")
    copy = (deliverables / "campaign-copy.md").read_text(encoding="utf-8")
    check(not re.search("[\u2013\u2014]", copy), "Campaign copy contains an em/en dash")
    placeholders = set(re.findall(r"\{\{([^{}]+)\}\}", copy))
    check(placeholders == {"first_name", "first_line", "sender_name"}, "Undocumented merge placeholder")
    emails = re.findall(r"^## Email[^\n]*\n(.*?)(?=^## |\Z)", copy, flags=re.M | re.S)
    check(len(emails) == 5 and all("reply STOP" in part for part in emails),
          "Expected first-email variants plus three follow-ups, each with opt-out")
    sequence = read_rows(deliverables / "sequence.csv")
    check(sum(row["channel"] == "email" for row in sequence) == 4
          and sum(row["channel"] == "linkedin" for row in sequence) == 3,
          "Sequence must contain four email steps and three LinkedIn steps")
    for filename in ("strategy-memo.pdf", "strategy-memo.md", "scale-cost.md", "email-review.md"):
        check((deliverables / filename).is_file(), "Missing deliverable: " + filename)

    tracked = subprocess.check_output(["git", "ls-files"], cwd=root, text=True).splitlines()
    tracked_set = set(tracked)
    check(".env" not in tracked, "Local .env must not be tracked")
    check(not any(name.startswith("tmp/") or name.startswith("session-ses_") for name in tracked),
          "Local temporary/session files are tracked")
    for filename in tracked:
        if filename.endswith(".md"):
            path = root / filename
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8-sig")
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if re.match(r"^[a-zA-Z]+:|^#", link):
                    continue
                target = unquote(link.split("#")[0].strip("<>"))
                check(not target or (path.parent / target).exists(),
                      "Broken local link: " + filename + " -> " + target)
                if target:
                    resolved = (path.parent / target).resolve()
                    try:
                        relative = resolved.relative_to(root.resolve()).as_posix()
                    except ValueError:
                        check(False, "Local link leaves repository: " + filename + " -> " + target)
                        continue
                    check(relative in tracked_set or any(name.startswith(relative.rstrip("/") + "/") for name in tracked),
                          "Link target is local-only, absent from checkout: " + filename + " -> " + target)
    return {"checks_pass": not errors, "research": len(research), "draft_ready": len(ready),
            "parked": len(parked), "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        report = validate()
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        report = {"checks_pass": False, "errors": [str(error)]}
    print(json.dumps(report, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
