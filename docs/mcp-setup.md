# Tool connections and authentication

The workflow can use authenticated MCP/app tools or direct provider APIs. These are alternative access routes to research, lookup and verification capabilities; no custom MCP server or package installation is required by the local export scripts.

## Registered hosted endpoints

[.codex/config.toml](../.codex/config.toml) registers eight hosted endpoints without credentials: Exa, Firecrawl, Tavily, Apollo, Prospeo, Hunter, Findymail and ZeroBounce. Project-scoped configuration is used for a trusted project. In a Codex CLI installation, inspect registrations and start a supported OAuth flow with:

```powershell
codex mcp list
codex mcp login firecrawl
```

Replace `firecrawl` with the chosen registered server name. A login command applies only when that server supports OAuth. Listing a server establishes configuration, not a successful lookup or available credits. See the [official OpenAI MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) for project configuration, listing and OAuth commands. Reload the relevant client/connection if newly configured tools are absent.

Credentials and OAuth state belong to the operator and are not checked into this repository. `.env` is an ignored source for direct API requests; it does not log hosted servers in. Do not paste API keys into the tracked configuration or embed them in MCP URLs. Claude Code can read the same instructions and skill with its own tool configuration; this TOML file is specific to Codex.

## Route by capability

| Provider | Repository access route | Operational considerations |
| --- | --- | --- |
| Exa | Registered hosted MCP; optional direct key. | Search for relevant pages; inspect the evidence before accepting a company. Account allowance must be checked independently. |
| Firecrawl | Registered hosted OAuth MCP; optional direct key. | Search/extract relevant pages. Authenticate the intended account; extraction credits are separate from email-provider credits. |
| Tavily | Registered hosted MCP; optional direct key. | Search/extraction alternative; check allowance and action cost. |
| Apollo | Registered hosted MCP; optional direct key. | Tool/plan permissions are endpoint-specific. Company and people discovery were denied on the tested Free account; do not infer that all enrichment routes are denied. Saved-contact search covers an existing address book. |
| Prospeo | Registered hosted MCP; optional direct key. | Named contact enrichment. Observe rate limits and confirm the required endpoint entitlement. |
| Hunter | Registered hosted MCP; optional direct key. | Named work-email discovery/verification where funded. A configured endpoint does not restore exhausted allowance. |
| Findymail | Registered hosted MCP; tested direct API. | Finder and verifier capacity differ. The tested API host is `app.findymail.com`. |
| ZeroBounce | Registered hosted OAuth MCP; tested direct API. | A direct API key is a usable alternative if hosted-client authentication is unavailable. Preserve normalized verdict, raw result and separate accept-all flag. |
| Lusha | Operator-managed app/plugin connection; optional direct key. | Not registered in the project TOML. Account usage and a named-profile batch worked on 18 October; individual profiles can be restricted. An earlier `Unknown tool` response was not evidence of zero credits. Test the available route before relying on it. |
| Icypeas | Tested direct API; hosted integration may be configured separately. | The synchronous finder/verifier use the API key alone. The balance route also requires the matching account email. No project MCP registration is needed for these routes. |
| Datagma | Tested direct API. | Named-buyer work-email recovery. Keep discovery attribution distinct from verification. |
| BounceBan | Tested standard direct verification API. | Specialist assessment for ambiguous domains; poll unfinished requests by ID. The separate waterfall host failed in an earlier environment. |
| Reoon, MillionVerifier | Direct API fallbacks. | Use funded mailbox-verification routes. No official project MCP connection was established for these providers. |

## Check access without confusing the layers

1. Confirm a search/page-reading tool is callable in the current session.
2. Choose one or more suitable funded finder/verifier routes. Check account capacity and the permission for the specific action, not merely the presence of a tool name.
3. Use existing credits and a bounded first sample. Account endpoints can return identity data; redact it from public receipts and never save authorization headers or credential-bearing URLs.
4. Apply the [runbook's waterfall](../skills/lead-research/SKILL.md). Log a no-result, denied route or rate limit, then use an appropriate alternative. Stop when the applicable evidence rule is met.
5. Save results and credit use with the run. A historical balance is not a promise that another operator or later run has the same capacity.

Only search, page reading, lookup, enrichment, balance and verification operations are within this workflow. Provider tools that send, enroll, import a campaign or export to CRM are outside the draft assignment. Local list export does not require an MCP connection.

## Tested access evidence

- [Clean-checkout billing run](../runs/2026-10-16-clean-checkout-billing/run-notes.md): live Findymail API use with local credentials in a clone, within the same connected agent session.
- [Email evidence review](../runs/2026-10-16-email-evidence-review/run-notes.md): direct ZeroBounce checks and separate accept-all handling.
- [Fresh-context SaaS run](../runs/2026-10-18-b2b-saas-outbound-fresh/README.md): separate agent without original chat history, supervised and sharing the current account's authenticated tools.
- [Provider access reference](provider-access.md): dated tested endpoints, authentication formats and known failure modes.

These records demonstrate particular routes and conditions. They do not transfer authentication to a new computer or guarantee a provider can recover an address in every segment.

## Provider references

[Exa MCP](https://exa.ai/mcp), [Firecrawl in Codex](https://www.firecrawl.dev/integrations/codex), [Tavily MCP](https://docs.tavily.com/documentation/mcp), [Apollo MCP](https://docs.apollo.io/docs/apollo-mcp), [Prospeo MCP](https://prospeo.io/api-docs/mcp), [Hunter MCP](https://hunter.io/mcp/), [Findymail MCP](https://help.findymail.com/en/article/findymail-mcp-model-context-protocol-1i6ifri/), [ZeroBounce MCP](https://zerobounce.net/docs/api-integrations/zerobounce-mcp-server/setup).

Provider documentation is linked for setup changes; it does not establish permissions on a particular account. Check the applicable official reference before changing a request after an endpoint failure.
