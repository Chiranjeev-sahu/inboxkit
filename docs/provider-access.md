# Direct provider access

These are working routes from dated project tests, provided to reduce setup mistakes in a fresh agent context. Use whichever authenticated MCP or direct API is available. No new server, package or automation is required. Check current official documentation if a route fails; log the failure and fall back rather than retrying an unverified hostname.

Read credentials from the local ignored `.env` without printing them. Never log a request URL containing a credential, authorization headers, or account identity. Save the provider verdict, named-buyer query, credit delta and relevant status fields. Saved credit counts are observations, not quotas guaranteed for another session. Account capacity is operator-specific; check it before credit-consuming calls rather than copying another account's balances.

## Free balance checks

| Provider | Method and URL | Authentication | Interpretation |
| --- | --- | --- | --- |
| Findymail | `GET https://app.findymail.com/api/credits` | `Authorization: Bearer <FINDYMAIL_API_KEY>` | Finder and verifier credits are separate. The working host is **app.findymail.com**; `api.findymail.com` failed DNS in the fresh-agent rehearsal. |
| Prospeo | `GET https://api.prospeo.io/account-information` | `X-KEY: <PROSPEO_API_KEY>` | Remaining credits do not guarantee bulk endpoint access. Pace requests after a 429. |
| Datagma | `GET https://gateway.datagma.net/api/ingress/v1/mine` | Query `apiId=<DATAGMA_API_KEY>` | Read `currentCredit`; redact credential-bearing URLs. |
| BounceBan | `GET https://api.bounceban.com/v1/account` | `Authorization: <BOUNCEBAN_API_KEY>` without Bearer | Returns credits and per-route limits. Strip `owner_email` from saved receipts. |
| ZeroBounce | `POST https://api.zerobounce.net/v2/getcredits` | Form field `api_key=<ZEROBOUNCE_API_KEY>` | Read `Credits`. |
| Reoon | `GET https://emailverifier.reoon.com/api/v1/check-account-balance/` | Query `key=<REOON_API_KEY>` | Instant credits and daily credits are distinct. |
| MillionVerifier | `GET https://api.millionverifier.com/api/v3/credits` | Query `api=<MILLIONVERIFIER_API_KEY>` | Bulk and renewing figures are components, not additive extra balances. |
| Hunter | `GET https://api.hunter.io/v2/account` | Query `api_key=<HUNTER_API_KEY>` | Inspect remaining searches/verifications and reset date; omit account identity. |
| Tavily | `GET https://api.tavily.com/usage` | `Authorization: Bearer <TAVILY_API_KEY>` | Separate key usage from account plan usage and pay-as-you-go. Stay within the existing allowance. |
| Icypeas | `POST https://app.icypeas.com/api/a/actions/subscription-information` | `Authorization: <ICYPEAS_API_KEY>` without Bearer; JSON `email` uses local `ICYPEAS_ACCOUNT_EMAIL` | Match the account email to the API key. Balance, synchronous finder and verifier routes were tested on 18 October. Keep account identity local. |

Apollo, Firecrawl and Lusha expose account-usage tools through their connected MCP/app routes. An account balance does not establish enrichment endpoint permissions. Exa's remaining account allowance was not established by the available search tool; check the dashboard if that balance is needed. MCP authentication is separate from `.env`; see [MCP setup](mcp-setup.md).

## Lookup and verification pitfalls

- Icypeas `POST https://app.icypeas.com/api/sync/email-search` takes `firstname`, `lastname`, `domainOrCompany`; its synchronous verifier at `/api/sync/email-verification` takes `email`. Both use bare API-key Authorization and JSON. The updated account passed both on 18 October. No accept-all boolean was returned; preserve existing flags or leave unreported values blank.
- Lusha account usage currently returns `Unknown tool` after the reported account switch. This is a tool-registration problem, not proof of zero credits or a plan denial. Recheck after refreshing the project connection; use funded alternatives in the meantime.

- Apollo's connected Free account returned `API_INACCESSIBLE` / `AUTH.AUTHORIZATION.ENDPOINT_ACCESS_DENIED` for both people search and company search on 18 October. Skip those two discovery routes unless plan/access changes; do not repeatedly probe them because credits are visible. Named-person enrichment and company enrichment were not established as blocked or usable by that test. A saved-contact search accesses an existing address book; an empty result is not a market-wide discovery result.
- Datagma's named-buyer finder worked at `https://gateway.datagma.net/api/ingress/v8/findEmail`. Its finder status does not replace the separately recorded verification assessment.
- BounceBan's standard single verification API worked. If a request is unfinished, poll its status using the returned ID rather than paying for repeated submissions. Its waterfall hostname was blocked in an earlier run.
- Use Reoon's mailbox-capable verification mode when checking delivery; a syntax/domain-only quick check is not mailbox verification.
- A positive provider verdict is probabilistic. Preserve accept-all separately, domain ownership proof where needed, and conflicting clear verdicts per the [runbook](../skills/lead-research/SKILL.md).
- Stop after a clear result. An extra verifier needs a specific unresolved question recorded in the run notes, not a desire to exercise all providers.

## Official references

[Findymail](https://app.findymail.com/docs/), [Prospeo](https://prospeo.io/api-docs/account-information), [Datagma](https://datagmaapi.readme.io/reference/ingressservice_getcredit), [BounceBan](https://github.com/bounceban-com/skill-email-verification/blob/main/introduction.md), [ZeroBounce](https://www.zerobounce.net/docs/email-validation-api-quickstart/v2-credit-balance), [Reoon](https://www.reoon.com/articles/api-documentation-of-reoon-email-verifier/), [MillionVerifier](https://developer.millionverifier.com/), [Hunter](https://hunter.io/api-documentation/v2), [Tavily](https://docs.tavily.com/documentation/api-reference/endpoint/usage), [Icypeas](https://api-doc.icypeas.com/subscriptions/subscription-information/).
