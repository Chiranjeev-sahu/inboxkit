# Draft email and LinkedIn sequence

Adapted from an earlier campaign draft on 15 October 2026. The earlier copy supplied the demo CTA, dashboard and domain-panel angle, and day 1 to day 20 interleaving. This version adds direct InboxKit claim links, signal-backed first lines, and the documented reply-based opt-out. All messages remain drafts. No contact has been imported, enrolled, or sent.

`{{first_name}}` maps directly to the explicit `first_name` field in [send-ready.csv](send-ready.csv), while `{{first_line}}` maps to `first_line`; check `first_line_source` before merge. The agency rows contain an `email_variant` decision: A emphasizes client-account management, B domain organization. These are source-informed copy choices, not measured performance winners. See the [full mapping](../docs/data-dictionary.md#merge-fields). The only sales CTA is a [30-minute InboxKit demo](https://www.inboxkit.com/demo) of client mailbox administration. Use either email 1A or 1B on day 3, never both. The [sequence schedule](sequence.csv) gives all day and stop conditions. The STOP instruction is an opt-out, not another sales CTA. A real send would first require a monitored reply-to and the [suppression procedure](../docs/opt-out-and-suppression.md).

## LinkedIn connection note, day 1

Hi {{first_name}}, I work with outbound agencies on email infrastructure. Would be glad to connect.

**Product claims:** none. Connection is the native LinkedIn action; there is no demo ask in this note. Do not send to an opted-out contact.

## Email 1A, day 3: client account management

**Subject:** Client mailbox administration

Hi {{first_name}},

{{first_line}}

I work with InboxKit. Agencies can manage client accounts from one dashboard, with SPF, DKIM, and DMARC configured automatically. If client mailbox administration is taking time from campaign work, the demo shows this workflow.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [agency dashboard](https://www.inboxkit.com/agency-email-solution), [automatic DNS records](https://www.inboxkit.com/pricing), [30-minute demo](https://www.inboxkit.com/demo). The prospect observation in `{{first_line}}` needs that row's `first_line_source`.

## Email 1B, day 3: domain organization

**Subject:** Organizing client domains

Hi {{first_name}},

{{first_line}}

InboxKit gives each domain its own panel and brings client accounts into one dashboard. That is the workflow I wanted to show you for managing agency infrastructure.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [per-domain panels](https://www.inboxkit.com/), [agency dashboard](https://www.inboxkit.com/agency-email-solution), [30-minute demo](https://www.inboxkit.com/demo). The prospect observation in `{{first_line}}` needs that row's `first_line_source`.

## LinkedIn follow-up 1, day 4 if connected and no reply

Thanks for connecting, {{first_name}}. I emailed about managing client accounts from one dashboard with InboxKit. The demo shows that workflow: https://www.inboxkit.com/demo

**Product-claim sources:** [agency dashboard](https://www.inboxkit.com/agency-email-solution), [demo](https://www.inboxkit.com/demo). Send only if email 1 was actually sent and the connection was accepted; the sequence is currently staged only.

## Email 2, day 8 if no reply

**Subject:** Re: client mailbox administration

Hi {{first_name}},

Following up on client mailbox administration. InboxKit configures SPF, DKIM, and DMARC records automatically. The demo covers how agencies manage client accounts from one dashboard.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [automatic DNS records](https://www.inboxkit.com/pricing), [agency dashboard](https://www.inboxkit.com/agency-email-solution), [30-minute demo](https://www.inboxkit.com/demo).

## LinkedIn follow-up 2, day 10 if connected and no reply

One last note, {{first_name}}. InboxKit configures DNS records automatically and provides a panel for each domain. The demo is here if useful: https://www.inboxkit.com/demo

**Product-claim sources:** [automatic DNS records](https://www.inboxkit.com/pricing), [per-domain panels](https://www.inboxkit.com/), [demo](https://www.inboxkit.com/demo).

## Email 3, day 14 if no reply

**Subject:** Client domain setup

Hi {{first_name}},

When a client adds domains, how those accounts are organized matters. InboxKit provides a panel per domain and one dashboard for client account management.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [per-domain panels](https://www.inboxkit.com/), [agency dashboard](https://www.inboxkit.com/agency-email-solution), [30-minute demo](https://www.inboxkit.com/demo).

## Email 4, day 20 if no reply

**Subject:** Closing the loop

Hi {{first_name}},

I will close the loop here. If client infrastructure becomes a priority, the InboxKit demo is here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim source:** [demo page](https://www.inboxkit.com/demo).

## Merge and stop checks

- Use email 1A for client-account operations or sending-setup evidence, and 1B for domain or campaign-infrastructure evidence. Hiring or client-case observations can support either variant when the source fits. Do not describe undated facts as recent or an old vacancy as still open.
- Send email only to a future human-approved `send-ready.csv` contact. A normalized `verification_status=catch_all` row is ambiguous and parked. A provider-positive `valid` row may separately have `verification_accept_all=true`; that risk remains visible and is not a delivery guarantee. LinkedIn steps require no opt-out and the connection acceptance condition shown above.
- Stop both channels immediately on any reply, booked meeting, or opt-out. A connection request not accepted gets no LinkedIn follow-ups.
- Before any real send, configure a monitored reply-to, confirm that STOP replies are processed into suppression, and replace `{{sender_name}}`. The copy by itself does not establish a working live opt-out.
