# Fresh signal and workflow test

Run on 15 October 2026 with the initial agency ICP. Target was a small fresh batch to exercise the newly written agent runbook, not 100 final rows. No email or LinkedIn message was sent. No paid credits were purchased.

## Rule set before sourcing

- Fit: the agency itself says it manages cold email or outbound email campaigns for clients.
- Candidate hiring signal: a dated role in client cold email campaign delivery or sending operations.
- Candidate case signal: a named client case with an attributable date within the 90-day measurement window. An update date alone does not prove that the client engagement is new.
- Buyer: founder or person responsible for campaign/infrastructure decisions. Work emails must be independently verified; catch-all remains uncertain.
- One buyer per distinct agency, no geography/language filter. The 90-day window is an experiment threshold, not a final ICP requirement.

## Sourcing log

| Company | Group | Disposition | Evidence and reason |
| --- | --- | --- | --- |
| botified | Hiring | Fit and signal; buyer/email found; valid | [Agency leadership](https://botified.ai/about), [production job listing updated 1 October](https://www.onlinejobs.ph/jobseekers/job/gtm-cold-email-campaign-specialist-contract-remote-1742066). |
| BuiltDiffernt | Case | Fit and signal; buyer/email found; catch-all | [Managed outbound agency](https://www.builtdiffernt.com/), [Market Partners case](https://builtdiffernt.com/case/market-partners), dated video 27 August and transcript check 24 September. The case measured research interviews rather than sales-qualified demos; the first line uses that actual outcome. |
| Seqnced | Case | Fit and signal; buyer found; email missing | [Agency](https://seqnced.com/about), [AgenticPM case published 26 September](https://seqnced.com/case-studies/agentic-private-markets), [founder LinkedIn](https://www.linkedin.com/in/remo-duzkale). Public search and Hunter returned no named work address; Lusha reported restricted; Findymail returned no email; Apollo returned HTTP 403. Prospeo had returned HTTP 429 in the earlier pilot and was not retried here. Do not invent `remo@seqnced.com`. |
| GrowthPal | Case | Fit; signal uncertain; buyer/email found; catch-all | [Agency and founder](https://growthpal.io/about/), [Passionfruit case updated 4 October](https://growthpal.io/case-studies/passionfruit/). The page calls its result an October month but does not give the campaign year; it was already updated on 4 October. Recency of the client work is unclear. A Lusha result for `growthpal.com` referred to a different company and was rejected. |
| Tevi Lab | Case | Fit, no qualifying recent named client case found | [Agency and founder](https://tevilab.com/about/), [case-study directory](https://tevilab.com/case-studies/). Available examples were older or anonymized. |
| Emporia | Case | Fit, no qualifying named client case found | [Managed cold email agency](https://emporiastudio.com/), [software-services case](https://emporiastudio.com/case-studies/software-services.html) is recent but masks the client name. |
| LeadHaste | Case | Fit; case has a conflict to review | [Agency leadership](https://leadhaste.com/about), [Globental case](https://leadhaste.com/case-studies/globental) is named and current but discloses that the people running LeadHaste also co-own Globental. Do not count it as an independent new-client signal. |
| Avalanche | Hiring | Identity uncertain | A [10 October campaign-operations job](https://www.onlinejobs.ph/jobseekers/job/Project-Manager-1395713) describes an agency named Avalanche, but the connection to [avalancheoutbound.com](https://avalancheoutbound.com/) was not established. No buyer lookup or verification was performed. |

Eight candidate agencies were examined; two met the current strict signal rule and had a named email, one met the signal rule without an email, one had uncertain case recency, and four failed or lacked enough evidence for this test. One of the two strict-signal rows had a clear-valid email. This is a small, search-led convenience sample and cannot estimate market-wide yield.

## Contact and verifier waterfall observations

- First-party sites and LinkedIn established named decision-makers. Lusha MCP preview was tried for botified, Seqnced, and GrowthPal. Botified and Seqnced were restricted; the GrowthPal record used a different domain and was discarded. One search credit was charged.
- Hunter found `jimmy@botified.ai` and `prabesh@growthpal.io`, each marked valid by its own finder. Hunter did not find Remo or David. Findymail found `david@builtdiffernt.com`; it did not find Remo. Apollo rejected the Remo enrichment request with HTTP 403. Provider failures were not treated as evidence that the person lacks an address.
- MillionVerifier returned `ok` / `good` for Jimmy, and `catch_all` / `risky` for David and Prabesh. Reoon returned `unknown` for Prabesh. ZeroBounce said `valid` but also `catchall_domain=true`; the conservative shared status stays `catch_all`. An additional Reoon/ZeroBounce attempt for David produced no captured result, so no agreement is claimed.
- Exact credit debit across Hunter, Findymail, Reoon, and ZeroBounce was not independently reconciled after every request. All attempted calls were within previously observed free-credit balances, and no payment was made.

## Outcome and next decision

The stricter evidence rule removed easy but weak sources, which is useful for list quality but lowers yield. Current strict, source-backed sample: 2 email rows, 1 clear-valid send-ready row. The immediate bottlenecks are reliable dated signals and named email verification, not finding agency websites. The main workflow still needs an end-to-end clean-checkout test on a new segment and enough volume to support 100 rows. Do not select the primary buying signal from this batch alone.
