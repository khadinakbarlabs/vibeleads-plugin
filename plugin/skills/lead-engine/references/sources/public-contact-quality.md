# Public contact quality source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

## contact-details-scraper

Exact owner: `khadinakbar`. Identity: `xUTDfDQougiuhikSc`. State: `public_schema_verified`.

Build `1.2.9` / `LWg9hKt5BPz5GkFKN`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/contact-details-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Use this field when the user provides specific website URLs or domain URLs to extract contacts from. Each URL is crawled independently and returns one consolidated contact record per domain. Do NOT use this when the user |
| `searchQueries` | array | Use this field when the user provides a business type, niche, or location query instead of specific URLs. Examples: 'dentists in Miami Florida', 'web design agencies London', 'plumbers Chicago'. The actor searches DuckDu |
| `maxPagesPerDomain` | integer; minimum=1; maximum=50 | Maximum number of pages to crawl per domain. Higher values find more contacts but cost more. Contact/About/Team pages are crawled first. Recommended: 5–15. |
| `maxDepth` | integer; minimum=0; maximum=5 | How many links deep to follow from the start URL. Depth 1 = only the homepage + directly linked pages. Depth 2 = one more level. Increase for large sites. |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of domains to extract contacts from and save to the dataset. Each domain = one output record. When using searchQueries, this caps how many websites from search results are processed. |
| `proxyConfig` | object | Proxy settings. Datacenter proxy is recommended for most websites. Use residential proxy only for sites that actively block scrapers. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## bulk-website-contact-extractor

Exact owner: `khadinakbar`. Identity: `TwNeQtj5TfaKDkcCK`. State: `public_schema_verified`.

Build `1.2.3` / `JI1UtSy1u7IYiaN58`; tag `latest`. Required keys: `startUrls`. [Full dated input schema](../schemas/bulk-website-contact-extractor.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Use this field when the user provides a list of website URLs to extract emails, phone numbers, or contact information from. Each URL is crawled independently and returns one result record. Accepts both plain strings ('ht |
| `maxPagesPerDomain` | integer; minimum=1; maximum=20 | How many pages to visit per input URL when hunting for contact info. The crawler always prioritises /contact, /about, /team, and /imprint pages before general pages. Higher values = more thorough extraction but more cred |
| `maxResults` | integer; minimum=0 | Maximum number of input URLs to process. Use when the user says 'process only the first 100', 'limit to 50 websites', or 'stop after 200 results'. Set to 0 to process all input URLs. Default: 1000. |
| `followContactPages` | boolean | When enabled, the crawler automatically discovers and follows links to /contact, /about, /team, /imprint, /support, and equivalent multilingual pages before extracting. Recommended: keep enabled for best email and phone  |
| `proxyConfiguration` | object | HTTP proxy settings. Leave as default (Apify datacenter proxies) for most websites. Switch to residential proxies only if target sites block datacenter IPs — residential proxies are slower and cost more. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-email-finder

Exact owner: `khadinakbar`. Identity: `QPGUyrwcV7CPITZdI`. State: `public_schema_verified`.

Build `0.1.12` / `tDP6W3W8zcXPLZb6f`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-email-finder.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `linkedinUrls` | array | Public LinkedIn profile URLs to find a work email for, e.g. 'https://www.linkedin.com/in/williamhgates'. Each profile is resolved to a name + current company via the primary managed public-data route (the managed fallbac |
| `directLeads` | array | Skip LinkedIn lookup and find an email directly from a known person + company. Each item is an object like {"fullName": "Jane Doe", "companyDomain": "acme.com", "companyName": "Acme"}. Use this when you already know the  |
| `includeUnverified` | boolean | When true (default), if the mail server cannot be SMTP-probed (port 25 blocked) or is catch-all, the highest-probability pattern email is still returned with a confidence score and an honest emailStatus. When false, only |
| `maxResults` | integer; minimum=1; maximum=10000 | Hard cap on how many leads are processed and billed this run (across linkedinUrls + directLeads). Protects your budget on large inputs. Defaults to 100. Minimum 1. |
| `maxCandidatesPerLead` | integer; minimum=1; maximum=15 | How many ranked email permutations to verify per person before stopping (verification stops early once a mailbox is SMTP-confirmed). Higher = more thorough, slower. Defaults to 15. Range 1-15. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## email-address-validator

Exact owner: `khadinakbar`. Identity: `Gvo4zJ8A4otiyCclv`. State: `public_schema_verified`.

Build `1.3.6` / `PwRc1YzjAkiG2PuYh`; tag `latest`. Required keys: `emails`. [Full dated input schema](../schemas/email-address-validator.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `emails` | array; minItems=1 | List of email addresses to validate. Pass a single address as a one-item array. Each entry is normalized to lowercase before validation. Example: ["jane@example.com", "info@acme.io"]. NOT a CSV file path or a domain — su |
| `checkSmtp` | boolean | When true, attempts a live SMTP RCPT TO probe to confirm the mailbox accepts mail. NOTE: most cloud platforms (Apify included, since it runs on AWS) block outbound port 25, so SMTP probes from Apify usually return 'unkno |
| `checkCatchAll` | boolean | When true and checkSmtp=true, probes a random non-existent address on the same domain to detect catch-all servers. Same cloud-port-25 caveat applies as checkSmtp. Default: false. |
| `concurrency` | integer; minimum=1; maximum=50 | How many emails to validate in parallel. Higher = faster but may hit per-host rate limits and cause 'unknown' SMTP results. Recommended 5–15 for most lists. Maximum 50. Default: 10. |
| `timeoutMs` | integer; minimum=1000; maximum=30000 | Per-connection timeout for the SMTP probe. Strict mailservers can take 5–10s. Lower values increase 'unknown' verdicts; higher values increase run time. Default: 8000 (8 seconds). Range: 1000–30000. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## neverbounce-alternative

Exact owner: `khadinakbar`. Identity: `rsNtTSJtoFuaUJF9M`. State: `public_schema_verified`.

Build `0.2.6` / `vfBUBZc3FjvUKXZYG`; tag `latest`. Required keys: `emails`. [Full dated input schema](../schemas/neverbounce-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `emails` | array; minItems=1; maxItems=1000 | List of email addresses to validate. Pass a single address as a one-item array. Each entry is normalized to lowercase before validation. Example: ["jane@example.com", "info@acme.io"]. NOT a CSV file path or a domain — su |
| `maxEmails` | integer; minimum=1; maximum=1000 | Hard cap for unique emails processed and charged in this run. Use 1000 for the largest supported batch or a smaller number to control event cost. Defaults to 1000. NOT a pagination offset; duplicate addresses are removed |
| `verificationTier` | string; standard, premium | Choose standard for the built-in preflight signals or premium for a deeper, owner-managed verification result. Premium runs are capped at 100 unique emails to keep the maximum charge predictable. |
| `checkSmtp` | boolean | When true, attempts a live SMTP RCPT TO probe to confirm the mailbox accepts mail. NOTE: most cloud platforms (Apify included, since it runs on AWS) block outbound port 25, so SMTP probes from Apify usually return 'unkno |
| `checkCatchAll` | boolean | When true and checkSmtp=true, probes a random non-existent address on the same domain to detect catch-all servers. Same cloud-port-25 caveat applies as checkSmtp. Default: false. |
| `concurrency` | integer; minimum=1; maximum=50 | How many emails to validate in parallel. Higher = faster but may hit per-host rate limits and cause 'unknown' SMTP results. Recommended 5–15 for most lists. Maximum 50. Default: 10. |
| `timeoutMs` | integer; minimum=1000; maximum=30000 | Per-connection timeout for the SMTP probe. Strict mailservers can take 5–10s. Lower values increase 'unknown' verdicts; higher values increase run time. Default: 8000 (8 seconds). Range: 1000–30000. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## zerobounce-alternative

Exact owner: `khadinakbar`. Identity: `kyarba8cynnNfvtBc`. State: `public_schema_verified`.

Build `0.1.3` / `rogOukwLhUgJwAhw1`; tag `latest`. Required keys: `emails`. [Full dated input schema](../schemas/zerobounce-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `emails` | array; minItems=1; maxItems=1000 | List of 1–1,000 full email addresses to validate. Use a JSON array such as ["jane@example.com", "info@acme.io"] and pass a single address as a one-item array. Entries are normalized to lowercase and normalized duplicates |
| `checkSmtp` | boolean | When enabled, the Actor attempts an SMTP RCPT TO probe after syntax and MX checks. Set true only when you need the additional SMTP signal; the default is false. Cloud hosts commonly restrict port 25, so an attempted prob |
| `checkCatchAll` | boolean | When enabled with the SMTP probe, the Actor tests a random address at the same domain for catch-all behavior. Set true only with checkSmtp=true; the default is false. Inconclusive SMTP responses remain null rather than b |
| `verificationTier` | string; standard, premium | standard uses this Actor's native syntax, DNS, classification, typo, and optional SMTP signals. premium uses an owner-managed EmailListVerify credential and adds a provider verdict when the Actor's Premium email verified |
| `maxEmails` | integer; minimum=1; maximum=1000 | Optional per-run cap from 1 to 1,000. The Actor processes the first normalized unique addresses only; later addresses are skipped and not charged. |
| `concurrency` | integer; minimum=1; maximum=50 | Number of addresses validated concurrently, from 1 to 50. Use 5–15 for routine lists; the default is 10. Higher settings can produce more inconclusive SMTP responses when a mail host rate-limits probes. This value is not |
| `timeoutMs` | integer; minimum=1000; maximum=30000 | Maximum wait per SMTP connection, from 1,000 to 30,000 milliseconds. Use 8,000 milliseconds by default; strict mail servers can take 5–10 seconds. Lower values can produce more unknown SMTP outcomes, while higher values  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
