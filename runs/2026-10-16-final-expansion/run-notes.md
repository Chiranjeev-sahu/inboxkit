# Final expansion, 16 October 2026

Continue the agreed agency ICP toward 100 distinct companies with one buyer each. Initial canonical count: 63 qualified companies and 59 provider-assessed send-ready draft contacts. Fit requires client cold-email/outbound infrastructure services; operational campaign examples or infrastructure details support relevance, not confirmed purchase intent. No date or geography cutoff. All outreach stays draft. Existing credits only; no purchases.

Research candidates are staged in `candidates.csv` and are not counted until evidence, named buyer/email, verification, duplicate and suppression checks are complete. Discovery evidence is in `discovery.json`. Public partner/customer suppression remains `data/suppression.csv`.

Discovery holds: Salesdorado is a media business with an exited founder; Leadspicker emphasizes software; Uptown Creation's discovered evidence is LinkedIn-focused; Respect.Studio is acquired and needs a current buyer/channel check. RevBoss now emphasizes warmer relationship-based email and is held rather than silently treating its historical cold-email model as current. OutboundView's current first-party page emphasizes calling; earlier third-party email references alone were not used for acceptance. Leadable's founder has a different current venture, requiring a current-role check before use.

## Result

**37 added companies, 100 total distinct companies, 92 draft send-ready contacts.** All 100 final-sheet emails have positive provider verification results. This batch staged 40 companies: 37 accepted, LeadBuds and Trigacy unresolved after finder misses, and Honeyleads held after Findymail returned `verified=false` for its published founder address. Leadable was resolved through current Head of Operations Rassim Ruwaiz, whose public profile describes ownership of client campaign delivery across email and other channels.

The 37-row batch has 33 send-ready contacts and four alternate-domain contacts. Its export reports zero duplicate or suppression exclusions. Canonical totals: 107 input rows, 100 qualified, 92 send-ready; the seven prior rejected/uncertain rows remain excluded. The final file is `deliverables/lead-sheet.csv`; `deliverables/send-ready.csv` is the smaller import draft. Company-only records were not used to pad the count.

## Provider results and limits

- Exa direct API and public web pages supplied sources and exact professional identities. Page extracts and search evidence are saved alongside this note. No application code or new architecture was added.
- Icypeas found 14 addresses across two eight-person batches. Its next 15-person batch was rejected because only about 5.3 existing credits remained. A smaller five-person batch found three addresses; a final two-person batch missed both. Receipt files preserve the outcomes.
- Prospeo reported 97 existing free-plan credits. The bulk endpoint returned 429. Its single-person endpoint worked when requests were spaced out, recovering relevant agency emails. Some matches returned addresses at different employers; these were rejected as mismatched associations. An overlapping Growtoro result corroborated an Icypeas address without improving yield; future runs should await the first finder before starting its fallback.
- Findymail began with seven finder credits and ten separate verifier credits. It recovered named alternate-domain emails and the replacement Chief Lead Officer address. Name variants mattered: Caliber's founder was found under the professional alias Efe Ozcanli after the full-name query missed. No addresses were generated from patterns.
- Lusha had two existing credits: one batch preview and one email-only reveal recovered Om Rafols. Two other profiles were compliance restricted and were not retried through Lusha. No phone numbers were revealed.
- BounceBan used 35 existing credits, ending at zero. Thirty-three checks gave positive results; the original Matt Bauman address and Bohdan Shtylyk check remained pending. Their receipt IDs are retained. Findymail used six existing verifier credits: four positive final addresses and two failed checks. Its verifier was the fallback after BounceBan's balance was exhausted or a result was slow. A positive verdict remains probabilistic.
- Connected Apollo reported 185 existing lead credits; no Apollo enrichment was performed in this batch. Its balance alone is not evidence that email discovery worked.

## Corrections and uncertainty

- `matt@mattbauman.me` was published by Matt but Findymail returned `verified=false`. Findymail then found **matt@chiefleadofficer.com** and its verifier returned `verified=true`. Only the latter is in the final sheet.
- `kyley@honeyleads.io` was published on Honeyleads' own site but returned `verified=false`; the company stays outside the final contact sheet.
- KNK's Nicklas lookup missed. The company About page identifies Kenneth Kather as founder/CEO and owner of sending infrastructure, and publishes his named address. That address passed Findymail verification.
- Findymail positively verified Caliber, Chief Lead Officer, KNK, and Leadowski. It returns no domain accept-all field. Those four flags remain blank/unknown, not false. Leadowski's slower BounceBan receipt is retained alongside its positive Findymail verdict; there is no clear contradictory undeliverable verdict.
- Martal, Proven Concept, TektonScale, and Rafols and Co use alternate email domains. They join four earlier alternate-domain contacts outside the send-ready export. The final sheet preserves the association and uncertainty.
- X27's public professional profile says Chairman while an older company page says CEO. The final title uses Co-Founder and Chairman. JumpCrew's finder labels iQor/current parent context while returning the sourced JumpCrew email; that role association is noted for human review before any send.
- Leadowski's first-party page describes operated client outbound systems, warmup, and sequences; client cold-email activity is corroborated by its client reviews at https://clutch.co/profile/leadowski. It is not described as a recent buying event.

All outreach remains draft. This expansion completed the 100-row research sheet; subsequent email-review verdicts and current export counts are recorded in the canonical dataset and individual review report.

Final profile audit also repaired an earlier SalesCaptain row: Bill Stathopoulos had the company LinkedIn URL. The current canonical and deliverable files now use his confirmed buyer profile, https://uk.linkedin.com/in/billstath. All 100 rows have buyer profile URLs, 100 unique emails, and no missing required cells. No first line contains an em dash or en dash; the export and whitespace checks pass.
