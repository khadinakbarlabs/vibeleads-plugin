# Events and partnerships source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## eventbrite-events-scraper

Exact owner: `khadinakbar`. Identity: `LZgovndFTKPXD4yno`. State: `public_schema_verified`.

Build `0.4.5` / `HBxgDKsfGBZJwOKeC`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/eventbrite-events-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Free-text keyword to search Eventbrite (e.g., 'tech conference', 'jazz concert', 'startup meetup'). Combined with location and date filters when provided. Leave empty when using startUrls or browsing by category alone. NOT an event ID and NOT an Eventbrite URL — for those use startUrls instead. |
| `location` | string | City or country slug used by Eventbrite (e.g., 'ny--new-york', 'ca--san-francisco', 'united-kingdom--london', 'united-states', 'online'). Format is two letters for state/region, double hyphen, then city name in lowercase with hyphens. Defaults to 'united-states' when omitted. NOT a free-text city name — must be the URL slug. |
| `category` | string; , music, business, food-and-drink, community, arts, film-and-media, sports-and-fitness, health, science-and-tech, travel-and-outdo | Eventbrite category slug to filter results (e.g., 'music', 'business', 'food-and-drink', 'health', 'arts', 'sports-and-fitness'). Leave empty for all categories. NOT a custom keyword — use searchQuery for that. See https://www.eventbrite.com/d/online/all-events/ for full list. |
| `dateFilter` | string; , today, tomorrow, this-weekend, this-week, next-week, this-month, next-month | Date-range filter applied on top of search results. One of the predefined Eventbrite ranges (e.g., 'today', 'this-weekend', 'next-month'). Leave empty to include all upcoming events. NOT a YYYY-MM-DD date — Eventbrite browse pages only support predefined ranges. |
| `format` | string; , class, conference, festival, performance, screening, seminar, tournament, convention, expo, game, party, rally, tour, race, attr | Event format filter (e.g., 'conference', 'festival', 'class', 'networking'). Combined with category and location filters. Leave empty to include all formats. NOT an online-only flag — use the 'onlineOnly' boolean for that. |
| `priceFilter` | string; , free, paid | Filter by free or paid events only. Leave empty to include both. NOT a numeric price range — Eventbrite browse pages do not support arbitrary price ranges. |
| `onlineOnly` | boolean | Restrict results to virtual/online events. When true, location is ignored. Defaults to false (both in-person and online included). |
| `startUrls` | array | Direct Eventbrite browse URLs or event page URLs to scrape. Use this for custom search filters not exposed by this Actor's inputs, or to scrape specific event detail pages. Any URL parameters are preserved (e.g., '?page=2'). Mutually exclusive with searchQuery and location — provide either startUrls OR the filter inputs, not both. |
| `maxResults` | integer; minimum=1; maximum=10000 | Maximum number of events to return. Eventbrite browse pages return 20 events per page with up to 49 pages per query (~1,000 events max per filter combination). Default 50 keeps run cost low for typical agent calls. Set higher for bulk extraction. |
| `includeDetails` | boolean | Fetch each event's detail page to extract full description, organizer name and profile URL, ticket tiers with prices, and structured pricing currency. When false, returns only browse-page fields (still 25+ fields). Adds one HTTP request per event but no extra event charge. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## 10times-events-scraper

Exact owner: `khadinakbar`. Identity: `Cea5rGbzIjeMykfDU`. State: `public_schema_verified`.

Build `0.1.17` / `Stq0O70UjVNZzfcOP`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/10times-events-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Direct 10times URLs to scrape. Accepts event detail pages (e.g. 'https://10times.com/ces-las-vegas'), city listing pages ('https://10times.com/berlin', 'https://10times.com/new-york-us'), category listings ('https://10times.com/conferences', 'https://10times.com/technology-events'), or search URLs ('https://10times.com/?query=fintech'). Mutually exclusive with searchQuery and city — use this for fully custom filtering 10times exposes in its UI but this Actor's inputs do not surface. |
| `searchQuery` | string | Free-text keyword to search 10times (e.g. 'fintech', 'medical devices', 'sustainability'). Combined with country and eventType filters when provided. Leave empty when using startUrls or browsing by city alone. NOT an event slug and NOT a full URL — for those use startUrls. |
| `city` | string | 10times city slug used in URLs (e.g. 'berlin', 'new-york-us', 'london-uk', 'singapore', 'dubai-ae', 'sao-paulo-br'). Combined with eventType, category, and date filters. Leave empty when using startUrls or searchQuery. NOT a free-text city name — must be the URL slug 10times uses on its city pages. |
| `country` | string; WW, US, GB, DE, FR, ES, IT, NL, AU, CA, JP, IN, BR, MX, CN, SG, AE, ZA, KR, ID, TH | Two-letter ISO country code to scope a search query to one country (e.g. 'US', 'DE', 'GB', 'IN', 'AE'). Use 'WW' or leave blank for worldwide. Ignored when city is set (city already implies country). NOT a country name — must be the ISO 3166-1 alpha-2 code. |
| `eventType` | string; all, tradeshow, conference, workshop, festival | Filter by event format. 'tradeshow' = exhibitions and trade fairs, 'conference' = paid speaker conferences, 'workshop' = hands-on training, 'festival' = public/cultural events. Applied client-side on discovered events. Defaults to 'all'. |
| `category` | string; all, technology, it, business, medical, health, education, industrial, building, auto, banking, food, entertainment, apparel, scie | Industry filter applied to event categories and description tags. Leave 'all' to include every industry. Use this with city/searchQuery to narrow by sector (e.g. 'technology' + 'berlin' = Berlin tech events). NOT a free-text industry name — must be one of the listed slugs. |
| `startDate` | string | Only return events starting on or after this date. Format YYYY-MM-DD (e.g. '2026-06-01'). Leave empty for all upcoming events. NOT a date range — pair with endDate to bound on both sides. |
| `endDate` | string | Only return events starting on or before this date. Format YYYY-MM-DD (e.g. '2026-12-31'). Leave empty for no upper bound. Pair with startDate for a bounded date window. |
| `onlineOnly` | boolean | Restrict results to virtual/online events. Defaults to false (both in-person and online included). |
| `maxItems` | integer; minimum=1; maximum=10000 | Maximum number of events to return. 10times listing pages show ~30 events per page; this Actor paginates until maxItems is met or the listing is exhausted. Default 50 keeps run cost low for typical agent calls (~$0.25). Set higher for bulk extraction. Hard ceiling 10000. |
| `includeDetails` | boolean | Fetch each event's detail page to extract full description, organizer details, visitor/exhibitor estimates, and rating. When false, returns only listing-page fields (still includes name, dates, venue, URL). Adds one HTTP request per event but no extra event charge. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## meetup-events-scraper

Exact owner: `khadinakbar`. Identity: `hRgmkDqjzRl5SxjUB`. State: `public_schema_verified`.

Build `0.3.2` / `x8esNNyE0wUoFjw2G`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/meetup-events-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Keyword searches run on Meetup events, one entry per term (e.g. 'technology', 'yoga', 'startup networking'). Pair with a location (city, zip, or lat+lon) — Meetup search is location-scoped. Leave empty if you only want group or event URLs. NOT a group or event URL. |
| `city` | string | City to scope the keyword search to (e.g. 'New York'). Combine with state/country for accuracy. Ignored for group-URL and event-URL modes. NOT a venue name. |
| `state` | string | State or region code for the search location (e.g. 'NY'). Optional refinement on top of city. Ignored outside search mode. NOT a country. |
| `country` | string | Two-letter country code for the search location (e.g. 'us', 'gb'). Optional. Ignored outside search mode. |
| `zip` | string | Postal code to scope the search (e.g. '10001'). Alternative to city. Ignored outside search mode. |
| `lat` | number | Latitude for a precise geo-scoped search (e.g. 40.7128). Use with lon and radius for map-bounded searches. Optional. Ignored outside search mode. |
| `lon` | number | Longitude for a precise geo-scoped search (e.g. -74.006). Use with lat and radius. Optional. Ignored outside search mode. |
| `radius` | number | Search radius in miles around the lat/lon or city (e.g. 50). Defaults to Meetup's default when omitted. Ignored outside search mode. |
| `eventType` | string; ANY, PHYSICAL, ONLINE, HYBRID | Restrict search results to a single format. PHYSICAL = in-person, ONLINE = virtual, HYBRID = both. Leave as 'Any' for all formats. Ignored outside search mode. |
| `startDate` | string | Only return search events starting on or after this ISO 8601 datetime (e.g. '2026-07-01T00:00:00Z'). Optional. Ignored outside search mode. |
| `endDate` | string | Only return search events starting on or before this ISO 8601 datetime (e.g. '2026-08-01T00:00:00Z'). Optional. Ignored outside search mode. |
| `minRsvpCount` | integer | Only return search events with at least this many RSVPs (e.g. 10) — filters out tiny events. Optional. Ignored outside search mode. |
| `sortField` | string; RELEVANCE, DATETIME | Order search results by RELEVANCE (Meetup's match score) or DATETIME (chronological). Defaults to RELEVANCE. Ignored outside search mode. |
| `groupUrls` | array | Meetup group URLs or urlnames to pull every event from (e.g. 'https://www.meetup.com/nyc-tech/' or just 'nyc-tech'). Returns the group's upcoming or past events (see groupEventStatus). NOT an event URL. |
| `groupEventStatus` | string; upcoming, past | For group-URL mode, choose which events to return: upcoming (future, ascending) or past (history, most-recent first). Defaults to upcoming. Only applies to groupUrls. |
| `eventUrls` | array | Specific Meetup event URLs or numeric event IDs to fetch directly (e.g. 'https://www.meetup.com/nyc-tech/events/315015546/' or '315015546'). Best for enriching a known list of events. NOT a group URL. |
| `maxItems` | integer; minimum=1 | Hard cap on total unique events returned across all modes (e.g. 200). Stops pagination and charging once reached. Defaults to 200. Raise for deep crawls. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## beehiiv-newsletter-scraper

Exact owner: `khadinakbar`. Identity: `qK1jqOSUmQsIdvBit`. State: `public_schema_verified`.

Build `1.0.11` / `o5xHYKkYLxkOP38j9`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/beehiiv-newsletter-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `publicationUrls` | array | Use this when you have Beehiiv newsletter homepage URLs (e.g. https://aibreakfast.beehiiv.com). The actor will scrape publication metadata and, based on scrapeMode, also enumerate and scrape posts. Use postUrls instead when you have direct post links. |
| `postUrls` | array | Use this when you have direct Beehiiv post URLs (e.g. https://aibreakfast.beehiiv.com/p/some-post-slug). Scrapes individual posts directly. Use publicationUrls instead to discover all posts from a newsletter homepage. |
| `scrapeMode` | string; metadata, metadata_posts, full | Controls how much data to extract. 'metadata' = newsletter info only (fastest, cheapest). 'metadata_posts' = newsletter info + full post list with dates and previews (recommended for most use cases). 'full' = everything including full post content (best for LLM training, research, archiving). |
| `maxPostsPerPublication` | integer; minimum=1; maximum=500 | Maximum number of posts to scrape per newsletter publication. Lower values reduce cost and run time. Set to 500 for full archive scraping. |
| `maxResults` | integer; minimum=1; maximum=5000 | Maximum total number of records (newsletter + post records combined) to return across all input publications. The actor stops as soon as this limit is reached. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## substack-posts-scraper

Exact owner: `khadinakbar`. Identity: `U2vs9AzwTDlMEbbWp`. State: `public_schema_verified`.

Build `0.2.2` / `BeQkpclKL1v1ZmlBp`; tag `latest`. Required keys: `startUrls`. [Full dated input schema](../schemas/substack-posts-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | One or more Substack publication URLs. Accepts publication roots (e.g. 'https://platformer.substack.com' or custom domain 'https://www.lennysnewsletter.com') and single post URLs ('https://.../p/some-post'). Each publication is paginated up to maxPosts. NOT a keyword search input — this actor scrapes by publication URL. |
| `maxPosts` | integer; minimum=1; maximum=2000 | Hard cap on the number of posts scraped and billed per publication. Each post counts as one billable result. Defaults to 50. Set lower for cheap test runs. |
| `includeBodyHtml` | boolean | When true (default), fetches each post's detail page to capture the complete article HTML. Public posts return full HTML; paid posts return metadata + paywall signal only. Adds one HTTP request per post. |
| `includeBodyText` | boolean | When true (default), includes a plain-text version of the article body (derived from the HTML). Public posts return full text; paid posts return the teaser only. Disable to reduce payload size. |
| `publishedAfter` | string | Optional ISO 8601 date or datetime. Only posts published on or after this date are returned, e.g. '2026-01-01' or '2026-06-01T00:00:00Z'. Leave empty for no lower bound. |
| `publishedBefore` | string | Optional ISO 8601 date or datetime. Only posts published on or before this date are returned. Leave empty for no upper bound. |
| `audience` | string; all, free, paid | Filter posts by paywall audience. 'all' (default) returns every post; 'free' returns only free posts; 'paid' returns only paid/paywalled posts (metadata + teaser). |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## scrape-luma-events

Exact owner: `khadinakbar`. Identity: `3JyCkOcgh4tjUanzW`. State: `public_metadata_unavailable`.

Live metadata/schema unavailable at inspection. Treat as a coverage gap until a fresh read verifies it; do not run from assumptions.
