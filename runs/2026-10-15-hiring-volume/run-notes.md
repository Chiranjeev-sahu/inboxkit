# Hiring-signal volume test, 2026-10-15

## Rule and scope

ICP: agencies that run managed cold email for clients. A company passes fit when its own site or job posting explicitly describes client cold email delivery. The candidate buying signal is a relevant outbound, GTM, campaign, or deliverability opening. For this experiment, measure whether its publication is within 90 days of 2026-10-15. Relative dates are recorded as observed, not converted to invented exact dates. A closed posting can still evidence a recent hiring event, but is flagged. This is a test of hiring as a signal, not final signal selection. No geography or language filter was applied.

Search covered public job pages, founder posts, and first-party agency sites. One company is one candidate even if it has multiple jobs. Search snippets were discovery cues; linked pages were inspected where possible. `leads.csv` contains the buyer work completed in this run, not all discovered companies. Existing runs are counted separately and their verified addresses were not rechecked.

Elapsed agent time for this test was approximately 11 minutes (15:41 to 15:52 UTC), including searching, buyer lookup, verification, and saving the audit. This was not a timed human reproduction from a clean checkout.

## Distinct companies examined

The table records 25 distinct named organizations. `fit_and_signal` means company fit and a relevant recent hiring source were reasonably evidenced; it does not mean we have a usable email. `signal_uncertain` means a relevant posting exists but its recency or agency identity needs confirmation. `older` is outside the test window. These are **not** 25 qualified contacts.

| Company | Disposition | Evidence and reason |
| --- | --- | --- |
| botified | fit_and_signal, prior run | [Job](https://www.onlinejobs.ph/jobseekers/job/gtm-cold-email-campaign-specialist-contract-remote-1742066) dated 2026-10-01; [fit](https://botified.ai/about). Existing valid buyer in strict-signal run. |
| Grow Surely | fit_and_signal, prior run | [Founder feed](https://ca.linkedin.com/in/gregory-martignoni) showed recent GTM strategist hiring; [fit](https://growsurely.com/services/cold-email-agency). Existing valid buyer in signal-conversion run. |
| StackOptimise | fit_and_signal, prior run | [Founder hiring post](https://www.linkedin.com/posts/penn-frank_were-hiring-gtm-engineer-at-stackoptimise-activity-7490059094163251200-mjGx) displayed two months old; [fit](https://www.stackoptimise.com/about-us). Existing buyer catch-all. |
| Hypergen | fit_and_signal | [GTM engineer post](https://www.linkedin.com/posts/aleksandar-ivanov-_were-hiring-a-gtm-engineer-who-talks-to-activity-7498718545263132672-2S1Y) reposted as two weeks old on [company LinkedIn](https://www.linkedin.com/company/hypergen); [fit](https://www.hypergen.io/about-us). Buyer catch-all. |
| SalesSourcers | fit_and_signal | [Job](https://ph.linkedin.com/jobs/view/gtm-engineer-at-salessourcers-4458142725) displayed one month old; [fit](https://www.salessourcers.com/). Buyer valid. |
| LeadRoad | fit_and_signal | [Job](https://in.linkedin.com/jobs/view/gtm-engineer-at-leadroad-4469832937) displayed two weeks old and explicitly says client email campaigns; [site](https://www.leadroad.io/). Findymail found [Nikhil Tundurwar](https://www.saleshandy.com/case-studies/leadroad), but the email is catch-all. |
| Sparklead | fit_and_signal | [Job](https://cy.linkedin.com/jobs/view/gtm-engineer-at-sparklead-4467740660) displayed three weeks old; [fit and founder](https://sparkleadgo.com/about). Founder [published email](https://link.me/alexanzartarian) is catch-all. |
| Snipe Outbound | fit_and_signal | [Job](https://za.linkedin.com/jobs/view/gtm-engineer-at-snipe-outbound-4478460526) displayed one hour old; [fit and founder](https://snipeoutbound.com/about/). Hunter had no result; Findymail found a catch-all email. |
| Pipeline Playbooks | signal_uncertain | [Job](https://uk.linkedin.com/jobs/view/gtm-engineer-cold-email-campaign-manager-at-pipeline-playbooks-4438632639) displayed three days old but search crawl metadata said three months old; [fit and founder email](https://www.pipelineplaybooks.com/). Buyer catch-all. |
| Flowd | signal_uncertain | [Job](https://uk.linkedin.com/jobs/view/gtm-engineer-at-flowd-4459687061) described client outbound but redirected on direct retrieval, so date not reliable; [fit](https://www.flowd.co.uk/about-us). Buyer catch-all. |
| VelocityFlow | signal_uncertain | [First-party hiring page](https://velocityflow.co/gtm-engineer/) and [fit](https://velocityflow.co/); publication date not found. |
| Olympo Labs | signal_uncertain | [Hiring repost](https://community.clay.com/members/b95b8cb0-612f-43a5-afb6-ff3423e323d6) displayed about three months old, near boundary; [fit](https://olympolabs.com/). |
| DigitalSalesLabs | signal_uncertain | [Wellfound role](https://wellfound.com/jobs/4095819-cold-email-inbox-manager-remote-us-hours) found, but publication and crawl age conflict. Client cold email is described in role; first-party fit not yet checked. |
| Pipehack | signal_uncertain | [Job](https://es.linkedin.com/jobs/view/gtm-engineer-at-pipehack-4392672527) displayed three weeks old but search crawl metadata six months old. Role describes client multichannel campaigns, but first-party fit missing. |
| hard.coded | signal_uncertain | [Job](https://wellfound.com/jobs/4262791-cold-email-specialist-copywriter) surfaced, but direct page failed and client cold email as a standing service is unproven. |
| Sparq Labs | signal_uncertain | [Job URL](https://in.linkedin.com/jobs/view/gtm-engineer-at-sparq-labs-4462789274) redirected. Possible [SparqLabs site](https://getsparq.ai/) describes outbound services, but company/domain identity needs confirmation. Do not confuse with Sparklead. |
| Six Figure Consulting | signal_uncertain | [Built In listing](https://builtin.com/job/gtm-engineer-email-marketing-operations-manager/9750179) was recently reposted; [older original listing](https://in.linkedin.com/jobs/view/lead-generation-specialist-at-six-figure-consulting-4185969723) showed one year. A repost is not proof of a new opening. |
| Anevo Marketing | older | [Founder hiring post](https://www.linkedin.com/posts/matthew-lucero_hiring-gtm-lead-remote-100k-activity-7437955652502634496-GDY_) displayed six months old; [fit](https://anevo.com/). |
| Beanstalk Consulting | older | [Hiring post](https://www.linkedin.com/posts/leonardo-sdraulig_hiring-gtm-engineer-at-beanstalk-consulting-activity-7412449430362259456-qHMj) displayed four months old. |
| getGTM | older | [Job](https://in.linkedin.com/jobs/view/customer-success-gtm-execution-lead-eir-at-getgtm-4381588583) displayed seven months old. |
| Pearl Lemon Group | older | [Wellfound role](https://wellfound.com/jobs/3770934-copywriting-intern-b2b-cold-email-linkedin-copywriting) had no recent publication evidence. |
| Crantech | older | [First-party job](https://www.crantech.uk/job-detail?id=1) dated 2026-02-12. |
| Premium Inboxes | not_fit | [Job](https://www.linkedin.com/jobs/view/gtm-engineer-founding-at-premium-inboxes-4456719333) is for an infrastructure supplier, not an agency running client cold email. |
| Go To Market Agency | not_fit | [Job](https://es.linkedin.com/jobs/view/gtm-engineer-%2B-sdr-%E2%80%93-linkedin-remoto-at-go-to-market-agency-4474682223) centers on LinkedIn; managed client cold email not established. |
| Roosevelt Marketing Outstaffing | identity_uncertain | [Recruiter job](https://al.linkedin.com/jobs/view/senior-gtm-engineer-cold-email-outbound-agency-experience-required-at-roosevelt-marketing-outstaffing-4384043916) hides the actual client agency, so no usable company/domain. |

## Conversion observed

- 25 named organizations examined, including 3 carried forward from earlier hiring runs; 8 pass fit plus recent hiring on current evidence, and 9 more have a relevant opening with material uncertainty. The first 8 are not an exhaustive market count.
- Of 7 buyer rows researched in this run: all 7 have named work emails, 1 is `valid`, and 6 are `catch_all`. The `valid` row is SalesSourcers.
- The **8 distinct fit-plus-recent-hiring agencies** include 3 from prior runs; their combined clear-valid buyer count is **3** (botified, Grow Surely, SalesSourcers). The other 5 verified hiring emails are catch-all. This is a cross-run tally, not the output of this run alone.
- Verification in this run: three MillionVerifier calls returned `error` and showed balance 487 after the first; Reoon gave six catch-all results and one safe/non-catch-all result. Hunter found one email, found no email for one buyer, and returned HTTP 429 on a third attempt. Findymail found the two buyers that lacked addresses after the Hunter step; its public API docs say one finder credit is charged per result. No cash was spent; free credits may have been consumed. Provider error and rate limiting are part of measured yield.
- The planned milestone of 20 distinct fit-plus-recent-hiring agencies was **not reached**: 8 were confirmed after examining 25 organizations. The number of qualified *company signals* is not the number of export-ready rows. No evidence here supports projecting 100 verified contacts from hiring alone in the remaining assignment time.
- No duplicates within this run. No suppression matches observed in this run. No messages were sent or imported.

## Interpretation and next experiment

Hiring has real supply, but a strict recent-job filter plus buyer email verification loses many accounts. Do not select or reject it as the sole signal from this small convenience sample. The next useful test is to resolve the 9 uncertain hiring sources and measure the same funnel for named client case studies. All 8 confirmed hiring accounts have a named buyer and an independently checked email across this and prior runs. Keep the $0 cash limit; check provider access and free-credit balance before additional calls. If the 100-row goal is infeasible under a single signal, bring that evidence into the strategy choice instead of silently treating agency fit as buying intent.
