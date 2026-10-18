# B2B SaaS outbound rehearsal

**Example of a new-ICP research run.** Live research on 18 October 2026 by a fresh-context agent, supervised by the parent agent. Two draft-ready contacts at two distinct companies. Nothing sent or imported. The original agency submission is separate.

## Open these files

1. [Ready leads](send-ready.csv): buyers, work emails, LinkedIn URLs, qualification signals, sources and first lines.
2. [Draft emails](draft-outreach.md): two personalized messages with prospect and InboxKit source links.
3. [Parked contacts](review-parked.csv): two verified contacts held for commercial infrastructure overlap.

## Request and rules

- **ICP:** B2B SaaS companies running their own outbound sales motion.
- **Target:** two distinct companies with one relevant buyer each.
- **Fit:** first-party evidence of a B2B software product.
- **Signal:** first-party evidence of the company's own outbound activity, not merely outbound product features or advice. No arbitrary recency cutoff; undated evidence stays undated.
- **Buyer:** current founder or revenue/growth operations leader with plausible infrastructure influence. Founder influence is inferred, not proven technical ownership.
- **Commercial suitability:** do not promote vendors selling competing sending infrastructure merely because they match the literal ICP.

## Result

| Company | Buyer | Provider assessment | Accept-all |
| --- | --- | --- | --- |
| HockeyStack | Buğra Gündüz, co-founder/CEO | BounceBan deliverable, score 99 | false |
| UserGems | Christian Kletzl, co-founder/CEO | BounceBan deliverable, score 97 | true |

Five companies examined: two accepted, two commercially parked, one signal unresolved. Five contact attempts: **four retained research rows = two ready + two parked**, plus one invalid attempt excluded. A departed buyer was also rejected before enrichment. No exported duplicates or local suppression matches.

Catch-all remains a visible risk alongside the positive provider assessment. Direct LinkedIn profiles could not be fully opened; company-authored evidence and profile links/indexed content corroborate identity. Sending need, buying intent and actual delivery are not established.

## Evidence when asked

| Question | Open |
| --- | --- |
| Why were these companies and buyers selected? | [Source excerpts and judgments](evidence/source-evidence.json), [company dispositions](evidence/companies-examined.csv), [buyer alternatives](evidence/buyer-alternatives.json) |
| What was attempted or rejected? | [All input attempts](evidence/leads.csv), [retained research](evidence/qualified.csv), [excluded address](evidence/excluded.csv) |
| Do the counts reconcile? | [Export audit](evidence/audit.json) |
| Which providers worked and what did they cost? | [Credit use](evidence/credit-use.json), [detailed run notes](evidence/run-notes.md). Individual finder/verifier receipts are alongside them. |
| What was the original prompt/rule? | [Inputs](evidence/inputs.json). The rule was declared in agent messages; this file was saved after research began. |
| What did supervisory review fix? | The commercial-fit review described below and in the [run notes](evidence/run-notes.md) |

This was a supervised fresh-context run sharing the current account's tools and credentials, not an independent desktop installation or an unassisted guarantee for every ICP. Two unnecessary second verifications and late commercial review consumed avoidable credits; the runbook was clarified. BounceBan's five reported per-result charges differ from its four-credit account debit; the discrepancy remains visible.

## Regenerate this layout

From the repository root:

```powershell
python scripts/prepare_export.py runs/2026-10-18-b2b-saas-outbound-fresh/evidence/leads.csv --output-dir runs/2026-10-18-b2b-saas-outbound-fresh --presentation
```

The agent maintains this summary and drafts. The export script regenerates the two top-level CSVs plus research, exclusions and audit under `evidence/`. Sources and receipts are retained. Default-agency continuations use their existing canonical paths and the original flat export command.
