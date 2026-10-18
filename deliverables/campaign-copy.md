# Draft email and LinkedIn sequence

Draft sequence reviewed 18 October 2026. The sequence develops four angles: client-account administration, DNS setup at client launch, sequencer compatibility, and a final fit check. Step 1 has two evidence-informed variants. Every product statement has a source; every email has the same demo CTA and reply-based opt-out. No contact has been imported, enrolled, or sent.

[Personalized examples](merged-email-previews.md) show the recipient fields merged from six selected contact/step combinations. The current 97 ready contacts were checked across all four email steps: 388 merges, 68 to 90 words each, one demo URL and a STOP opt-out per email. Sender identity remains an operator setting.

`{{first_name}}` maps directly to the explicit `first_name` field in [send-ready.csv](send-ready.csv), while `{{first_line}}` maps to `first_line`; check `first_line_source` before merge. The agency rows contain an `email_variant` decision: A emphasizes client-account management, B domain organization. These are source-informed copy choices, not measured performance winners. See the [full mapping](../docs/data-dictionary.md#merge-fields). The only sales CTA is a [30-minute InboxKit demo](https://www.inboxkit.com/demo) of client mailbox administration. Use either email 1A or 1B on day 3, never both. The [sequence schedule](sequence.csv) gives all day and stop conditions. The STOP instruction is an opt-out, not another sales CTA. A real send would first require a monitored reply-to and the [suppression procedure](../docs/opt-out-and-suppression.md).

## LinkedIn connection note, day 1

Hi {{first_name}}, I work with outbound agencies on email infrastructure. Would be glad to connect.

**Product claims:** none. Connection is the native LinkedIn action; there is no demo ask in this note. Do not send to an opted-out contact.

## Email 1A, day 3: client account management

**Subject:** client mailbox administration

Hi {{first_name}},

{{first_line}}

I work with InboxKit. If you manage several client campaigns, keeping their mailbox accounts organized can become a separate operations task. InboxKit brings client accounts into one dashboard. The demo shows that view so you can compare it with how your team manages clients today.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [agency dashboard](https://www.inboxkit.com/agency-email-solution), [30-minute demo](https://www.inboxkit.com/demo). The prospect observation in `{{first_line}}` needs that row's `first_line_source`. The operational concern is conditional, not a claim that this prospect has reported that pain.

## Email 1B, day 3: domain organization

**Subject:** organizing client domains

Hi {{first_name}},

{{first_line}}

When you add sending domains for a client, keeping those setups organized is part of the launch. InboxKit gives each domain its own panel and brings client accounts into one dashboard. The demo shows that layout so you can assess it against your current process.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [per-domain panels](https://www.inboxkit.com/), [agency dashboard](https://www.inboxkit.com/agency-email-solution), [30-minute demo](https://www.inboxkit.com/demo). The prospect observation in `{{first_line}}` needs that row's `first_line_source`.

## LinkedIn follow-up 1, day 4 if connected and no reply

Thanks for connecting, {{first_name}}. I emailed about the client-account side of agency infrastructure. InboxKit brings those accounts into one dashboard. You can see that view in the demo: https://www.inboxkit.com/demo

**Product-claim sources:** [agency dashboard](https://www.inboxkit.com/agency-email-solution), [demo](https://www.inboxkit.com/demo). Send only if email 1 was actually sent and the connection was accepted; the sequence is currently staged only.

## Email 2, day 8 if no reply

**Subject:** your client launch checklist

Hi {{first_name}},

One practical part of a new client launch is getting DNS records in place. InboxKit configures SPF, DKIM, and DMARC automatically. If your team handles those records manually today, that is the setup workflow to evaluate in the demo. You can compare it with the steps your team currently owns.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [automatic DNS records](https://www.inboxkit.com/pricing), [30-minute demo](https://www.inboxkit.com/demo). The manual-work premise is conditional; no time saving or deliverability outcome is promised.

## LinkedIn follow-up 2, day 10 if connected and no reply

If your team uses Smartlead or Instantly, {{first_name}}, InboxKit integrates with both. That connection is another part of the infrastructure workflow to evaluate. The demo is here: https://www.inboxkit.com/demo

**Product-claim sources:** [Smartlead and Instantly integrations](https://www.inboxkit.com/pricing), [demo](https://www.inboxkit.com/demo). Existing sequencer use is conditional, not an invented prospect fact.

## Email 3, day 14 if no reply

**Subject:** keep your existing sequencer

Hi {{first_name}},

An infrastructure change also has to fit the campaign tools your team uses. If Smartlead or Instantly is part of your workflow, InboxKit integrates with both. The demo is a chance to evaluate that connection alongside the client-account view and decide whether the setup fits your agency's process.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [Smartlead and Instantly integrations](https://www.inboxkit.com/pricing), [agency dashboard](https://www.inboxkit.com/agency-email-solution), [30-minute demo](https://www.inboxkit.com/demo). The sequencers are integrations; no competitor comparison is made.

## Email 4, day 20 if no reply

**Subject:** closing the loop

Hi {{first_name}},

Final note from me on client infrastructure. If centralizing client accounts, organizing domains, or automating DNS setup would be useful to evaluate, the demo covers that workflow. You can use it to compare the process with your current setup. I will leave the decision with you.

Book a 30-minute demo here: https://www.inboxkit.com/demo

{{sender_name}}

To opt out, reply STOP and I will remove you from future emails.

**Product-claim sources:** [agency dashboard](https://www.inboxkit.com/agency-email-solution), [domain panels and automatic DNS](https://www.inboxkit.com/pricing), [demo page](https://www.inboxkit.com/demo).

## Merge and stop checks

- Use email 1A for client-account operations or sending-setup evidence, and 1B for domain or campaign-infrastructure evidence. Hiring or client-case observations can support either variant when the source fits. Do not describe undated facts as recent or an old vacancy as still open.
- Send email only to a future human-approved `send-ready.csv` contact. A normalized `verification_status=catch_all` row is ambiguous and parked. A provider-positive `valid` row may separately have `verification_accept_all=true`; that risk remains visible and is not a delivery guarantee. LinkedIn steps require no opt-out and the connection acceptance condition shown above.
- Stop both channels immediately on any reply, booked meeting, or opt-out. A connection request not accepted gets no LinkedIn follow-ups.
- Before any real send, configure a monitored reply-to, confirm that STOP replies are processed into suppression, and replace `{{sender_name}}`. The copy by itself does not establish a working live opt-out.
