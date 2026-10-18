# Independent recruitment run notes

## Scope and sequence

Run date 2026-10-18, fresh checkout baseline 76f3329. Read AGENTS.md, CLAUDE.md, original assignment, CONTEXT, decisions, open questions, provider access, data dictionary and ordered lead-research skill. No original-chat lead suggestions used. No source/policy/canonical campaign/provider-setting/Git-history changes made. Only the new run contains persistent output.

The run definition was saved before detailed company qualification. Initial broad discovery searches identified public candidates; a search hit alone was not an examined-company decision. Four organizations received active first-party qualification review: Ripple Recruitment, Optiveum, Wedoe Search Group and Axe Talent. Incidental search-result mentions were not assessed as candidates. No geography/language filter, recent-event cutoff or default client cold-email service requirement was applied.

## Qualification judgments

Optiveum and Axe Talent are explicit boutique recruitment firms. Optiveum's named QUERTUM PL case documents senior .NET developer hires for a software company and carries publication date 2024-11-15, engagement September-November 2024. Axe's named Nomic Labs (HardHat) case describes a compiler engineering lead hired from Meta. Compiler engineering is software engineering; this was not inferred from the unrelated BAE systems-engineer case. Axe case is undated. Neither case is called recent. Current first-party pages identify Tomasz and Natalia as founders; direct personal LinkedIn access was restricted, but the exact personal URL was recovered and identity corroborated using the company About link (Tomasz) or publicly indexed personal profile (Natalia).

Commercial suitability is a separate, provisional judgment. Recruiting and candidate outreach can create mailbox/domain administration work; neither firm's current sending volume, sequencer, budget or intent was established. Optiveum's inspected services were recruitment, outsourcing and hub setup. Axe's own software builds academic resumes. No competing mailbox/domain/warmup business found. Both founders plausibly influence vendor spend; no source proves either personally owns sending infrastructure.

Ripple has a real Chaptr front-end-developer placement case, but current services emphasize manufacturing/engineering and boutique scale was unclear. Held as signal_uncertain rather than silently treating a historical software case as current specialist positioning. Wedoe meets literal boutique/engineering placement fit (Later case, solo founder, four active searches maximum) but its explicit warm-introduction/referral model and cold-DM rejection give weak commercial evidence for scalable cold-email infrastructure; a commercial hold prevented enrichment. These company-level holds are in company-dispositions.csv, not extra retained contacts in review-parked.csv. No buyer rows were fabricated for unadvanced accounts.

## Provider choices, failures and recovery

Public-page search/read used the built-in web tool. No separately metered Exa/Firecrawl/Tavily/contact discovery searches were charged. Initial direct Icypeas and BounceBan balance checks failed with URLError in the sandbox and consumed no known credits. The authorized network retry succeeded; no credential or provider configuration was changed. Icypeas free balance was 48.900000999999996; BounceBan 95. Both had usable credits, so Icypeas was used before Datagma under the documented provisional finder order.

A named email was not exposed on Optiveum's inspected contact page. Icypeas returned Tomasz Polikowski at optiveum.com with status FOUND and certainty ultra_sure. Axe's homepage publicly provides natalia@axetalent.com, so no finder credit was spent there. No guessed email or generic inbox was assigned to a buyer.

BounceBan regular single verification was selected first under the runbook. Current official documentation was checked for auth, cost and polling. Both calls completed synchronously with status success, so no resubmission or polling was necessary. Tomasz: deliverable, score 99, accept-all false. Natalia: deliverable, score 97, accept-all true. Under current policy each is normalized valid; Natalia's domain risk remains true separately. Neither clear verdict was followed with an unnecessary second verifier. No contradictory clear result exists. Same website/email domains, so alternate-domain proof was not needed.

LinkedIn direct requests returned 999/cache misses. Personal URLs were preserved and corroboration limitations recorded. Ripple's guessed /about-us/ failed, then site navigation supplied /about/. Axe's dedicated case detail failed browser cache extraction, then a direct public HTML GET succeeded (HTTP 200); the saved fetch-status receipt records that success. Printing that page first failed with local Windows cp1252 UnicodeEncodeError; the follow-up set stdout to UTF-8 and successfully inspected the detail. BounceBan documentation web extraction also failed; direct public OpenAPI YAML inspection established the standard endpoint and query schema. None of these public reads consumed finder/verifier credits.

## Credits and cash

Three credit-consuming actions total of twelve permitted: one Icypeas finder (1 credit), two BounceBan verifications (2 credits). Icypeas balance after 47.900000999999996, observed delta 1. BounceBan after 93, delta 2. Separate provider credits are not a shared currency; total is three actions and three units across their accounts. Four successful free balance calls plus two initial failed free balance attempts. Finder/verifier action budget remaining: 9. Additional cash spent: $0. No purchase, paid top-up, install, settings change, contact, enrollment or CRM import.

## Suppression, deduplication and counts

Local suppression uses normalized exact company name, website and email domain, and address. Public InboxKit homepage trusted-by, partner list and customer cases were inspected; no retained company named. This does not establish private account state. Two distinct company domains and two distinct emails; duplicate count 0 and local/public suppression matches 0. No invalid replacement attempts.

Requested 2 companies and 2 buyers; achieved 2 companies and 2 complete buyer contacts. Four companies examined: 3 literal fit_and_signal, 1 signal_uncertain; 2 commercially retained and 2 not advanced. Company dispositions are separate from contact export counts. Contact attempts 2; retained research 2; valid 2, catch_all 0, unknown 0, invalid 0; accept-all true 1. Export ready/review/excluded counts and reconciliation are in audit.json. Source facts, snippets, source dates and inference are in source-evidence.json. Provider receipts and credit-ledger.csv preserve the raw assessments. No evidence indicates confirmed purchasing intent. Provider-positive results do not guarantee delivery.

## Reproduce

From this clean checkout, use an existing Python 3.9+ runtime. Credentials stay in ignored .env. Follow the runbook with the saved ICP and rules; current tools/account credits are external prerequisites. Repeat sourcing or provider actions only if intentionally refreshing evidence, and account for their credits. To regenerate the saved mechanical export without API calls:

```powershell
python scripts/prepare_export.py runs/2026-10-18-software-recruitment-independent/evidence/leads.csv --output-dir runs/2026-10-18-software-recruitment-independent --presentation
```

Use validation-results.json for actual test results. The existing submission checker validates the canonical assignment, not new-ICP source judgments. This run's audit and explicit source review provide the relevant two-contact checks.

## Final validation result

New-run audit: 2 input, 2 research, 2 ready, 0 parked, 0 excluded; reconciles true. Structural, receipt, local-link, risk-flag, copy dash and opt-out checks passed. All 3 existing unit tests passed. Existing canonical submission checker passed with its own 100/97/3 counts; those do not describe this new run. Only the new run is untracked/changed; source, policy and existing data remain unchanged. An initial link audit ran before its own validation report existed; final link audit resolves the reference.
