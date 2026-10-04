# Reviews and directories source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [qualified business/contact-use gate](../contact-use.md). Provider result bounds are not recommended audience sizes; optional contact extraction must be disabled during discovery.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## clutch-scraper

Exact owner: `khadinakbar`. Identity: `QHYkMFubWuHnbLnyR`. State: `public_schema_verified`.

Build `1.2.2` / `27B2oV8TNUXZm46JW`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/clutch-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `categoryUrl` | string | Use this when you have one Clutch.co category, service, or directory URL to scrape, such as https://clutch.co/it-services, /web-developers, or /agencies/digital-marketing. If searchUrls is set, searchUrls wins. This actor scrapes listing pages, not individual /profile/ review pages. |
| `searchUrls` | array | Use this when you want to scrape several Clutch.co listing pages in one run. Each item should be a category, service, search, or location directory URL that shows company cards. Example: https://clutch.co/web-developers. Do not pass individual company profile URLs here. |
| `startUrls` | array | Use this when calling from Apify integrations that provide request-list objects. Accepts Clutch.co listing URLs as strings or objects with a url field. Kept for backwards compatibility with older clutch-scraper integrations. |
| `location` | string | Use this when you want Clutch to narrow the directory server-side with the geolocation query parameter. Examples: United States, London, India. Leave empty for global listings. |
| `minRating` | number; minimum=0; maximum=5 | Use this when you only want companies with a Clutch star rating at or above the chosen value. Decimals are allowed, for example 4.5. Companies with no rating are dropped when this is set. |
| `minReviews` | integer; minimum=0 | Use this when you only want companies with at least this many Clutch reviews. Companies with no visible review count are dropped when this is set. |
| `verifiedOnly` | boolean | Use this when you want only companies that show a Clutch verified badge. Defaults to false. |
| `excludeSponsored` | boolean | Use this when you want to drop paid or featured placements and keep only organic listing cards. Defaults to false. |
| `serviceKeyword` | string | Use this when you want a case-insensitive filter against each company's displayed services. Example: mobile app, SEO, software. Leave empty to keep all services. |
| `locationKeyword` | string | Use this when you want a case-insensitive filter against each company's displayed location text. Example: New York or India. Leave empty to keep all locations. |
| `maxResults` | integer; minimum=1; maximum=5000 | Maximum company records to return and bill for. Pagination stops once this limit is reached. Bounds: 1 to 5000. |
| `maxPages` | integer; minimum=1; maximum=500 | Safety cap on listing pagination per start URL. Increase it for very large categories or restrictive filters. Defaults automatically from maxResults. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | Number of parallel browser pages. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## clutch-listings-scraper

Exact owner: `khadinakbar`. Identity: `qGeA0rcK8hiWhot9T`. State: `public_schema_verified`.

Build `1.1.3` / `dGlQSUvveanQRYZPR`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/clutch-listings-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchUrls` | array | Use this when you want to scrape one or several Clutch category, service, or location directory pages in the same run. Supply public listing pages rather than individual /profile/ pages. This list takes precedence over One agency directory URL. Leave the list empty to use that single-URL field or the built-in digital-marketing fallback. |
| `categoryUrl` | string | Use this when you have one Clutch listing page and prefer a simple URL field. A full URL or path such as /it-services works. It is ignored whenever Agency directory URLs contains at least one entry. Omit both URL fields to use the built-in digital-marketing agencies directory. |
| `location` | string | Use this when Clutch should narrow every supplied directory URL server-side. The value is added through Clutch's geolocation query parameter. Values such as United States or London are useful starting points. Leave it empty for the directory's default geography. |
| `maxResults` | integer; minimum=1; maximum=5000 | Use this to cap both returned agencies and scraped-listing event charges. The crawler stops after this many validated rows. A lower Apify run charge limit always takes precedence. Start with 20 to 50 agencies when testing a new directory. |
| `maxPages` | integer; minimum=1; maximum=100 | Use this to put a hard pagination boundary on each supplied directory URL. The limit applies independently to every starting URL. Lower it for quick samples. Raise it when a narrow client-side filter needs more source pages. |
| `minRating` | number; minimum=0; maximum=5 | Use this when you only want agencies whose listing card has at least this Clutch star rating. Values from zero through five are accepted. Agencies without a visible rating are excluded when this filter is set. Leave the field unset to keep rated and unrated agencies. |
| `minReviews` | integer; minimum=0 | Use this when an agency must have at least a specific number of visible Clutch reviews. Zero and positive integers are accepted. Agencies without a visible review count are excluded when this filter is set. Leave the field unset to keep agencies regardless of review count. |
| `verifiedOnly` | boolean | Use this when your shortlist should contain only listing cards where a Clutch verification badge is visible. Verification is detected from the directory card rather than inferred from other fields. Keep it off to include verified and unverified agencies. Combine it with other filters to make a stricter shortlist. |
| `excludeSponsored` | boolean | Use this when you want an organic agency shortlist without sponsored or featured listing cards. Sponsored status is detected from the card and its tracked links. Keep it off when paid placements should remain in their displayed order. The output always includes is_sponsored for independent auditing. |
| `serviceKeyword` | string | Use this when at least one service shown on the listing card must contain a phrase such as mobile app or SEO. Matching is case-insensitive and uses substring logic. This filters collected cards; it is not a Clutch search query. Leave it empty to accept every visible service mix. |
| `locationKeyword` | string | Use this when the location displayed on each agency card must contain a phrase such as New York or India. Matching is case-insensitive and uses substring logic. This filter runs after the cards are collected. For Clutch's server-side geography, use Clutch geolocation instead. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | Use this advanced control to set how many Clutch directory requests run in parallel. Two is the reliability-oriented default. Keep the default unless runtime matters more than conservative request pacing. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## clutch-reviews-scraper

Exact owner: `khadinakbar`. Identity: `8z0phzG4wUZAHGn2T`. State: `public_schema_verified`.

Build `1.1.2` / `YxWiw21IUWaqR6Ogg`; tag `latest`. Required keys: `profileUrls`. [Full dated input schema](../schemas/clutch-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `profileUrls` | array | One or more Clutch.co agency profiles to scrape reviews from. Accepts full URLs (e.g. 'https://clutch.co/profile/wedowebapps') or bare slugs (e.g. 'wedowebapps'). Each profile is paginated automatically to collect its review history. NOT a Clutch category or search URL — for company listings use the clutch-scraper actor instead. |
| `maxReviews` | integer; minimum=1; maximum=5000 | Maximum total number of reviews to scrape across all profiles in this run (e.g. 100). The run stops and billing ends once this cap is reached. Defaults to 100. This is a hard cost cap — see the Pricing tab for current per-review pricing. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | How many profile pages to load in parallel (e.g. 2). Defaults to 2. Keep at 1-3 for reliability. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## g2-product-reviews-scraper

Exact owner: `khadinakbar`. Identity: `FwIxRhXDEbykgdeqc`. State: `public_schema_verified`.

Build `1.2.2` / `BsvaC7eHgGDD3WS11`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/g2-product-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | G2 product or reviews URLs to scrape, one record per review returned. Each must look like https://www.g2.com/products/{slug}/reviews (e.g. https://www.g2.com/products/slack/reviews); the /reviews suffix is optional and added automatically. Defaults to none — provide this OR searchQuery. NOT a G2 category, compare, or vendor-profile URL. |
| `searchQuery` | string | Product name or keyword to search on G2, then scrape the matching products' reviews. Free text, e.g. 'project management software' or 'Salesforce'. Defaults to empty — provide this OR startUrls. NOT a URL; paste URLs into startUrls instead. |
| `maxReviewsPerProduct` | integer; minimum=1; maximum=5000 | Upper bound on how many reviews to extract for each product, newest or most-helpful first. Accepts 1–5000. Defaults to 50. This is per product, not a run-wide total — total cost scales with this times the number of products. |
| `maxProductsPerSearch` | integer; minimum=1; maximum=100 | In search mode, how many matching products to take from the G2 search results. Accepts 1–100. Defaults to 5. Ignored when you pass startUrls instead of a searchQuery. |
| `includeReviews` | boolean | When true (default), search mode visits each matched product and scrapes its reviews. When false, search mode returns only product summary cards (name, URL) — cheaper for discovery. Has no effect in URL mode, which always scrapes reviews. |
| `sortReviewsBy` | string; newest, helpful | Order in which G2 returns reviews before the per-product cap is applied. 'newest' fetches the most recent reviews first; 'helpful' fetches the most-helpful first. Defaults to 'newest'. Affects which reviews you get when maxReviewsPerProduct is smaller than the total. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `debug` | boolean | When true, writes a per-product diagnostic dump (JSON-LD nodes, selector hits, HTML head) to the key-value store for troubleshooting extraction. Defaults to false. Leave off for normal runs — it adds no review data and slightly slows the run. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## capterra-reviews-scraper

Exact owner: `khadinakbar`. Identity: `vPxFQ4unR0IzHFm9H`. State: `public_schema_verified`.

Build `1.1.9` / `axM1fQROQpyZTRtHG`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/capterra-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Capterra product or reviews URLs to scrape, one record per review returned. Each must look like https://www.capterra.com/p/{id}/{slug}/reviews/ (e.g. https://www.capterra.com/p/135003/Slack/reviews/); the /reviews/ suffix is optional and added automatically. Defaults to none — provide this OR searchQuery. NOT a Capterra category, search, or comparison URL. |
| `searchQuery` | string | Product name or keyword to search on Capterra, then scrape the matching products' reviews. Free text, e.g. 'project management software' or 'Slack'. Defaults to empty — provide this OR startUrls. NOT a URL; paste URLs into startUrls instead. |
| `maxReviewsPerProduct` | integer; minimum=1; maximum=5000 | Upper bound on how many reviews to extract for each product, newest or most-helpful first. Accepts 1–5000. Defaults to 50. This is per product, not a run-wide total — total cost scales with this times the number of products. |
| `maxProductsPerSearch` | integer; minimum=1; maximum=100 | In search mode, how many matching products to take from the Capterra search results. Accepts 1–100. Defaults to 5. Ignored when you pass startUrls instead of a searchQuery. |
| `includeReviews` | boolean | When true (default), search mode visits each matched product and scrapes its reviews. When false, search mode returns only product summary cards (name, rating, review count, URL) — cheaper for discovery. Has no effect in URL mode, which always scrapes reviews. |
| `sortReviewsBy` | string; newest, helpful | Order in which Capterra returns reviews before the per-product cap is applied. 'newest' fetches the most recent reviews first; 'helpful' fetches the most-upvoted first. Defaults to 'newest'. Affects which reviews you get when maxReviewsPerProduct is smaller than the total. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `debug` | boolean | When true, writes a per-product diagnostic dump (JSON-LD nodes, selector hits, HTML head) to the key-value store for troubleshooting extraction. Defaults to false. Leave off for normal runs — it adds no review data and slightly slows the run. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## trustradius-reviews-scraper

Exact owner: `khadinakbar`. Identity: `lFAe0OfsgZUuP83kR`. State: `public_schema_verified`.

Build `0.1.7` / `8yFHWhzNQmVrzhQ0S`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/trustradius-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | TrustRadius product or reviews URLs to scrape. Each must look like https://www.trustradius.com/products/{slug}/reviews (product root URLs are normalized). Provide this OR productSlugs OR searchQuery. |
| `productSlugs` | array | TrustRadius product slugs without the full URL, e.g. slack or hubspot. Provide this OR startUrls OR searchQuery. |
| `searchQuery` | string | Product name or keyword to search on TrustRadius, then scrape matching products. Free text such as Slack or CRM. Provide this OR startUrls OR productSlugs. |
| `maxReviewsPerProduct` | integer; minimum=1; maximum=5000 | Upper bound on reviews extracted per product (1-5000). Defaults to 50. Prefill uses 1 for a cheap health check. |
| `maxProductsPerSearch` | integer; minimum=1; maximum=100 | In search mode, how many matching products to take (1-100). Defaults to 5. Ignored for startUrls/productSlugs. |
| `includeReviews` | boolean | When true (default), search mode scrapes reviews for each matched product. When false, search returns product cards only (product-found billing). |
| `includeProductSummary` | boolean | When true and includeReviews is false, URL/slug mode may emit a product card. Leave false for review-only runs. |
| `sortReviewsBy` | string; newest, helpful | TrustRadius sort before the per-product cap: newest maps to most-recent; helpful maps to most-helpful. |
| `starRating` | array | Optional market-style 1-5 star filter mapped to TrustRadius 0-10 bands (5 stars approx 8-10). Empty means no filter. |
| `companySize` | array | Optional reviewer company-size filter: small / medium / large (best-effort from public firmographics). |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `debug` | boolean | When true, writes a first-page diagnostic dump to the key-value store. Leave off for normal runs. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## gartner-peer-insights-scraper

Exact owner: `khadinakbar`. Identity: `bZkCe9FVekifmOMXD`. State: `public_schema_verified`.

Build `0.1.9` / `Pz0yLWZhKNoERwACk`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/gartner-peer-insights-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `productUrls` | array | Gartner Peer Insights product page URLs. Accepts short form https://www.gartner.com/reviews/product/{slug} or long market/vendor/product/reviews URLs. Use this when you already know the product page. NOT a free-text search — use searchTerms or productSlugs for that. |
| `marketUrls` | array | Gartner market/category listing URLs such as https://www.gartner.com/reviews/market/meeting-solutions. Returns product cards (name, rating, review count, SEO slug). NOT individual product review pages — use productUrls for those. |
| `productSlugs` | array | Product SEO names without a full URL (e.g. zoom-meetings, salesforce-sales-cloud). Converted to /reviews/product/{slug}. Prefer productUrls when you have the canonical link. |
| `searchTerms` | array | Free-text product names slugified into /reviews/product/{slug} lookups (e.g. Zoom Meetings → zoom-meetings). Best-effort public slug resolution; prefer exact productUrls when known. NOT a full Gartner site search API. |
| `startUrls` | array | Optional requestListSources-style URL list. Same classification as productUrls/marketUrls. Prefer productUrls or marketUrls for clarity. |
| `maxReviewsPerProduct` | integer; minimum=1; maximum=500 | Hard cap on review/highlight rows saved per product. Default 5 for quality tests. Range 1-500. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `maxProducts` | integer; minimum=1; maximum=200 | Hard cap on product cards saved from each market URL. Default 20. Range 1-200. |
| `includeProductSummary` | boolean | If true (default), saves one product profile row (ratings, vendor, description) per product URL in addition to review rows. |
| `includeReviewHighlights` | boolean | If true (default), also saves public likes/dislikes highlight snippets as review-highlight rows when present on the product page. |
| `sort` | string; helpful, newest | Ignored for public page samples. Default most helpful. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `sessionCookie` | string | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## software-reviews-all-in-one-scraper

Exact owner: `khadinakbar`. Identity: `Z0dljKpv1KUYcpL5C`. State: `public_schema_verified`.

Build `1.0.32` / `ekBUBsAu0bWettlHx`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/software-reviews-all-in-one-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | List of product or reviews URLs from G2, Capterra, TrustRadius, SoftwareAdvice, or GetApp. Platform is auto-detected from the domain. Use this when you already know the product page. NOT a search term — use 'searchQuery' for that. |
| `searchQuery` | string | Free-text software product name to find across platforms (e.g., 'Slack', 'HubSpot CRM', 'Notion'). Returns matching products from each enabled platform. Defaults to empty. NOT a URL — use 'startUrls' for direct product pages. |
| `platforms` | array | Platforms used in search mode (ignored for startUrls — URL auto-detects). Defaults to G2, Capterra, TrustRadius. Add 'softwareadvice' or 'getapp' for the Gartner-family discovery sites. NOT used when startUrls is provided. |
| `maxReviewsPerProduct` | integer; minimum=1; maximum=5000 | Hard cap on reviews scraped per product (across all pages). Lower this to control PPE spend. Default 100. Range 1-5000. NOT total reviews across products — set this per-product. |
| `maxProductsPerSearch` | integer; minimum=1; maximum=100 | Hard cap on products returned by each search per platform. Defaults to 10. Range 1-100. Only used in search mode. |
| `includeReviews` | boolean | If true (default), scrapes individual reviews. If false, returns product summary cards only (name, rating, review count, URL) — cheaper for product discovery without review content. NOT a content filter — use 'maxReviewsPerProduct' to limit volume. |
| `sortReviewsBy` | string; newest, helpful | Review sort order. 'newest' returns most recent first, 'helpful' returns highest-voted first. Default 'newest'. NOT a filter — all matching reviews returned regardless of sort. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `debug` | boolean | When true, the first page of each product is dumped to the run's key-value store under 'DEBUG-<platform>-<slug>' for selector diagnostics. Leave OFF for production scrapes — it makes runs slower and clutters KV. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## trustpilot-company-scraper

Exact owner: `khadinakbar`. Identity: `dwzGa9UOUzw2nggC4`. State: `public_schema_verified`.

Build `1.0.4` / `dWv9wxd8lQH6ePNIm`; tag `latest`. Required keys: `queries`. [Full dated input schema](../schemas/trustpilot-company-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | Use this when you need Trustpilot company records from domains, company URLs, search terms, or category pages. Enter one item per line: 'apple.com' or 'https://www.trustpilot.com/review/apple.com' returns a company profile; '/categories/bank' returns a category leaderboard; 'online banks' runs company search. NOT for individual review text — use the trustpilot-reviews-scraper actor for reviews. |
| `mode` | string; auto, profile, search, category | Use this when you want to force how every company target is interpreted. 'auto' detects profile, search, or category per item; 'profile' treats each item as a company domain or Trustpilot review URL; 'search' runs Trustpilot company search; 'category' treats each item as a category slug or URL. Defaults to auto and is NOT a review filter. |
| `country` | string | Use this when search or category results should be scoped to a Trustpilot market. Enter a two-letter ISO country code such as 'US', 'GB', 'DE', 'FR', or 'AU'; leave empty for global trustpilot.com. Ignored for profile mode because company profiles resolve to canonical pages. NOT a language or review-country filter. |
| `maxResultsPerQuery` | integer; minimum=1; maximum=1000 | Use this to cap how many company records are returned for each target. Profile targets always return at most 1 company; search and category targets paginate until this cap is reached or results run out. Defaults to 50 with a hard cap of 1000 per target to protect budget. NOT a review-count limit. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## trustpilot-reviews-scraper

Exact owner: `khadinakbar`. Identity: `AdXgrEqrRSjvp9q6u`. State: `public_schema_verified`.

Build `1.0.22` / `gT8oczsXNZB6qzAca`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/trustpilot-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyIdentifiers` | array | Use this field when the user provides domains (e.g. 'apple.com'), Trustpilot review URLs (e.g. 'https://www.trustpilot.com/review/apple.com'), or company names (e.g. 'Apple'). Enter one per line. Accepts all three formats — the actor resolves each to the correct Trustpilot page automatically. |
| `maxReviewsPerCompany` | integer; minimum=0 | Maximum number of reviews to scrape per company. Set to 0 for unlimited (scrapes all available reviews). Default is 100. |
| `filterStars` | array | Only scrape reviews with these star ratings. Leave empty to scrape all ratings. Use when the user wants only positive reviews (4-5 stars) or only negative reviews (1-2 stars). |
| `filterLanguage` | string | Only scrape reviews written in this language. Use ISO 639-1 codes: 'en' for English, 'de' for German, 'fr' for French, 'es' for Spanish, 'nl' for Dutch. Leave empty for all languages. |
| `filterDateRange` | string; , last30days, last3months, last6months, last12months | Only scrape reviews published within this date range. Leave empty to scrape all dates. |
| `sortBy` | string; recency, relevance | Sort order for reviews. 'recency' returns newest first. 'relevance' returns most helpful first (Trustpilot default). |
| `onlyVerified` | boolean | When enabled, only scrape reviews from verified purchases or verified invitations. Reduces quantity but improves data quality for market research. |
| `onlyWithReplies` | boolean | When enabled, only scrape reviews that have received a reply from the company. Useful for analyzing how companies handle customer feedback. |
| `includeCompanyInfo` | boolean | When enabled, each review record includes company metadata: trust score, total review count, categories, and domain. Disable to reduce output size when only review content is needed. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-maps-reviews-scraper

Exact owner: `khadinakbar`. Identity: `AktHAcFexdMKzxCux`. State: `public_schema_verified`.

Build `0.4.10` / `tiHTLlwqds0E2OetA`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/google-maps-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | List of Google Maps URLs to scrape reviews from. Accepts place URLs (https://www.google.com/maps/place/...), search URLs, CID URLs (?cid=...), and shortened maps.app.goo.gl links. Each URL yields reviews for one place. Do NOT paste Google Search result URLs — only maps.google.com / google.com/maps URLs are supported. |
| `placeIds` | array | Google Place IDs (format ChIJ... or 0x...:0x...). Each is resolved to a place page and its reviews are scraped. Example: 'ChIJLU7jZClu5kcR4PcOOO_ouTY' for Eiffel Tower. Leave empty if you are providing startUrls — either input works. |
| `dataIds` | array | Google Maps internal data IDs in 0x...:0x... format. Use this when you already have a Maps CID/data ID and want the most reliable direct extraction path. Example: 0x89c259a9b3117469:0xd134e199a405a163. Not a Google Place ID starting with ChIJ — use Place IDs for that format. |
| `searchQuery` | string | Free-text business name or keyword (e.g., 'Joe's Pizza Manhattan' or 'Apple Store Regent Street'). Used with the location field to find one place and scrape its reviews. Leave empty if you are providing startUrls or placeIds — do NOT use this for broad searches, use a specific business name. |
| `location` | string | City, region, or country used to disambiguate the searchQuery (e.g., 'New York, NY' or 'London, UK'). Ignored when startUrls or placeIds are provided. Leave empty for global search on searchQuery. |
| `maxReviews` | integer; minimum=1; maximum=5000 | Maximum reviews to scrape per place. Use 10–50 for testing, 100–500 for typical monitoring, 1000+ for deep analysis. Google usually caps accessible reviews at around 4000 even for high-volume places. Billing is per review scraped, so set this to match your budget. |
| `reviewsSort` | string; newest, mostRelevant, highestRanking, lowestRanking | Order in which reviews are fetched from Google. 'newest' is best for monitoring recent feedback, 'mostRelevant' matches Google's default, 'highestRanking' / 'lowestRanking' for best/worst first. Affects which reviews you hit the maxReviews cap on. |
| `reviewSearchQuery` | string | Optional keyword to search inside Google Maps reviews before extraction. Use this when you only need reviews mentioning a phrase such as 'parking' or 'refund'. Defaults to no keyword filter. Not a business search query — use Search Query above to find the place itself. |
| `language` | string; en, es, fr, de, it, pt, nl, pl, ru, ja, ko, zh-CN, ar, tr, hi, id, vi, th, sv, no, da, fi, cs, el, he | Language for the Google Maps UI and for review translations. 'en' returns English UI, reviews stay in their original language. Affects Google's 'N reviews' parsing and the text of the 'a month ago' date labels. |
| `countryCode` | string | Two-letter Google region hint used for Maps review requests. Use this when review ordering or place resolution should match a specific market, for example US, GB, DE, or PK. Defaults to US. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `includePersonalData` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## yelp-reviews-scraper

Exact owner: `khadinakbar`. Identity: `vpR3p6zMAMTvOtBZp`. State: `public_schema_verified`.

Build `0.1.28` / `Or82uyy6giJjR4jgE`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/yelp-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | List of Yelp business pages to scrape reviews from. Each entry is a full Yelp URL (e.g., `https://www.yelp.com/biz/molinari-delicatessen-san-francisco`). Up to 50 entries per run. NOT a search URL or category URL — this actor scrapes reviews of a SPECIFIC business, not lists of businesses (for that use yelp-scraper-all-in-one). For bare slugs, use the businessSlugs field instead. |
| `businessSlugs` | array | Alternative to startUrls: pass bare Yelp business slugs (e.g., `molinari-delicatessen-san-francisco`) — one per line. Combined with startUrls if both provided. Useful when integrating from spreadsheets or databases that store slugs only. |
| `maxReviewsPerBusiness` | integer; minimum=1; maximum=5000 | Hard cap on reviews returned per business. Yelp displays up to thousands of reviews on popular businesses; 100 is a good default for monitoring. Range 1-5000. Affects PPE cost: each review = $0.0005, so 100 reviews = $0.05 per business. |
| `sortBy` | string; relevance_desc, date_desc, date_asc, rating_asc, rating_desc, elites_desc | How Yelp orders the returned reviews. `relevance_desc` (Yelp default) surfaces highest-engagement reviews first. `date_desc` returns newest first — best for monitoring fresh feedback. `rating_asc` surfaces 1-star complaints, `rating_desc` surfaces 5-star praise. |
| `language` | string; en, es, fr, de, it, pt, nl, ja, tr, ar, pl, ru, zh, ko, all | Two-letter ISO code (e.g., `en`, `es`, `fr`, `de`, `it`, `pt`, `nl`, `ja`) to filter reviews by language. Leave as `en` for English-only. Set to `all` for every language. Yelp does its own language detection — non-matching reviews may still slip through. |
| `dateFrom` | string | Earliest review date to include (inclusive). Format YYYY-MM-DD, e.g., `2025-01-01`. Leave empty for no lower bound. Filtered client-side after fetch — applies AFTER Yelp's sort. |
| `dateTo` | string | Latest review date to include (inclusive). Format YYYY-MM-DD, e.g., `2026-06-18`. Leave empty for no upper bound. |
| `includeBusinessSummary` | boolean | When true, push one extra dataset item per business with aggregate metadata (name, url, total review count, average rating, address, categories). Useful for joining reviews to business context. Does NOT add a charge — business resolution is already billed once per URL. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## glassdoor-reviews-scraper

Exact owner: `khadinakbar`. Identity: `3X4kIn91FXgsrRiKw`. State: `public_schema_verified`.

Build `1.1.2` / `UcTas1AZ1HG9yhajK`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/glassdoor-reviews-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Use this when you already have Glassdoor company review URLs. Enter URLs like https://www.glassdoor.com/Reviews/Apify-Reviews-E3100324.htm. Defaults to a small Apify company review sample when no input is provided. This is not for job listing URLs or profile login pages. |
| `companyNames` | array | Use this when you want the actor to search Glassdoor for company review pages first. Enter one company name per line, for example Apify or OpenAI. Defaults to empty and is less reliable than direct review URLs. This is not a general web search query field. |
| `maxReviewsPerCompany` | integer; minimum=1; maximum=1000 | Use this to cap review rows collected from each Glassdoor company page. Accepts integers from 1 to 1000, with 25 as the default. Lower it for quick reputation samples and raise it for deeper analysis. This is a review count, not a page count. |
| `maxResults` | integer; minimum=1; maximum=5000 | Use this to cap the total review rows saved across the whole run. Accepts integers from 1 to 5000, with 50 as the default. The actor stops before charging beyond this cap. This does not include diagnostic rows. |
| `sortBy` | string; recent, popular, default | Use this to prefer recent or popular Glassdoor reviews when the page exposes sorting controls. Choose recent for monitoring new employee feedback, popular for broad sentiment sampling, or default for Glassdoor's page order. Defaults to recent. This does not filter by rating. |
| `includeSubRatings` | boolean | Use this to include culture, compensation, career, work-life, and management ratings when Glassdoor exposes them. Defaults to true for richer HR analysis. Disable it only when you need smaller rows. This does not infer ratings that are not visible. |
| `includeEmployerResponses` | boolean | Use this to include public employer reply text when Glassdoor shows a response under a review. Defaults to true for employer-brand monitoring. Disable it to reduce output size. This does not contact or enrich employer data outside Glassdoor. |
| `responseFormat` | string; detailed, concise | Use this to choose compact or detailed rows for AI agents and analytics pipelines. concise keeps the core company, rating, title, pros, cons, and date fields. detailed includes sub-ratings, employment metadata, source snippets, and employer responses. Defaults to detailed. |
| `debug` | boolean | Use this when a run returns diagnostic rows and you need HTML or response samples for troubleshooting. Defaults to false to keep storage small. This is not needed for normal scraping. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
