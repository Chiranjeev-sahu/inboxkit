# New ICP broader live workflow test

Date: 2026-10-16. Target: at most three complete contacts, separate from the agency campaign. No messages were sent or imported.

## Rule declared before this second screen

Company fit: a B2B software company with an **established internal SDR/outbound team or repeatable outbound engine**. Signal: a public, currently listed SDR/outbound leadership hire whose work includes email outreach or outbound sequencing. The company-fit evidence need not explicitly prove that the team already sends cold email. This is deliberately broader than the [earlier strict test](../2026-10-16-new-icp-live-gate/run-notes.md), which yielded zero of four. Fit and hiring signal remain separate. A visible job opening is enough for this test; an exact posting date is recorded only if a stable date is available. Relative LinkedIn ages varied across captures, so `signal_date` remains blank. The test is about rerun mechanics, not a new InboxKit campaign segment choice.

## Source screen and contact choice

The [candidate log](candidates.csv) records three accepted companies. [Zuddl's official careers page](https://www.zuddl.com/culture) listed the Manager, Sales Development role on capture day, and [the employer's LinkedIn job](https://www.linkedin.com/jobs/view/sdr-manager-at-zuddl-4466847970) said the hire would inherit an established engine and use email among other channels. [Zuddl's product site](https://www.zuddl.com/) confirms software. [Sharan Suresh's LinkedIn profile](https://in.linkedin.com/in/thesharansuresh) shows Zuddl; [The Org](https://theorg.com/org/zuddl) lists VP of Marketing. The SDR manager job says it reports to the CEO, so Sharan's ownership of sending infrastructure is **not confirmed**. Sharan is a plausible senior growth-side buyer, not a proven infrastructure owner.

[Traversal's own site](https://www.traversal.com/blog/leadership-announcement) establishes its software and names Jim Cavanaugh SVP Worldwide Sales. Its [employer-hosted SDR Lead role](https://jobs.ashbyhq.com/traversal/58cbbf79-37e0-4519-ac6a-0f05aeabd56f/) describes a current small SDR pod and sequences across email, phone, and social; [the LinkedIn job mirror](https://www.linkedin.com/jobs/view/sales-development-representative-lead-at-traversal-4469288258) exposed the text when the ATS page required JavaScript. This supports an outbound team and relevant hire, but does not establish its present email volume.

[DOSS's product page](https://www.doss.com/products/platform) establishes operations software. [Scott Dilena's hiring post](https://www.linkedin.com/posts/scottdilena_we-are-hiring-a-sales-development-manager-activity-7497688815898198017-Olx-) links the [employer-hosted manager job](https://jobs.ashbyhq.com/doss/1431038c-9364-4bb9-bccc-a411302879ff), describes eight existing SDRs, and says they bring outbound opportunities. [DOSS's company post](https://www.linkedin.com/posts/doss-com_meet-scott-our-new-gtm-manager-and-the-latest-activity-7364712384826875905-Kh9a) introduced Scott as GTM Manager about one year earlier. His current hiring activity supports continued affiliation; an updated title is not established. The strict earlier rule still does not pass because **current cold-email sending is not explicitly proven**.

The local `data/suppression.csv` had no exact email/domain/company match for these three. A public-site check of [InboxKit partners](https://www.inboxkit.com/partners) and [customer stories](https://www.inboxkit.com/customer-stories) found no named match; that does **not** prove any is not already a customer. No duplicate email or domain appeared in this test. No InboxKit product claim or campaign sequence was generated for this alternate ICP.

## Lookup and verification waterfall

For each named buyer, first-party pages did not show a named work email. Icypeas sync email discovery returned `FOUND` with `ultra_sure` certainty for `sharan@zuddl.com` (search id `K-ECQ6EB8ztoLJeX0yqq`), `jim@traversal.com` (`d6sDQ6EBr29ea0KaAOqc`), and `scott@doss.com` (`OgwDQ6EBGkhls2OoL6nP`). Icypeas is the **email-to-person association source**; the verifier does not independently prove that association. Datagma was not called because the finder stop condition was met for each buyer.

BounceBan account balance was 74 available credits before verification. Its single-email API returned the following clear results, each on October 16:

| Buyer | Result | Score | `is_accept_all` | Result id |
| --- | --- | ---: | --- | --- |
| Sharan Suresh | `deliverable` | 99 | `false` | `bdi-fbea8446` |
| Jim Cavanaugh | `deliverable` | 97 | `true` | `ig9-eaf7c967` |
| Scott Dilena | `deliverable` | 99 | `false` | `5ba-c938f0d6` |

All three were `success`, `is_role=false`, and `is_disposable=false`. Under the runbook these become **provider-assessed `valid`**; the accept-all flag remains separate. The Traversal domain may accept arbitrary addresses, so Jim's mailbox existence is less certain despite BounceBan's specialist verdict. These are not observed delivery outcomes. The post-check balance was **71** available credits, confirming three existing credits were used. No cash purchase was made. ZeroBounce, Reoon, and MillionVerifier were not called because the verifier stop condition was met.

## Measured result and limits

The second screen examined three selected candidates and accepted three under its **broader** rule. Finder results: 3/3 found. Verifier results: 3/3 `deliverable`, including one accept-all domain. The mechanical export produced **3 qualified research rows and 3 draft send-ready rows**, with zero duplicate, suppression, or structural exclusions; see `audit.json`. "Send-ready" here means it passed the documented data gate, not that it was imported or that the buyer and mailbox are certain. This tiny search-selected sample does not estimate scalable yield, bounce rate, or the likelihood of reaching 100 agency leads. The main agency sheet is separate and unchanged. The buyer-role uncertainty for Sharan, exact job posting dates, and true mailbox ownership remain review points. A stronger follow-up would sample new accounts consecutively under one fixed rule rather than select three promising ones.
