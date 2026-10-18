# Lead fields and import mapping

The canonical agency source is `runs/2026-10-15-second-pass/leads.csv`. New ICP inputs live at `runs/<run-id>/evidence/leads.csv`. Export preserves source columns while standardizing the accept-all header. Provider JSON receipts retain their original provider field names.

## Contact and evidence fields

| Field | Meaning |
| --- | --- |
| `name` | Full professional name. Do not replace this with a guessed mailbox owner. |
| `first_name` | Agent-reviewed greeting name, recorded explicitly. Historical files without it remain reproducible but need the field before merging current copy. |
| `title`, `company`, `domain` | Current role, organization and normalized website domain. A founder's infrastructure influence can be inferred only when disclosed. |
| `linkedin_url` | Personal profile URL, not just the company page. Record access/corroboration limits. |
| `email`, `email_source` | Named work email and finder/public-source attribution. Generic inboxes do not become named buyers. |
| `qualification_status` | `qualified`, `uncertain` or `rejected`; agent judgment of the supplied ICP and signal. |
| `signal`, `signal_source`, `signal_date` | Operational relevance fact, its source, and visible date. Undated facts are not called recent. |
| `fit_source` | Public page establishing the company-fit rule. It can also prove the signal when it genuinely supports both. |
| `first_line`, `first_line_source` | Truthful prospect-specific opening and supporting page. No invented InboxKit claim. |
| `email_variant` | For the staged agency sequence: `A` for client-account administration, `B` for domain organization. Chosen from existing operational evidence, not a measured winning variant. New ICPs define their own copy; this field can be absent when no variants are used. |
| `review_note` | Evidence judgment, inference, uncertainty and proof links in plain language. |

## Verification and hold fields

| Field | Meaning |
| --- | --- |
| `verification_status` | `valid` is positive provider-assessed delivery, not guaranteed mailbox existence; `catch_all` is ambiguous; `unknown` is unresolved; `invalid` is a clear negative. |
| `verification_provider`, `verification_raw`, `verification_date` | Provider, exact assessment/score and observation date. Do not refresh the date without a real check. |
| `verification_accept_all` | Canonical exported domain flag: `true`, `false`, or unreported blank. Three older agency records retain literal `unknown`. Never convert blank/unknown to false. |
| `is_accept_all` | Historical/provider-style alias accepted on input. Export renames it to `verification_accept_all`; conflicting nonblank values cause an error. Raw receipts remain unchanged. |
| `email_domain_ownership_status` | `proven` only when public evidence establishes the alternate domain's relationship to the listed organization. |
| `email_domain_ownership_sources` | Pipe-separated HTTP(S) evidence URLs for that judgment. The script validates format, not the truth of the pages. |
| `send_ready_hold_reason` | Explicit unresolved issue that prevents promotion even when a provider is positive. |
| `review_reason`, `exclusion_reason` | Export-generated reason for a parked or excluded record. |

A positive `valid` result can coexist with `verification_accept_all=true` under the user's agreed policy. A contradictory clear negative or explicit hold prevents promotion. The extra exact-address and second-verifier checks for four historical contacts are targeted exceptions, not requirements imposed on every new contact.

## Files and counts

- `leads.csv`: every attempted contact row, including failures; the company-disposition log can also contain companies without a contact.
- `qualified.csv`: retained research after mechanical gates.
- `send-ready.csv`: draft contacts passing the current ready gate.
- `review-parked.csv`: retained research with visible holds or uncertainty.
- `excluded.csv`: failed/invalid/duplicate/suppressed attempts, never silently erased.
- `audit.json`: generated counts and reasons. **Research = ready + parked. Input attempts = research + excluded.** Company-log counts are a different denominator.

## Merge fields

| Campaign value | CSV field or operator setting |
| --- | --- |
| Recipient address | `email` |
| `{{first_name}}` | `first_name`, explicitly recorded; do not map `name` into this placeholder. |
| `{{first_line}}` | `first_line`, with evidence in `first_line_source`. |
| First email 1A or 1B | `email_variant=A` or `B`; use exactly one version. Subsequent email steps are shared. |
| `{{sender_name}}` | Operator-provided sender identity, replaced when configuring any separately authorized campaign. It is deliberately a draft placeholder, not a missing contact field. |
| Company/title/profile | Map `company`, `title` and `linkedin_url` to native/custom fields as needed. |
| Risk/evidence fields | Keep as custom fields or retain alongside the imported list; never silently relabel catch-all risk. |

The schedule in `deliverables/sequence.csv` references templates in `campaign-copy.md`; it is not a Smartlead/Instantly-native sequence upload. Platform field mapping and sequence setup would be a later human-controlled step. The assignment remains draft-only. A monitored reply-to and suppression reconciliation must precede any separately authorized live sending.
