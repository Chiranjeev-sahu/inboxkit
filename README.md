# InboxKit GTM campaign and research workflow

This repository stages a sourced LinkedIn and email campaign for InboxKit and provides an agent-led process for repeating the research with a new ideal customer profile (ICP). A researcher can start with a natural-language segment, identify companies and buyers, recover and verify work emails, write source-backed first lines, and produce audited draft lists.

**Agency campaign: 100 distinct-company research rows = 97 draft-ready contacts + 3 parked contacts.** Each retained row has a named buyer, personal LinkedIn URL, work email, qualification evidence and personalized first line. All outreach remains draft. The counts describe saved research and provider assessments, not observed email delivery or campaign replies.

The [original assignment](GTM%20Engineer%20Hiring%20Assignment.txt) defines the requested work. [CONTEXT.md](CONTEXT.md) defines the business terms. Codex and Claude Code follow the same repository instructions; the workflow does not require the original chat history.

## Contents

- [Review the campaign](#review-the-campaign)
- [What qualifies a company](#what-qualifies-a-company)
- [How the workflow operates](#how-the-workflow-operates)
- [Setup from a clean checkout](#setup-from-a-clean-checkout)
- [Credentials and tool access](#credentials-and-tool-access)
- [Natural-language requests](#natural-language-requests)
- [Output routing and continuations](#output-routing-and-continuations)
- [Reading the data and email labels](#reading-the-data-and-email-labels)
- [Trace one prospect through the workflow](#trace-one-prospect-through-the-workflow)
- [Provider roles and fallbacks](#provider-roles-and-fallbacks)
- [Export and validation commands](#export-and-validation-commands)
- [Scripts and tests](#scripts-and-tests)
- [Troubleshooting](#troubleshooting)
- [Repository map and reading order](#repository-map-and-reading-order)
- [Scaling and evidence boundaries](#scaling-and-evidence-boundaries)
- [Complete tracked-file inventory](#complete-tracked-file-inventory)

## Review the campaign

The main campaign artifacts are together in `deliverables/`. Start with the one-page memo, inspect the research sheet, then read the copy and sequence. Supporting evidence remains in dated run folders so it can be checked without crowding the main outputs.

| File | What it contains | How to use it |
| --- | --- | --- |
| [strategy-memo.pdf](deliverables/strategy-memo.pdf) | One-page strategy: segment, operational signal, offer, CTA, three-week cadence and demo-volume assumptions. | Read first for the campaign rationale. |
| [strategy-memo.md](deliverables/strategy-memo.md) | Editable memo source with supporting links. | Inspect wording, math and product citations. |
| [lead-sheet.csv](deliverables/lead-sheet.csv) | All 100 retained research rows, including three parked cases. | Open as a UTF-8 sheet; inspect company, buyer, evidence and verification fields together. |
| [send-ready.csv](deliverables/send-ready.csv) | The 97 contacts that pass the current draft-export gate. | Use as the candidate contact import file after any separately authorized platform mapping. |
| [review-parked.csv](deliverables/review-parked.csv) | Three retained contacts with specific unresolved reasons. | Read the hold rather than assuming every research row is eligible for outreach. |
| [campaign-copy.md](deliverables/campaign-copy.md) | Four email steps, two versions of email 1, a LinkedIn connection note and two follow-ups. Product claims have InboxKit source links. | Read templates and their offer logic. Select one step-1 variant per contact. |
| [sequence.csv](deliverables/sequence.csv) | Email/LinkedIn schedule and template references over three weeks. | Follow the timing and channels; this is a schedule, not a sequencer-native sequence upload. |
| [ten-first-lines.csv](deliverables/ten-first-lines.csv) | Ten workflow-produced personalized openings, matching the research sheet. | Compare each opening with its supporting source. All 100 research rows also have first lines. |
| [merged-email-previews.md](deliverables/merged-email-previews.md) | Six recipient-personalized draft emails covering both opening variants and a full follow-up progression. | Inspect the actual merged wording, source links and visible email-risk annotations. |
| [scale-cost.md](deliverables/scale-cost.md) | The requested scaling paragraph plus detailed workload, batching, measurement and cost reasoning. | Distinguish the proposed 2,000-contact scenario from observed results. |
| [email-review.md](deliverables/email-review.md) | Individual verdicts for eight alternate-domain cases and four targeted email checks. | Understand why domain proof can permit a row while a hold or verification conflict prevents another. |

For a compact example using a different segment, open the [B2B SaaS run](runs/2026-10-18-b2b-saas-outbound-fresh/README.md). Its root contains the summary, ready list, drafts and parked list. Detailed receipts sit under `evidence/`.

## What qualifies a company

The default campaign targets outbound, lead-generation and GTM agencies that publicly sell, build, operate or support client cold-email/outbound infrastructure. The selected buyer is normally a founder, head of growth or person plausibly responsible for sending infrastructure. The research distinguishes four questions:

1. **Company fit:** Does a public company page establish the client outbound service?
2. **Operational signal:** Is there concrete evidence of delivery or expansion, such as a client campaign, sending volume, infrastructure operation, a relevant hire or service expansion?
3. **Buyer relevance:** Does the selected person's current role plausibly connect to the infrastructure decision? An inferred founder responsibility is labeled as an inference.
4. **Commercial suitability:** Is the company a plausible new InboxKit customer rather than an existing public partner/customer or a vendor selling its own competing infrastructure?

Fit and operational activity indicate relevance. They do not establish purchase intent, budget, a present deliverability problem or a decision to switch providers. A single first-party page can support both fit and activity if it genuinely contains both facts.

There is no mandatory 90-day cutoff, named-client requirement or unstated geography/language filter. Visible dates are recorded; older or undated evidence is not described as recent. The broader operational rule followed low-yield experiments with strict hiring and recent case-study signals. [Decisions and rationale](docs/decisions.md) and [dated experiments](runs/README.md) show that progression.

The unit is **one buyer at one distinct company**. Multiple decision-makers do not fill the target. Organization aliases, subsidiaries and alternate domains need agent judgment in addition to mechanical domain checks. Smartlead and Instantly remain integrations under the brief, not automatic competitive exclusions.

## How the workflow operates

```text
Natural-language ICP and requested count
  -> declared company-fit, signal and buyer rules
  -> company discovery and first-party evidence
  -> commercial suitability and suppression check
  -> named buyer and personal LinkedIn profile
  -> work-email discovery through available fallbacks
  -> provider verification and exception review
  -> source-backed first line and draft copy
  -> deterministic export gates
  -> research, ready, parked, excluded and audit outputs
```

The process is agentic because the research agent chooses queries, inspects sources, judges evidence, selects buyers, routes fallbacks and resolves exceptions. The [lead-research skill](skills/lead-research/SKILL.md) supplies the ordered runbook. [AGENTS.md](AGENTS.md) points Codex to [CLAUDE.md](CLAUDE.md), which sets shared campaign and routing rules.

| Agent responsibility | Script responsibility |
| --- | --- |
| Translate the supplied ICP into testable rules. | Require the expected input columns and normalize basic values. |
| Find and inspect sources; judge whether statements support fit and signals. | Check required fields, URL formats and email syntax. |
| Establish current buyer identity and interpret provider results. | Apply recorded verification status, explicit holds and domain-proof fields. |
| Prove alternate-domain relationships using public pages. | Require a recorded approval and HTTP(S) proof links for promotion. |
| Identify related organizations and compare a new batch with earlier work. | Remove repeated emails/domains in the complete input and match suppression entries. |
| Write truthful first lines, summaries and drafts; record uncertainty and provider costs. | Write consistent output subsets and reconcile their counts. |

**The Python export does not discover companies, call finders/verifiers, interpret a webpage or generate campaign copy.** A populated URL field proves only that a URL was supplied; the agent must establish what the source says. There is no hidden application server or provider orchestration service to start.

## Setup from a clean checkout

### Prerequisites

- Git, for checkout and tracked-file consistency checks.
- Python **3.9 or newer**. The checked-in scripts and tests use only the standard library; there is no package installation step.
- Codex or Claude Code, opened in this repository, for a live research run.
- A working search/page-reading route and existing funded finder/verifier access for new contact research. These may be connected tools or direct APIs. Offline checks need neither API keys nor account login.

### Clone and inspect

PowerShell, from the parent directory where you want the checkout:

```powershell
git clone https://github.com/Chiranjeev-sahu/inboxkit.git
cd inboxkit
python --version
python -m unittest discover -s tests -v
python scripts/check_submission.py
```

If Windows exposes Python through the launcher, replace `python` with `py -3`. On macOS/Linux, use an installed Python 3.9+ executable, commonly `python3`; the Python commands otherwise work the same way. Commands below assume the repository root as the working directory.

The checker prints JSON with `checks_pass`, `research`, `draft_ready`, `parked` and `errors`. A successful saved-package check reports 100, 97 and 3 respectively, with an empty error list. It does not retrieve live sources or spend provider credits.

### Prepare live research access

Create a local credential template only if it does not already exist:

```powershell
if (!(Test-Path .env)) { Copy-Item .env.example .env }
```

Fill only the routes you plan to use. Open the folder in the research agent, supply an ICP and target count, and let it follow the repository instructions. Opening the project alone does not trigger a run. Account authentication and provider allowance belong to the operator; a clean checkout reproduces files and offline gates without inheriting another person's sign-in.

## Credentials and tool access

[.env.example](.env.example) lists optional direct-API settings. It contains no usable credentials. `.env` is ignored and stays local. The scripts checked into this repository do not automatically load it; the agent reads selected credentials privately when constructing a direct API request. Do not display credentials or save credential-bearing URLs/headers in evidence.

| Settings | Intended role | Required when |
| --- | --- | --- |
| `EXA_API_KEY`, `TAVILY_API_KEY` | Search alternatives. | Using the corresponding direct API rather than an authenticated tool. |
| `FIRECRAWL_API_KEY` | Page extraction/search alternative. | Using Firecrawl directly. |
| `APOLLO_API_KEY`, `PROSPEO_API_KEY`, `HUNTER_API_KEY`, `FINDYMAIL_API_KEY`, `LUSHA_API_KEY`, `DATAGMA_API_KEY` | Named business-contact discovery/enrichment fallbacks. Some also verify. | Calling the particular provider's API with allowed endpoints and usable credits. |
| `ICYPEAS_API_KEY` | Synchronous email finder and verifier. | Using Icypeas directly. Tested routes use the key alone in Authorization. |
| `ICYPEAS_ACCOUNT_EMAIL` | Account email matching the Icypeas key. | Checking the tested subscription/balance endpoint. This is the provider account email, not a prospect address. |
| `ICYPEAS_API_SECRET`, `ICYPEAS_USER_ID` | Legacy/provider-route-specific credentials. | Only if a selected endpoint explicitly needs them; the tested synchronous finder, verifier and balance routes do not. |
| `BOUNCEBAN_API_KEY`, `ZEROBOUNCE_API_KEY`, `REOON_API_KEY`, `MILLIONVERIFIER_API_KEY` | Email-verification alternatives. | Using the selected direct verifier API. |

No run needs all providers. A working web research tool plus suitable funded email discovery and verification can support a small run. Calling every provider for every row is not a quality requirement.

[.codex/config.toml](.codex/config.toml) registers eight hosted MCP endpoints without keys. It is separate from `.env` and does not itself authenticate accounts. For trusted project configuration, server listing and supported OAuth login commands, see the [MCP guide](docs/mcp-setup.md), which links official OpenAI documentation. Plugins/app connections can supply additional tools without appearing in that file. Claude Code can use the same runbook with its own authenticated tools; the Codex configuration is client-specific.

## Natural-language requests

### A different ICP

> Read the repository instructions. My ICP is B2B cybersecurity SaaS companies expanding their own outbound sales team. Find two distinct companies with one relevant current buyer each. State the company-fit and operational-signal rules before searching. Check commercial suitability, find personal LinkedIn profiles and named work emails, verify with existing credits, and write cited first lines and draft outreach. Save this as a new run using the presentation layout. Spend $0 additional cash and send nothing.

The segment and requested count are inputs. The agent must derive fit, signal and buyer relevance from that input, rather than applying the default agency rule to every segment. A small sample makes evidence and tool issues visible before a larger expansion. The common schema and export gates remain stable.

### Additional default-agency companies

> Continue the default agency ICP. Find five additional distinct companies. Check them against the full existing company list and suppression before enrichment. Append attempts and evidence to the canonical agency workflow, preserve current rows and holds, regenerate exports, and refresh the existing deliverable CSVs. Use existing credits, spend $0 additional cash and send nothing.

This intentionally extends the existing campaign. It does not create a second competing agency master sheet or replace previous rows. The assignment baseline of 100 is not a cap on explicitly requested additions.

### Resume a specific run

> Resume `runs/<actual-run-id>/`. Read its inputs, company dispositions, provider receipts and run notes. Continue the incomplete stages without repeating successful paid lookups. Keep its fit/signal rules and output routing, preserve exclusions and holds, then regenerate and explain the resulting counts.

The agent saves progress in files. There is no automatic job queue or resume scheduler; the saved next actions and receipts let a fresh agent continue deliberately. Do not treat a dated earlier run's stricter rules as current policy without consulting the current runbook.

## Output routing and continuations

| Request | Editable research source | Generated/reviewer outputs | Evidence |
| --- | --- | --- | --- |
| Current agency campaign or explicit continuation | `runs/2026-10-15-second-pass/leads.csv` | Flat exports beside that input; corresponding CSV snapshots in `deliverables/`. | Canonical notes plus referenced dated batch folders. |
| Different ICP | `runs/<run-id>/evidence/leads.csv` | Four top-level presentation files shown below. | Inputs, company dispositions, exclusions, audit, source excerpts, receipts and detailed notes under `evidence/`. |
| Synthetic gate demonstration | `demo/leads.csv` and `demo/suppression.csv` | Saved example in `demo/output/` or a temporary comparison under `tmp/`. | Synthetic fixtures only. |

A new ICP uses this layout:

```text
runs/<run-id>/
  README.md                 # Agent-written rules, results and links
  send-ready.csv            # Generated draft contact subset
  draft-outreach.md         # Agent-written messages and citations
  review-parked.csv         # Generated retained contacts with reasons
  evidence/
    inputs.json             # Request, count and declared rules
    leads.csv               # All attempted contact rows
    qualified.csv           # Generated retained research
    excluded.csv            # Generated failed/invalid/duplicate/suppressed attempts
    audit.json              # Generated counts and reasons
    run-notes.md            # Decisions, provider attempts, costs and next actions
    ...                     # Company log, source excerpts and sanitized receipts
```

The agent writes the summary and drafts; `prepare_export.py --presentation` writes the five generated CSV/JSON outputs. A root summary should explain a shortfall or uncertainty rather than fabricate completion. Companies inspected without a selected contact belong in the company-disposition log, so examined-company counts can exceed contact attempts.

The default agency deliberately retains its earlier flat layout. Its [canonical input](runs/2026-10-15-second-pass/leads.csv) has 107 contact attempts. Seven are excluded; 100 remain research, split 97 ready and 3 parked. [Canonical audit](runs/2026-10-15-second-pass/audit.json). Research snapshots in `deliverables/` are copies, not independent editable masters.

After source edits, regenerate the complete accumulated canonical input, inspect the audit and refresh the three deliverable CSVs. Update current count summaries when additions change totals. Preserve older dated batch observations as history. A new ICP never overwrites the agency files. Cross-run organization equivalence and deduplication against prior runs require the agent's comparison; the exporter sees only its supplied input and suppression file.

## Reading the data and email labels

The [data dictionary](docs/data-dictionary.md) documents every campaign field and merge mapping. The core row contains name, title, company, domain, personal LinkedIn URL, work email, verification status, qualification signal and sources. Additional fields preserve email discovery, verification date/raw result, first line, domain proof and holds.

| Label | Interpretation | Output treatment |
| --- | --- | --- |
| `qualified` company/contact | Agent judged the supplied fit and signal rules satisfied. | Still subject to mechanical exclusions and ready/hold checks. |
| `valid` email | A provider assessed it deliverable/verified, with no unresolved contradictory clear negative. | Eligible for the draft ready gate when other conditions pass. |
| `catch_all` email status | Only ambiguous accept-all assessments are available. | Research/parked when other required fields pass. |
| `unknown` email status | Missing result, timeout or unresolved clear-verdict conflict. | Research/parked when other required fields pass. |
| `invalid` email | Clear undeliverable or malformed result. | Excluded contact attempt; research can try an alternative buyer/address. |
| `verification_accept_all=true` | Provider reports a domain that accepts arbitrary addresses. | Separate risk field, compatible with a positive specialist `valid` assessment. |
| Blank accept-all flag | No boolean supplied. | Remains blank. It is not converted to false. Three older ready records retain literal `unknown`. |
| Explicit hold | A recorded unresolved identity, commercial or targeted evidence issue. | Parked even when the provider verdict is positive. |

**Research = send-ready + review-parked. Input contact attempts = research + excluded.** The 100-row research sheet contains 99 provider-valid statuses and one unknown; two provider-valid records remain parked under targeted evidence holds. Ready-domain flags are 64 true, 30 false and 3 literal unknown. These are separate counts, not mutually interchangeable definitions of validity.

For alternate email domains, a positive verifier does not establish company ownership. The agent must record public proof of the organizational relationship, with `email_domain_ownership_status=proven` and proof URLs. The eight reviewed agency cases have that proof. The [individual report](deliverables/email-review.md) explains each verdict and the three remaining parked cases.

Copy maps `{{first_name}}` to explicit `first_name` and `{{first_line}}` to `first_line`. `{{sender_name}}` is the operator's sender identity. `email_variant` selects agency email 1A or 1B; it is evidence-based personalization, not a measured experiment winner. Risk/provenance columns can remain alongside a later platform import as custom fields or audit evidence. Never silently drop them to make the list appear stronger.

## Trace one prospect through the workflow

The separate SaaS run provides a short evidence trail for **HockeyStack / Buğra Gündüz**:

1. **Fit and activity:** The [company's outbound playbook](https://www.hockeystack.com/resources/playbook/how-we-started-outbound) describes its own outbound motion. This supports operational relevance beyond merely selling a product that mentions outbound.
2. **Buyer and address:** Its [Y Combinator company profile](https://www.ycombinator.com/companies/hockeystack) corroborates the founder and publishes the named address. Infrastructure influence is a founder-role inference, not proof of technical ownership.
3. **Verification:** The saved [BounceBan assessment](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-hockeystack.json) reports deliverable, score 99, accept-all false. It records that assessment at that time, without guaranteeing delivery.
4. **Personalization:** The [input/source record](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/source-evidence.json) connects the prospect fact to a first line; the [draft](runs/2026-10-18-b2b-saas-outbound-fresh/draft-outreach.md) separately cites InboxKit pages for product statements.
5. **Export:** The contact appears in the [ready CSV](runs/2026-10-18-b2b-saas-outbound-fresh/send-ready.csv). The [audit](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/audit.json) reconciles it with another ready company, two commercial-overlap holds and one invalid contact attempt.

The same run retains an invalid first UserGems contact and a verified alternative buyer. It also parks vendors whose infrastructure offering creates commercial overlap. These are documented decisions, not silent replacements of failed results. The [run summary](runs/2026-10-18-b2b-saas-outbound-fresh/README.md) explains the supervised fresh-context conditions and source-access limitations.

## Provider roles and fallbacks

| Stage | Available routes | Selection rule |
| --- | --- | --- |
| Discover companies/pages | Agent web tools, Exa, Tavily; Firecrawl search/extraction. | Use relevant incremental results; inspect first-party evidence before accepting a company. |
| Establish buyer/profile | Company pages, indexed personal LinkedIn content, available enrichment tools. | Corroborate current role and employer; preserve direct-profile access limitations. |
| Recover named work email | Public named addresses, Lusha, Apollo, Prospeo, Hunter, Findymail, Icypeas, Datagma. | Skip denied/exhausted routes; stop once a suitable named match is found. Icypeas precedes Datagma when both are usable, based on the saved ten-buyer comparison. |
| Verify | BounceBan specialist first when available; Icypeas, ZeroBounce, Reoon, MillionVerifier as suitable fallbacks. | Stop at a clear assessment. Use extra checks for a specific ambiguity or targeted requirement, not to exercise every service. |
| Dedupe/suppress/export | Local standard-library Python. | Apply deterministic gates to researched rows and the supplied suppression data. |

The [provider comparison](runs/2026-10-16-provider-comparison/run-notes.md) recovered eight saved addresses with Icypeas versus five with Datagma. This supports their relative recovery order on that sample, not a universal quality ranking. The [verification pilot](runs/2026-10-16-email-verification-pilot/run-notes.md) motivated specialist-first handling for ambiguous agency domains. Higher price alone is not evidence of a more accurate verdict.

Account balances, endpoint permissions and tool registration are different checks. A visible tool may have no credits; a funded account may deny a specific API endpoint. Save sanitized results, action costs and failures. For asynchronous verification, poll the existing request ID rather than submit the same paid job repeatedly. [Direct API routes](docs/provider-access.md) and [MCP setup](docs/mcp-setup.md) cover authentication and known pitfalls.

Existing access/credits supported the saved work with $0 additional cash. This is a budget condition, not a claim that providers, agent usage or later production are free. A paid scenario in the cost note is not authorization to purchase it.

## Export and validation commands

### New ICP: generate the presentation outputs

After the agent has saved researched input rows, replace the folder name with the real run ID:

```powershell
python scripts/prepare_export.py runs/<run-id>/evidence/leads.csv --output-dir runs/<run-id> --presentation
```

`<run-id>` is a placeholder, not a literal shell argument. For a directly runnable example that does not alter the saved run:

```powershell
python scripts/prepare_export.py runs/2026-10-18-b2b-saas-outbound-fresh/evidence/leads.csv --output-dir tmp/saas-export --presentation
```

Open `tmp/saas-export/send-ready.csv`, `review-parked.csv` and `evidence/audit.json`. This repeats only the mechanical export; it reuses saved research and calls no provider.

### Default campaign: regenerate and refresh snapshots

Run after researched source changes and inspect the generated audit before copying:

```powershell
python scripts/prepare_export.py runs/2026-10-15-second-pass/leads.csv
Copy-Item runs/2026-10-15-second-pass/qualified.csv deliverables/lead-sheet.csv
Copy-Item runs/2026-10-15-second-pass/send-ready.csv deliverables/send-ready.csv
Copy-Item runs/2026-10-15-second-pass/review-parked.csv deliverables/review-parked.csv
python scripts/check_submission.py
```

The copy commands intentionally replace generated snapshots. Edit the source input and evidence, not one exported copy in isolation. To compare a change first, use `--output-dir tmp/<comparison-name>` and inspect differences without replacing the canonical outputs.

### Demonstrate bad emails, duplicates and suppression

```powershell
python scripts/prepare_export.py demo/leads.csv --suppression demo/suppression.csv --output-dir tmp/demo-output
```

The synthetic fixture exercises invalid emails, exact-email/domain duplicates, suppression and review cases. Inspect `tmp/demo-output/excluded.csv`, `review-parked.csv` and `audit.json`; [saved demo output](demo/output/audit.json) is also tracked for inspection. Fixture rows are not real campaign prospects.

### Validate the saved package offline

```powershell
python -m unittest discover -s tests -v
python scripts/check_submission.py
```

The package check temporarily regenerates canonical agency exports under ignored `tmp/`, compares saved results, checks the deliverable snapshots and verifies repository links. It does not overwrite campaign outputs or refresh live verification dates. To check a new-ICP export, regenerate it into a temporary comparison folder as shown above and inspect its audit and subsets; the package checker does not automatically regenerate every dated run.

### Refresh the public partner audit, when needed

```powershell
python scripts/refresh_public_partners.py
```

This optional command makes live HTTP requests to the partner URLs in the saved sitemap inventory and overwrites `docs/inboxkit-partner-audit.csv`. It does not discover a new sitemap or automatically modify `data/suppression.csv`. Review the extracted names/domains and source pages before updating suppression and re-exporting affected lists. It is separate from offline validation and is not needed to inspect the saved campaign.

## Scripts and tests

| File | Behavior | Scope |
| --- | --- | --- |
| [prepare_export.py](scripts/prepare_export.py) | Reads agent-researched CSV, normalizes email/domain and accept-all alias, applies field/status/URL/duplicate/suppression rules, honors explicit holds and recorded domain proof, writes five output files. | Deterministic gates. It cannot independently judge identity, claims or group ownership. Input order matters: the first passing row occupies an email/domain; rank the preferred buyer before exporting. |
| [check_submission.py](scripts/check_submission.py) | Checks saved contact/merge fields, CSV structure, subset reconciliation, canonical/deliverable agreement, temporary regeneration, first-line examples, copy placeholders/opt-outs, sequence shape and tracked Markdown local-file links. | Offline package consistency. Requires Git and tracked public files; no provider calls, PDF visual inspection, remote link checks or semantic source verification. |
| [refresh_public_partners.py](scripts/refresh_public_partners.py) | Fetches saved partner profile URLs, parses headings/website sections, records resolved domains or fetch/review failures. | Optional live public audit. Six fetch workers; human/agent review precedes suppression edits. |
| [test_prepare_export.py](tests/test_prepare_export.py) | Runs the export against synthetic edge cases and both flat/presentation layouts. | Integration regression coverage for invalid, duplicate, suppressed, alternate-domain and held records, plus count reconciliation. |
| [test_submission_fields.py](tests/test_submission_fields.py) | Tests canonical accept-all naming, conflict refusal, preservation of blank risk flags and required greeting/variant mapping. | Prevents the field ambiguities found during review. |
| [offline-checks.yml](.github/workflows/offline-checks.yml) | Defines unit tests and saved-package checks on Python 3.9 and 3.12. | Credential-free CI definition; it does not run live research. |

`prepare_export.py --help` describes CLI flags. By default, suppression is read from `data/suppression.csv` relative to the current directory; a custom file can be passed with `--suppression`. The exporter permits a missing suppression file, so running from the repository root with the expected file present matters. Use the package checker for the saved campaign and inspect which suppression file a new run uses.

## Troubleshooting

| Symptom | Explanation and action |
| --- | --- |
| Running Python produces no new prospects. | Export consumes researched rows. Give the agent an ICP/count and ask it to follow the skill first. |
| `python` is not recognized. | Use an installed Python 3.9+ launcher (`py -3` on Windows or `python3` where appropriate). No author-specific runtime path is required. |
| Unicode names display incorrectly. | Open CSVs with UTF-8 import; keep the original Unicode names. In a Windows terminal, `python -X utf8 ...` can force UTF-8 output. |
| A hosted tool is listed but returns `Unknown tool`. | Registration can be stale after connection changes. Refresh the intended app/server connection and inspect tools in a fresh project chat; use a working alternative meanwhile. This error does not establish a zero balance. |
| API responds 401/403 or `API_INACCESSIBLE`. | Check matching account/key and endpoint entitlement. A balance or successful saved-contact search does not establish company discovery access. Do not repeat denied paid calls. |
| A provider responds 429. | Save progress, respect pacing and resume/poll or use a suitable fallback. Repeated immediate retries do not restore capacity. |
| A finder returns no address. | Try the next funded suitable finder or another relevant buyer. Preserve the failed lookup; do not present a guessed pattern as a verified identity. |
| Verifier says catch-all. | Preserve the ambiguous raw result. A specialist can provide another assessment where useful; keep the domain flag separate from normalized status. |
| Providers return clear positive and clear negative results. | Retain both and park the unresolved case. An ambiguous catch-all result alone is not a clear negative. |
| Email domain differs from the company website. | Establish a public organizational relationship, record proof URLs and approval, or park with the missing link. Verification alone cannot resolve ownership. |
| `Conflicting accept-all fields`. | Reconcile `is_accept_all` and `verification_accept_all` against receipts in the source input. Blank/unknown is not false. |
| LinkedIn blocks direct profile access. | Keep the personal profile URL and corroborate role through company-authored material/indexed content; state the access limitation rather than claiming a full profile inspection. |
| Too few companies meet the rules. | Report examined, accepted, rejected and uncertain counts, then propose an explicit rule/source change. Do not silently fill the count with multiple people per company or unrelated businesses. |
| A snapshot is stale. | Regenerate from canonical input and the intended suppression file, inspect audit/exclusions, refresh deliverable copies and update current counts. Do not edit a generated CSV alone. |
| A public Markdown link works locally but fails in a clone. | Ensure its target is tracked. The checker rejects links that depend on local-only files even when they exist on the author's computer. |

More operational detail is in the [operator guide](docs/operator-guide.md). The [suppression procedure](docs/opt-out-and-suppression.md) explains exact-email, domain and company-name matching and how reply opt-outs would feed a later authorized live campaign. The local gate cannot remove somebody already enrolled in an external platform.

## Repository map and reading order

```text
AGENTS.md / CLAUDE.md       Agent entry and shared rules
CONTEXT.md                 Business definitions and constraints
GTM Engineer ... .txt      Original authoritative assignment
deliverables/              Campaign memo, sheets, copy, schedule and scaling
skills/lead-research/       Ordered research and exception-handling runbook
scripts/                   Export, offline package check, public partner refresh
tests/                     Standard-library regression tests
data/                      Public suppression input
demo/                      Synthetic input and saved gate output
docs/                      Schema, evidence policy, setup and product sources
runs/                      Dated research, provider receipts and audit trails
.codex/                    Optional hosted MCP registrations
.github/workflows/         Offline CI definition
.env.example               Blank optional credential template
```

| Document/data file | Purpose and relationship |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Small Codex entry point directing research to the shared rules and skill. |
| [CLAUDE.md](CLAUDE.md) | Shared run routing, budget, draft-only, claim and validation rules. |
| [CONTEXT.md](CONTEXT.md) | Business problem, goals, terms and constraints; useful before reading field/status details. |
| [skills/lead-research/SKILL.md](skills/lead-research/SKILL.md) | Six ordered stages, completion criteria, provider fallback policy and both output layouts. |
| [docs/decisions.md](docs/decisions.md) | Current policy choices, reasons and supporting observations. |
| [docs/open-questions.md](docs/open-questions.md) | Evidence boundaries and hypotheses; separates current policy from what the saved work cannot establish. |
| [docs/campaign-feasibility.md](docs/campaign-feasibility.md) | Qualified-booking definition, benchmark denominator audit and conditional 30-day campaign capacity plan. |
| [docs/data-dictionary.md](docs/data-dictionary.md) | Contact/evidence/hold fields, normalized accept-all naming, file counts and merge mapping. |
| [docs/operator-guide.md](docs/operator-guide.md) | Concise setup, access checks, export/refresh commands, safe reruns and failure handling. |
| [docs/mcp-setup.md](docs/mcp-setup.md) | Optional hosted registration, operator authentication and API fallback distinctions. |
| [docs/provider-access.md](docs/provider-access.md) | Dated tested direct-API routes, authentication formats and endpoint pitfalls. |
| [docs/product-claims.md](docs/product-claims.md) | Candidate InboxKit claim wording with first-party source links. |
| [docs/inboxkit-site-research.md](docs/inboxkit-site-research.md) | Site inventory interpretation, relevant product context and public customer/partner exclusions. |
| [docs/inboxkit-proof-audit.md](docs/inboxkit-proof-audit.md) | Product/customer proof review and limits on performance claims. |
| [docs/inboxkit-sitemap-inventory.csv](docs/inboxkit-sitemap-inventory.csv) | Saved 409-URL sitemap inventory. Listing a URL does not mean every page was read. |
| [docs/inboxkit-partner-audit.csv](docs/inboxkit-partner-audit.csv) | Saved audit of 56 public partner profiles, names and domains. |
| [data/suppression.csv](data/suppression.csv) | 129 public suppression entries: 56 domains and 73 partner/customer names. Public evidence does not replace a private customer/opt-out list. |
| [docs/opt-out-and-suppression.md](docs/opt-out-and-suppression.md) | Local suppression behavior and monitored reply-opt-out procedure for separately authorized sending. |
| [docs/sourcing-pilot.md](docs/sourcing-pilot.md), [docs/signal-search-batch.md](docs/signal-search-batch.md) | Historical experiments, not current qualification overrides. |
| [runs/README.md](runs/README.md) | Index of every public run, including the canonical agency master and supporting experiments. |
| [.gitattributes](.gitattributes), [.gitignore](.gitignore) | Text checkout conventions and exclusion of credentials and temporary output. |

For review, read **memo -> sheet -> copy/schedule -> email review -> runbook -> example new ICP -> checks**. For an audit, follow each row's source/provenance into the dated run. For maintenance, edit canonical inputs or policy first, then regenerate snapshots. You do not need to open hundreds of receipts to understand the campaign; the complete inventory below is an appendix for tracing a particular file.

## Scaling and evidence boundaries

Scaling requires more distinct qualifying companies, not just a larger export. The [scale/cost note](deliverables/scale-cost.md) proposes batches of 50 to 100, cumulative deduplication, saved attempts, provider recovery measurements and accepted-contact yield. Its 2,000-contact workload and conditional provider-cost scenarios are explicit assumptions, not demonstrated throughput or total production cost. The 97/100 ready share describes selected research survivors, not the yield of every company examined.

The campaign's 15-demo goal and funnel math are planning assumptions. No messages were sent, so replies, bounces, meetings and variant performance were not measured. Verification is a provider assessment with source date and uncertainty. Product claims come from linked InboxKit pages; prospect observations have their own sources. A URL inventory is not a full-site validation, and historical verification dates are not silently refreshed by re-exporting.

The [fresh-context SaaS example](runs/2026-10-18-b2b-saas-outbound-fresh/README.md) used a clean clone without the original conversation history and produced two draft-ready contacts under supervision using the same authenticated account. It demonstrates one new-segment run and the saved interface; it does not guarantee arbitrary-ICP yield or transfer account authentication to another computer. Its documented commercial-fit correction and rejected contacts remain in the evidence.

The scripts establish mechanical consistency. Source support, current roles, organization aliases, suitability and copy relevance remain agent judgments that should be inspected. Public partner/customer suppression is bounded by publicly visible pages. Credentials and tool access are operator prerequisites for a live run; the saved campaign and offline checks remain inspectable without them.

## Complete tracked-file inventory

Every public tracked file is listed below, grouped so a reader can identify both final outputs and supporting records. Run files are dated observations: a receipt's filename describes its role, while the run notes and row evidence provide interpretation. Generated snapshots can be reproduced from the matching input under that run's recorded policy. Earlier snapshots may reflect earlier rules and should not be combined into the current lead count.

<details>
<summary>Root and configuration (10 files)</summary>

| File | Role |
| --- | --- |
| [.codex/config.toml](.codex/config.toml) | Optional hosted MCP endpoint registrations without credentials. |
| [.env.example](.env.example) | Blank optional local credential template. |
| [.gitattributes](.gitattributes) | Text file and newline conventions. |
| [.github/workflows/offline-checks.yml](.github/workflows/offline-checks.yml) | Credential-free Python test and consistency-check CI definition. |
| [.gitignore](.gitignore) | Keeps credentials, temporary output and local author material out of Git. |
| [AGENTS.md](AGENTS.md) | Codex entry point to shared instructions. |
| [CLAUDE.md](CLAUDE.md) | Shared campaign, routing and validation instructions. |
| [CONTEXT.md](CONTEXT.md) | Business problem, goals, glossary and constraints. |
| [GTM Engineer Hiring Assignment.txt](GTM%20Engineer%20Hiring%20Assignment.txt) | Original authoritative hiring brief. |
| [README.md](README.md) | Project overview, complete operating guide and file inventory. |

</details>

<details>
<summary>data (1 files)</summary>

| File | Role |
| --- | --- |
| [data/suppression.csv](data/suppression.csv) | Reviewed public partner/customer suppression input. |

</details>

<details>
<summary>deliverables (11 files)</summary>

| File | Role |
| --- | --- |
| [deliverables/campaign-copy.md](deliverables/campaign-copy.md) | Email variants, follow-ups, LinkedIn copy and citations. |
| [deliverables/email-review.md](deliverables/email-review.md) | Eight domain-proof and four targeted verification verdicts. |
| [deliverables/lead-sheet.csv](deliverables/lead-sheet.csv) | 100-row retained agency research snapshot. |
| [deliverables/merged-email-previews.md](deliverables/merged-email-previews.md) | Fully merged draft examples with factual prospect and product citations. |
| [deliverables/review-parked.csv](deliverables/review-parked.csv) | Three retained agency holds and their reasons. |
| [deliverables/scale-cost.md](deliverables/scale-cost.md) | Scaling method, measurement and conditional cost scenarios. |
| [deliverables/send-ready.csv](deliverables/send-ready.csv) | 97-contact draft-ready snapshot. |
| [deliverables/sequence.csv](deliverables/sequence.csv) | Three-week touch schedule with template references. |
| [deliverables/strategy-memo.md](deliverables/strategy-memo.md) | Editable strategy memo with sources. |
| [deliverables/strategy-memo.pdf](deliverables/strategy-memo.pdf) | Rendered one-page strategy memo. |
| [deliverables/ten-first-lines.csv](deliverables/ten-first-lines.csv) | Ten sourced personalized examples matching the research sheet. |

</details>

<details>
<summary>demo (7 files)</summary>

| File | Role |
| --- | --- |
| [demo/leads.csv](demo/leads.csv) | Synthetic contact cases for demonstrating mechanical gates. |
| [demo/output/audit.json](demo/output/audit.json) | Saved synthetic demonstration: generated reconciliation counts and gate reasons. |
| [demo/output/excluded.csv](demo/output/excluded.csv) | Saved synthetic demonstration: generated excluded contact attempts and reasons. |
| [demo/output/qualified.csv](demo/output/qualified.csv) | Saved synthetic demonstration: generated retained research under this run's policy. |
| [demo/output/review-parked.csv](demo/output/review-parked.csv) | Saved synthetic demonstration: generated retained contacts with unresolved reasons. |
| [demo/output/send-ready.csv](demo/output/send-ready.csv) | Saved synthetic demonstration: generated draft-ready contacts for this run. |
| [demo/suppression.csv](demo/suppression.csv) | Synthetic suppression fixture, not real customer data. |

</details>

<details>
<summary>docs (15 files)</summary>

| File | Role |
| --- | --- |
| [docs/campaign-feasibility.md](docs/campaign-feasibility.md) | Qualified-booking target, benchmark denominator audit and conditional 30-day workload plan. |
| [docs/data-dictionary.md](docs/data-dictionary.md) | Fields, statuses, file relationships and platform merge mapping. |
| [docs/decisions.md](docs/decisions.md) | Current policy decisions and rationale. |
| [docs/inboxkit-partner-audit.csv](docs/inboxkit-partner-audit.csv) | Public partner-profile names, domains and fetch results. |
| [docs/inboxkit-proof-audit.md](docs/inboxkit-proof-audit.md) | Product/customer proof review and claim limitations. |
| [docs/inboxkit-site-research.md](docs/inboxkit-site-research.md) | Saved site research and inventory interpretation. |
| [docs/inboxkit-sitemap-inventory.csv](docs/inboxkit-sitemap-inventory.csv) | Saved InboxKit URL inventory. |
| [docs/mcp-setup.md](docs/mcp-setup.md) | Hosted tool registration, authentication and fallback guide. |
| [docs/open-questions.md](docs/open-questions.md) | Evidence boundaries, hypotheses and validation considerations. |
| [docs/operator-guide.md](docs/operator-guide.md) | Concise operating commands, access checks and troubleshooting. |
| [docs/opt-out-and-suppression.md](docs/opt-out-and-suppression.md) | Suppression gate and reply-based removal procedure. |
| [docs/product-claims.md](docs/product-claims.md) | Candidate product claims with InboxKit citations. |
| [docs/provider-access.md](docs/provider-access.md) | Tested API routes, authentication and endpoint pitfalls. |
| [docs/signal-search-batch.md](docs/signal-search-batch.md) | Historical signal search observations. |
| [docs/sourcing-pilot.md](docs/sourcing-pilot.md) | Historical sourcing pilot observations. |

</details>

<details>
<summary>runs/2026-10-15-case-volume (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-15-case-volume/audit.json](runs/2026-10-15-case-volume/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-15-case-volume/excluded.csv](runs/2026-10-15-case-volume/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-15-case-volume/leads.csv](runs/2026-10-15-case-volume/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-15-case-volume/qualified.csv](runs/2026-10-15-case-volume/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-15-case-volume/run-notes.md](runs/2026-10-15-case-volume/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-15-case-volume/send-ready.csv](runs/2026-10-15-case-volume/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-15-hiring-volume (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-15-hiring-volume/audit.json](runs/2026-10-15-hiring-volume/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-15-hiring-volume/excluded.csv](runs/2026-10-15-hiring-volume/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-15-hiring-volume/leads.csv](runs/2026-10-15-hiring-volume/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-15-hiring-volume/qualified.csv](runs/2026-10-15-hiring-volume/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-15-hiring-volume/run-notes.md](runs/2026-10-15-hiring-volume/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-15-hiring-volume/send-ready.csv](runs/2026-10-15-hiring-volume/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-15-presentation (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-15-presentation/audit.json](runs/2026-10-15-presentation/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-15-presentation/excluded.csv](runs/2026-10-15-presentation/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-15-presentation/leads.csv](runs/2026-10-15-presentation/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-15-presentation/qualified.csv](runs/2026-10-15-presentation/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-15-presentation/run-notes.md](runs/2026-10-15-presentation/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-15-presentation/send-ready.csv](runs/2026-10-15-presentation/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-15-second-pass (7 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-15-second-pass/audit.json](runs/2026-10-15-second-pass/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-15-second-pass/excluded.csv](runs/2026-10-15-second-pass/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-15-second-pass/leads.csv](runs/2026-10-15-second-pass/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-15-second-pass/qualified.csv](runs/2026-10-15-second-pass/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-15-second-pass/review-parked.csv](runs/2026-10-15-second-pass/review-parked.csv) | Generated retained contacts with unresolved reasons. |
| [runs/2026-10-15-second-pass/run-notes.md](runs/2026-10-15-second-pass/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-15-second-pass/send-ready.csv](runs/2026-10-15-second-pass/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-15-signal-conversion (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-15-signal-conversion/audit.json](runs/2026-10-15-signal-conversion/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-15-signal-conversion/excluded.csv](runs/2026-10-15-signal-conversion/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-15-signal-conversion/leads.csv](runs/2026-10-15-signal-conversion/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-15-signal-conversion/qualified.csv](runs/2026-10-15-signal-conversion/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-15-signal-conversion/run-notes.md](runs/2026-10-15-signal-conversion/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-15-signal-conversion/send-ready.csv](runs/2026-10-15-signal-conversion/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-15-strict-signal (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-15-strict-signal/audit.json](runs/2026-10-15-strict-signal/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-15-strict-signal/excluded.csv](runs/2026-10-15-strict-signal/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-15-strict-signal/leads.csv](runs/2026-10-15-strict-signal/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-15-strict-signal/qualified.csv](runs/2026-10-15-strict-signal/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-15-strict-signal/run-notes.md](runs/2026-10-15-strict-signal/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-15-strict-signal/send-ready.csv](runs/2026-10-15-strict-signal/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-15-twenty-candidate (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-15-twenty-candidate/audit.json](runs/2026-10-15-twenty-candidate/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-15-twenty-candidate/excluded.csv](runs/2026-10-15-twenty-candidate/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-15-twenty-candidate/leads.csv](runs/2026-10-15-twenty-candidate/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-15-twenty-candidate/qualified.csv](runs/2026-10-15-twenty-candidate/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-15-twenty-candidate/run-notes.md](runs/2026-10-15-twenty-candidate/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-15-twenty-candidate/send-ready.csv](runs/2026-10-15-twenty-candidate/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-agency-quality-audit (1 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-agency-quality-audit/run-notes.md](runs/2026-10-16-agency-quality-audit/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs/2026-10-16-agency-scale-batch-01 (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-agency-scale-batch-01/audit.json](runs/2026-10-16-agency-scale-batch-01/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-agency-scale-batch-01/excluded.csv](runs/2026-10-16-agency-scale-batch-01/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-agency-scale-batch-01/leads.csv](runs/2026-10-16-agency-scale-batch-01/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-agency-scale-batch-01/qualified.csv](runs/2026-10-16-agency-scale-batch-01/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-agency-scale-batch-01/run-notes.md](runs/2026-10-16-agency-scale-batch-01/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-agency-scale-batch-01/send-ready.csv](runs/2026-10-16-agency-scale-batch-01/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-agency-scale-batch-02 (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-agency-scale-batch-02/audit.json](runs/2026-10-16-agency-scale-batch-02/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-agency-scale-batch-02/excluded.csv](runs/2026-10-16-agency-scale-batch-02/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-agency-scale-batch-02/leads.csv](runs/2026-10-16-agency-scale-batch-02/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-agency-scale-batch-02/qualified.csv](runs/2026-10-16-agency-scale-batch-02/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-agency-scale-batch-02/run-notes.md](runs/2026-10-16-agency-scale-batch-02/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-agency-scale-batch-02/send-ready.csv](runs/2026-10-16-agency-scale-batch-02/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-agency-scale-batch-03 (1 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-agency-scale-batch-03/run-notes.md](runs/2026-10-16-agency-scale-batch-03/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs/2026-10-16-agency-scale-batch-04 (1 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-agency-scale-batch-04/run-notes.md](runs/2026-10-16-agency-scale-batch-04/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs/2026-10-16-clean-checkout-billing (8 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-clean-checkout-billing/audit.json](runs/2026-10-16-clean-checkout-billing/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-clean-checkout-billing/excluded.csv](runs/2026-10-16-clean-checkout-billing/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-clean-checkout-billing/finder-result.json](runs/2026-10-16-clean-checkout-billing/finder-result.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-clean-checkout-billing/leads.csv](runs/2026-10-16-clean-checkout-billing/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-clean-checkout-billing/qualified.csv](runs/2026-10-16-clean-checkout-billing/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-clean-checkout-billing/run-notes.md](runs/2026-10-16-clean-checkout-billing/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-clean-checkout-billing/send-ready.csv](runs/2026-10-16-clean-checkout-billing/send-ready.csv) | Generated draft-ready contacts for this run. |
| [runs/2026-10-16-clean-checkout-billing/verification-result.json](runs/2026-10-16-clean-checkout-billing/verification-result.json) | Saved email-verification response; interpret with this run's notes. |

</details>

<details>
<summary>runs/2026-10-16-distinct-company-expansion (13 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-distinct-company-expansion/audit.json](runs/2026-10-16-distinct-company-expansion/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-distinct-company-expansion/companies.csv](runs/2026-10-16-distinct-company-expansion/companies.csv) | Company discovery/qualification inventory. |
| [runs/2026-10-16-distinct-company-expansion/enriched-buyers.csv](runs/2026-10-16-distinct-company-expansion/enriched-buyers.csv) | Buyer enrichment observations. |
| [runs/2026-10-16-distinct-company-expansion/enriched-export/audit.json](runs/2026-10-16-distinct-company-expansion/enriched-export/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-distinct-company-expansion/enriched-export/excluded.csv](runs/2026-10-16-distinct-company-expansion/enriched-export/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-distinct-company-expansion/enriched-export/qualified.csv](runs/2026-10-16-distinct-company-expansion/enriched-export/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-distinct-company-expansion/enriched-export/send-ready.csv](runs/2026-10-16-distinct-company-expansion/enriched-export/send-ready.csv) | Generated draft-ready contacts for this run. |
| [runs/2026-10-16-distinct-company-expansion/enriched-leads.csv](runs/2026-10-16-distinct-company-expansion/enriched-leads.csv) | Researched input after buyer/contact enrichment. |
| [runs/2026-10-16-distinct-company-expansion/excluded.csv](runs/2026-10-16-distinct-company-expansion/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-distinct-company-expansion/leads.csv](runs/2026-10-16-distinct-company-expansion/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-distinct-company-expansion/qualified.csv](runs/2026-10-16-distinct-company-expansion/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-distinct-company-expansion/run-notes.md](runs/2026-10-16-distinct-company-expansion/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-distinct-company-expansion/send-ready.csv](runs/2026-10-16-distinct-company-expansion/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-email-evidence-review (14 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-email-evidence-review/credit-use.json](runs/2026-10-16-email-evidence-review/credit-use.json) | Saved provider debits and cost reconciliation. |
| [runs/2026-10-16-email-evidence-review/https-caliberoutbound-com.json](runs/2026-10-16-email-evidence-review/https-caliberoutbound-com.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-chiefleadofficer-com.json](runs/2026-10-16-email-evidence-review/https-chiefleadofficer-com.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-keyoutreachlabs-com.json](runs/2026-10-16-email-evidence-review/https-keyoutreachlabs-com.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-knkoutbound-com-about.json](runs/2026-10-16-email-evidence-review/https-knkoutbound-com-about.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-pearllemon-com-about-us.json](runs/2026-10-16-email-evidence-review/https-pearllemon-com-about-us.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-pearllemonleads-com-about-us.json](runs/2026-10-16-email-evidence-review/https-pearllemonleads-com-about-us.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-rafols-co.json](runs/2026-10-16-email-evidence-review/https-rafols-co.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-www-keyoutreach-com-about-us.json](runs/2026-10-16-email-evidence-review/https-www-keyoutreach-com-about-us.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-www-leadowski-io.json](runs/2026-10-16-email-evidence-review/https-www-leadowski-io.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/https-www-omrafols-com.json](runs/2026-10-16-email-evidence-review/https-www-omrafols-com.json) | Saved public page extraction for domain/identity review. |
| [runs/2026-10-16-email-evidence-review/published-email-checks.json](runs/2026-10-16-email-evidence-review/published-email-checks.json) | Saved checks for public corroboration of named addresses. |
| [runs/2026-10-16-email-evidence-review/run-notes.md](runs/2026-10-16-email-evidence-review/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-email-evidence-review/zerobounce-results.json](runs/2026-10-16-email-evidence-review/zerobounce-results.json) | Saved email-verification response; interpret with this run's notes. |

</details>

<details>
<summary>runs/2026-10-16-email-verification-pilot (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-email-verification-pilot/controls.json](runs/2026-10-16-email-verification-pilot/controls.json) | Verification control observations. |
| [runs/2026-10-16-email-verification-pilot/datagma.json](runs/2026-10-16-email-verification-pilot/datagma.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-email-verification-pilot/remaining-bounceban.json](runs/2026-10-16-email-verification-pilot/remaining-bounceban.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-16-email-verification-pilot/results.json](runs/2026-10-16-email-verification-pilot/results.json) | Saved verification-pilot results; see accompanying run notes. |
| [runs/2026-10-16-email-verification-pilot/run-notes.md](runs/2026-10-16-email-verification-pilot/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-email-verification-pilot/second-negative-control.json](runs/2026-10-16-email-verification-pilot/second-negative-control.json) | Additional negative-control verifier result. |

</details>

<details>
<summary>runs/2026-10-16-final-expansion (48 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-final-expansion/audit.json](runs/2026-10-16-final-expansion/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-final-expansion/buyer-search-final.json](runs/2026-10-16-final-expansion/buyer-search-final.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/buyer-search-last.json](runs/2026-10-16-final-expansion/buyer-search-last.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/buyer-search-more.json](runs/2026-10-16-final-expansion/buyer-search-more.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/candidates.csv](runs/2026-10-16-final-expansion/candidates.csv) | Candidate discovery inventory before final contact gating. |
| [runs/2026-10-16-final-expansion/company-dispositions.csv](runs/2026-10-16-final-expansion/company-dispositions.csv) | Company-level fit/signal and discovery dispositions. |
| [runs/2026-10-16-final-expansion/company-pages-extra.json](runs/2026-10-16-final-expansion/company-pages-extra.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/company-pages-final.json](runs/2026-10-16-final-expansion/company-pages-final.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/company-pages-more.json](runs/2026-10-16-final-expansion/company-pages-more.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/company-pages.json](runs/2026-10-16-final-expansion/company-pages.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/discovery-broad.json](runs/2026-10-16-final-expansion/discovery-broad.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/discovery-extra.json](runs/2026-10-16-final-expansion/discovery-extra.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/discovery-final.json](runs/2026-10-16-final-expansion/discovery-final.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/discovery-more.json](runs/2026-10-16-final-expansion/discovery-more.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/discovery.json](runs/2026-10-16-final-expansion/discovery.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/excluded.csv](runs/2026-10-16-final-expansion/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-final-expansion/final-checks.json](runs/2026-10-16-final-expansion/final-checks.json) | Saved final-batch checks and reconciliation observations. |
| [runs/2026-10-16-final-expansion/findymail-extra.json](runs/2026-10-16-final-expansion/findymail-extra.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/findymail-final.json](runs/2026-10-16-final-expansion/findymail-final.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/findymail-last.json](runs/2026-10-16-final-expansion/findymail-last.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/findymail-results.json](runs/2026-10-16-final-expansion/findymail-results.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/findymail-verification.json](runs/2026-10-16-final-expansion/findymail-verification.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/first-party-links.json](runs/2026-10-16-final-expansion/first-party-links.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/follow-up-evidence.json](runs/2026-10-16-final-expansion/follow-up-evidence.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/icypeas-batch-2.json](runs/2026-10-16-final-expansion/icypeas-batch-2.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-batch-3-small.json](runs/2026-10-16-final-expansion/icypeas-batch-3-small.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-batch-3.json](runs/2026-10-16-final-expansion/icypeas-batch-3.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-batch-4.json](runs/2026-10-16-final-expansion/icypeas-batch-4.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-batch.json](runs/2026-10-16-final-expansion/icypeas-batch.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-results-2.json](runs/2026-10-16-final-expansion/icypeas-results-2.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-results-3.json](runs/2026-10-16-final-expansion/icypeas-results-3.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-results-4.json](runs/2026-10-16-final-expansion/icypeas-results-4.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/icypeas-results.json](runs/2026-10-16-final-expansion/icypeas-results.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/leads.csv](runs/2026-10-16-final-expansion/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-final-expansion/prospeo-extra.json](runs/2026-10-16-final-expansion/prospeo-extra.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/prospeo-last.json](runs/2026-10-16-final-expansion/prospeo-last.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/prospeo-single.json](runs/2026-10-16-final-expansion/prospeo-single.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/prospeo-singles.json](runs/2026-10-16-final-expansion/prospeo-singles.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/prospeo-throttled.json](runs/2026-10-16-final-expansion/prospeo-throttled.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/provider-balances.json](runs/2026-10-16-final-expansion/provider-balances.json) | Dated sanitized provider capacity observation for interpreting this run; not a current allowance. |
| [runs/2026-10-16-final-expansion/public-email-search.json](runs/2026-10-16-final-expansion/public-email-search.json) | Saved search response supporting candidate or buyer discovery. |
| [runs/2026-10-16-final-expansion/published-email-pages.json](runs/2026-10-16-final-expansion/published-email-pages.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/qualified.csv](runs/2026-10-16-final-expansion/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-final-expansion/replacement-finders.json](runs/2026-10-16-final-expansion/replacement-finders.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-16-final-expansion/run-notes.md](runs/2026-10-16-final-expansion/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-final-expansion/send-ready.csv](runs/2026-10-16-final-expansion/send-ready.csv) | Generated draft-ready contacts for this run. |
| [runs/2026-10-16-final-expansion/small-agency-pages.json](runs/2026-10-16-final-expansion/small-agency-pages.json) | Saved public page/source response supporting qualification or identity. |
| [runs/2026-10-16-final-expansion/verification.json](runs/2026-10-16-final-expansion/verification.json) | Saved email-verification response; interpret with this run's notes. |

</details>

<details>
<summary>runs/2026-10-16-interview-rehearsal (1 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-interview-rehearsal/run-notes.md](runs/2026-10-16-interview-rehearsal/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs/2026-10-16-lusha-recovery (2 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-lusha-recovery/contacts.csv](runs/2026-10-16-lusha-recovery/contacts.csv) | Saved recovered contact data. |
| [runs/2026-10-16-lusha-recovery/run-notes.md](runs/2026-10-16-lusha-recovery/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs/2026-10-16-new-icp-broader-live (7 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-new-icp-broader-live/audit.json](runs/2026-10-16-new-icp-broader-live/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-new-icp-broader-live/candidates.csv](runs/2026-10-16-new-icp-broader-live/candidates.csv) | Candidate discovery inventory before final contact gating. |
| [runs/2026-10-16-new-icp-broader-live/excluded.csv](runs/2026-10-16-new-icp-broader-live/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-new-icp-broader-live/leads.csv](runs/2026-10-16-new-icp-broader-live/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-new-icp-broader-live/qualified.csv](runs/2026-10-16-new-icp-broader-live/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-new-icp-broader-live/run-notes.md](runs/2026-10-16-new-icp-broader-live/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-new-icp-broader-live/send-ready.csv](runs/2026-10-16-new-icp-broader-live/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-new-icp-live-gate (7 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-new-icp-live-gate/audit.json](runs/2026-10-16-new-icp-live-gate/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-new-icp-live-gate/candidates.csv](runs/2026-10-16-new-icp-live-gate/candidates.csv) | Candidate discovery inventory before final contact gating. |
| [runs/2026-10-16-new-icp-live-gate/excluded.csv](runs/2026-10-16-new-icp-live-gate/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-new-icp-live-gate/leads.csv](runs/2026-10-16-new-icp-live-gate/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-new-icp-live-gate/qualified.csv](runs/2026-10-16-new-icp-live-gate/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-new-icp-live-gate/run-notes.md](runs/2026-10-16-new-icp-live-gate/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-new-icp-live-gate/send-ready.csv](runs/2026-10-16-new-icp-live-gate/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-new-icp-offline-smoke (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-new-icp-offline-smoke/audit.json](runs/2026-10-16-new-icp-offline-smoke/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-new-icp-offline-smoke/excluded.csv](runs/2026-10-16-new-icp-offline-smoke/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-new-icp-offline-smoke/leads.csv](runs/2026-10-16-new-icp-offline-smoke/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-new-icp-offline-smoke/qualified.csv](runs/2026-10-16-new-icp-offline-smoke/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-new-icp-offline-smoke/run-notes.md](runs/2026-10-16-new-icp-offline-smoke/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-new-icp-offline-smoke/send-ready.csv](runs/2026-10-16-new-icp-offline-smoke/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-provider-comparison (3 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-provider-comparison/comparison.csv](runs/2026-10-16-provider-comparison/comparison.csv) | Tabular provider recovery comparison. |
| [runs/2026-10-16-provider-comparison/comparison.json](runs/2026-10-16-provider-comparison/comparison.json) | Detailed provider comparison responses/observations. |
| [runs/2026-10-16-provider-comparison/run-notes.md](runs/2026-10-16-provider-comparison/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs/2026-10-16-sourcing-test (6 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-sourcing-test/audit.json](runs/2026-10-16-sourcing-test/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-16-sourcing-test/excluded.csv](runs/2026-10-16-sourcing-test/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-16-sourcing-test/leads.csv](runs/2026-10-16-sourcing-test/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-16-sourcing-test/qualified.csv](runs/2026-10-16-sourcing-test/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-16-sourcing-test/run-notes.md](runs/2026-10-16-sourcing-test/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-16-sourcing-test/send-ready.csv](runs/2026-10-16-sourcing-test/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-16-zerobounce-reconciliation (2 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-16-zerobounce-reconciliation/checks.csv](runs/2026-10-16-zerobounce-reconciliation/checks.csv) | Individual reconciliation checks. |
| [runs/2026-10-16-zerobounce-reconciliation/run-notes.md](runs/2026-10-16-zerobounce-reconciliation/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs/2026-10-18-b2b-saas-outbound-fresh (31 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-18-b2b-saas-outbound-fresh/README.md](runs/2026-10-18-b2b-saas-outbound-fresh/README.md) | Run overview, rules, counts and evidence navigation. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/draft-outreach.md](runs/2026-10-18-b2b-saas-outbound-fresh/draft-outreach.md) | Agent-written sourced draft outreach for this ICP. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/audit.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/audit.json) | Generated reconciliation counts and gate reasons. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/balances-after.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/balances-after.json) | Dated sanitized provider capacity observation for interpreting this run; not a current allowance. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/bounceban-balance-before.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/bounceban-balance-before.json) | Dated sanitized provider capacity observation for interpreting this run; not a current allowance. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/buyer-alternatives.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/buyer-alternatives.json) | Buyer alternatives and identity decisions. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/companies-examined.csv](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/companies-examined.csv) | Company-level dispositions, including companies without contact rows. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/completion-check.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/completion-check.json) | Saved run-specific completion assertions. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/credit-use.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/credit-use.json) | Saved provider debits and cost reconciliation. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/excluded.csv](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/excluded.csv) | Generated excluded contact attempts and reasons. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-salesforge.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-salesforge.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-saleshandy.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-saleshandy.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-usergems-alternative.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-usergems-alternative.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-usergems-fallback.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-usergems-fallback.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-usergems.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/finder-usergems.json) | Saved contact-provider lookup or job response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/findymail-balance-before.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/findymail-balance-before.json) | Dated sanitized provider capacity observation for interpreting this run; not a current allowance. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/inputs.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/inputs.json) | Saved request, target and declared qualification rules. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/leads.csv](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/leads.csv) | Input contact attempts, including unsuccessful records. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/prior-run-dedupe.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/prior-run-dedupe.json) | Comparison against existing research before acceptance. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/qualified.csv](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/qualified.csv) | Generated retained research under this run's policy. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/run-notes.md](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/run-notes.md) | Dated decisions, methods, failures and interpretation. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/source-evidence.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/source-evidence.json) | Saved source excerpts and fit, signal or buyer judgments. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-hockeystack.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-hockeystack.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-salesforge.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-salesforge.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-saleshandy.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-saleshandy.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-second-salesforge.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-second-salesforge.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-second-saleshandy.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-second-saleshandy.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-usergems-alternative.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-usergems-alternative.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-usergems.json](runs/2026-10-18-b2b-saas-outbound-fresh/evidence/verification-usergems.json) | Saved email-verification response; interpret with this run's notes. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/review-parked.csv](runs/2026-10-18-b2b-saas-outbound-fresh/review-parked.csv) | Generated retained contacts with unresolved reasons. |
| [runs/2026-10-18-b2b-saas-outbound-fresh/send-ready.csv](runs/2026-10-18-b2b-saas-outbound-fresh/send-ready.csv) | Generated draft-ready contacts for this run. |

</details>

<details>
<summary>runs/2026-10-18-parked-resolution (5 files)</summary>

| File | Role |
| --- | --- |
| [runs/2026-10-18-parked-resolution/evidence/bounceban-balance-before.json](runs/2026-10-18-parked-resolution/evidence/bounceban-balance-before.json) | Dated sanitized provider capacity observation for interpreting this run; not a current allowance. |
| [runs/2026-10-18-parked-resolution/evidence/current-mx.json](runs/2026-10-18-parked-resolution/evidence/current-mx.json) | Saved run evidence; interpret with the accompanying run notes. |
| [runs/2026-10-18-parked-resolution/evidence/lusha-followup.json](runs/2026-10-18-parked-resolution/evidence/lusha-followup.json) | Saved run evidence; interpret with the accompanying run notes. |
| [runs/2026-10-18-parked-resolution/evidence/public-address-checks.json](runs/2026-10-18-parked-resolution/evidence/public-address-checks.json) | Saved run evidence; interpret with the accompanying run notes. |
| [runs/2026-10-18-parked-resolution/run-notes.md](runs/2026-10-18-parked-resolution/run-notes.md) | Dated decisions, methods, failures and interpretation. |

</details>

<details>
<summary>runs (1 files)</summary>

| File | Role |
| --- | --- |
| [runs/README.md](runs/README.md) | Index of canonical research and all public dated runs. |

</details>

<details>
<summary>scripts (3 files)</summary>

| File | Role |
| --- | --- |
| [scripts/check_submission.py](scripts/check_submission.py) | Offline saved-package, snapshot, merge and tracked-link validation. |
| [scripts/prepare_export.py](scripts/prepare_export.py) | Deterministic normalization, exclusion, review and export gates. |
| [scripts/refresh_public_partners.py](scripts/refresh_public_partners.py) | Optional live refresh of the saved public partner-profile audit. |

</details>

<details>
<summary>skills (1 files)</summary>

| File | Role |
| --- | --- |
| [skills/lead-research/SKILL.md](skills/lead-research/SKILL.md) | Ordered agent research and exception-handling procedure. |

</details>

<details>
<summary>tests (2 files)</summary>

| File | Role |
| --- | --- |
| [tests/test_prepare_export.py](tests/test_prepare_export.py) | Export integration regression tests for both output layouts. |
| [tests/test_submission_fields.py](tests/test_submission_fields.py) | Accept-all alias and campaign merge-field regression tests. |

</details>
