# InboxKit GTM campaign context

This project develops a sourced prospect list and draft LinkedIn/email campaign for InboxKit, a cold-email infrastructure product. The business objective is a campaign that could produce 15 qualified demos in 30 days, with the assumptions and contact-volume math stated in the strategy memo. The [original assignment](GTM%20Engineer%20Hiring%20Assignment.txt) defines the requested work; this document defines the vocabulary used throughout the repository.

## Audience and qualification language

**ICP:** A description of the companies and buyers a research run should identify. The default ICP covers outbound, lead-generation and GTM agencies serving client businesses; a supplied new ICP defines its own fit rule.

**Segment fit:** Public evidence that a company matches the supplied ICP. For the default agency campaign this means selling, building, operating or supporting client cold-email or outbound infrastructure.

**Operational signal:** A sourced fact establishing active, relevant work, such as a client campaign, sending infrastructure, volume, service expansion or relevant hiring. It indicates relevance rather than confirmed purchase intent. Dates add context; an arbitrary 90-day cutoff is not an eligibility rule.

**Buyer:** A named current founder, head of growth or infrastructure owner with a relevant role. The evidence should distinguish direct technical ownership from inferred executive influence.

**Commercial suitability:** A judgment that the company is a plausible InboxKit prospect as well as matching the literal ICP. Competing sending-infrastructure products warrant review. A sequencer integration by itself is not a competitive exclusion.

**Distinct company:** One organization in the accepted list, even if it has aliases, alternate sending domains or multiple possible contacts. Additional buyers are lookup alternatives rather than additional counted companies.

## Evidence language

**Prospect evidence:** Public sources supporting company fit, operational relevance, buyer identity, work-email association or personalization.

**Product evidence:** A supporting `inboxkit.com` page for an InboxKit claim used in the strategy or copy. It is separate from prospect evidence.

**Source-backed first line:** A truthful opening sentence derived from the prospect's recorded source. Undated evidence is not described as recent.

**Domain relationship proof:** Public evidence connecting an alternate email domain to the listed organization through the same organization, parent/subsidiary relationship, rebrand or shared leadership. A finder result or positive verifier is insufficient on its own.

## Verification and disposition language

**Verification status:** A normalized email assessment. `valid` means a provider returned a clear positive deliverable/verified verdict without a conflicting clear negative; `catch_all` means ambiguity; `unknown` means unresolved; `invalid` means a clear negative.

**Accept-all flag:** A separate domain-risk observation. A positive delivery assessment may coexist with accept-all=true. Blank is unreported; three older agency records retain literal `unknown`. Neither is equivalent to false.

**Explicit hold:** A recorded evidence or verification issue that prevents promotion even if the provider verdict is positive.

**Research row:** A retained qualified company/buyer record with required fields and sources, including records awaiting review.

**Draft-ready row:** A retained research record that passes the current verification, domain-relationship, deduplication, suppression and hold rules. This is a list-quality label, not a delivery guarantee or authorization to contact someone.

**Parked row:** A retained research record with an explicit unresolved reason. Research equals draft-ready plus parked.

**Excluded attempt:** A failed, invalid, duplicate, suppressed or nonqualified record retained in the attempt history. Input attempts equal research plus excluded attempts.

**Suppression:** Email addresses, domains or normalized company names that must be excluded. Public partner/customer evidence supplements, rather than substitutes for, private account records before an authorized campaign.

## Execution language

**Provider waterfall:** Suitable sources tried for a particular job, with a fallback on failure or unresolved evidence and a stop when the quality rule is met. Company discovery, email finding and verification are separate jobs.

**Run:** A saved research request, its decisions, evidence, attempts and generated outputs.

**Canonical agency dataset:** The cumulative source records behind the default agency campaign. Reviewer-facing deliverables are generated snapshots of this source.

**Clean checkout:** A fresh repository checkout that can run the documented local checks and research procedure with the reader's own agent, web access and provider credentials.

For implementation and file paths, see the [README](README.md). [Decisions](docs/decisions.md) records tradeoffs; the [data dictionary](docs/data-dictionary.md) defines column-level meanings.
