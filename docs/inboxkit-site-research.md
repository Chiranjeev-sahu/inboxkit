# InboxKit site research for the assignment

**Dated source record.** Page observations and inventory counts below retain their original retrieval dates. This file was reviewed for consistency on 18 October 2026, without recrawling the live site. Recheck the relevant source before changing a product claim or preparing a later live campaign.

Checked 15 October 2026. The [public sitemap](https://www.inboxkit.com/sitemap.xml) lists 409 URLs. Its complete URL inventory is in [inboxkit-sitemap-inventory.csv](inboxkit-sitemap-inventory.csv): 227 `/learn`, 58 `/partners`, 32 `/alternatives`, 30 `/resources`, 24 `/compare`, 11 `/case-studies`, 5 `/customer-stories`, and the core pages. This is a **site inventory**, not a claim that all 409 pages were read or that their claims were validated. For a 6 to 8 hour assignment, reading all 227 articles would add cost and noise without clearly improving the agency offer. Read the core product, agency, integration, and relevant customer pages before writing copy; inspect more articles only when a specific claim needs support.

## Product context that can inform an offer

| InboxKit-published fact | Direct page | Use in copy |
| --- | --- | --- |
| Google Workspace and Microsoft 365 mailbox infrastructure for outreach teams | [Homepage](https://www.inboxkit.com/) | Describe the mailbox layer; do not promise an inbox rate. |
| Automated SPF, DKIM, and DMARC setup | [Pricing](https://www.inboxkit.com/pricing) | A concrete agency operations benefit; no guaranteed placement claim. |
| Multiple workspaces and unlimited team members | [Pricing](https://www.inboxkit.com/pricing) and [agency solution](https://www.inboxkit.com/agency-email-solution) | Potential fit for agencies managing several clients. |
| Smartlead and Instantly connectivity | [Smartlead guide](https://www.inboxkit.com/learn/inboxkit-smartlead-integration), [Instantly guide](https://www.inboxkit.com/learn/inboxkit-instantly-integration) | Treat them as integrations. Do not imply InboxKit replaces the sequencer. |
| Warmup | [Pricing](https://www.inboxkit.com/pricing), [warmup page](https://www.inboxkit.com/email-warmup) | The pricing page lists warmup as an add-on, while the homepage says built-in. Avoid saying it is included at no extra charge. |
| Flat per-mailbox billing with no base plan/minimum on current pricing page | [Pricing](https://www.inboxkit.com/pricing) | Check again before quoting an amount or billing period. |

These are claims **made by InboxKit on its own site**, which satisfies the assignment's source rule for product statements. They are not independent validation of performance. The message should connect a documented agency signal to one relevant capability, not recite the whole feature list. Existing [product-claims.md](product-claims.md) contains shorter candidate wording.

## Prospect exclusion discovered during site review

**Updated after the full public partner audit on 15 October.** The first three examples below explain how the issue was discovered. The [partner audit](inboxkit-partner-audit.csv) now covers **all 56 public partner profiles**, with both official names and domains. [suppression.csv](../data/suppression.csv) has **56 partner domains and 73 distinct public partner/customer name entries**. The [proof audit](inboxkit-proof-audit.md) covers all 11 case studies and homepage customer logos.

The [partner directory](https://www.inboxkit.com/partners) and customer pages are relevant to **who should receive a new-customer campaign**:

- [Hypergen / Hypernova](https://www.inboxkit.com/partners/hypergen-hypernova) lists `www.hypergen.io` as a certified partner.
- [Understory](https://www.inboxkit.com/partners/understory) lists `www.understoryagency.com` as a certified partner. Understory also appears on the [homepage](https://www.inboxkit.com/).
- [LeadHaste](https://www.inboxkit.com/partners/leadhaste) is a certified partner and has an [InboxKit customer case study](https://www.inboxkit.com/case-studies/leadhaste-millions-emails-automated-dns-inboxkit).

These domains and partner names are now in `data/suppression.csv` and must not enter a new-customer export. Their underlying research remains in the working sheet for audit. A search miss on the public site does **not** prove another agency is not already a customer; a private CRM suppression check remains unknown.

## Offer angles considered during site research

1. **Agency setup burden:** For an agency adding client campaigns, mailbox and DNS administration may absorb operator time. InboxKit's [agency solution](https://www.inboxkit.com/agency-email-solution) and [pricing](https://www.inboxkit.com/pricing) support a message about account organization and DNS setup. A prospect's recorded operational evidence supports the reason to contact them; a recent hire or named case is optional under the current rule.
2. **Keep the sequencer:** A team using Smartlead or Instantly may care that InboxKit mailboxes connect to the tool it already runs. Use the relevant [Smartlead](https://www.inboxkit.com/learn/inboxkit-smartlead-integration) or [Instantly](https://www.inboxkit.com/learn/inboxkit-instantly-integration) page. Do not claim the agency uses either unless prospect evidence shows it.
3. **Proof before promise:** An [InboxKit agency customer story](https://www.inboxkit.com/case-studies/actiscale-automated-mailbox-stack-inboxkit) could be cited as one customer's reported experience, with the customer named. It must not become a general performance guarantee.

The [draft campaign](../deliverables/campaign-copy.md) uses the agency setup burden as its offer context and links to InboxKit's [30-minute demo page](https://www.inboxkit.com/demo) as its one sales CTA. No messages have been sent.
