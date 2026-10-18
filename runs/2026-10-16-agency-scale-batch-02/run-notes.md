# Agency scale batch 02

**Date:** 16 October 2026
**Target:** disposition another consecutive group of surfaced companies under the selected hiring signal.
**Fit rule:** a public source must show that the company runs managed cold email or outbound campaigns for clients.
**Signal rule:** a dated hiring page within 90 days must show a role responsible for client campaign operations or sending infrastructure.

## Result

- 13 surfaced companies were dispositioned.
- 2 cleared fit, signal, buyer, suppression, and email-verification gates.
- 4 remained uncertain because the company boundary, publication date, or role ownership was not clear enough.
- 3 were not usable segment matches.
- 1 anonymous posting could not become a company row.
- 2 were duplicates of the canonical dataset.
- 1 was a publicly suppressed InboxKit partner.
- No message was sent and nothing was imported.

## Accepted

1. **ProspectOut:** the [first-party About page](https://prospectout.com/about-us/) describes fully managed cold email and LinkedIn outreach for clients and identifies Jahidul Islam as founder. The agency's [30 August hiring post](https://www.linkedin.com/posts/prospectout_prospectout-is-looking-for-a-talented-cold-activity-7499789129333956608-mTw2) assigns a campaign manager client research, strategy, copy, optimization, reply handling, and meetings. Lusha matched Jahidul's exact LinkedIn profile and returned `jahidul@prospectout.com` with A+ confidence. BounceBan returned `deliverable`, score 99, `is_accept_all=false`.
2. **Growleads:** the [first-party site](https://growleads.io/) says Growleads runs cold email, LinkedIn, and GTM systems for clients. A [24 September job listing](https://jobboard.co.in/gtm-associate_jaipur-c278688/2026-09-growleads-io-ai-powered-bb-lead-generation-agency_i4215481516) assigns a GTM Associate client outbound campaigns, cold email, reply handling, and campaign support; it also publishes `sarthak@growleads.io`. [Sarthak Mittal's profile](https://www.linkedin.com/in/connectsarthak) identifies him as Head of GTM and Strategy. BounceBan returned `deliverable`, score 97, `is_accept_all=true`.

Both companies were checked against `data/suppression.csv` and the canonical dataset before provider work. The verifier results are predictions rather than observed delivery, and the accept-all flag remains visible.

## Provider observations

- One Icypeas discovery request was submitted for Jahidul Islam. The response returned `success=true` but the local parser did not expose a search identifier or email, so it was not treated as a result and was not repeated. Whether that incomplete response consumed a credit was not established.
- A Lusha preview matched the exact ProspectOut founder and charged one credit. Revealing only email charged one further credit and returned two A+ work addresses; the company-domain address was selected. No phone was revealed. The read-only usage check then showed 28 of 40 free-plan credits remaining.
- Sarthak's named work email was published in the job listing, so no finder was called.
- Two BounceBan checks completed successfully. The account endpoint showed 71 credits before and 68 after. That three-credit balance change does not reconcile with the two documented verification requests, so the notes preserve the observed values instead of claiming an exact per-call burn.

## Other dispositions

| Company or result | Disposition | Reason |
| --- | --- | --- |
| AirOps | uncertain | The role clearly operates high-volume outbound across client accounts, but AirOps presents primarily as a software and content-engineering company; the agency segment boundary is unclear. |
| GrowthifyU | uncertain | The role describes ownership of 5–10 live client cold-email accounts, but an exact publication date and a suitable decision maker were not established. |
| Dragon Fruit Studio | uncertain | Client cold-email operations were visible, but the surfaced internship page did not provide a reliable publication date or leadership contact. |
| Flowd | uncertain | A recent client-success hire was visible, but the role owns the client relationship while another team runs the campaigns; it is weak evidence for infrastructure expansion. |
| Pavago listing | not usable | Pavago was recruiting for an unnamed outbound-agency client, so the actual company could not be identified or suppressed. |
| Adscular Agency | not fit | Its recent cold-email hire was for Adscular's own client acquisition rather than managed client campaigns. |
| M3USA | not fit | The role operates M3's internal and subsidiary outbound rather than an agency service sold to external clients. |
| Anonymous Upwork agency | no company | The posting described relevant work but did not disclose a company identity. |
| Snipe Outbound | duplicate | Existing canonical row. |
| Provena AI | duplicate | Existing canonical row. |
| Hypergen | suppressed | Public InboxKit partner already in the suppression list. |
| ProspectOut | accepted | Cleared every gate. |
| Growleads | accepted | Cleared every gate. |

## Yield and next batch

This batch produced two accepted rows from 13 dispositions. Across scale batches 01 and 02, five of 26 dispositions became qualified rows. That is a measured search yield for these queries, not a population estimate. Continue the rule for another batch, but keep monitoring whether dated agency hiring evidence can reach 100 rows within the remaining time and credits.
