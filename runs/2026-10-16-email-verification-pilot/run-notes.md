# Catch-all verification pilot, 16 October 2026

## Question and method

The prior [second-pass run](../2026-10-15-second-pass/run-notes.md) had 23 qualified addresses labeled `catch_all` by MillionVerifier or Reoon. Those tools could not establish whether the individual mailboxes existed. The operator supplied existing-credit access to BounceBan, Icypeas, and Datagma and asked to test the specialist services before relying on cheaper checks. No credit pack was bought, and no email was sent.

BounceBan's [API documentation](https://github.com/bounceban-com/skill-email-verification/blob/main/introduction.md) defines `deliverable` as its positive result, reports a score and `is_accept_all`, and charges one credit per completed standard API verification. Its waterfall hostname was blocked by Cloudflare in this environment, while the standard API worked. The first five catch-all addresses were also checked with [Icypeas email verification](https://api-doc.icypeas.com/find-emails/email-verification/). Four named buyers were checked with [Datagma's work-email finder](https://datagmaapi.readme.io/reference/ingressservice_findemailv8); finder output is corroboration of an address, not the main delivery verdict.

## Results

| Check | Observed result |
| --- | --- |
| BounceBan on all 23 previously catch-all qualified addresses | 23 `deliverable`; 22 had `score=97, is_accept_all=true`; Danish Lead Co. had `score=99, is_accept_all=false`. [Individual results](remaining-bounceban.json) and [initial five](results.json). |
| BounceBan on two invented addresses at previously accept-all domains | Both `undeliverable`, `score=0`, while `is_accept_all=true`. These controls show the service did not simply mark every address at those domains deliverable. [Controls](controls.json), [second control](second-negative-control.json). |
| BounceBan on previously clear-valid Newlead address | `deliverable`, `score=99`, `is_accept_all=false`. |
| Icypeas on five catch-all candidates | Five `FOUND` at `ultra_sure`. It returned `NOT_FOUND` for one invented address **and** for the previously clear-valid Newlead address. `NOT_FOUND` is therefore insufficient by itself to reject a lead in this small test. [Results](results.json), [controls](controls.json). |
| Datagma named-buyer finder | It returned the expected address with `Valid` for Shields Outbound and Grundwerk Digital, but `NotFound` for David & Goliath and VelocityFlow. [Results](datagma.json). |

The test supports using BounceBan's specialist verdict to resolve these 23 ambiguous SMTP results, with the `is_accept_all` flag preserved. It does **not** establish actual delivery or a measured bounce rate; no messages were sent. Vendor scores are predictions, not proof that a human monitors the inbox. A previously reported `catch_all` is an indeterminate result, not a clear `undeliverable` contradiction. The [updated lead input](../2026-10-15-second-pass/leads.csv) retains earlier raw verdicts alongside BounceBan's result, score, flag, and date.

After applying the repository's suppression and duplicate gates, the sheet remains **28 qualified research rows**. All 28 now have a positive verifier verdict, but **26 enter the send-ready draft export**. Of those 26, **20 still have `is_accept_all=true`**, two have `false`, and four have no accept-all flag from their recorded verifier. Thus the export is a set of provider-assessed delivery candidates, not 26 mailbox-confirmed addresses. Two other addresses use domains different from their agency sites; verification of delivery alone does not prove those addresses belong to the target companies, so they remain research-only pending better linkage. The [audit](../2026-10-15-second-pass/audit.json) records both counts. Nothing was imported into a sequencer.

## Provisional workflow choice

For the next agency email, find a named buyer and work address first, then use BounceBan while existing credits remain. Stop on a clear verdict; use Icypeas or other verifiers when BounceBan is ambiguous or unavailable. Keep `is_accept_all` and each raw result visible. Datagma belongs in the finder waterfall when the address is missing, not as a substitute for specialist verification. Check balances before a larger run and do not spend credits merely to exercise every provider. This order is provisional because the pilot was small, search-selected, and did not measure real bounces.
