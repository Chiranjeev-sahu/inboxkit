# Campaign feasibility and measurement

**18 October 2026 | Public source review and proposed operating assumptions | All outreach stays draft**

The [original assignment](../GTM%20Engineer%20Hiring%20Assignment.txt) asks for a campaign that could **book 15 qualified demos in 30 days**. Attendance is tracked separately from the strategy memo's booking target. Nothing has been sent, so this submission has no observed reply or booking rate.

## External observations and their limits

[Sales.co's first-party report](https://sales.co/research/cold-email-conversion-rate-benchmarks), published October 6, 2026, covers first emails March 6-August 31, outcomes through October 6: at least 36 days per contact. A contact is one address within one campaign, not necessarily a globally unique person. Pooled results: 336,257 contacts, 627,085 emails, 971 positive replies (0.2888%). Booking data covers only Sales.co's own service campaign:

| Reported count / denominator | Recalculated rate |
| --- | ---: |
| 296 positive replies / 124,513 contacts | 0.2377% |
| 143 company bookings / 124,513 contacts | 0.11485% |
| 98 bookings naming cold email / 124,513 contacts | 0.07871% |
| 94 bookings within 30 days / 124,513 contacts | 0.07549% |

Positive includes questions, deferrals and referrals; latest reply determines classification. Cancelled bookings are removed; one meeting counts per company. Forty-five bookings lacked a personal reply, so **143/296 = 48.31% is not positive-reply-to-booking conversion**. Median booking delay: nine days; 49/143 came after 30 days. Cold calls and LinkedIn also contributed. Email preceding booking does not establish causation. No InboxKit agency qualification or held-meeting rate is provided. These are different-offer observations, not this campaign's forecast. [Methodology and booking definitions](https://sales.co/research/cold-email-conversion-rate-benchmarks#methodology).

## Target-implied requirement

Treat **2,000 unique, eligible contacts, one per company**, as a capacity hypothesis, not a demonstrated addressable pool or an assignment requirement. To obtain 15 qualified bookings from that denominator by campaign day 30 requires **15 / 2,000 = 0.75%**. Equivalently, contacts required = 15 / measured qualified-booking rate within the relevant campaign window. That rate is presently unknown.

Define a qualified booking before activation: a confirmed calendar reservation with a current founder, head of growth or infrastructure owner at an eligible agency delivering client outbound, with a documented infrastructure need or evaluation interest. Confirm qualification in the booking exchange/form; do not require attendance to establish it. Count one booking per company, remove cancellations, and dedupe reschedules. Count reservations made by day 30 even if the meeting is held later; this is a proposed interpretation of “book,” to state explicitly. Report pending qualification separately.

Do not force every booking through positive replies. Record both reply-assisted and direct bookings. If using a reply funnel, add the direct path and prevent overlap. The 100-company research sample and the initial 97-contact ready pilot cannot demonstrate a reliable 0.75% outcome rate.

## Proposed 30-day capacity plan

This example preserves cohort-relative LinkedIn days 1/4/10 and email days 3/8/14/20 from the [memo](../deliverables/strategy-memo.md). Cohort launch means relative day 1; offsets are therefore +2/+7/+13/+19 for email.

| Calendar days | Proposed action and constraint |
| --- | --- |
| Before day 1 | Have eligible contacts, monitored reply routing, suppression, calendar access and existing usable sending capacity ready. Confirm the budget and operator limits. |
| Day 1 | Launch the 97 currently draft-ready contacts as the pilot. The three held companies remain outside sending. Email 1 falls on calendar day 3. |
| Days 3-5 | Inspect early bounces, opt-outs, replies, personalization and routing. Correct failures before adding volume. This is an early operational check; the full pilot sequence is unfinished. |
| Days 6-10 | Conditional expansion: cohorts of 380, 380, 380, 380 and 383 = 1,903 additional accepted contacts. Combined with the 97-contact pilot this makes 2,000. Stop or reduce expansion if early evidence or capacity warrants it. |
| Days 12-29 | Complete remaining email touches; the last cohort's relative day 20 is calendar day 29. |
| Day 30 | Reconcile unique contacts, qualified bookings and attribution. Preserve later outcomes separately. |

The upper bound is **2,000 x four = 8,000 email attempts** before reply/booking/opt-out stops. This exact cohort schedule peaks at **477 attempts/day** on days 8, 14 and 20; 8,000/30 is only a calendar average of about 267/day. These are workload calculations, not safe sending limits. If the operator approves a per-mailbox daily cap of c, the peak requires at least ceil(477/c) usable mailboxes, plus any capacity reserved for other traffic. Domain allocation, mailbox health, throttling and sequencer limits must also fit. No universal safe cap is assumed.

Apply LinkedIn only to a prioritized subset whose account allowance and manual workload fit. Its size remains uncommitted until checked; do not assume 2,000 invitations. Follow-ups require acceptance. Stop both channels on any reply, booking or opt-out. Later cohorts have less time to convert before calendar day 30. Waiting for the pilot's complete conversion result would prevent this expansion schedule; if early checks fail, report the resulting target/capacity gap.

## Offer support and execution costs

The [InboxKit agency page](https://www.inboxkit.com/agency-email-solution) supports centralized client-account administration and automated SPF/DKIM/DMARC setup. It also describes a 14-day launch workflow, so newly provisioned infrastructure cannot be presumed ready on campaign day 1. The [pricing page](https://www.inboxkit.com/pricing) supports per-domain admin panels and integrations including Smartlead and Instantly. It lists $3/mailbox/month on monthly billing, or $2.50/month billed annually; warmup is listed as an add-on. Mailbox-only monthly cost is therefore $3 x usable mailbox count; domains, warmup, sequencer, data, agent usage and review remain additional. These prices do not establish deliverability or booking yield.

The single CTA is the [30-minute InboxKit demo](https://www.inboxkit.com/demo). That page asks for company, business email, target cold-email volume and referral source. A submitted form is not itself proof of a booked, qualified slot. Confirm the calendar outcome and available sales capacity. Keep all copy source-backed; do not turn product placement claims into a guaranteed campaign result.

## Attribution, pilot evidence and unknowns

Maintain company/contact IDs, cohort, variant, first-touch and email dates, selected LinkedIn touches, actual sends, human/positive reply labels, booking timestamp, qualification evidence, cancellation/reschedule state and opt-out. Use the shared company/contact ID to dedupe channels. Capture self-reported source and touch history; report email-only, LinkedIn-only and assisted bookings without summing overlapping counts. Attribution is descriptive unless a suitable experiment establishes incremental effect.

For the planning hurdle, use unique eligible contacts first-touched as the denominator, including contacts whose email subsequently bounces. Show attempted, delivered, bounced and pre-send-suppressed totals separately; any delivered-contact conversion rate needs its own labeled denominator. Report calendar-day-30 results alongside days since first touch for each cohort; incomplete cohorts must remain visibly immature. Record attendance as a later separate metric.

Still unknown: the reachable pool of 2,000 eligible companies, sourcing throughput and all-in cost, usable mailbox/domain inventory, LinkedIn allowance, bounce and opt-out rates, positive replies, qualified bookings, time to book, sales availability and channel contribution. The [scale-cost note](../deliverables/scale-cost.md) addresses list production. Feasibility depends on these measurements; the plan does not promise 15 demos.
