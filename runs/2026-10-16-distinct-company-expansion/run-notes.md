# Distinct-company expansion, 16 October 2026

The user requires 100 distinct companies with one buyer each. Multiple buyers at an existing company do not count as new company progress. The earlier 61-profile Lusha search was enrichment of existing domains, not evidence that relaxed sourcing found more companies.

Minimum company fit: a public company page describes delivery, construction, or operation of client cold-email/outbound services or infrastructure. Record a concrete operational detail, client example, testimonial, campaign volume, or relevant hire as the activity signal. A single first-party page may prove both facts. Neither a named client nor a dated event is mandatory. Operational evidence supports likely infrastructure relevance; it does not prove purchase intent or dissatisfaction with a current provider. Recency is recorded where known, never invented.

One named professional buyer, LinkedIn profile, sourced work email, actual verification status, source URLs, suppression check, and unique company remain necessary for the final contact sheet. Catch-all work emails are allowed with the risk flag visible. Missing contacts stay in the company inventory until enriched.

`companies.csv` records newly researched company matches. This is a staging inventory, not the final contact sheet and does not increase the canonical count by itself. Sources were fetched using Exa on 16 October. Metrics and testimonials are the agencies' own claims and are used as operational evidence, not independently proven customer outcomes. Public customer/partner suppression and canonical-domain comparisons are applied before enrichment.

## Completed in this pass

Five new companies entered the canonical list: TechGTM Systems, Leveraged Outbound, DFY Meetings, Smarter Outbound, and ColdIQ. Buyer identity was checked against first-party pages and professional LinkedIn profiles. Kyle, Ivan, and Michel have explicitly published named work emails. Papa and Michael use named addresses from Hunter saved in the prior real project research; those addresses were freshly verified, not reconstructed from patterns.

BounceBan balance was 66 before this pass and 61 after five checks. All five returned `deliverable`; Kyle, Papa, Michael, and Ivan had score 97 and accept-all true, while Michel had score 99 and accept-all false. Provider verdicts are probabilistic. No paid credits were purchased. The five rows passed the existing suppression and duplicate export gate with no exclusions.

Initial checkpoint: 34 to 39 distinct companies, with 37 provider-assessed send-ready drafts. This checkpoint was superseded by the follow-up below.

The company inventory has 39 dispositions: 30 fit-and-activity matches (including the five initial completed rows), one fit-only record with partner-attributed results, six records needing email-channel evidence, one software-only record, one newsletter/data-only record, and one failed fetch. Company service and activity facts can share a source page; no recent-event requirement was reintroduced.

## Follow-up: 25 staged companies processed

Twenty-four of the 25 staged company matches now have complete named-buyer rows with LinkedIn, sourced work email, BounceBan verdict, company evidence, and a sourced first line. They were added to the canonical list, rather than left only in staging. `enriched-buyers.csv` stores buyer and provider evidence; `enriched-leads.csv` stores the joined lead rows; `enriched-export/` stores this batch's checked exports. The root `leads.csv` and exports preserve the initial five-company pass.

At this checkpoint, final snapshots contained **63 distinct companies** and **59 draft send-ready contacts**. Forty-one send-ready addresses carried an accept-all flag. Four final-sheet contacts used alternate email domains and remained outside send-ready. The follow-up 24 passed duplicate and suppression checks with zero exclusions; 22 entered send-ready. All provider verdicts remain probabilistic. The later final expansion supersedes these totals.

Icypeas supplied most named addresses; published professional addresses, Lusha, and Findymail recovered other buyers. Lusha restricted two profiles, so alternative buyers/providers were used. Hunter had no usable credits; previous Apollo/Prospeo access failures were not treated as successful lookups. Keyless Exa MCP hit its free limit; the existing direct Exa key and web sources were used. Automatic approval review rejected the Datagma query-key request; other providers completed the usable rows. No new credits were purchased.

BounceBan balance decreased from 61 to 35 in this follow-up: 24 deliverable named addresses and two undeliverable SaaS Outbound alternatives. The initial five checks had previously decreased 66 to 61. Each retained row records its verifier receipt ID, score, date, and accept-all flag.

### SaaS Outbound held, not counted

Icypeas found no usable address for the founders. Findymail returned `annus@saasoutbound.co` for Annus Bin Zia and `awais@saasoutbound.co` for Awais Bin Zia. BounceBan returned **undeliverable**, score 0, accept-all false for both (receipt IDs `bh3-68604b1a` and `rs2-af22ee62`). On the final source recheck, https://saasoutbound.net/ redirected to an Account Suspended page. The earlier fit match therefore does not justify a current completed prospect row. Its staged disposition remains visible; neither invalid email appears in the final sheet.

### Buyer details worth preserving

- Octopus Outbound: current professional display name Hemlata Pokharel uses `/manisha-pokharel`; Findymail returned the corresponding `manisha@` address. The alias and accept-all uncertainty are recorded in the row.
- CIENCE: Thomas Cornelius is founder and CEO of parent graph8, rather than being described as CIENCE's current operating CEO. Company/parent sources support the relationship.
- Pearl Lemon Leads and Salesaladin: named emails use alternate group/company domains. They remain review-only under the existing export gate.

This pass left 37 companies to find. The [subsequent final expansion](../2026-10-16-final-expansion/run-notes.md) supplied those 37, reaching **100 distinct companies and 92 draft send-ready contacts**. No outreach was sent or imported.
