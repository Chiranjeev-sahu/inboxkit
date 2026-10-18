# New ICP offline clean-checkout smoke test

Date: 2026-10-16
Target: three qualified contact rows, initially one buyer per company.
ICP: B2B SaaS companies (not agencies) that publicly operate an in-house cold-email outbound motion, with a recent relevant SDR or outbound-operations hiring signal.

## Company-fit rule

Pass only when first-party public evidence establishes both (1) a company sells its own subscription/cloud software to business customers and (2) its internal team currently conducts cold-email prospecting to acquire customers for that software. Exclude agencies, managed outbound service providers, and companies whose only evidence is offering email software, newsletter marketing, inbound follow-up, or outbound work for clients. Do not infer an existing motion solely from plans to build one. No geography or language filter applies. This replaces the agency fit rule for this run only.

Exact fit evidence needed: canonical company domain; first-party product/pricing/about page URL and quoted excerpt demonstrating own B2B SaaS product; first-party team/process article or job page URL and quoted excerpt explicitly demonstrating internal cold-email prospecting for its own sales; capture/access date and any publication date. One page may support multiple facts if each is explicit. Search snippets and job titles alone are insufficient. Missing or ambiguous evidence stays uncertain.

## Separate buying-signal rule

Pass only with a relevant SDR or outbound-operations hiring event published or explicitly reposted within the preceding 90 days: 2026-07-18 through 2026-10-16 inclusive (0 to 90 elapsed calendar days). This is a declared test threshold for recent, not an inferred permanent requirement. Duties must explicitly include cold-email prospecting or operating its sending infrastructure, domains/mailboxes, deliverability, or outbound sequencer workflows for the company's own sales. Generic sales hiring does not qualify. Hiring suggests possible capacity or infrastructure demand; it does not prove purchase intent.

Exact signal evidence needed: employer careers page or employer-authorized ATS job URL, employer identity/domain association, job title, quoted relevant duties, explicit publication/repost date, capture date, and open/closed status. A search indexing date is not a publication date. Missing dates remain signal_uncertain; older jobs are older; closed jobs remain uncertain and are not accepted as current hiring. A job proposing a future outbound team can support the signal but cannot alone prove the existing-motion fit rule.

## Contact and export evidence for a future authorized online run

For each accepted company, record separate fit and signal URLs, excerpts and dates, then name/title/LinkedIn URL of the sending-infrastructure owner, founder, head of growth or outbound-operations leader; named work email and its source; verifier provider, exact verdict, normalized status and verification date. Preserve uncertainty and conflicting results. Record a truthful first line with its prospect source URL. Normalize/dedupe and check local suppression plus public customer/partner evidence before export. No public checks or contact discovery are attempted here. Only qualified rows can enter the research export; only valid email rows with matching company domains can enter the draft send-ready export under the existing script.

## Offline execution boundary

No real leads can be sourced in this offline test. No people, companies, or email addresses are searched for or invented. No network, browser, MCP, API, external service, or .env access is permitted or used. Only local instructions, documentation, the export script and its local suppression file are used. Discovery, enrichment, verification, public customer/partner checks, and personalization are unexecuted because no candidates exist. No outreach is generated or sent. Existing agency deliverables are untouched.

Read: AGENTS.md, CLAUDE.md, GTM Engineer Hiring Assignment.txt, CONTEXT.md, skills/lead-research/SKILL.md, docs/decisions.md, docs/open-questions.md, and scripts/prepare_export.py. The original assignment remains authoritative for the broader assignment; this user-directed SaaS smoke test does not replace its agency deliverables.

Input: leads.csv contains the 13 required columns and six audit columns, header only. No placeholder rows.
Command: python scripts/prepare_export.py runs/2026-10-16-new-icp-offline-smoke/leads.csv

## Actual results

Export command exited successfully (exit code 0). audit.json reports input_rows=0, qualified_rows=0, send_ready_rows=0, alternate_email_domain_rows=0, alternate_email_domain_review_rows=0, verification_statuses={}, excluded_reasons={}.

Companies examined: 0. Rejected: 0. Uncertain: 0. Leads found: 0. Qualified: 0. Clear-valid: 0. Send-ready: 0. Duplicates: 0. Suppressed: 0. Excluded: 0. Verification buckets valid/catch_all/unknown/invalid: all 0, with no verification performed. Target shortfall: 3.

Generated qualified.csv, send-ready.csv, excluded.csv and audit.json in this run directory. Empty inputs exercise schema acceptance and output generation, not populated-row deduplication, suppression, evidence quality, email verification or provider access.

Outcome: the offline clean-checkout agent workflow worked for reading the repository runbook, deriving new-segment rules without inheriting agency fit, creating a header-only input and executing the local export successfully. Live end-to-end lead sourcing remains untested. The bottleneck is the deliberate offline boundary, not observed market yield. A future separately authorized online run would test a three-company cited sample against these exact rules before considering any rule change. This smoke test does not complete the broader assignment.

## Online attempt and environment finding

Before this offline run, an independent Codex invocation with the local `.env` was proposed for up to ten existing-credit finder/verifier calls. Automatic approval review **rejected that invocation before it started**, reasoning that it could transmit named candidate identity and email data to third-party providers without specific authorization for those payloads and destinations. No lookup or verifier call was made in that attempt. The copied `.env` was removed from the temporary checkout. An initial offline CLI attempt in the host temp directory could not start its local command runner; the same credential-free, offline task succeeded from a fresh clone inside the authorized workspace. The clone was removed after these artifacts were copied here.
