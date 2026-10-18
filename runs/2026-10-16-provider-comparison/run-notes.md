# Ten-buyer email provider comparison, 16 October 2026

## Question and sample

The operator asked whether the waterfall was relying only on BounceBan and requested a ten-record test of Icypeas and Datagma before changing the order. This is a **provider comparison on ten already qualified agency buyers**, not ten newly sourced leads. Using buyers with an existing named address let both finders receive the same name and domain, and let Icypeas verification be compared with saved BounceBan results without paying to recheck the same address. The sample was selected from the [second-pass sheet](../2026-10-15-second-pass/leads.csv): it excludes the five buyers previously checked with Icypeas and the four buyers previously queried with Datagma. It is small and search-selected.

The working company-fit rule remains agencies running managed cold email for clients. Hiring and dated named-client cases remain the two candidate buying signals. Each buyer's earlier fit, signal, identity, source, and suppression review remain in the second-pass run; this comparison did **not** requalify those facts or add rows. No email was sent or imported.

## Method

- **Finders:** Query [Icypeas email discovery](https://api-doc.icypeas.com/find-emails/email-discovery/) and [Datagma Find Work Verified Email](https://datagmaapi.readme.io/reference/ingressservice_findemailv8) with the same buyer name and agency domain. Count an exact match to the existing email separately from a vendor `FOUND` or `Valid` label. A no-result is a miss, not proof that an address is invalid.
- **Verifiers:** Query [Icypeas email verification](https://api-doc.icypeas.com/find-emails/email-verification/) for each existing address. Compare its raw result with [BounceBan results already saved](../2026-10-16-email-verification-pilot/remaining-bounceban.json). No new BounceBan credit was spent. All ten prior BounceBan results were `deliverable`, score 97, with `is_accept_all=true`.
- **Costs:** [Icypeas publishes](https://api-doc.icypeas.com/how-works/credit-cost/) one credit per found email and 0.1 per tested email. The ten calls imply about eight finder credits plus one verification credit at those published rates; the account balance was not available in the responses. Datagma reported `creditBurn=1` on five found results and `0` on five misses. Its returned `currentCredit` shifted from 96 to 92 across calls but appeared to lag individual burns, so treat per-response burn as the better observed measure. No credits were bought.

## Results

| Measure on the same ten buyers | Icypeas | Datagma | BounceBan |
| --- | ---: | ---: | ---: |
| Finder returned exact saved address | 8/10 | 5/10 | Not a finder |
| Finder found an address on the two Icypeas misses | Not applicable | 0/2 | Not a finder |
| Verification of the saved address | 10/10 `FOUND`, `ultra_sure` | Finder's `Valid` on 5/10; no separate verification was run | 10/10 prior `deliverable`, score 97, all flagged accept-all |

[The compact comparison](comparison.csv) shows every buyer, source, exact match, and verdict. [The sanitized API record](comparison.json) preserves the returned fields used in the comparison without credentials. Icypeas missed OneGTM and Outreachify as a finder while its verifier returned `FOUND` for the addresses already known at both agencies. Both finders missed OneGTM; its work address is published by [the agency itself](https://getaob.com/how-i-work). Datagma did not add an email on Icypeas's two misses in this sample.

These counts measure **recovery of previously collected candidate addresses**, not actual mailbox existence, send outcomes, independent finder accuracy, or expected yield on fresh prospects. Icypeas and BounceBan can share the same blind spot on accept-all domains. The prior [negative-control pilot](../2026-10-16-email-verification-pilot/run-notes.md) rejected two invented addresses with BounceBan, while Icypeas had a `NOT_FOUND` result on a previously clear-valid Newlead address. No provider can be called infallible from this evidence.

## Revised working waterfall

1. Search first-party pages for a named buyer's work address. If one is available, do not spend finder credits to rediscover it.
2. When a named address is missing, try **Icypeas email discovery before Datagma** while existing credits last. In this sample Icypeas recovered more known addresses at the same published one-credit-per-found-email scale, and Datagma had no incremental match on Icypeas misses. Keep Datagma available as a fallback: zero incremental yield in two misses is too small to prove it will never help. Other usable finders remain fallbacks according to access and balance. Stop when a suitable buyer-address match is found.
3. For verification, retain **BounceBan first on catch-all or otherwise ambiguous agency addresses** while existing credits last. Its 23-address prior pilot and negative controls give the strongest local evidence for this specific problem. Use Icypeas as fallback or for a conflict, not automatically after every clear BounceBan result. Preserve the accept-all flag and raw verdict. The 10/10 positive agreement here supports availability of Icypeas but does not justify calling it a stronger verifier or guaranteeing delivery.

The next useful test is on **consecutive newly sourced buyers with missing emails**. Record incremental finds, qualified rows, actual credit debit, and verifier conflicts. If this order fails on fresh prospects, change it again. Qualified research rows: unchanged at 28; send-ready draft rows: unchanged at 26. New leads and new send-ready rows in this comparison: **zero**.
