# Lusha recovery, 16 October 2026

Lusha was used against the existing qualified agency domains with decision-maker title filters. The search returned 61 profiles. Two search calls consumed three free credits. Email reveal was attempted for 25 entitled profiles and returned 21 profiles, consuming 20 reveal credits. The provider returned 26 named work-email addresses in the saved inventory; three profiles were compliance-restricted and did not produce an address. Several profiles returned more than one address, so the inventory is intentionally an attempt log rather than 26 distinct people.

ZeroBounce verified the first 20 addresses in one batch window. The second batch was blocked by ZeroBounce's five-call daily rate limit. `contacts.csv` preserves the exact status and whether the address is an alternate domain or catch-all.

This inventory is not appended to the canonical list automatically. Most domains are already represented in the one-domain-per-row export, and the assignment workflow rejects duplicate domains. Four addresses represent previously unseen domains or domain variants, while the rest are enrichment candidates for existing accounts. A follow-up run must select one buyer per domain, confirm fit and signal sources, resolve alternate-domain ownership, and use another verifier for rows marked `unknown`.
