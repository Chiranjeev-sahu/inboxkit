# Workflow decisions and rationale

These are the policies used by the current runbook and exports. Dated experiments show the observations behind them; an experiment's earlier rule does not override current policy.

| Decision | Rationale | Supporting implementation or evidence |
| --- | --- | --- |
| Target agencies delivering client cold email/outbound infrastructure in the default campaign. | Their work creates relevant mailbox/domain administration needs and matches the brief's buyer group. | [Strategy memo](../deliverables/strategy-memo.md), [runbook](../skills/lead-research/SKILL.md). |
| Use concrete operational evidence, with dates when visible. | Hiring and recent named-client cases can be useful, but strict versions yielded few additions. Delivery, infrastructure, campaign volume and expansion are alternative evidence. | [Sourcing experiments](../runs/README.md). |
| Keep fit, operational relevance and purchase intent distinct. | A company can match the segment and run outbound without demonstrating intent to buy InboxKit. | [Context definitions](../CONTEXT.md). |
| Do not impose an unstated geography/language filter or mandatory 90-day cutoff. | These filters are not part of the default brief and can unnecessarily restrict the candidate pool. | [Qualification procedure](../skills/lead-research/SKILL.md). |
| Count one best-fit buyer per distinct company. | This produces account coverage rather than filling a target through multiple contacts at the same organization. | Company/email deduplication in [prepare_export.py](../scripts/prepare_export.py). |
| Let the agent research and judge evidence; let code perform repeatable mechanical checks. | Source interpretation, buyer selection and copy need contextual judgment. CSV normalization and exclusion rules benefit from deterministic execution. | [CLAUDE.md](../CLAUDE.md), [scripts](../README.md#scripts-and-tests). |
| Use Codex or Claude Code through the same repository entry points. | The repeatable process lives in the files rather than a particular conversation's history. | [AGENTS.md](../AGENTS.md), [CLAUDE.md](../CLAUDE.md). |
| Use role-specific provider fallbacks and stop at a clear result. | Recovery matters when one provider misses, but unnecessary calls spend credits without improving the row. | [Provider access](provider-access.md), [comparison](../runs/2026-10-16-provider-comparison/run-notes.md). |
| Check commercial suitability before enrichment. | A broad outbound SaaS ICP can include vendors that sell competing sending infrastructure. Sequencer integrations alone are not exclusions. | [New-ICP example](../runs/2026-10-18-b2b-saas-outbound-fresh/README.md). |
| Preserve provider verdict and accept-all flag separately. | Domain ambiguity and a positive mailbox assessment are different observations. Verification remains probabilistic. | [Schema](data-dictionary.md), [verification pilot](../runs/2026-10-16-email-verification-pilot/run-notes.md). |
| Park contradictory clear verifier results or explicit evidence holds. | A positive result should not silently cancel a conflicting clear negative or unresolved targeted evidence requirement. | [Email review](../deliverables/email-review.md). |
| Require public relationship proof for alternate email domains. | Delivery assessment does not establish that a domain belongs to the listed organization. | Ownership fields and ready gate in [export script](../scripts/prepare_export.py). |
| Apply the extra exact-address/second-verifier checks only to the four targeted historical rows. | Those checks arose from a specific review; they are not a publication requirement for every finder-sourced contact. | [Twelve individual verdicts](../deliverables/email-review.md). |
| Preserve attempts, holds and rejected results. | The accepted list is interpretable only when its research denominator and failures are visible. | Run inputs, company logs, exclusions and audit files. |
| Keep new ICPs separate and default-agency continuations cumulative. | A new segment must not overwrite the existing campaign, while a continuation must dedupe against the full history. | [Output routing](../README.md#output-routing-and-continuations). |
| Export one accept-all column and explicit copy-merge fields. | Consistent names prevent ambiguous platform mapping while historical provider receipts retain their native fields. | [Data dictionary](data-dictionary.md). |
| Keep outreach in draft and demonstrate local suppression. | The assignment evaluates the research/campaign system. A future authorized campaign also requires monitored opt-out handling and private account suppression. | [Campaign copy](../deliverables/campaign-copy.md), [suppression procedure](opt-out-and-suppression.md). |

## Provider order is evidence-driven

The ten-buyer comparison recovered eight saved addresses with Icypeas versus five with Datagma, so Icypeas precedes Datagma when both are funded and suitable. This is a provisional recovery observation, not a universal accuracy ranking. BounceBan's specialist results support trying it first for ambiguous agency addresses when available. Account permissions, action costs, incremental recovery and actual verdicts determine fallbacks on each run.

## Copy and offer

The default offer demonstrates client mailbox administration, domain organization and DNS setup. Email 1A emphasizes client-account management; 1B emphasizes domain organization. Each row's `email_variant` records the selected angle from its source evidence. The campaign uses a single demo CTA, interleaved LinkedIn/email touches and reply-based opt-out. Product claims link to first-party InboxKit pages in the [copy](../deliverables/campaign-copy.md).

The follow-ups develop DNS setup, existing-sequencer compatibility and a final fit check. Recipient-personalized examples are in the [merged previews](../deliverables/merged-email-previews.md). The 30-day outcome is qualified bookings, not attendance; the [feasibility note](campaign-feasibility.md) defines the denominator, timing and conversion assumptions. Campaign volume is calculated from the 15-booking target independently of the assignment's separate 2,000-row list-scaling exercise. Illustrative booking rates are not measured forecasts; the earlier fixed 2,000-contact campaign scenario is retired.

Offer duration and booking destination are checked against the product page alongside feature claims. The published demo is 30 minutes; adapting to a new ICP does not justify inventing a shorter slot. This check was added after the [independent recruitment run](../runs/2026-10-18-software-recruitment-independent/README.md) produced correct research with a draft-offer mismatch caught during subsequent review.
