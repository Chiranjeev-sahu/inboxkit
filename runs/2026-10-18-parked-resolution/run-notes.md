# Targeted parked-contact follow-up

**18 October 2026 | Three existing companies | Draft only**

This follow-up attempts to resolve the three holds in the canonical agency research without weakening the targeted public-address rule. It does not add companies, erase attempts or redate old verification results. Sources were inspected through public search and direct HTTP retrieval; [saved address checks](evidence/public-address-checks.json) and [current MX answers](evidence/current-mx.json) record the observations.

| Company | Finding | Current verdict |
| --- | --- | --- |
| Chief Lead Officer / Matt Bauman | [Company page](https://www.chiefleadofficer.com/) and [founder's site](https://mattbauman.me/) support the role and client outbound work. The founder publishes `matt@mattbauman.me`, which had previously failed verification, rather than the held `matt@chiefleadofficer.com`. A fresh DNS MX query for mattbauman.me returned no MX answer. No newly verified published alternative or relevant alternative buyer was established. | **Remain parked.** The held address still lacks the exact public person-to-mailbox link. The website-domain address has routing but that does not prove the mailbox's owner. |
| Leadowski / Bohdan Shtylyk | A current Lusha lookup returned the same named business address, `bohdan@leadowski.io`, with confidence A+. This is finder corroboration, not a new mailbox-verification verdict or public company publication. The [company site](https://www.leadowski.io/) did not publish a named address in the retrieved HTML. A fresh DNS MX query returned no MX answer. | **Remain parked.** Earlier Findymail-positive/ZeroBounce-negative conflict and exact-address gap remain unresolved. Another positive finder is not grounds to vote away the clear negative. |
| Caliber Outbound / Kerim Efe Ozcanli | [Company](https://caliberoutbound.com/), [About](https://caliberoutbound.com/about), [privacy](https://caliberoutbound.com/privacy) and [terms](https://caliberoutbound.com/terms) publish `info@caliberoutbound.com`, not the held `eozcanli@caliberoutbound.com`. The site describes a single operator. No other relevant current buyer with a sourced named work address was established. | **Remain parked.** A generic company inbox is not substituted for the named buyer; the targeted exact-address evidence is still missing. |

No MX answer is a routing diagnostic, not by itself a universal proof of undeliverability: SMTP can have an implicit address-record fallback. It does not resolve either existing evidence hold. The [DNS resolver endpoint](https://developers.google.com/speed/public-dns/docs/doh/json) documents the query interface used. No new mailbox verdict is claimed.

## Provider behavior and cost

The previously unavailable Lusha connection is callable. The three-profile batch returned one named Leadowski email and restrictions for the other two profiles; restricted lookups were not retried through other private-data finders. The provider reports **two credits charged**. Invalid-schema attempts before the corrected call did not return a contact; their charge was not separately established. [Sanitized receipt](evidence/lusha-followup.json).

BounceBan's [balance endpoint](evidence/bounceban-balance-before.json) confirmed available existing capacity. No new verification job was submitted: a third vote on the unchanged Leadowski address would not resolve public ownership, and the other two held addresses already have positive verdicts. Additional cash spent: **$0**. No sending, enrollment, CRM export or live campaign import occurred.

## Reconciliation

All original 100 research companies remain. **100 research = 97 draft-ready + 3 parked**. Original provider dates, statuses and accept-all flags are preserved. The canonical rows gain this follow-up provenance; the export snapshots are regenerated. This follow-up records a genuine unresolved result rather than promoting rows to hit a count.
