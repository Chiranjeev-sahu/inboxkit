"""Refresh the public InboxKit partner inventory from the saved sitemap URLs.

This is an optional, standard-library-only audit. It does not change suppression
automatically: a human/agent checks the extracted names and domains first.
"""

import csv
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SITE_MAP = ROOT / "docs/inboxkit-sitemap-inventory.csv"
OUTPUT = ROOT / "docs/inboxkit-partner-audit.csv"


class ProfileParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_heading = False
        self.website_depth = 0
        self.heading = []
        self.website_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.in_heading = True
        if tag == "section":
            if attrs.get("id") == "website":
                self.website_depth = 1
            elif self.website_depth:
                self.website_depth += 1

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_heading = False
        if tag == "section" and self.website_depth:
            self.website_depth -= 1

    def handle_data(self, data):
        if self.in_heading:
            self.heading.append(data)
        if self.website_depth:
            self.website_text.append(data)


def inspect(url):
    row = {"name": "", "profile_url": url, "listed_website": "", "domain": "",
           "status": "", "checked_at": date.today().isoformat()}
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; public partner audit)"})
        with urlopen(request, timeout=25) as response:
            parser = ProfileParser()
            parser.feed(response.read().decode("utf-8", errors="replace"))
        row["name"] = " ".join("".join(parser.heading).split())
        text = " ".join(parser.website_text)
        match = re.search(r"(?:www\.)?[a-z0-9][a-z0-9.-]+\.[a-z]{2,}(?:/[^\s]*)?", text, re.I)
        if match:
            row["listed_website"] = match.group(0)
            row["domain"] = (urlparse("https://" + match.group(0)).hostname or "").removeprefix("www.")
        row["status"] = "name_and_domain" if row["name"] and row["domain"] else "review_needed"
    except Exception as exc:
        row["status"] = "fetch_failed:" + type(exc).__name__
    return row


def main():
    with SITE_MAP.open(newline="", encoding="utf-8-sig") as handle:
        urls = [row["url"] for row in csv.DictReader(handle)
                if "/partners/" in row["url"] and not row["url"].endswith("/become-a-partner")]
    with ThreadPoolExecutor(max_workers=6) as executor:
        rows = list(executor.map(inspect, urls))
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} partner profiles; {sum(r['status'] == 'name_and_domain' for r in rows)} domains resolved")
    for row in rows:
        if row["status"] != "name_and_domain":
            print(row["profile_url"], row["status"])


if __name__ == "__main__":
    main()
