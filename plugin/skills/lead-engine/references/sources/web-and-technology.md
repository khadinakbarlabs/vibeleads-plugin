# Web and technology source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## scrape-google-serp

Exact owner: `khadinakbar`. Identity: `z0r97dqhtUQk2AXd8`. State: `public_schema_verified`.

Build `1.0.21` / `ZnPFdByDFDsblxVt8`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/scrape-google-serp.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | Use this field when the user provides keywords or search terms. Enter one or more queries — each is scraped separately, one result record per page. Do NOT use this when the user provides a direct Google search URL — use startUrls for that. |
| `startUrls` | array | Use this field when the user provides a specific Google search URL (e.g. https://www.google.com/search?q=...). Country/language settings are embedded in the URL itself. Do NOT use this for plain keyword queries — use queries instead. |
| `maxResultsPages` | integer; minimum=1; maximum=50 | How many pages of Google results to scrape per query. Each page = 10 organic results (default). 1 = positions 1–10, 3 = positions 1–30, 10 = positions 1–100. Each page = 1 billing event. |
| `resultsPerPage` | integer; minimum=10; maximum=100 | Number of organic results per page. Google default is 10. Increase for more results per billing event (up to 100). Recommended values: 10, 20, 30, 50, 100. |
| `countryCode` | string | Google country targeting. Controls which regional Google index is queried. Examples: US, GB, DE, FR, AU, CA, IN, BR, JP, MX. Leave empty for global results. |
| `languageCode` | string | Google interface and results language. Examples: en, es, de, fr, pt, ja, zh-CN, ar, ru. Controls Google UI language and biases results toward that language. |
| `includeAds` | boolean | Extract paid Google Ads appearing at the top and bottom of results pages. Results stored in the ad_results array field. |
| `includeFeaturedSnippet` | boolean | Extract the featured snippet (answer box / Position 0) when present on the SERP. Stored in the featured_snippet field. |
| `includePeopleAlsoAsk` | boolean | Extract the 'People Also Ask' questions section. Useful for content research, FAQ generation, and topic clustering. Stored in the people_also_ask array. |
| `includeRelatedSearches` | boolean | Extract related search suggestions from the bottom of the SERP. Excellent for keyword research and topic mapping. Stored in the related_searches array. |
| `includeKnowledgeGraph` | boolean | Extract the Knowledge Graph panel (entity info box) when present. Contains entity title, type, description, and official website. Stored in the knowledge_graph field. |
| `maxConcurrency` | integer; minimum=1; maximum=20 | Number of parallel requests sent to Google. Recommended: 5 for standard use, 2–3 if experiencing blocks. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## bing-search-scraper

Exact owner: `khadinakbar`. Identity: `Vwq0iHM2LAMo5Vvq6`. State: `public_schema_verified`.

Build `0.3.3` / `J4auTGWjcgkncXwEE`; tag `latest`. Required keys: `queries`. [Full dated input schema](../schemas/bing-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | List of free-text search queries (e.g., 'best crm software 2026') or full Bing search URLs (https://www.bing.com/search?q=...). Each query produces one or more result records. Defaults to a sample marketing query. NOT for Bing Maps URLs — use the bing-maps-scraper actor instead. |
| `country` | string; US, GB, CA, AU, DE, FR, ES, IT, NL, BR, MX, IN, JP, CN, KR, RU, TR, AE, SG, ZA, SE, NO, DK, FI, PL, PT, ID, TH, VN, PH, MY, AR, CL | Defaults to 'US'. NOT a city name or 3-letter code. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `language` | string; en, es, de, fr, it, pt, nl, ru, ja, ko, zh, ar, tr, pl, sv, no, da, fi, id, th, vi, hi | Two-letter ISO language code for Bing UI/results filter (e.g., 'en', 'es', 'de'). Combines with country to form the Bing market parameter (e.g., en + US = en-US). Defaults to 'en'. NOT a locale string like 'en-US'. |
| `safeSearch` | string; off, moderate, strict | Bing SafeSearch level: 'off' = no filter, 'moderate' = blur explicit images only, 'strict' = filter all adult content. Defaults to 'moderate'. NOT a content quality filter. |
| `maxResultsPerQuery` | integer; minimum=1; maximum=200 | Hard cap on result records emitted per query, including organic, ads, Copilot answer, PAA, and related searches. Defaults to 50. Range 1-200. NOT the number of Bing result pages — pagination is automatic until this cap is reached. |
| `includeAds` | boolean | When true, paid ads at top/bottom of SERP are extracted as records with type='ad'. Defaults to true. NOT a setting for Microsoft Advertising API. |
| `includeCopilotAnswer` | boolean | When true, the Copilot/AI Overview answer block above results is extracted as one record with type='copilot_answer'. Defaults to true. NOT a separate Copilot Chat API call. |
| `includeRelatedSearches` | boolean | When true, 'People also ask' (PAA) questions and 'Related searches' suggestions are emitted as records with type='paa' or 'related'. Defaults to true. NOT scraping of PAA expanded answers — only the questions and related queries are returned. |
| `fallbackMode` | string; auto, always, never | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## website-tech-stack-detector

Exact owner: `khadinakbar`. Identity: `CSan7jscwV91lGDM9`. State: `public_schema_verified`.

Build `0.1.5` / `Vdq2LM5o2PnTAWSfV`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/website-tech-stack-detector.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `websiteUrls` | array; maxItems=50 | Example: https://www.shopify.com or shopify.com. Only http(s) public hosts are accepted — no localhost, private IPs, or credentialed URLs. Prefer full https URLs. Duplicate URLs are deduped. Each successful detection costs $0.01. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `startUrls` | array | Optional alias for websiteUrls using Apify request-list objects. Prefer websiteUrls for agents. Each entry needs a public http(s) url field. Merged and deduped with websiteUrls. |
| `maxUrls` | integer; minimum=1; maximum=50 | Hard cap on unique URLs processed after dedupe. Defaults to 25. Maximum 50. Lower this to bound spend. Each successful detection costs $0.01 plus platform usage. |
| `includeEvidence` | boolean | When true, each technology includes a short public-signal evidence excerpt (HTML/header snippet). Defaults to true. Set false for smaller rows when only names and categories are needed. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=60 | HTTP timeout per URL attempt. Defaults to 25. Range 5–60. Does not change pricing. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## website-stack-evidence-audit

Exact owner: `khadinakbar`. Identity: `XFAdEZmNTVz0ZnZ9M`. State: `public_schema_verified`.

Build `0.1.15` / `tdtZmgG9wavfBtxhH`; tag `latest`. Required keys: `startUrls`. [Full dated input schema](../schemas/website-stack-evidence-audit.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array; maxItems=50 | Public website URLs to audit, for example `https://example.com`. The Actor normalizes each URL to its domain and checks the selected same-site paths. Submit up to 50 entries; Maximum domains controls how many are processed. Use public HTTP(S) websites rather than technology names or reverse-search queries. |
| `dataMode` | string; live_only, hybrid_premium | Choose `live_only` for the $0.005 current public-page audit, or `hybrid_premium` for a $0.06 result that combines live evidence with the owner-managed the keyword-data API Domain Technologies catalog. Premium catalog results include provider freshness provenance and can rescue a domain when its live pages are unavailable. If the provider fails but live evidence succeeds, the Actor automatically persists and bills only the base audit. |
| `pathsToInspect` | array; minItems=1; maxItems=4 | Relative public paths inspected for every supplied domain, for example `/`, `/pricing`, and `/contact`. The default samples several common pages because a homepage alone can miss payment or support integrations. This is not a list of external URLs and cross-site paths are rejected. |
| `maxPagesPerDomain` | integer; minimum=1; maximum=4 | Hard cap for same-site public pages inspected per domain, from 1 to 4. Defaults to 3 and uses the earliest valid entries from Same-site paths to inspect. This is not a website-depth crawl or a limit on technology detections. |
| `maxDomains` | integer; minimum=1; maximum=50 | Hard cap for distinct domain audits from Start URLs, from 1 to 50. Defaults to 10 so a run remains predictable even when a larger URL list is supplied. This is not a pagination setting or a reverse technology search limit. |
| `useApifyProxy` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `responseFormat` | string; detailed, concise | Choose `detailed` to return technology evidence with the public signal that matched, or `concise` for only name, categories, and confidence. Defaults to detailed for auditability and is best for reviews or migration research. This setting does not change which pages are requested or which signatures are available. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## wappalyzer-alternative

Exact owner: `khadinakbar`. Identity: `d2R7wTDKZYk1ekBfh`. State: `public_schema_verified`.

Build `1.0.13` / `FXjYJy1wq4IG9Ynj6`; tag `latest`. Required keys: `startUrls`. [Full dated input schema](../schemas/wappalyzer-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array; minItems=1; maxItems=25 | Public website URLs or domains to profile. Enter a hostname such as apify.com or a complete http(s) URL. The Actor follows normal redirects and records the final URL. Use only URLs you are authorized to analyze. |
| `maxUrls` | integer; minimum=1; maximum=25 | Hard cap for this run after invalid URLs and duplicates are removed. Defaults to 10 and can never exceed 25. Lower this value to keep a pilot run tightly bounded. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=60 | Maximum wait for each current public website response. Defaults to 25 seconds and can never exceed 60 seconds. A timed-out live page becomes a source warning while provider catalog evidence can still return a report. |
| `useProviderCatalog` | boolean | Combine the keyword-data API's domain technology catalog with current public-page evidence. Defaults to true for broader coverage and keeps provider credentials owner-managed. Turn it off for a live-page-only observation that makes no provider request; the report event price is unchanged. |
| `useApifyProxyFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## website-seo-spider

Exact owner: `khadinakbar`. Identity: `f0PPU2rWRKUBwAfeZ`. State: `public_schema_verified`.

Build `0.2.5` / `VgcoYYZsbn0qxADMx`; tag `latest`. Required keys: `startUrls`. [Full dated input schema](../schemas/website-seo-spider.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | One or more public website URLs where the crawl begins. Example: https://example.com. Each seed keeps its own startUrl provenance. Same-hostname or same-domain links are followed up to maxPages. |
| `crawlScope` | string; same-hostname, same-domain, page-only | Which internal links to follow from each HTML page. same-hostname stays on the exact host; same-domain also follows subdomains; page-only fetches the start URLs and stops. Defaults to same-hostname. |
| `maxPages` | integer; minimum=1; maximum=2000 | Hard cap on public pages fetched in this run. Example: 10. Default 100, maximum 2000. Prefill 10 keeps the first sample bounded. When useful in-scope URLs remain at this cap, the run finishes PARTIAL. |
| `maxDepth` | integer; minimum=0; maximum=20 | How many link hops from a start URL the crawler may follow. 0 means unlimited within maxPages. Default 10, prefill 3. Depth 0 is the start URL itself. Enable seedFromSitemap to add sitemap URLs as extra starts. |
| `seedFromSitemap` | boolean | When true, read robots.txt Sitemap entries and /sitemap.xml, then add in-scope URLs to the crawl queue up to maxPages. Defaults to false. Useful for coverage beyond the homepage link graph. |
| `respectRobotsTxt` | boolean | When true, skip paths disallowed for the crawler user-agent in robots.txt. Defaults to true. Turn off only for sites you are authorized to audit beyond the public robots policy. |
| `ignoreUrlParameters` | boolean | When true, strip query strings before uniqueness so /page and /page?ref=nav count as one URL. Defaults to false. Enable for tracking-parameter cleanup; it does not rewrite canonical tags on the page. |
| `maxConcurrency` | integer; minimum=1; maximum=20 | Parallel HTTP requests. Default and prefill are 5; maximum 20. The crawler also applies a small same-domain delay for stable collection. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `fetchMode` | string; direct, residential | Direct HTTP is the lower-cost default. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## website-backlink-checker

Exact owner: `khadinakbar`. Identity: `rCohK9eJbjiovPN6s`. State: `public_schema_verified`.

Build `0.1.2` / `wnDuwfaprrBJR108n`; tag `latest`. Required keys: `targets`. [Full dated input schema](../schemas/website-backlink-checker.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `targets` | array; minItems=1; maxItems=10 | Domains or page URLs to check for inbound links. Example: ["moz.com"] or ["https://moz.com/learn"]. Protocol and www are stripped for domains; a path keeps page-level lookup. Duplicates collapse. Capped at 10 targets. This is NOT an API-key field. |
| `mode` | string; backlinks, referring_domains, anchors, summary | Which inbound-link report to run. backlinks returns referring page URLs with anchor, dofollow, and first seen. referring_domains lists linking root hosts. anchors groups by anchor text. summary returns one overview row with backlink and referring-domain counts. Default backlinks. This is NOT a login or API key field. |
| `maxResults` | integer; minimum=1; maximum=100 | Maximum dataset rows to write per target (1-100). Defaults to 5 so quality tests and agent calls stay cheap. summary still writes at most one row per target. Raise this after you confirm the output shape. |
| `dofollowOnly` | boolean | When true, keep only dofollow inbound links in backlink, referring-domain, and anchor reports. Defaults to false so mixed follow types are returned. Ignored by summary mode. |
| `excludeLost` | boolean | When true, drop inbound links that the index marks as lost. Defaults to true. summary mode still reports live counts for the target. |
| `includeSubdomains` | boolean | When true, inbound-link reports include subdomain data for the target. Defaults to true. Does not crawl the live website. |
| `excludeInternalBacklinks` | boolean | When true, summary and referring-domain reports drop internal subdomain links. Defaults to true. Helps keep the export focused on external referring hosts. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## backlink-opportunity-finder

Exact owner: `khadinakbar`. Identity: `n1uR8aWhzOBYhxLJl`. State: `public_schema_verified`.

Build `1.0.14` / `vNnmZncbiNljp3kNk`; tag `latest`. Required keys: `keywords`. [Full dated input schema](../schemas/backlink-opportunity-finder.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `keywords` | array; minItems=1; maxItems=10 | Use this when you need relevant link prospects for one or more topics. Add up to 10 phrases, for example "project management software" or "remote team collaboration". The actor combines each phrase with the selected prospect footprints. |
| `targetDomain` | string | Use this when you want to avoid returning pages from your own website. Enter a hostname or URL such as example.com. Leave blank if you do not have a domain to exclude. |
| `opportunityTypes` | array | Use this when you want specific public-page footprints. Choose resource pages, guest-post guidelines, listicles, directories, podcasts, or expert roundups. If empty, the actor searches resource pages, guest posts, and listicles. |
| `excludeDomains` | array | Use this when known competitors, marketplaces, or irrelevant publishers should be excluded. Enter hostnames such as competitor.com; subdomains are also excluded. Filtering happens before dataset events are charged. |
| `countryCode` | string | Use this when you need Google results localized to a two-letter country code. Enter values such as US, GB, or AU. The default is US; it affects result localization, not a publisher's verified location. |
| `languageCode` | string | Use this when you need results in a specific language. Enter a language code such as en, de, or es. The default is en; it does not translate page text. |
| `maxResultsPerKeyword` | integer; minimum=1; maximum=100 | Use this when you need a strict per-keyword cap on saved, billable prospects. Enter 1 to 100; the default is 25. Duplicate, excluded, and low-relevance results do not count toward this cap. |
| `maxPagesPerQuery` | integer; minimum=1; maximum=5 | Use this advanced limit to control SERP coverage and provider requests. Enter 1 to 5; the default is 1. This is a query-page cap, not a guaranteed number of returned prospects. |
| `minimumRelevanceScore` | integer; minimum=0; maximum=100 | Use this when you want to discard weaker text matches before they are saved or charged. Enter 0 to 100; the default is 35. The score is a transparent heuristic based on keyword overlap, footprint cues, and result position, not a domain-authority metric. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
