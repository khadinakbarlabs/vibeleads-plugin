# News and funding research source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

## google-news-scraper

Exact owner: `khadinakbar`. Identity: `7vQKF8hrfRaAk7g50`. State: `public_schema_verified`.

Build `0.2.2` / `bbFYlpHrCcdAZ0ewm`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/google-news-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | List of search keywords or phrases to look up on Google News. Each query fetches its own RSS feed. Supports Google search operators: use quotes for exact match ("climate change"), minus to exclude (-bitcoin), OR for alte |
| `topics` | array | Select from Google News built-in topic sections. Each selected topic fetches its own RSS feed of top headlines. Use this for broad category monitoring without keywords. Can be combined with searchQueries. |
| `topicUrls` | array | Advanced: Paste the URL of any Google News section, topic page, or custom RSS feed directly. Both HTML page URLs (https://news.google.com/topics/...) and RSS URLs (https://news.google.com/rss/topics/...) are accepted — t |
| `startUrls` | array | Advanced: Provide raw Google News RSS feed URLs directly. Use for custom queries already formatted as RSS (e.g. from Google Alerts exports). Each URL must be a valid RSS feed returning XML. |
| `maxResultsPerQuery` | integer; minimum=1; maximum=100 | Maximum number of articles to extract per search query or topic feed. Google News RSS feeds return up to 100 articles per request. Default is 100. For bulk jobs with many queries, set lower (e.g. 10–20) to stay within bu |
| `regionLanguage` | string; US:en, GB:en, AU:en, CA:en, IN:en, DE:de, AT:de, CH:de, FR:fr, BE:fr, CH:fr, ES:es, MX:es, AR:es, CO:es, IT:it, PT:pt, BR:pt, NL:n | Controls the Google News edition to query — determines language, regional sources, and geographically relevant articles. Format: COUNTRY_CODE:language_code (e.g. US:en, GB:en, DE:de, FR:fr, JP:ja). Defaults to US:en (US  |
| `timeRange` | string; any, 1h, 1d, 7d, 30d, 1y | Filter articles by how recently they were published. Use '1h' for breaking news, '1d' for daily monitoring, '7d' for weekly digests. Defaults to 'any' (no time filter — returns all available articles). |
| `extractFullText` | boolean | When enabled, the actor visits each article page and extracts the full body text. Produces a full_text field and word_count field on each record. Ideal for AI/LLM pipelines, RAG (Retrieval-Augmented Generation), sentimen |
| `decodeUrls` | boolean | When enabled, attempts to resolve the real article URL (source_url) by following Google News redirect links. Note: Google News uses JavaScript-based URL encoding that cannot be fully resolved via HTTP redirects alone — s |
| `deduplicateResults` | boolean | When enabled (default), removes duplicate articles across queries and topics based on URL. Prevents the same article from appearing multiple times when it matches several search queries or topics simultaneously. Disable  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## reuters-news-scraper

Exact owner: `khadinakbar`. Identity: `OBza10QwXDnly48T3`. State: `public_schema_verified`.

Build `0.1.4` / `u7diyk8LB4K1twMpd`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/reuters-news-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `sections` | array | Reuters sections to pull from the public Google News sitemap (headline, publish time, image, tags, URL). Select one or more. Use "latest" for all English paths. reuters.com HTML is DataDome-blocked — this Actor returns s |
| `searchKeywords` | array | Optional case-insensitive keywords. Keep only articles whose headline, summary, or keywords contain at least one term (e.g. ['Fed','oil']). Leave empty to keep all items from selected sections. |
| `searchQuery` | string | Optional topic search via Bing News RSS filtered to reuters.com. Use when section sitemap browsing is too broad. Returns headline + snippet + URL. Leave empty to skip. |
| `articleUrls` | array | Optional list of reuters.com article URLs. Matched against the public news sitemap when possible; otherwise a URL-derived title/date row is returned. Does not scrape article HTML (DataDome) and does not return full body  |
| `languages` | array | Language/locale filter from the URL path. Default is English only (en). Add de/es/fr/pt for localized Reuters editions, or "all" to keep every locale present in the sitemap pages fetched. |
| `sinceHours` | integer; minimum=0 | Optional recency window. If set to e.g. 24, only articles with publishedAt within the last 24 hours are kept. Use 0 (default) for all currently returned sitemap/search items. |
| `maxItems` | integer; minimum=1; maximum=500 | Hard cap on articles scraped and billed across all sources. Each accepted article is one billable article-found event. Defaults to 50. Prefill 10 for cheap quality tests. |
| `maxSitemapPages` | integer; minimum=1; maximum=8 | How many Reuters news-sitemap pages to fetch (~50 URLs each, offset by 100). Default 4 (~200 candidate URLs before section/language filters). Raise only when maxItems is large. |
| `proxyConfiguration` | object | Optional Apify proxy. The public news sitemap and Bing News RSS usually work without a proxy. Enable only if your environment blocks outbound XML/RSS. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## financial-times-news-scraper

Exact owner: `khadinakbar`. Identity: `3pqzg1Y6WzZM4ceLY`. State: `public_schema_verified`.

Build `0.1.3` / `3zcfq86p6sMGX981j`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/financial-times-news-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `sections` | array | Financial Times public RSS sections to scrape (headlines, standfirsts, images, publish times). Select one or more. Defaults to International home + Markets. Returns public feed metadata — not full paywalled article body  |
| `searchKeywords` | array | Optional case-insensitive keywords. Keep only articles whose headline, standfirst, or keywords contain at least one term (e.g. ['Fed','oil']). Leave empty to keep all items from selected sections. |
| `searchQuery` | string | Optional topic search via Bing News RSS filtered to ft.com. Use this instead of FT site search (robots.txt disallows /search). Returns headline + snippet + URL. Leave empty to skip. |
| `articleUrls` | array | Optional list of ft.com /content/{uuid} URLs. Each URL is enriched from public Open Graph / meta tags only when HTML is reachable. Often blocked by Cloudflare without Residential proxy. Does not bypass the FT paywall or  |
| `sinceHours` | integer; minimum=0 | Optional recency window. If set to e.g. 24, only articles with publishedAt within the last 24 hours are kept. Use 0 (default) for all currently returned feed/search items. |
| `maxItems` | integer; minimum=1; maximum=500 | Hard cap on articles scraped and billed across all sources. Each accepted article is one billable article-found event. Defaults to 50. Set lower for cheap test runs. |
| `proxyConfiguration` | object | Optional Apify proxy. Official FT RSS feeds normally work without one. Enable Residential only if HTML URL enrich is Cloudflare-blocked. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## bloomberg-news-scraper

Exact owner: `khadinakbar`. Identity: `PdjMcLv1UDIkh4NEM`. State: `public_schema_verified`.

Build `0.1.10` / `LA00VjEbGcOlJuQrn`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/bloomberg-news-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `sections` | array | Bloomberg news sections to pull through a public news index (e.g. 'markets', 'technology', 'crypto'). Select one or more. Defaults to 'markets'. This returns recent indexed Bloomberg articles, not a search of the full ar |
| `searchKeywords` | array | Optional case-insensitive keywords to keep only articles whose headline or indexed summary contains at least one of them (e.g. ['AI','Fed','oil']). Leave empty to return all recent indexed articles in the selected sectio |
| `tickers` | array | Optional stock tickers to keep only articles whose headline or indexed summary mentions at least one symbol (e.g. ['AAPL','IREN','TSLA']). Leave empty to disable ticker filtering. |
| `sinceHours` | integer; minimum=0 | Optional recency window. If set to e.g. 24, only indexed articles published within the last 24 hours are returned. Use 0 (default) for all currently indexed results. |
| `maxItems` | integer; minimum=1; maximum=2000 | Hard cap on the number of articles scraped and billed across all selected sections. Each article counts as one billable result. Defaults to 100. Set lower for cheap test runs. |
| `proxyConfiguration` | object | Optional Apify proxy. The public news index normally works without one, so leave this off unless you hit a transient network block. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## sec-edgar-all-in-one-scraper

Exact owner: `khadinakbar`. Identity: `2Jte3UqcYwduMjhid`. State: `public_schema_verified`.

Build `0.2.7` / `1lOQfeND2N6stdCw9`; tag `latest`. Required keys: `query`. [Full dated input schema](../schemas/sec-edgar-all-in-one-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `query` | string | What to fetch. Accepts: stock ticker (e.g. 'AAPL', 'MSFT'), 10-digit CIK (e.g. '0000320193'), SEC accession number (e.g. '0000320193-25-000123'), full filing URL (e.g. 'https://www.sec.gov/Archives/edgar/data/320193/...' |
| `mode` | string; auto, company, filing, search, insider, holdings, activist, xbrl, form-d, recent | Override auto-detection. 'auto' = guess from query shape (recommended). 'company' = list filings for ticker/CIK. 'filing' = fetch one filing by accession/URL. 'search' = full-text keyword search across all filings. 'insi |
| `formTypes` | array | Filter results to specific SEC form types. Examples: ['10-K', '10-Q'] for annual + quarterly, ['8-K'] for current reports, ['4'] for Form 4 insider transactions. Leave empty for all forms. Applies to company, search, ins |
| `dateFrom` | string | Lower-bound filing date in YYYY-MM-DD format (e.g. '2024-01-01'). Filters to filings on or after this date. Leave empty for no lower bound. Applies to company, search, insider, holdings, recent modes. |
| `dateTo` | string | Upper-bound filing date in YYYY-MM-DD format (e.g. '2026-05-28'). Filters to filings on or before this date. Leave empty for no upper bound (defaults to today). Applies to company, search, insider, holdings, recent modes |
| `maxResults` | integer; minimum=1; maximum=10000 | Cap on total dataset items returned across all modes. Each item is one filing, XBRL fact, insider trade, 13F position, search hit, or feed entry — charged $0.005 each. Range 1-10000. Defaults to 100. |
| `includeFullText` | boolean | If true, fetches and includes the plain-text body of filings (HTML stripped) under `fullText` field. Increases run time and bandwidth substantially. Applies to filing and company modes when filings are fetched individual |
| `enableAiSummary` | boolean | If true, generates a structured AI summary per filing (key points, risks, financial highlights) using Gemini 2.5 Flash. Charged $0.03 per summary IN ADDITION to the $0.005 result fee. Applies to filing and company modes. |
| `xbrlConcept` | string | Specific XBRL concept to fetch in xbrl mode (e.g. 'Revenues', 'Assets', 'NetIncomeLoss', 'EarningsPerShareBasic'). Leave empty to fetch all available concepts for the company. Applies to xbrl mode only. Uses us-gaap taxo |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
