# Research run index

The main campaign artifacts are in [deliverables](../README.md#review-the-campaign). Dated runs preserve how companies were sourced, what providers returned and why records were accepted, parked or excluded. They are not additional lists to combine into the final count.

## Start with the current sources of truth

- [Canonical agency dataset](2026-10-15-second-pass/run-notes.md): 107 contact attempts; 100 distinct-company research rows = 97 draft-ready + three parked. See its [audit](2026-10-15-second-pass/audit.json).
- [Individual email review](../deliverables/email-review.md): eight alternate-domain proof verdicts and four targeted checks, including the three remaining holds/conflicts.
- [New-ICP example](2026-10-18-b2b-saas-outbound-fresh/README.md): readable run summary, ready list, sourced draft outreach and parked list; details under `evidence/`.

Current research statuses are 99 provider-valid and one unknown. Ready-domain flags are 64 true, 30 false and three literal unknown. These observations retain their actual source/verification dates. New exports do not reverify emails.

## Every public run

| Folder / entry point | Role |
| --- | --- |
| [2026-10-15-case-volume](2026-10-15-case-volume/run-notes.md) | Case-study signal sourcing and verification experiment. |
| [2026-10-15-hiring-volume](2026-10-15-hiring-volume/run-notes.md) | Hiring signal sourcing and verification experiment. |
| [2026-10-15-presentation](2026-10-15-presentation/run-notes.md) | Earlier agency output snapshot; historical policy and counts. |
| [2026-10-15-second-pass](2026-10-15-second-pass/run-notes.md) | **Canonical agency master.** All contact attempts, current research, ready/parked subsets and exclusions. |
| [2026-10-15-signal-conversion](2026-10-15-signal-conversion/run-notes.md) | Earlier signal-to-contact conversion experiment. |
| [2026-10-15-strict-signal](2026-10-15-strict-signal/run-notes.md) | Strict signal sourcing experiment before later operational-rule decisions. |
| [2026-10-15-twenty-candidate](2026-10-15-twenty-candidate/run-notes.md) | Earlier twenty-candidate sourcing and verification batch. |
| [2026-10-16-agency-quality-audit](2026-10-16-agency-quality-audit/run-notes.md) | Source and verification quality corrections at that stage. |
| [2026-10-16-agency-scale-batch-01](2026-10-16-agency-scale-batch-01/run-notes.md) | Consecutive company dispositions and additional qualified agency contacts. |
| [2026-10-16-agency-scale-batch-02](2026-10-16-agency-scale-batch-02/run-notes.md) | Further consecutive dispositions and qualified additions. |
| [2026-10-16-agency-scale-batch-03](2026-10-16-agency-scale-batch-03/run-notes.md) | Hiring-signal experiment, including no-addition outcomes. |
| [2026-10-16-agency-scale-batch-04](2026-10-16-agency-scale-batch-04/run-notes.md) | Recent named-client case-study experiment and its sourcing limits. |
| [2026-10-16-clean-checkout-billing](2026-10-16-clean-checkout-billing/run-notes.md) | Live billing-software ICP run in a clone with local credentials; same connected agent session. |
| [2026-10-16-distinct-company-expansion](2026-10-16-distinct-company-expansion/run-notes.md) | Company inventory, buyer enrichment and intermediate export snapshots under broader operational evidence. |
| [2026-10-16-email-evidence-review](2026-10-16-email-evidence-review/run-notes.md) | Public alternate-domain proof and targeted second-verifier/address-corroboration evidence. |
| [2026-10-16-email-verification-pilot](2026-10-16-email-verification-pilot/run-notes.md) | Specialist and fallback verification checks, including controls. |
| [2026-10-16-final-expansion](2026-10-16-final-expansion/run-notes.md) | Final sourcing/enrichment batch reaching the 100-company research baseline; failed attempts retained. |
| [2026-10-16-interview-rehearsal](2026-10-16-interview-rehearsal/run-notes.md) | Historical workflow rehearsal and execution observations. |
| [2026-10-16-lusha-recovery](2026-10-16-lusha-recovery/run-notes.md) | Recovered contacts and source/provider attribution. |
| [2026-10-16-new-icp-broader-live](2026-10-16-new-icp-broader-live/run-notes.md) | Broader live new-segment experiment with dispositions and gates. |
| [2026-10-16-new-icp-live-gate](2026-10-16-new-icp-live-gate/run-notes.md) | Live new-ICP qualification and export gate experiment. |
| [2026-10-16-new-icp-offline-smoke](2026-10-16-new-icp-offline-smoke/run-notes.md) | Offline new-ICP schema/gate smoke test; not new live enrichment. |
| [2026-10-16-provider-comparison](2026-10-16-provider-comparison/run-notes.md) | Ten-buyer Icypeas/Datagma recovery comparison and its limitations. |
| [2026-10-16-sourcing-test](2026-10-16-sourcing-test/run-notes.md) | Fixed-rule sourcing observations and export results. |
| [2026-10-16-zerobounce-reconciliation](2026-10-16-zerobounce-reconciliation/run-notes.md) | Individual ZeroBounce checks reconciled against prior email judgments. |
| [2026-10-18-b2b-saas-outbound-fresh](2026-10-18-b2b-saas-outbound-fresh/README.md) | Supervised fresh-context SaaS run; two ready companies, two commercial holds and one invalid contact attempt. |

## How to read a run

Start with its summary or run notes. Inspect `leads.csv` for attempted contacts, `qualified.csv` for retained research, `send-ready.csv` and `review-parked.csv` for the reconciled subsets, and `excluded.csv` for failed gates. `audit.json` gives counts and reasons. Provider/source JSON files support individual judgments; they are saved observations rather than fresh API calls.

Earlier runs used earlier qualification and verification policies. Their dated observations remain useful, but the current [runbook](../skills/lead-research/SKILL.md) and [decisions](../docs/decisions.md) govern new work. Some early snapshots lack a parked file or newer merge columns; keep their historical scope rather than treating them as current campaign imports.

New ICPs use four presentation files at the run root and put detailed records under `evidence/`. Default-agency continuations append to the existing canonical flat input and refresh the same deliverable CSVs. See [routing and continuation rules](../README.md#output-routing-and-continuations).
