---
name: lead-research
description: Turn a supplied ICP into sourced, enriched, verified, deduplicated, suppression-checked prospect rows for the InboxKit assignment. Use for pilot or live rerun.
---

# Lead research runbook

Use this runbook when the operator supplies an ICP or asks for a sourcing run. Work as the research agent. Keep mechanical checks small and repeatable. Route the request before writing: a new ICP uses a new `runs/<run-id>/` with the presentation layout in step 6; an explicit default-ICP continuation extends the canonical agency dataset using the continuation branch in that step. Create a new directory only when running.

## 1. Define the run

Record the ICP text, date, target count, fit rule, candidate signal rule, and what evidence would qualify each. Derive these rules from the supplied ICP; do not carry the current campaign's company-fit rule into a new segment. For the current agency campaign, company fit means a public source says the agency sells, builds, operates, or supports cold-email or outbound infrastructure for client companies. The selected signal is public evidence that the agency is actively operating or expanding multi-client outbound. Evidence can be a relevant hire, a named client campaign, current multi-client campaign or sending volume, or a service expansion tied to client outbound. Record dates when visible. Evidence inside 90 days is stronger, but 90 days is not an eligibility cutoff. Label older or undated evidence honestly and never describe it as recent. State the rule before searching.

For the final agency submission, the user's target is 100 distinct companies with one buyer each. Use concrete client campaign delivery, infrastructure operation, a client example or testimonial, campaign volume, or a relevant hire as operational evidence. This signals infrastructure relevance, not confirmed purchase intent. A named client and an event date are optional.

Completion: the rules can be applied to a new company without relying on the conversation's memory.

## 2. Discover and qualify companies

Search public sources with whichever connected tools work in the current environment: Codex/Claude web tools, Exa, or Tavily. Fetch specific pages with browser/web tools or Firecrawl when extraction helps. Capture a first-party page that proves the supplied company-fit rule and a page that proves the selected signal. For the current agency run those are often a service page plus a job, client case, current operating-scale page, or service-expansion page; a different ICP may need different evidence. A search snippet alone is a lead to inspect, not final proof. Record every examined company and a disposition: `fit_and_signal`, `fit_only`, `signal_uncertain`, `not_fit`, or `duplicate`. Explain uncertain dates, closed jobs, unnamed clients, and service overlap. Do not use geography or language as an unstated filter.

The same first-party page may serve as both fit and signal source when it supports both facts. Record which statements prove service fit and which prove activity; separate URLs are not mandatory.

Before spending enrichment credits, judge commercial suitability for InboxKit separately from literal ICP fit. Check whether the prospect supplies its own competing mailbox/domain infrastructure or has another concrete reason not to be a plausible new customer. Record the evidence and park an unresolved overlap with a specific reason; do not count it as a ready prospect merely because it runs outbound. A sequencer integration alone is not a competitive exclusion: Smartlead and Instantly are integrations under the brief. Apply the supplied ICP without silently replacing it with the agency segment.

Completion: every accepted candidate has a domain, a fit URL, and a signal URL; rejected and uncertain candidates have short reasons. Report the number examined so yield can be measured.

## 3. Find the buyer and work email

When both have usable existing credits, try Icypeas email discovery before Datagma for a missing named-buyer address. In the [ten-buyer comparison](../../runs/2026-10-16-provider-comparison/run-notes.md), Icypeas recovered 8 saved addresses and Datagma 5, with no Datagma increment on the two Icypeas misses. This relative order is provisional and does not rank the other finders.

Choose a founder, owner of sending infrastructure, or head of growth before an AE. Capture the person's name, title, and LinkedIn URL. Search first-party contact pages for a named work email. If missing, use a role-specific waterfall over usable providers: connected Lusha MCP, Apollo, Prospeo, Hunter, Findymail, Icypeas, Datagma, and other available contact sources. Check access, balance, and cost before calls; batch where efficient. On a no-result, restriction, rate limit, or low-confidence mismatch, log the outcome and try the next suitable provider. Stop when a named buyer/work-email match meets the lookup rule. Do not spend a credit merely to exercise a provider. Keep a generic inbox out of a named buyer row. A named finder result may use an alternate company email domain; record the finder query/association and flag the domain mismatch for review rather than treating the website domain as an absolute requirement.

For direct API access, consult [tested provider routes](../../docs/provider-access.md) before constructing requests. This supplies working authentication/endpoint details, not a fixed provider order or a guarantee of remaining credits. Read local keys privately; save only sanitized receipts. After a clear verifier result, stop unless a documented ambiguity warrants another check.

Completion: each retained contact has name, title, LinkedIn URL, email and email-source URL/provider, or an explicit missing field and reason.

## 4. Verify and label

Run a verifier waterfall using existing credits, with the catch-all specialist BounceBan first when available. Stop at a clear result; use Icypeas as a corroborating check or fallback when BounceBan is ambiguous, then ZeroBounce, Reoon, or MillionVerifier where access and remaining credits make them useful. The [October 16 pilot](../../runs/2026-10-16-email-verification-pilot/run-notes.md) supports this provisional order for these agency domains. Record each provider's exact result, score, accept-all flag, date, and credit use. An SMTP-only `catch_all` verdict means that provider could not distinguish the mailbox; it is not itself a contradiction of a specialist `deliverable` verdict. A specialist result is still probabilistic. If providers return conflicting clear deliverable and undeliverable results, keep the conservative status and both raw results. Translate raw responses to:

- `valid`: a verifier gives an unambiguous **provider-assessed** deliverable result without a contradictory clear-undeliverable result. This does not mean mailbox existence or delivery is guaranteed. Preserve `is_accept_all=true` separately when relevant. This is the only email status eligible for the draft send-ready export.
- `catch_all`: only accept-all/ambiguous results are available; keep the row for review, not send-ready.
- `unknown`: timeout, missing credit, no result, or unresolved disagreement; keep for review.
- `invalid`: undeliverable or malformed; exclude from the deliverable contact sheet until replaced by a verified alternative buyer/email. Keep it in the attempt log.

The user's 16 October decision defines `valid` as a positive provider `deliverable` or `verified` result, with the domain accept-all flag recorded separately. This supersedes the earlier blanket stance against labeling a provider-verified catch-all-domain address valid. A domain's ambiguous accept-all response does not cancel a positive mailbox assessment; a conflicting clear-undeliverable verdict remains an unresolved disagreement and is parked as `unknown` with both results. Keep a blank accept-all field blank unless a reporting verifier supplies a boolean. If an email is invalid, try another buyer or address before discarding the account; retain all 100 final research rows and their attempt history.

For an alternate email domain, open first-party company/About/contact/footers, relevant group sites, and the buyer's LinkedIn profile. Promote only when public evidence establishes the same organization, a parent/subsidiary/rebrand, or shared leadership. Record proof URLs in `review_note` and pipe-separated `email_domain_ownership_sources`, and set `email_domain_ownership_status=proven` only after judging that evidence. A finder or verifier result alone is insufficient. Otherwise state the exact missing link and leave it parked. Matching names or copied site branding alone do not establish ownership.

Only the four historical rows in the [targeted email review](../../deliverables/email-review.md) additionally require buyer LinkedIn and public company corroboration of the exact address, plus a second verifier reporting accept-all where credits permit. Their missing exact-address links are explicit `send_ready_hold_reason` values. These extra checks are a targeted user-requested review; they do not apply to new finder-sourced contacts. For new runs, follow the stop-at-clear-result rule above and retain any actual verification conflict.

Completion: every retained email has provider, raw result, normalized status, and verification date. Report the count in each status bucket.

## 5. Dedupe, suppress, and personalize

Normalize the company domain and email for comparisons. Retain one best-fit buyer per distinct company in the final sheet. If there are multiple candidates, record the others as lookup alternatives rather than counting them toward 100. Treat aliases and alternate domains of the same organization as one company. Compare every email, domain, and exact normalized company name with `data/suppression.csv` if present; it has columns `type,value,reason`, where type is `email`, `domain`, or `company`. Suppressed rows are removed from export and logged with reason. Do not erase the source/attempt record. Remove exact email duplicates and flag duplicate domains for review.

Before export, check candidate organizations against InboxKit's public partner and customer pages. A named current partner or customer belongs in suppression and the attempt log, not a new-customer prospect export. The public pages are incomplete evidence of account status; a no-match is not proof that the company is not already a customer.

Write one truthful first line per accepted row from the recorded prospect fit or signal page. Link its source. If the fact is uncertain, use a plain agency-specific observation without a date or avoid that personalization. Do not introduce an InboxKit product claim into a prospect first line.

Completion: exported rows have no suppressed email/domain, no duplicate email, and no unsupported first line. The run notes state the duplicate and suppression counts, including zero.

## 6. Save and audit

`leads.csv` must contain at least `name,title,company,domain,linkedin_url,email,verification_status,qualification_status,signal,signal_source,fit_source,first_line,first_line_source`. Set `qualification_status` to `qualified`, `uncertain`, or `rejected`. Add `signal_date,email_source,verification_provider,verification_raw,verification_date,review_note` for auditability. Record an explicit agent-reviewed `first_name` for copy merges; for the staged agency sequence also select `email_variant=A` (client accounts) or `B` (domain organization) from the row's evidence. Use the canonical exported field `verification_accept_all`; raw provider receipts may retain `is_accept_all`. See the [schema and mapping](../../docs/data-dictionary.md). Historical inputs without newer copy fields remain exportable but need those fields before importing current templates. Keep source URLs alongside facts. Save rejected or failed lookup details concisely in `run-notes.md`; never save keys or raw API responses with secrets. For a new ICP, the field names stay stable while the evidence used for fit and signal changes.

For a **new ICP**, keep exactly four presentation files at `runs/<run-id>/`: `README.md`, `send-ready.csv`, `draft-outreach.md`, and `review-parked.csv`. Put input rows in `evidence/leads.csv`; keep inputs, company dispositions, source excerpts, provider receipts, credit records and detailed `run-notes.md` under `evidence/` too. Write drafts only for retained contacts; if none are ready, make the draft file explain that instead of fabricating copy. The agent writes the README with the ICP, fit/signal rules, requested/achieved counts, ready/review/excluded totals, key uncertainties, and relative links to outputs and evidence. Use it as the interview entry point.

Export a new ICP with `python scripts/prepare_export.py runs/<run-id>/evidence/leads.csv --output-dir runs/<run-id> --presentation`. It writes the two presentation CSVs at the run root, and `qualified.csv`, `excluded.csv`, and `audit.json` under `evidence/`. Keep local receipt references in the research records resolvable inside the evidence folder.

For an **explicit default-agency continuation**, retain the existing flat layout: append new distinct-company attempts to `runs/2026-10-15-second-pass/leads.csv` without erasing prior rows or provenance. Dedupe against the entire canonical dataset, not just the latest batch. Save new source/provider evidence as a dated batch and reference it from the appended rows. Run `python scripts/prepare_export.py runs/2026-10-15-second-pass/leads.csv` without `--presentation`. Refresh `deliverables/lead-sheet.csv` from canonical `qualified.csv`, and the existing `deliverables/send-ready.csv` and `deliverables/review-parked.csv` from their canonical equivalents. Reconcile and update current count summaries. Preserve earlier dated snapshots and valid first-line examples. The 100-company assignment target is a baseline, not a cap when the user expressly asks for additions. Do not add another company now merely because this branch is documented.

Historical runs retain their original layouts unless specifically reorganized. The original flat export command remains supported. Before declaring either layout import-ready, inspect the audit and review reasons. The script checks structure, duplicates, suppression, and documented alternate-domain approval; the agent judges evidence quality. `valid` rows enter the draft export when their domain matches or its relationship is proven with URLs, and no `send_ready_hold_reason` remains. Catch-all flags are separate risk fields. A qualified `catch_all` or `unknown` row remains research-only; a conflicting verification result is preserved as `unknown` pending resolution. Historically rejected qualification/invalid attempts remain in `leads.csv` and `excluded.csv`. For this final 100-company sheet retain every existing research row and show its current uncertainty. Report and reconcile **research = send-ready + review-parked**; neither subset may overlap or silently lose a research row.

Completion: another agent can rerun the steps from a clean checkout with the original ICP, these files, the operator's `.env`, and access to the stated MCP or web tools; no hidden chat history is needed.
