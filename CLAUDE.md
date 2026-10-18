# InboxKit GTM assignment

You are the research and campaign agent. The operator may be Codex or Claude Code. Read `GTM Engineer Hiring Assignment.txt` before an assignment run. Read `CONTEXT.md` for terminology, `docs/decisions.md` for agreed choices, and `docs/open-questions.md` when making an unresolved choice. Evidence from a live run can overturn a provisional choice; record why.

## Run a new ICP

1. Ask the operator for an ICP only if none was supplied. State a testable company-fit rule and one or more candidate buying signals. Keep fit separate from intent. When a different segment is supplied, derive its rules from that ICP rather than carrying over the current agency rule. For the current agency submission, follow the operational evidence rule in the runbook and target 100 distinct companies with one buyer each. Hiring and client cases are evidence options; a recent dated event is not mandatory.
2. Read and execute `skills/lead-research/SKILL.md`. It defines evidence, provider waterfall, contact and email status, deduplication, suppression, outputs, and completion checks. Keep the run understandable enough to explain live in a 45-minute review.
3. Produce a small cited sample before expanding. Report the number examined, rejected, uncertain, found, and clear-valid. Escalate a rule change when evidence is insufficient rather than silently widening the ICP.

For a new ICP, create a separate `runs/<run-id>/` with the presentation layout in runbook step 6. For "more companies" or "continue" under the default agency ICP, extend `runs/2026-10-15-second-pass/leads.csv`, dedupe against the existing dataset, rerun its legacy export command, and refresh the corresponding existing deliverable CSVs. Preserve old rows and evidence, retain new batch provenance, and update actual counts instead of capping an explicitly requested extension at 100. A new ICP never overwrites that agency dataset. Use the current runbook and decisions as policy; dated experiments record what happened under earlier rules.

## Campaign rules

- Every InboxKit product claim in strategy or copy needs a supporting `inboxkit.com` page URL. Prospect claims need their own source URLs. Gather only the product pages needed for the copy, then check each claim.
- Draft every message. Do not send, enroll contacts, or import them into a live sequencer. The sheet should be ready for a later human-controlled import.
- Campaign copy uses no em dash or en dash, has one ask per message, and includes a working opt-out in every email. Smartlead and Instantly are integrations, not competitors.
- Keep API keys in a local `.env` or the operator's environment. Never print keys or commit secrets. Stay within available free credits and the user's $0 cash budget. Ask before any paid usage.

## Validation

Before reporting that the saved package is consistent, run `python scripts/check_submission.py` and the unit tests. The check validates contact fields, exported subsets, saved snapshots and repository references offline. The agent judges source support, buyer identity and commercial relevance. The [operator guide](docs/operator-guide.md) explains setup and commands; the [data dictionary](docs/data-dictionary.md) defines merge fields.

Keep documentation focused on reproducible behavior, artifacts and technical evidence. The original assignment remains authoritative for the requested work.
