# Hiring versus case conversion test

Run 15 October 2026. ICP: agencies that manage cold email for clients. Target: a small matched contact test, not the 100-row submission. No outreach was sent, no credits were purchased, and the `.env` was kept local.

## Decision rules before lookup

- Hiring: public opening for cold email campaign delivery or operations at an identified agency, apparently within the 90-day test window.
- Case: named client with attributable recent engagement or results, not merely a recently edited page.
- Founder or infrastructure owner; one buyer per agency. Work email must be named and checked by an independent verifier. Clear-valid only goes to send-ready.
- Relative LinkedIn timestamps are recorded as such. They should be replaced with exact post dates if the case is used in the final sheet. The 90-day window remains an experiment threshold, not a permanent ICP rule.

## Accounts taken through contact verification

| Group | Agency | Signal and buyer | Email source and result |
| --- | --- | --- | --- |
| Hiring | [Grow Surely](https://growsurely.com/services/cold-email-agency) | [Gregory Martignoni](https://ca.linkedin.com/in/gregory-martignoni) posted about hiring a strategist for cold email campaigns; profile showed **6d** at review. | [Greg published his address](https://community.clay.com/members/9679469d-4647-4e53-852c-a98cba58aeb4). MillionVerifier **ok / good**. Qualified and clear-valid. |
| Hiring | [StackOptimise](https://www.stackoptimise.com/about-us) | [Penn Frank's GTME hiring post](https://www.linkedin.com/posts/penn-frank_were-hiring-gtm-engineer-at-stackoptimise-activity-7490059094163251200-mjGx) describes client campaign ownership; displayed **2mo**. Buyer Felix is a co-founder. | Site publishes `felix@stackoptimise.com`; Hunter also found it. MillionVerifier **catch_all / risky**, Reoon **catch_all**. Qualified, held from send-ready. |
| Case | [RevenueFlow](https://www.revenueflow.com/) | [Sales Xceleration case](https://www.revenueflow.com/case-studies/sales-xceleration) gives client start in July and calls through 9 October. Tim Carden owns technology as CMO / CTO. | Hunter found `tim@revenueflow.com`; MillionVerifier **catch_all / risky**, Reoon **catch_all**. Qualified, held. |
| Case | [Groundswell](https://groundswellgtm.com/) | [Deligatr case](https://groundswellgtm.com/case-studies/rev-ops-agency-outbound-rebuild) names six accounts taken over in June and results through 13 September. Charlie Brown founded and runs the agency. | Hunter found `charlie@groundswellgtm.com`; MillionVerifier **catch_all / risky**, Reoon **catch_all**. Qualified, held. |
| Case, boundary check | [ReplyLead](https://replylead.com/contact.html) | [CEO Coaching International case](https://replylead.com/case-studies/ceo-coaching-international/) was updated in September but the client began in 2024. Recent work is claimed, not dated precisely enough for this test. | Public `mark@replylead.com`; MillionVerifier **catch_all / risky**, Reoon **safe** with `is_catch_all=true`, ZeroBounce **valid** with `catchall_domain=true`. Conservative shared status **catch_all**. Signal uncertain, excluded. |

## Measured output

- Hiring: 2 identified agencies checked, 2 qualified email rows, **1 clear-valid**.
- Named recent case: 2 identified agencies checked, 2 qualified email rows, **0 clear-valid**.
- Boundary case: 1 additional agency checked, signal uncertain, catch-all, excluded.
- No duplicate domains or addresses; suppression file contained only its header. The export script records the mechanical audit.
- Public search and Hunter supplied the addresses. Hunter found 3 of 3 requested names. Five MillionVerifier checks, four Reoon checks and one ZeroBounce conflict check were made against existing credits. The provider balance display was not reliably reconciled to request-level debit; no monetary purchase was made.

This deliberately selected identifiable accounts and is far too small to infer 100-row yield or pick a primary signal statistically. It shows that verifier outcome, especially catch-all domains, remains the dominant contact bottleneck even when signal and buyer are clear. Hiring produced one clear-valid in this set; case studies produced none. The result supports a **provisional preference for hiring** if another larger batch repeats it, but the final signal selection remains open. The case-study arm can still be useful for personalization and a secondary signal.

## Further sourcing observations

- [Growbots' opening](https://workpivot.online/job/account-manager-client-success-remote-us) is recent and identifiable, but the role is client success rather than email operations, and Growbots mixes software with managed service. It was screened out of the strict matched test.
- Several dated agency openings identified in [the search batch](../../docs/signal-search-batch.md) hide the employer, so they cannot become agency rows.
- A case page yields at most one first-pass agency row, even when it contains many named clients. A recent update cannot be treated as a new client win without evidence of when the engagement began.
