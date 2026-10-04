# Startups and software source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## producthunt-scraper-pro

Exact owner: `khadinakbar`. Identity: `DTljt4BJQ9K6xJp14`. State: `public_schema_verified`.

Build `1.4.18` / `whXk8LCCY8pQrxg03`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/producthunt-scraper-pro.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `mode` | string; leaderboard, search, topic, urls | How to find products. Use 'leaderboard' for top-ranked products by time period. Use 'search' when the user provides a keyword. Use 'topic' for a ProductHunt topic slug. Use 'urls' for specific ProductHunt URLs. |
| `leaderboardPeriod` | string; daily, weekly, monthly, yearly | Only used when mode='leaderboard'. Choose 'daily', 'weekly', 'monthly', or 'yearly'. |
| `searchQuery` | string | Used when mode='search'. Filters products returned by Product Hunt's current official API window against name, tagline, description, and topics (for example 'AI writing tools'). |
| `topic` | string | Used when mode='topic'. The ProductHunt topic URL slug (e.g. 'artificial-intelligence', 'developer-tools', 'productivity'). |
| `startUrls` | array | Used when mode='urls'. Accepts specific Product Hunt post/product-launch URLs and dated leaderboard URLs (for example /leaderboard/monthly/2026/7). Each URL is resolved through the official Product Hunt API, not by scraping Product Hunt pages. |
| `maxResults` | integer; minimum=1; maximum=20000 | Maximum number of products to return. Default is 100. |
| `excludeProductHuntUrls` | array | Optional resumable-run list. Products whose Product Hunt post or product-launch URL appears here are skipped before website or email enrichment and do not consume maxResults. Use URLs from an earlier dataset when a large week, month, or year reaches its result limit. |
| `productHuntResumeCursor` | string | Optional opaque cursor from RUN_SUMMARY.nextProductHuntCursor. Use it with the same mode, filters, date range, and exclusions to continue directly after a capped page without re-indexing all prior Product Hunt pages. |
| `includeAllProducts` | boolean | Enabled by default so date ranges and leaderboard URLs include featured and non-featured Product Hunt posts up to maxResults. Disable to request featured posts only. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | Maximum concurrent product-enrichment jobs. Default is 3 to keep browser and website traffic bounded. |
| `enrichEmails` | boolean | When enabled (the default), enriches each verified product website. It visits the homepage and up to four same-site contact, about, team, privacy, or terms pages linked from that homepage, then checks up to two public maker homepages and can use the managed contact finder if deliverable-email slots remain. |
| `resolveWebsites` | boolean | Recommended and enabled by default. Resolves Product Hunt redirect-only links through redirect metadata, official maker sites and their product links, bounded domain hypotheses, then owner-managed search providers. Every candidate must pass product-identity and ownership checks before it is accepted. |
| `maxWebsitePages` | integer; minimum=1; maximum=5 | Bounded public-site crawl limit. Default and maximum are 5 total pages: homepage plus up to four directly linked allowed pages. |
| `maxEmailsPerProduct` | integer; minimum=1; maximum=3 | Returns and bills for up to this many ranked public email addresses associated with the product or its listed makers. Default and maximum are 3. |
| `verifyEmails` | boolean | Enabled by default. Verifies every selected public email with the Actor's managed EmailListVerify integration. Each result includes the exact provider status; invalid, disposable, and spam-trap results are never presented as verified emails. |
| `findContacts` | boolean | Enabled by default. After product-site and maker-homepage public discovery, use the managed EmailListVerify Contact Finder with a Product Hunt maker name first, then a domain-only fallback only if deliverable-email slots remain. Provider calls and credit ceilings remain bounded per product. |
| `websiteUrlOverrides` | array | Optional approved mapping for a Product Hunt product. Each item accepts productHuntUrl, productSlug, productName, or productId plus websiteUrl. A valid override takes priority over managed automatic website resolution. |
| `startDate` | string | For leaderboard daily mode: query a specific date. Leave blank for today. Use with endDate to scrape a date range in one run (e.g. startDate=2026-03-01, endDate=2026-03-07 → full week). |
| `endDate` | string | Optional end date for multi-day scraping in one run. Only used in daily leaderboard mode. Example: startDate=2026-03-01, endDate=2026-03-07 returns all products launched across that 7-day window. |
| `lookbackDays` | integer; minimum=1; maximum=365 | Alternative to startDate: scrape the last N days from today. E.g. lookbackDays=7 pulls the last week. Ignored when startDate is provided. |
| `outputMode` | string; full, lean, leads | Controls what gets returned. 'full' = all fields (default). 'lean' = minimal fields optimized for LLM/AI agent context windows (name, tagline, website, upvotes, rank, emails, topics). 'leads' = full fields but only products where at least 1 email was found — perfect for outreach lists. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## ycombinator-scraper

Exact owner: `khadinakbar`. Identity: `it8FpWzwrVxQlmofi`. State: `public_schema_verified`.

Build `0.3.2` / `j1pHOt66gxJfNGihP`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/ycombinator-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Any Y Combinator URL. Mix and match company URLs, jobs URLs, filter URLs in the same run. The actor auto-detects which extractor to use per URL. Leave empty to use the Filter fields below. Example URLs: 'https://www.ycombinator.com/companies?batch=Spring%202026&industry=B2B', 'https://www.ycombinator.com/companies/airbnb', 'https://www.ycombinator.com/companies/stripe/jobs/jdBhPmD-frontend-engineer-identity', 'https://www.ycombinator.com/jobs?role=eng'. |
| `mode` | string; companies, jobs | Pick a target surface. Companies runs an Algolia search with the filter fields below. Jobs paginates the `/jobs` board with role/location filters. Ignored when Start URLs is non-empty. |
| `query` | string | Keyword search across company names, one-liners, descriptions (Companies mode) or job titles + descriptions (Jobs mode). Leave empty to skip keyword filtering. Example: 'developer tools', 'AI agents', 'fintech'. NOT a regex — Algolia matches partial words. |
| `batches` | array | Companies mode only. Pick one or more batches (cohorts). Leave empty for no batch filter. Example: ['Spring 2026', 'Winter 2026']. Spring/Summer/Fall/Winter naming follows YC's own taxonomy. |
| `industries` | array | Companies mode only. Pick one or more industries. Empty = no industry filter. YC's top-level taxonomy: B2B, Consumer, Healthcare, Fintech, Engineering/Product/Design, Industrials, Education, Real Estate and Construction, Government. |
| `regions` | array | Companies mode only. Pick one or more HQ regions. Empty = no region filter. Use 'Remote' or 'Fully Remote' for distributed teams. |
| `topCompany` | boolean | Companies mode only. Limit results to companies flagged as 'Top' by Y Combinator (a curated subset, ~500 companies). Useful for VC sourcing and competitive landscape mapping. |
| `isHiring` | boolean | Companies mode only. Limit to companies currently marked as hiring on YC. Combine with `scrapeOpenJobs` to fetch the actual job postings. |
| `nonprofit` | boolean | Companies mode only. Limit to companies marked as nonprofits. Leave off to include both commercial and nonprofit YC orgs. |
| `minTeamSize` | integer; minimum=0; maximum=100000 | Companies mode only. Smallest team size to include. Leave 0 for no minimum. Example: 10 returns companies with team_size >= 10. |
| `maxTeamSize` | integer; minimum=0; maximum=100000 | Companies mode only. Largest team size to include. Leave 0 for no maximum. Example: 50 returns companies with team_size <= 50. |
| `jobRole` | string; , eng, design, product, ops, marketing, sales, support, recruiting-hr, science | Jobs mode only. Filter the YC jobs board by role category. Empty = all roles. Maps to YC's `/jobs?role=...` query string. |
| `jobLocation` | string | Jobs mode only. Filter by city slug or 'remote'. Empty = all locations. Common values: 'san-francisco', 'new-york', 'london', 'remote', 'india', 'seattle', 'los-angeles', 'austin'. |
| `scrapeFounders` | boolean | Companies mode only. Fetch `/companies/{slug}` for each company and add the `founders[]` array (name, title, bio, LinkedIn URL, Twitter URL, has_email flag, avatar). Adds one HTTP request per company. Each founder counts as one enrichment event ($0.001). |
| `scrapeOpenJobs` | boolean | Companies mode only. Adds the `openJobs[]` array to each company (title, salary, equity, visa, location, apply URL). If `scrapeFounders` is also true, both are populated from the same single HTTP fetch. Each job counts as one enrichment event ($0.001). |
| `scrapeJobDescriptions` | boolean | Jobs mode only. Fetch each job detail page (`/companies/{slug}/jobs/{slug}`) for the full long-form description, hiring manager, and related jobs. Slower (one HTTP per job) but produces the richest job records for downstream NLP. No enrichment event charged — already covered by the base $0.005/job. |
| `scrapeNewsAndLaunches` | boolean | Companies mode only. Adds `newsItems[]` (title, url, date) and `launches[]` (YC Launch posts) to each company. Same HTTP fetch as founders/jobs enrichment, so no extra requests if any company enrichment is already on. |
| `maxResults` | integer; minimum=0; maximum=100000 | Hard cap on number of records to return. The actor stops cleanly once this many records have been emitted. Set 0 for no cap (will scrape the full ecosystem — 5,700+ companies or all open jobs). Pagination honors `startPage` and `pageLimit` regardless of this cap. |
| `startPage` | integer; minimum=0; maximum=9999 | Companies-mode + Jobs-mode (company iteration) pagination start. 0 = first page. 5 = skip first 500 companies, start from company 501. Useful for resuming long crawls or splitting work across runs. Each Algolia page = 100 companies. Ignored when paste-URL mode is used (URL-only routing). |
| `pageLimit` | integer; minimum=0; maximum=1000 | Companies-mode + Jobs-mode (company iteration). Maximum number of 100-result Algolia pages to traverse. 0 = unlimited (will exhaust the result set up to Algolia's hard 1000-page server cap). Useful to scope a run: `pageLimit=10` = at most 1,000 companies enumerated. Ignored when paste-URL mode is used. |
| `monitoringMode` | boolean | When true, persists every emitted company id / job id to the STATE key-value collection. On subsequent runs, only IDs not yet seen are emitted — perfect for scheduled cron runs that should only output 'what's new'. State is per Apify user/actor. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## shopify-app-store-scraper

Exact owner: `khadinakbar`. Identity: `nvdkTgPT0l2uOTwgl`. State: `public_schema_verified`.

Build `0.1.6` / `PHleqO9nxZ3AlPKoa`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/shopify-app-store-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | Free-text keywords searched on the Shopify App Store, one app niche per line (e.g. 'email marketing', 'product reviews'). Each query returns a paginated list of matching app cards. Leave empty if you are passing app, category, or review URLs in 'Start URLs' instead. NOT an app URL — to scrape one specific app use 'Start URLs'. |
| `startUrls` | array | Direct apps.shopify.com URLs; the mode is auto-detected per URL. App page (apps.shopify.com/klaviyo-email-marketing) returns full app detail; a /reviews URL returns merchant reviews; a /categories/<slug> URL returns the category app list; a /search?q= URL runs a search. Use this for precise targets instead of free-text 'Search queries'. |
| `mode` | string; auto, search, category, app_detail, reviews | Forces a scraping mode instead of auto-detecting from the URL. 'auto' (default) detects search vs category vs app_detail vs reviews from each input. Set explicitly only to override detection (e.g. force 'reviews' on a bare app URL). Most users should leave this on 'auto'. |
| `scrapeReviews` | boolean | When scraping app detail pages (or apps found via search/category with 'Enrich details' on), also paginate that app's merchant reviews and emit one record per review. Adds review-scraped charges. Defaults to false. Ignored when the input is already a /reviews URL. |
| `enrichDetails` | boolean | For search and category modes, visit each app's detail page to add full metadata (description, pricing plans, developer, works-with, languages) instead of just the listing card. Slower and adds one app-scraped charge per app. Defaults to false (fast card-level listing only). |
| `maxApps` | integer; minimum=1; maximum=5000 | Hard cap on how many apps to return per search query or category, across pagination. Caps the app-scraped charge so cost stays predictable. Defaults to 50; set 0 or leave default for typical runs. Does not limit reviews — use 'Max reviews per app' for that. |
| `maxReviews` | integer; minimum=1; maximum=20000 | Hard cap on reviews scraped per app (10 reviews per page). Caps the review-scraped charge. Defaults to 100. Only applies when scraping reviews (a /reviews URL, or 'Also scrape reviews' enabled). |
| `reviewSort` | string; most_recent, highest_rating, lowest_rating, most_helpful | Order reviews are returned in when scraping reviews. 'most_recent' (default) is newest first; 'highest_rating' / 'lowest_rating' sort by stars; 'most_helpful' uses Shopify's helpfulness ranking. Ignored outside review scraping. |
| `reviewRating` | integer; minimum=0; maximum=5 | Only scrape reviews with this exact star rating (1-5). Leave at 0 (default) to scrape all ratings. Useful for pulling only 1-star complaints or 5-star praise. Ignored outside review scraping. |
| `country` | string | 'US', 'GB'). Affects geo-targeted pricing/currency shown on listings. Defaults to 'US'. Uppercase ISO-3166 alpha-2. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `maxConcurrency` | integer; minimum=1; maximum=50 | Maximum parallel requests. Defaults to 10. Lower it (e.g. Raising it rarely helps and risks more blocks. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## salesforce-appexchange-scraper

Exact owner: `khadinakbar`. Identity: `wHmSH8gBGgMFVKYMU`. State: `public_schema_verified`.

Build `1.1.2` / `wtkmHaSwZ6LcAk1da`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/salesforce-appexchange-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `listingUrls` | array | Specific AppExchange listings to scrape. Paste full detail URLs (e.g. 'https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000FguFBUAZ') or just the raw listing id ('a0N4V00000FguFBUAZ'). When this list is non-empty the actor scrapes exactly these and ignores browse settings below. Leave empty to browse the catalog by type instead. |
| `listingType` | string; App, Consulting | Which AppExchange catalog to enumerate when no Listing URLs are given. 'App' = solutions/apps under appxListingDetail (the main catalog, ~4,200 listings, richest data). 'Consulting' = partner consultants. Defaults to 'App'. Ignored when Listing URLs are provided. |
| `keyword` | string | Optional case-insensitive substring filter applied to each browsed listing's name, tagline, description, publisher and categories. Example: 'marketing'. This is a literal substring match over scraped data, NOT Salesforce's relevance-ranked search. Leave empty to return listings in catalog order. |
| `maxResults` | integer; minimum=1; maximum=5000 | Maximum number of listings to return and bill for (one 'listing-scraped' charge each). Applies to both direct and browse modes. Defaults to 50; allowed range 1–5000. In keyword mode the actor stops as soon as this many matches are found. |
| `maxScan` | integer; minimum=1; maximum=5000 | Only used in browse mode WITH a keyword: how many catalog listings to fetch and inspect while looking for matches. Higher values find more matches but cost more compute. Defaults to 400; allowed range up to 5000. Ignored when no keyword is set or when Listing URLs are provided. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## apify-store-scraper

Exact owner: `khadinakbar`. Identity: `LfwBeMS8ej3n1p8QK`. State: `public_schema_verified`.

Build `1.1.9` / `ayBhicZJtq7VicLHU`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/apify-store-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `categoryNames` | array | Filter by one or more store categories. Leave empty for ALL categories. E.g. 'AI', 'Lead Generation', 'Social Media', 'E-commerce', 'Developer Tools', 'Marketing', 'SEO Tools'. |
| `sortBy` | string; popularity, newest, lastUpdate, totalUsers, relevance | Sort order. 'popularity' = most users first (default). 'newest' = recently published. 'lastUpdate' = recently updated. 'totalUsers' = by total user count. 'relevance' = relevance score. |
| `pricingModels` | string; All, FREE, PAID | Filter by pricing. 'All' = both free and paid. 'FREE' = free actors only. 'PAID' = paid actors only. |
| `maintainedBy` | string; All Developers, apify | 'All Developers' = everyone (default). 'apify' = official Apify-built actors only. |
| `maxItems` | integer; minimum=0 | Max actors to scrape. 0 = all (26,000+ actors). Set a smaller number for a quick sample. |
| `enrichDetails` | boolean | When true (default), fetches the full actor detail page per actor to add: publish date (created_at), last modified, current version, build number, memory/timeout defaults, SEO title/description, README summary. Slower but much richer output. Set false for a fast shallow scan. |
| `detailConcurrency` | integer; minimum=1; maximum=20 | Parallel detail fetches per batch (1–20). Higher = faster. Default: 10. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## startup-investors-scraper

Exact owner: `khadinakbar`. Identity: `KNOFDhdwSdfQQi9uj`. State: `public_schema_verified`.

Build `0.1.7` / `jlh2R8CGhdkgvehKs`; tag `latest`. Required keys: `lists`. [Full dated input schema](../schemas/startup-investors-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `lists` | array | OpenVC lists to scrape. Pass a sector keyword (ai → ai-investors), a full slug (fintech-investors), or a full https://www.openvc.app/investor-lists/... URL. Each list yields public investor rows with check size and thesis. |
| `investorTypes` | array | Optional. Keep investors whose type contains one of these strings (e.g. VC firm, Angel, Family office, Accelerator). |
| `stages` | array | Optional. Keep investors covering a stage that contains one of these (e.g. Prototype, Early Revenue, Scaling, Seed, Series A). |
| `geographies` | array | Optional. Keep investors targeting a country/region that contains one of these (e.g. USA, France, Europe). |
| `checkSizeContains` | array | Optional. Keep investors whose check-size text contains one of these (e.g. $500k, $1M). |
| `leadOnly` | boolean | If true, keep only investors that lead rounds (Lead = Yes/Always/Sometimes — excludes Never/No). |
| `maxInvestors` | integer; minimum=1; maximum=5000 | Maximum investor rows to return across all lists. Each persisted row charges $0.025. Prefill 10 keeps quality tests cheap. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## pitchbook-scraper

Exact owner: `khadinakbar`. Identity: `AUNBd9g5ZZk4E4YzN`. State: `public_schema_verified`.

Build `0.2.8` / `2umH6XWQrBuz2Xh2D`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/pitchbook-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `profileUrls` | array | Use this when you already have public PitchBook profile, research, or news URLs. Enter up to 25 HTTPS URLs such as https://pitchbook.com/profiles/company/127635-40. When direct public HTML is unavailable, the optional Google fallback can recover only publicly indexed title and description metadata. The actor rejects login, dashboard, and private subscription URLs. |
| `maxItems` | integer; minimum=1; maximum=25 | Use this when limiting cost and run time. Sets the number of accepted URLs to process, from 1 to 25; default 10. It is not a search-results limit because this actor does not discover or crawl private PitchBook pages. |
| `useApifyProxy` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `useGoogleSearchFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## acquire-com-scraper

Exact owner: `khadinakbar`. Identity: `IzMeaEaveAmTFhndd`. State: `public_metadata_unavailable`.

Live metadata/schema unavailable at inspection. Treat as a coverage gap until a fresh read verifies it; do not run from assumptions.
