# Scaling to 2,000 rows and cost per contact

**Updated 17 October 2026. Proposed scaling approach, not a completed 2,000-row run. All outreach remains draft.**

## Paragraph for the assignment

To scale to 2,000 rows, I would expand discovery across agency directories, relevant software-partner lists, company case studies, and targeted web searches, then inspect first-party evidence under the same fit and signal rules. These are candidate sources, not automatic qualification. Process 50 to 100 new, distinct companies per batch: qualify the company, identify its infrastructure buyer and LinkedIn profile, find and verify a named work email through available provider fallbacks, and generate a source-backed first line. Save completed work and failed attempts so later batches resume without repeating paid calls. Check each batch against the accumulated company list and suppression records before enrichment, then reconcile research, send-ready, and parked outputs. Measure accepted contacts per company examined, time, provider debits, and review effort; use those results to project the remaining work and change low-yield discovery sources. **The submission used $0 additional cash, but production is not free.** As an email-data example, [Findymail's $99/month credit-based Starter allowance](https://www.findymail.com/pricing/) would allocate **$0.0495 per contact if it yields 2,000 accepted contacts**. Discovery, fallback providers, agent usage, and review are additional. Neither the total production cost nor a pool of 2,000 qualifying companies has been demonstrated.

## 1. Define what the 2,000 rows represent

The assignment asks how the list scales to 2,000 rows. A research row and a send-ready contact are different outputs:

- **Research:** A distinct company and buyer, with the required fields, source evidence, verification status, and visible uncertainty. Parked contacts can remain here with their exact missing link.
- **Send-ready draft:** A research contact that also passes the current provider-verdict, identity/domain, deduplication, suppression, and explicit-hold rules. Accept-all risk stays visible separately.
- **Parked:** A retained research contact with a specific unresolved reason. Do not count it as send-ready merely to reach a target.

Our present submission is **100 research rows = 97 send-ready + three parked**. Scaling preserves those distinctions. A 2,000-row research sheet does not automatically contain 2,000 send-ready contacts. The capacity examples below use **2,000 send-ready contacts as an illustrative planning scenario**, not an extra assignment requirement. Cost per usable contact uses accepted send-ready output as its denominator.

## 2. Expand discovery before expanding enrichment

The first bottleneck is finding enough genuinely new companies. Repeating the same search can repeatedly return agencies we already examined.

| Candidate source to test | What it can contribute | What the agent must establish |
| --- | --- | --- |
| Agency directories and company listings | A broad pool of outbound, lead-generation, and GTM agencies | Whether the agency actually sells or operates client outbound infrastructure; a directory category alone is insufficient. |
| Relevant software-partner and expert directories | Agencies already working with outbound tools | Current service evidence and eligibility. Check InboxKit's own partners/customers against suppression; a partner listing is not proof of buying intent. |
| Agency case studies and client results | Concrete examples of campaign delivery or sending operations | The company behind the page, what work it performed, and any visible dates. A named client or 90-day event remains optional under the agreed rule. |
| Targeted web searches | Agencies using less obvious descriptions such as outbound systems, white-label delivery, or deliverability services | The same company-fit and operational-evidence rules, without silently broadening the ICP. |
| Similar companies surfaced from accepted agencies | Additional candidate vocabulary and adjacent providers | Independent evidence for each new company. Similarity is a discovery aid, not acceptance. |

Use the available search tools, such as Exa, Tavily, or the agent's web search, to locate candidates. Fetch relevant pages with available page/browser tools or Firecrawl when useful. Their exact order depends on working access, remaining credits, and incremental results. This is a proposed routing approach, not a claim that every provider has capacity for 2,000 rows.

For each source or search family, record how many new candidates it contributes and how many ultimately become accepted contacts. When a source mostly returns duplicates or weak fits, change the discovery angle. Do not relax qualification automatically. The existence of 100 accepted companies does not establish that this same segment contains 2,000 reachable, eligible companies.

## 3. Move each batch through an ordered workflow

A working batch size of **50 to 100 new companies** makes progress inspectable. It is a proposed operating size, not a tested throughput guarantee or a required software limit.

| Stage | Work performed | Saved outcome |
| --- | --- | --- |
| Screen candidates | Normalize domains and company names; compare with previously examined organizations and suppression before spending contact credits. Treat known aliases/group domains as one organization. | New eligible candidates, duplicates, suppressed organizations, and reasons. |
| Qualify the company | Open evidence for company fit and client outbound activity. Record dates when visible and preserve older/undated labels. | Qualified, uncertain, or rejected disposition with URLs and reasoning. |
| Identify the buyer | Prefer the founder, head of growth, or infrastructure owner. Confirm the personal LinkedIn profile and relevant role. | One selected buyer per company, with alternatives retained as lookup attempts. |
| Find a work email | Check public named addresses, then use suitable providers in a waterfall. Move on after a no-result, mismatch, restriction, or unavailable provider. | Named address and its source, or an explicit unresolved lookup. |
| Verify and resolve exceptions | Preserve exact provider verdicts and accept-all flags. Review alternate-domain relationships; honor targeted evidence holds and clear-verdict conflicts. | Provider-valid, ambiguous, unknown/conflicting, or invalid outcome, with reasons. |
| Personalize and export | Write a first line from the recorded evidence. Run mechanical field, duplicate, suppression, and export checks. | Research sheet, draft send-ready subset, parked subset, and an audit. |

Qualify companies before spending scarce contact credits. Write the final personalized line after the company and contact work is sufficiently complete to justify the effort. Stop a provider waterfall when the applicable evidence rule is met; calling every service for every row would consume credits without necessarily improving the list.

A failed email lookup should not immediately discard a qualified company. Try a suitable alternative provider or buyer, record what happened, and park the company when no usable route remains. A clear verifier conflict stays visible; do not keep buying checks just to obtain the desired verdict. Existing positive results and sources can be reused during the run when still applicable; record their dates so later refresh decisions are explicit.

## 4. Preserve progress and deduplicate across batches

The current export script checks the CSV supplied to it. **It does not automatically maintain a cross-batch database, schedule research, or resume provider jobs.** The larger CSV alone is not the scaling solution.

The proposed operating procedure uses the existing files:

1. Maintain one accumulated candidate/attempt inventory containing normalized company domain, source, disposition, selected buyer, provider attempts, and the remaining next action. Save concise provider outcomes and relevant timestamps alongside each batch.
2. Compare new candidates with that inventory and the suppression list before enrichment. Reuse completed evidence rather than researching the same organization under another spelling or domain.
3. Save each batch's researched rows and run notes. If interrupted, resume at the next incomplete stage instead of restarting discovery and paid lookups.
4. Combine accepted research rows into a cumulative input and run the existing export gate across that full input. Checking only a new batch would miss duplicates between batches.
5. Inspect duplicate exclusions and known aliases. The agent must judge organization/group equivalence; the script cannot infer every parent, subsidiary, or rebrand from spelling alone.
6. Reconcile cumulative research = send-ready + parked. Keep rejected, suppressed, duplicate, and failed attempts in the attempt history rather than silently losing them or counting them toward the target.

This procedure is a proposal for coordinating more work with the current file-based workflow. It has not been demonstrated at 2,000 rows and does not assume a new application, database, or parallel-agent architecture.

## 5. Measure the funnel and locate the bottleneck

Record every consecutive batch, including failures. Do not measure only the final successful contacts.

| Measure | Calculation or record | Why it matters |
| --- | --- | --- |
| Discovery freshness | New unique unsuppressed candidates / raw candidates collected | Shows whether a search source is expanding the pool or recycling it. |
| Company qualification rate | Companies meeting fit and signal rules / new unique companies examined | Shows whether discovery is targeting the right organizations. |
| Accepted-contact yield | New send-ready contacts / new unique unsuppressed companies examined | Converts a contact target into an estimated research workload. |
| Contact recovery | New addresses recovered by each fallback, plus its calls and debits | Shows which fallbacks improve coverage and at what cost. |
| Active work time | Agent processing and operator review time by stage | Identifies slow evidence, identity, email, and personalization work. |
| Elapsed time | Batch start/finish and time spent waiting for rate limits or provider jobs | Prevents active work estimates from becoming unrealistic completion promises. |
| Parked reasons | Counts for missing buyer, missing email, verification conflict, domain proof, or another explicit hold | Shows what blocks progress and what evidence would resolve it. |
| Data and usage cost | Actual provider debits, purchases or allocated subscription amounts, and agent usage | Supports a production estimate based on work performed. |

The current **97/100 ready share is not an overall 97% sourcing yield**. Those 100 rows are selected survivors of earlier searches, failed lookups, exclusions, and reviews. It also says nothing about observed bounces because no messages were sent.

### Illustrative workload calculation, not a measured forecast

Suppose a consecutive batch of **100 new unique, unsuppressed companies** produces:

| Funnel stage | Companies/contacts remaining |
| --- | ---: |
| New unique companies examined | 100 |
| Meet company fit and operational-evidence rules | 70 |
| Correct buyer identified | 60 |
| Named address receives a positive provider verdict | 48 |
| Pass remaining evidence and export checks | 40 |

This assumed batch yields **40 accepted contacts / 100 companies examined = 40%**. Producing 2,000 accepted contacts would then require approximately **2,000 / 0.40 = 5,000 new unique companies examined**. Raw discovery would need to produce more candidates because duplicates and suppressed organizations are removed before this denominator.

If the existing 97 send-ready contacts count toward that 2,000-contact planning scenario, the remaining target is **1,903**. At the same assumed 40% yield, it would require approximately **4,758 additional unique companies examined**. This is arithmetic, not evidence that those companies exist or that later batches will preserve the yield.

Time follows the same logic. **Estimated active work hours = additional companies to examine / measured companies processed per active hour**, plus any review effort not already included in that measured rate. Track waiting time separately and avoid double-counting review. Re-estimate after later batches; the easiest companies may be found first.

## 6. Keep quality visible as volume grows

The agent remains responsible for the evidence on every accepted row. The export script checks required fields, structure, duplicates, suppression, proof-decision fields, and explicit holds; it does not prove that a source actually supports the claim.

At each batch boundary, review the source evidence and first lines for factual support. Inspect all unresolved domain/identity cases before promotion and sample ordinary completed rows to check for drift, such as a generic inbox assigned to a founder, a wrong-company LinkedIn profile, or an undated claim described as recent. If a sample reveals a repeated error, inspect the affected batch or source and correct the pattern before expanding.

Keep the accepted catch-all policy unchanged: a positive provider deliverable/verified verdict can be valid while accept-all=true stays visible. Unreported flags stay unreported; the three existing literal unknown flags remain visible. A targeted hold or conflicting clear negative still prevents promotion. Scaling does not justify removing those distinctions.

## 7. Scale according to evidence, credits, and source availability

- Continue discovery sources that produce genuinely new accepted contacts at manageable effort. Change sources when duplicate rates rise or qualification yield falls.
- Respect provider rate limits and save the pending state. A temporary rate limit is a reason to pace or use a suitable fallback, not to rebuild the architecture.
- Check usable balances before credit-consuming calls. Exhausted free credits mean switching to an available fallback, retaining an unresolved row, or reporting the capacity limit. A paid plan in a scenario is not authorization to purchase it.
- If the segment cannot supply enough qualifying companies under the agreed rules, report the remaining gap and evidence. Any ICP change requires an explicit decision; do not add multiple buyers at one company or weaken the signal silently to fill the count.

A credible scale forecast requires a measured consecutive sourcing batch under fixed rules, including failed and parked candidates in its workload and cost denominator.

## 8. Cost per accepted contact

| Cost measure | Amount | Interpretation |
| --- | ---: | --- |
| Additional cash spent on this submission | $0 | Existing access and credits were used. Previously paid subscriptions and time still have a cost. |
| Illustrative email-data subscription | $99 for one month | Published Findymail credit-based Starter scenario, checked 17 October 2026; not a purchase or a measured price for our actual waterfall. |
| Allocated provider cost if 2,000 contacts are accepted | $0.0495 per contact | $99 / 2,000, including unused subscription capacity. |
| Allocated provider cost if only 1,000 contacts are accepted | $0.099 per contact | Lower accepted output raises cost per contact even when the subscription price stays fixed. |
| Full researched-contact cost | Not yet measured | Discovery, enrichment, verification fallbacks, allocated agent usage, and human review. |

The [Findymail pricing page](https://www.findymail.com/pricing/) lists 5,000 finder credits with included verification and 5,000 separate verifier credits in that credit-based Starter scenario. It also lists prospecting plans. Confirm the applicable plan, API access, allowances, and fallback costs before purchasing. Nominal credits do not prove that the provider can find 2,000 eligible buyers. Findymail was tested as one fallback, not as the sole source for the full target.

**Full list-production cost per accepted contact = (search and extraction costs + finder and verifier costs + allocated agent costs + review hours x hourly rate) / accepted send-ready contacts.**

Include costs incurred on failed and parked candidates in the numerator. Use an explicit allocation for existing subscriptions and a stated review rate; count each expense once. Sending infrastructure and sequencer costs belong in a separate campaign-execution budget. Do not present the five-cent provider scenario as the all-in cost of a researched lead.

## Scaling summary

> I would scale discovery as well as enrichment. I would source new agencies through several channels, process them in batches, save attempts so work is not repeated, and check every batch against the accumulated list and suppression records. Then I would measure accepted contacts per company examined, active work time, and credit use. That tells me how much work remains and which stage needs improvement. The current script handles export checks; research and contact recovery remain agent-led. Five cents is a conditional email-provider example. The full production cost and the available pool of 2,000 qualifying companies still need evidence.
