# Fresh agency sourcing test

**Date:** 16 October 2026
**Target:** 10 consecutive candidates examined before any scale decision.
**ICP fit rule:** a public source must show that the company runs managed cold email or outbound campaigns for clients.
**Candidate buying signals:** (A) a relevant hiring post for client campaign or sending operations, or (B) a named client case published or updated within the 90-day test window. The 90-day window is a measurement for this experiment, not a permanent ICP rule.

## Examined candidates

| Candidate | Disposition | Evidence and next action |
| --- | --- | --- |
| GrowthPal.io | `signal_uncertain`, contact unresolved | [Agency home](https://growthpal.io/) describes managed outbound systems and client campaigns. The [case index](https://growthpal.io/case-studies/) was updated 4 October 2026, but the agency's [canonical information](https://growthpal.io/llm-info/) explicitly says not to describe Passionfruit as a GrowthPal client engagement because that work was led by the founder at a previous agency. Fit is strong; the current-company buying signal is not established. |
| Rev Ascension | `signal_uncertain` | [Carbon Box Media case](https://revascension.io/case-studies/carbon-box-media) appears recent and describes managed cold email and calling, but the page could not be fetched in this session. Do not add as qualified until the source can be re-opened and the agency buyer is established. |
| Palmstone Partners | `signal_uncertain` | [Argorant case](https://argorant.com/case-studies/palmstone-partners-agency-campaigns) clearly says the agency runs outbound as a service, but the case publication date and a first-party agency page were not established. Keep as a research lead, not a qualified row. |
| GrowthGrid | `fit_only` | [First-party site](https://www.growthgrid.org/) clearly describes end-to-end cold email for cloud consulting clients and names founder Neta Arbel, but no dated hiring or named-client case signal was found in this pass. Revisit with a signal search. |
| Understory Agency | `duplicate` | Existing row in the second-pass input; its PatientNow case is already tracked. |
| Groundswell | `duplicate` | Existing row with the Deligatr case. |
| RevenueFlow | `duplicate` | Existing row with the Sales Xceleration case. |
| Danish Lead Co. | `duplicate` | Existing row with the TobinLeff case. |
| Modern Inbound | `signal_uncertain` | Recent case index was found, but client names were anonymized, so it does not meet the named-client signal rule. |
| Gelo | `signal_uncertain` | Relevant campaign-manager hiring evidence was found, but the company also sells sending inboxes and the fit boundary needs a deliberate partner/competitor decision before adding it. |

## Yield

No new company passed both the fit and current-company signal screen in this test. Five were uncertain or fit-only, four were duplicates, and one was held for a partner/competitor decision. The current bottleneck is evidence quality and contact resolution, not a need to loosen the fit rule. One Lusha credit was spent on a domain-mismatched result; no row was accepted from it, and no rows were invented to reach a target.

## Contact lookup result

The first finder attempt was Lusha, filtered to `growthpal.io` and founder or operations titles. It returned four records for the separate `growthpal.com` M&A company, including a Prabesh Khanal record, and charged one existing Lusha credit. Because the provider domain did not match the researched company, none of those records was accepted. This is a provider identity mismatch, not evidence that GrowthPal.io lacks a buyer or email.

Apollo's people search was also tried without revealing a contact. The connected plan denied the search endpoint (`API_INACCESSIBLE`), so no Apollo credit was used and no result was accepted.

## Next action

Find a current-company hiring signal or a clearly attributed GrowthPal.io client case before trying another finder. If that evidence appears, resolve a named work email with an explicit domain-identity check and then run the same BounceBan-first verification and suppression checks. Repeat the fixed-rule search in batches of ten only after one new company clears both evidence gates.

## Consecutive follow-up batch

The next search batch produced these dispositions:

- **Pipeline Playbooks:** accepted. Its [first-party site](https://www.pipelineplaybooks.com/) describes done-for-you cold email and LinkedIn delivery, and its [LinkedIn role](https://uk.linkedin.com/jobs/view/gtm-engineer-cold-email-campaign-manager-at-pipeline-playbooks-4438632639) describes a current hire to oversee client campaign decisions. The site publishes Joel Wylie's named address. ZeroBounce returned `valid` with `catchall_domain=true`; it was added to the main research input as a provider-assessed valid row with the flag preserved.
- **Beanstalk Consulting:** fit and signal evidence were strong, but ZeroBounce returned `do_not_mail` with `role_based_catch_all` for the founder address. It remains uncertain and out of send-ready pending another named buyer or a clearer result. Sources: [about page](https://www.beanstalkconsulting.co/about), [current company hiring post](https://www.linkedin.com/company/beanstalk-consultingco).
- **Cymate:** relevant hiring and fit evidence was found, but the company is already in the public InboxKit suppression file. It was not added.
- **Zero Risk Growth:** fit and outbound service evidence were found, but no named current hiring or named-client case signal was established in this pass. It remains fit-only.

This follow-up adds one qualified row after examining four new companies. The combined test therefore has one accepted new company, several explicit holds, and a measurable provider failure. It does not justify claiming a general 100-row yield yet.

## Second follow-up search batch

- **Hypergen:** duplicate and publicly suppressed; the current job listing is another source for an existing InboxKit partner, so it was not added.
- **VelocityFlow:** duplicate of the existing row; its first-party GTM Engineer page corroborates the managed client operation but does not create a new company.
- **GTMx:** fit evidence is strong and the site shows recent campaign activity, but no qualifying hiring post or clearly attributed named-client case was established in this pass. It remains fit-only.
- **Anonymous Upwork agency posts:** relevant campaign-operations jobs were found, but the company and buyer were not identifiable from the public listing. They remain unqualified.

No new row was added from this batch. The fixed rule is producing real agency fits, but the current signal and identity gates are the limiting steps. That is evidence to keep the rule explicit while continuing consecutive searches, not a reason to fill the sheet with fit-only agencies.

## Third follow-up search batch

- **SalesCaptain:** fit and recent Senior GTM Engineer hiring evidence were found. Its [site](https://www.salescaptain.io/) describes managed cold email and LinkedIn campaigns, and the [role listing](https://remotenex.us/job/senior-gtm-engineer-6) is dated 6 October 2026. A named founder is known, but only a generic team email was found in this pass, so it remains pending contact lookup.
- **atomGTM:** fit and an open GTM Engineer or CSM hiring page were found. The [about page](https://atomgtm.com/about-us/) identifies founder Faham Zia and the [careers page](https://atomgtm.com/careers/) describes client outbound operations, but the available addresses are generic careers or hello mailboxes. Keep pending a named work email.
- **Viralnetix:** strong fit and named client proof are visible on the [first-party site](https://viralnetix.com/), but no current hiring signal or dated case publication was established in this pass. It remains fit-only.
- **Hypergen:** duplicate and publicly suppressed, as documented above.

No additional row was added from this batch. The next useful experiment is a capped finder lookup for SalesCaptain and atomGTM, with domain identity checked before any email is accepted.

## Third follow-up verification

- **SalesCaptain:** accepted after the capped contact check. The [site](https://www.salescaptain.io/) describes managed cold email and LinkedIn campaigns, and the [Senior GTM Engineer role](https://remotenex.us/job/senior-gtm-engineer-6) is dated 6 October 2026. A public event PDF publishes `bill@salescaptain.io`, while the SalesCaptain company profile corroborates the named founder identity. ZeroBounce returned `valid`, `catchall_domain=false`, with Google Workspace MX. The row was added to the main input and send-ready export. BounceBan was not called for this address in this session.

This adds one qualified and send-ready row. The test is now 36 input rows, 29 qualified, and 27 send-ready after the provider gate. It still does not support claiming a 100-row yield; the next batches should continue the same evidence and identity checks.
