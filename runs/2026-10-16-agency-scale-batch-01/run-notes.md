# Agency scale batch 01

**Date:** 16 October 2026
**Target:** examine at least ten consecutive surfaced companies under the selected hiring signal.
**Fit rule:** a public source must show that the company runs managed cold email or outbound campaigns for clients.
**Signal rule:** a dated hiring page within 90 days must show a role responsible for client campaign operations or sending infrastructure.

## Result

- 13 surfaced companies were dispositioned.
- 3 cleared fit, signal, buyer, suppression, and email-verification gates.
- 2 remained uncertain.
- 3 were not fit for this segment.
- 3 were duplicates of the canonical dataset.
- 1 was a publicly suppressed InboxKit partner.
- 1 had a relevant hiring signal outside the 90-day window.
- 3 existing BounceBan credits were used. No finder credit was needed because each accepted buyer had a publicly published named work email.

## Accepted

1. **1SecondLeads:** the [first-party site](https://www.1secondleads.com/) says it builds and runs client outbound engines and identifies Ivan Malinovski as Founder and Operations Head. The [LinkedIn job](https://mk.linkedin.com/jobs/view/cold-outbound-campaign-manager-gtm-engineer-at-1secondleads-4463036526) displayed as two weeks old and covers email and LinkedIn delivery across client accounts. The [first-party blog](https://blog.1secondleads.com/best-b2b-lead-generation-agencies/) publishes `ivan@1secondleads.com`. BounceBan returned `deliverable`, score 97, `is_accept_all=true`.
2. **IGTMS:** the [first-party team page](https://igtms.com/about-us) says the team installs revenue systems for client companies and identifies Lejs Hajradinovic as Head of GTM and Cold Outreach with `lejs@igtms.com`. A [9 October job listing](https://www.mediabistro.com/jobs/3543100878-outbound-campaign-manager) covers client campaign delivery, domains, inboxes, warm-up, and deliverability. BounceBan returned `deliverable`, score 99, `is_accept_all=false`.
3. **Sendō:** the [first-party site](https://www.sendo.agency/fr/home) describes managed GTM engineering, data, cold and warm outreach, and identifies Raphaël Tourenq as cofounder. His [4 August hiring post](https://www.linkedin.com/posts/raphaeltourenq_were-hiring-again-full-remote-dear-network-activity-7490345526761140224-GaQ6) covers client LinkedIn and cold-email campaign operations and publishes `raphael@sendo.agency`. BounceBan returned `deliverable`, score 97, `is_accept_all=true`.

All three were checked against `data/suppression.csv` and the canonical dataset before verification. No match was found. The positive verifier results are provider assessments, not observed delivery, and the accept-all flags remain visible.

## Other dispositions

| Company | Disposition | Reason |
| --- | --- | --- |
| IGTMS | accepted | Cleared all gates. |
| 1SecondLeads | accepted | Cleared all gates. |
| Sendō | accepted | Cleared all gates. |
| Gelo | uncertain | Relevant hiring is recent, but the company also sells sending inboxes; the partner or competitor boundary remains unresolved. |
| Reverrr | uncertain | Strong agency and role evidence, but no visible publication date was established. |
| Ciridae | not fit | The role operates the software company's own outbound motion rather than managed client campaigns. |
| Procurify | not fit | Software company hiring for its own pipeline campaigns. |
| Manatal | not fit | Software company building its own outbound system. |
| Snipe Outbound | duplicate | Existing canonical row. |
| Six Figure Consulting | duplicate | Existing canonical row. |
| SalesCaptain | duplicate | Existing canonical row. |
| Hypergen | suppressed | Public InboxKit partner already in the suppression list. |
| Zero Risk Growth | older | Relevant role was published outside the 90-day measurement window. |

## Yield and next batch

This consecutive search-selected batch produced 3 accepted rows from 13 dispositions. That is useful progress, but it is not a population yield estimate. Continue the same fixed rule in another batch, prioritizing first-party or dated job pages and checking duplicates and suppression before contact work.
