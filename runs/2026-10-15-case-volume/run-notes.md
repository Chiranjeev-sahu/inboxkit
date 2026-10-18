# Named-client case signal pilot

Run on 15 October 2026. ICP: agencies that manage cold email for clients. This is a case-signal sourcing experiment, not the assignment's 100-row submission. No outreach was sent and no cash purchase was made. Existing provider credits may have been consumed.

## Rule set before searching

- Company fit: a public first-party page shows managed cold email for clients, including an agency that operates a client's outbound system.
- Candidate signal: a **named client** and dated, attributable cold email engagement or result inside the last 90 days. A recently edited page by itself does not establish recent client work. The 90-day window is an experimental measurement, not a permanent ICP constraint.
- One infrastructure owner or founder per agency. A named work email must pass an independent verifier before it is called valid. Catch-all and missing emails stay out of send-ready.
- Search snippets only identified candidates. First-party fit and signal pages were inspected before qualification. No geography filter was applied.

## New domains examined

| Agency | Disposition | Evidence and reason |
| --- | --- | --- |
| [Nividh](https://nividh.com/about/) | fit_and_signal | Its [iMeta Technologies case](https://nividh.com/agencies/imeta-technologies/) states managed outbound with activity through 5 August 2026. [Authors page](https://nividh.com/authors/) names the founder; [Harsh's LinkedIn](https://www.linkedin.com/in/hershey2776) and Lusha preview corroborate his role. Named email unresolved. |
| [OneGTM](https://getaob.com/how-i-work) | fit_and_signal | Its [Coastal Recruiting case](https://getaob.com/coastal-recruiting-case-study) says it ran candidate cold email and LinkedIn through September 2026, with results through 29 September. Garrett publicly lists `gw@getaob.com` on the fit page; independent Reoon says catch-all. OneGTM also has a hiring signal, so signal groups are not exclusive. |
| [YBOS](https://ybos.ai/about) | fit_and_signal | [Case page](https://ybos.ai/case-studies), last updated 29 September, calls WorkVentures a live cold email client campaign. [Team page](https://ybos.ai/team) names Nathan as the infrastructure owner. A named work email is missing and the LinkedIn match needs corroboration. |
| [Tirvio](https://tirvio.com/results/) | signal_uncertain | Named Kravo result and Smartlead story are visible, but the current page does not date the Kravo engagement within the test window. The dated Smartlead story is about Tirvio, not a newly dated client engagement. |
| [Montazzo](https://montazzo.com/lead-generation-agency-london/) | signal_uncertain | Its [ScoutLab case](https://montazzo.com/case-studies/scoutlab/) was updated in September and names the client, but the page does not establish when the outbound engagement occurred. An updated case page alone does not satisfy the rule. |
| [ColdIQ](https://coldiq.com/blog/best-cold-email-agencies) | not_fit for this pilot | It runs managed outbound, but its [inboxes page](https://coldiq.com/inboxes) also sells domains and mailboxes that overlap InboxKit's product. The [August client account](https://somethinginc.com/blog/coldiq-multichannel-reply-rate-case-study/) found here also leaves the client unnamed. Keep this overlap visible rather than treating it as an ordinary agency lead. |
| [Luxite](https://luxiteai.com/results/sarah) | fit_only | Its recruiting case identifies only Sarah and her role, not a named client company. |

Search also resurfaced eight previously examined domains: Understory, Lead Gen Jay, RevenueFlow, Groundswell, BuiltDiffernt, Seqnced, ReplyLead and GrowthPal. They were not counted as new agencies or new rows. The last two had already been marked uncertain on signal recency. The first six have case evidence in earlier pilot files. A case page with several clients still gives at most one first-pass agency row.

## Contact and provider outcomes

- Hunter's free account endpoint reported **0 remaining** search credits (50/50 used), **0 remaining** verification credits (100/100 used), and a **30 October 2026** reset date. This reports account availability at lookup time; the user's expiry email might describe another credit bucket.
- First-party search found Garrett's named work address. Reoon returned `catch_all` and `is_safe_to_send=false`, so it is held from send-ready.
- Findymail lookup returned no usable result for Harsh Sachdev and Nathan Garcia. The calls did not reveal a named address. No outcome was inferred from the mere presence of a key.
- Lusha account usage showed a free plan with 37 credits remaining before the preview. A two-contact preview cost one search credit. Harsh matched Nividh but offered **phone only**, not email, as a revealable field. The Nathan lookup returned a different `ybos.fr` company and a different LinkedIn URL; that record was discarded. No phone reveal was purchased with included credits.
- Prior Apollo and Prospeo attempts returned 403 and 429 respectively; their usable capacity remains unresolved. They were not retried on these names just to exercise the waterfall. MillionVerifier had recently returned errors, so Reoon handled the one actual address.

## Measured output and comparison

- **7 new domains examined**: 3 fit with dated named client work, 2 signal-uncertain, 1 fit-only under the named-client rule, and 1 with direct product overlap excluded from this pilot.
- **3 new company-signal candidates**, but only **1 complete buyer/email row**; it is catch-all. The mechanical export has **1 qualified row and 0 send-ready rows**, with 2 excluded for missing required contact fields. No duplicates or suppressions in this run.
- Earlier hiring volume research examined 25 organizations and found 8 distinct recent fit+signal accounts across its pilot and earlier runs, with 3 clear-valid buyer emails. This new case search is smaller and search-selected. It cannot establish a statistically reliable yield difference, but it provides no evidence to displace hiring as the provisional primary signal.
- Across earlier work, six case agencies already had date-supported client evidence; the new search adds three company-signal candidates. Their email outcomes remain the bottleneck. Count these as an observed pool, not as nine ready rows.

The case signal is useful for specific first lines and can supplement hiring where the evidence is strong. It is not yet credible as the sole path to 100 complete rows under the current 90-day and named-client rules. Test one broader, clearly stated evidence window or a third signal before promising scale. Any rule change must be recorded, and uncertain rows must not be silently promoted.

The run's `leads.csv` is the working sheet. `qualified.csv`, `send-ready.csv`, `excluded.csv`, and `audit.json` were produced by `python scripts/prepare_export.py runs/2026-10-15-case-volume/leads.csv`. No campaign copy or send action was generated in this run.

## Follow-up provider comparison after the operator's question

We tested the same query, `cold email agency case study named client September 2026`, once in each search provider using existing credits, and also checked the Codex web search result. This was a **single-query probe**, not a benchmark of overall provider quality.

| Provider | Observed top-ten result mix | Practical role from this probe |
| --- | --- | --- |
| Exa Search API | Returned several agency case pages, including Understory, SMGP, Lead Gen Jay and Groundswell. Some were existing leads and some failed the date rule after inspection. The API reported `costDollars.total=0.007` for the call. | Promising candidate discovery. Read original pages and dates before qualification. |
| Tavily basic Search API | Top ten were mostly directories, guides and tool articles rather than agency client cases. | Backup search with different queries; this one query did not show incremental qualified leads. |
| Firecrawl Search v2 | Top ten strongly overlapped Tavily's generic results. | Search may still help in other query shapes, but was weak on this one. |
| Codex web search | Found Understory and other first-party cases, including previously unseen Newlead and Modern Inbound pages that still need qualification. | Useful baseline and follow-up search without spending these API credits. |

We then used one Firecrawl **scrape**, with `proxy=basic`, on the [SMGP / BRVC page](https://smgp.co/case-studies/brvc-67000-new-client-revenue-cold-email/) returned by Exa because the Codex web reader could not fetch it. Firecrawl extracted the page successfully. Its own source note dates the BRVC testimonial to **January 2026** and does not establish recent work inside the 90-day test window, so it was not added as a qualified account. This demonstrates Firecrawl's value for fetching difficult pages without treating a search hit as proof. We did not crawl whole websites, install MCPs, or make a paid purchase.
