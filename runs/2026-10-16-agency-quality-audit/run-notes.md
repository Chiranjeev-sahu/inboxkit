# Agency quality audit

**Date:** 16 October 2026
**Scope:** read-only review of the 33-row second-pass input against the InboxKit brief and the lead-research runbook. No messages were sent and no sequencer import occurred.

## Result

- 33 input companies reviewed.
- 27 rows remain `qualified` in the research export.
- 4 rows remain `uncertain` and 2 remain `rejected` in the attempt log.
- 25 rows enter the draft `send-ready.csv` export.
- 2 qualified rows use an alternate email domain and remain review-only.
- 27 retained emails have a positive BounceBan specialist verdict. The `is_accept_all` flag is preserved; it is not treated as proof of mailbox existence.

## Corrections made

1. **ThynkGrowth / Faraz Ahmed** remains in the attempt record but changed from `qualified` to `uncertain`. The agency fit is supported by its public site, which describes managed client campaigns and live InboxKit deployment. The observed Content Engineer role is primarily content work with only occasional cold-email copy, so it is not strong evidence of the selected campaign-operations buying signal.
2. **Danish Lead Co. / Frederik Jakobsen** had a contradictory review note. BounceBan returned `is_accept_all=false`; the note now preserves the earlier MillionVerifier catch-all result as historical raw evidence instead of saying the current flag is true.
3. The research/export counts at this audit stage were corrected to 27 qualified and 25 send-ready; later cumulative totals are recorded in the canonical dataset.

After this audit, the fixed-rule follow-up sourcing test added Pipeline Playbooks and SalesCaptain as qualified rows, while Beanstalk remained uncertain. Two scale batches then added 1SecondLeads, IGTMS, Sendō, ProspectOut, and Growleads. The current repository totals are therefore 34 qualified and 32 send-ready; the base audit counts above remain useful as the before/after checkpoint.

## Evidence checks

The named email sources were opened or reviewed for Garrett Wolfe, Alexan Zartarian, Gregory Martignoni, Felix Frank, Frederik Jakobsen, Kasper Hallberg, Ankit Modi, and Faraz Ahmed. Each source publishes or explicitly contains the recorded address. Faraz's address is explicitly included in the public ThynkGrowth hiring post, so it is not a guessed address.

Six Figure Consulting was rechecked against its public Built In role and site. The role says it manages client outbound campaigns, sources and verifies lead data, and maintains deliverability and domain health. It stays qualified despite the company having other consulting lines.

Relative-age evidence such as “two weeks ago” or “one month ago” is preserved in row notes where the source did not expose an absolute date. No exact date was invented. These rows remain qualified only when the observed relative age was within the 90-day test window; otherwise the row is uncertain or rejected.

## Remaining limitations

- A verifier's positive result is provider-assessed deliverability, not proof that a person monitors the mailbox.
- Accept-all flags remain visible and should be reviewed before any real send.
- This is still a search-selected sample. Its yield cannot be projected to the 100-row target.
- The next step is a predeclared fixed-rule sourcing experiment for new agencies, recording examined, rejected, uncertain, and accepted companies before expanding the list.
