# Software recruitment: independent rerun

Observed 18 October 2026. Fresh checkout baseline: `76f3329`. All outreach remains draft; nothing sent, enrolled or imported.

## Request and rules

ICP: boutique recruitment agencies placing software engineers for technology businesses, with a public named-client placement case study. Requested two distinct companies and one current founder or managing director each, with named work emails, personal LinkedIn URLs, verification, sourced first lines and draft outreach. Existing credits only, $0 additional cash; limits of 12 examined companies and 12 credit-consuming finder/verifier actions.

Fit requires explicit boutique positioning or a demonstrably small specialist team, independently led recruitment and software-engineering placements for technology clients. The signal requires a first-party named-client placement case. No recent-event cutoff or geography filter. Recruitment delivery establishes relevance; it does not establish buying intent. The default campaign's client cold-email service rule is not used.

Commercial suitability was checked before enrichment. Optiveum offers recruitment, outsourcing and hub setup. Axe Talent's own AI product is an academic resume builder. No competing mailbox/domain infrastructure offering was found in the inspected services. Employer/candidate outreach may create mailbox administration needs; current volumes, tooling, pain, budget and purchase intent remain unconfirmed. Founder vendor influence is inferred; infrastructure ownership is unproven.

## Outcome

| Measure | Requested or limit | Achieved |
| --- | --- | --- |
| Distinct retained companies | 2 | 2 |
| Current founder buyers with personal LinkedIn and named work email | 2 | 2 |
| Companies examined | maximum 12 | 4 |
| Retained research contacts | 2 | 2 |
| Draft-ready contacts | provider-valid gate | 2 |
| Parked contact rows | report actual | 0 |
| Excluded contact attempts | report actual | 0 |
| Companies not advanced | report actual | 2 |
| Credit-consuming finder/verifier actions | maximum 12 | 3 |
| Additional cash | $0 | $0 |

Research reconciles: **2 = 2 ready + 0 parked**. Contact attempts: **2 = 2 research + 0 excluded**. Duplicate and suppression counts are zero. Company-level holds are in the disposition log; they are not extra contacts in the empty review CSV.

| Company | Buyer | Case | Verification |
| --- | --- | --- | --- |
| Optiveum | Tomasz Polikowski, Co-Founder & Managing Partner | QUERTUM PL senior .NET hires | BounceBan deliverable, score 99, accept-all false |
| Axe Talent | Natalia Rostova, Founder, Headhunter & Director | Nomic Labs (HardHat) compiler engineering lead | BounceBan deliverable, score 97, accept-all true |

Work emails are in [send-ready.csv](send-ready.csv). Positive provider assessments are probabilistic and do not guarantee mailbox existence or delivery. The accept-all flag is retained separately under current policy. No contradictory clear verifier result was returned; further verifier spending stopped.

Optiveum's case is dated 15 November 2024, covering September-November 2024; Axe's case is undated. Neither is described as recent. LinkedIn direct access returned 999/cache errors. Tomasz's exact personal URL is linked by the company About page and company LinkedIn lists him; Natalia's publicly indexed personal profile agrees with the current company founder biography. Full personal profiles could not be inspected.

Ripple has a named developer placement case but uncertain current software specialist/boutique fit. Wedoe Search Group meets literal fit with Later engineering placements, but its warm-referral model and four-search capacity cap gave weak evidence of need for scalable cold-email infrastructure. No enrichment credits were spent on either. Public InboxKit partner/customer checks and local suppression had no match; public lists cannot prove private account status.

## Review the package

- [Draft-ready contacts](send-ready.csv)
- [Individual first lines and draft email/LinkedIn sequence](draft-outreach.md)
- [Parked contacts, header only because there are none](review-parked.csv)
- [Input rows](evidence/leads.csv), [company dispositions](evidence/company-dispositions.csv), [source snippets and evidence judgments](evidence/source-evidence.json)
- [Audit](evidence/audit.json), [research export](evidence/qualified.csv), [excluded attempts](evidence/excluded.csv)
- [Run definition](evidence/run-definition.md), [full notes and recovery log](evidence/run-notes.md), [credit ledger](evidence/credit-ledger.csv)
- [Icypeas receipt](evidence/01-icypeas-tomasz-finder.json), [Tomasz verification](evidence/02-bounceban-tomasz.json), [Natalia verification](evidence/03-bounceban-natalia.json)
- [Suppression review](evidence/suppression-review.json), [validation results](evidence/validation-results.json)

Three actions consumed existing credits: Icypeas 1 (48.900001 to 47.900001) and BounceBan 2 (95 to 93). Balance checks were free. Nine allowed finder/verifier actions remain. No paid upgrade or new dependency was needed. Network sandbox failures were solved by the authorized network execution route; browser page failures used direct public HTML/documentation fallback. Windows page-print encoding was fixed by setting UTF-8. Details and sanitized provider results are preserved under evidence.

## Offer, cadence and scale

The reviewed offer is the documented [30-minute InboxKit demo](https://www.inboxkit.com/demo) to assess mailbox/domain administration for recruitment outreach. The [draft sequence](draft-outreach.md) interleaves four emails and three conditional LinkedIn touches over 20 days, with two alternative first emails and reply STOP in every email. InboxKit mailbox and automatic SPF/DKIM/DMARC claims link to the inspected [product homepage](https://www.inboxkit.com/). Sender identity remains an explicit draft placeholder. Any future activation requires monitored reply opt-outs and private account suppression reconciliation.

This two-contact sample establishes neither a conversion rate nor the available market. Its three provider actions are observed costs for these contacts only. Scaling requires further consecutive batches, current provider capacity and measured research effort; the [campaign feasibility note](../../docs/campaign-feasibility.md) and [cost method](../../deliverables/scale-cost.md) distinguish target requirements from forecasts. No new success rate is inferred from two rows.

## Independent execution and subsequent review

The research agent completed company selection, buyer/email recovery, verification, source-backed first lines and export without parent intervention. The parent then inspected the sources and receipts. This used the same authenticated tool accounts and locally supplied credentials, not a separate machine or account installation.

Post-run review found an unsupported 15-minute demo offer in the initial drafts. The published offer was corrected to the documented 30-minute demo and booking URL; follow-ups gained distinct operational angles and explicit booking stop conditions. An unnecessary hypothetical conversion forecast was removed from this summary. Contact data, verdicts, flags, source facts and original provider receipts were unchanged. The shared runbook now requires source-checking offer duration and destination as well as features. [Review results](evidence/post-run-review.json) distinguish these editorial corrections from the successful independent research run.

## Regenerate

From repository root with Python 3.9+:

```powershell
python scripts/prepare_export.py runs/2026-10-18-software-recruitment-independent/evidence/leads.csv --output-dir runs/2026-10-18-software-recruitment-independent --presentation
```

The export is offline. Live evidence refreshes require the operator's ignored .env and working web/provider access. No secret is included in this package. The new-run structural/link/copy audit passed. All 3 unit tests passed. The existing canonical submission checker passed (100 research, 97 ready, 3 parked in that separate agency dataset). Those canonical counts are not this run's counts. Source-quality and suitability judgments remain agent-reviewed; see the saved validation report for exact results.
