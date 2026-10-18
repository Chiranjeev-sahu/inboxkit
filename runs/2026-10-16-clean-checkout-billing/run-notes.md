# Live run from a fresh local checkout

Date: 16 October 2026. Checkout: `ce11557`, created with `git clone --no-hardlinks` from the local repository. The initial `git status --porcelain` was empty. The operator supplied the ignored `.env` as documented; no credentials were committed. The root instructions and unit test loaded from the clone.

## Test prompt and rules

Agent-selected rehearsal prompt: "Find one founder or CEO at a B2B subscription or usage-based billing software company with publicly documented API integrations. Record operational evidence separately from intent, source the work email, verify it using existing credits, personalize a first line, and export drafts."

Fit: software sold to businesses for subscription or usage-based billing. Operational signal: public API/integration documentation and customer deployment evidence. This rule is derived from the rehearsal ICP; the agency managed-cold-email rule is not applied. It is a system portability test, not an argument that all billing founders are qualified InboxKit buyers. No recent hiring or purchase-intent claim is made.

## Execution and result

One company examined, one accepted, zero rejected, zero uncertain. Lago's homepage identifies usage-based/subscription billing, REST APIs, signed webhooks, integrations, and customer deployments: https://getlago.com/. Founder/CEO identity is corroborated by the professional profile https://www.linkedin.com/in/anhthochuong and the sourced finder record. The first line refers only to the homepage's product facts.

Provider commands ran with the fresh clone as their working directory and read its locally supplied ignored credentials. Findymail balance before the run: two finder credits and four verifier credits. One finder returned `anhtho@getlago.com` for the named founder and exact company domain; one verification returned `verified=true`, provider Google. Expected remaining balance is one finder and three verifier credits; no purchase. Findymail does not return a domain accept-all field, so it remains unspecified rather than false.

Run `python scripts/prepare_export.py runs/2026-10-16-clean-checkout-billing/leads.csv` from this checkout. The actual export produced one qualified and one send-ready draft, no duplicates and no suppressed matches. The copied public suppression list was applied. The synthetic demonstration additionally excluded an invalid email, duplicate email, duplicate domain and two suppressed records; its catch-all row remained research-only. The unit test passed.

This was a real clone plus live provider execution by the same connected Codex desktop session. It demonstrates that the checked-in files and documented credential route work from a clean checkout in this environment. It does not claim a separate new agent/session was launched, that every MCP was authenticated, or that an unconfigured interviewer machine will inherit this session's access. The earlier independent CLI failure remains recorded separately.

The rehearsal contact stays outside the 100-agency campaign. No email, LinkedIn message, sequencer import or CRM write occurred.
