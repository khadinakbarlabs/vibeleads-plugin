# Suppliers and tenders source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## alibaba-listings-scraper

Exact owner: `khadinakbar`. Identity: `15WbTOWces7c1L664`. State: `public_schema_verified`.

Build `1.2.5` / `fGTnSVTOsR7B3fZtR`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/alibaba-listings-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Free-text keyword to search Alibaba B2B products (e.g. 'wireless earbuds'). The Actor opens the Alibaba search-results page and collects every product listing card across pages. Leave empty if you instead provide startUrls. NOT a single product URL — this Actor searches and returns many products, it does not scrape one product-detail page. |
| `startUrls` | array | Optional list of Alibaba search or category URLs to scrape directly (e.g. https://www.alibaba.com/trade/search?SearchText=led+strip or a /catalog/ URL). Use this instead of, or together with, searchQuery. Product-detail URLs (/product-detail/...) and non-Alibaba URLs are ignored — this Actor only scrapes search/category result pages. |
| `maxResults` | integer; minimum=1; maximum=10000 | Maximum number of product records to return. The Actor auto-paginates until this cap is reached, then stops, so it doubles as your cost ceiling (each product is one billable event). Defaults to 100. Set higher for bulk sourcing research. |
| `sortBy` | string; relevance, transactionDesc, responseRate, priceAsc, priceDesc, newest | Order in which Alibaba returns the search results. 'relevance' is Alibaba Best Match (default); 'transactionDesc' surfaces high-transaction suppliers; 'responseRate' surfaces fast-responding suppliers; 'priceAsc'/'priceDesc' sort by price; 'newest' shows recently listed items. Applies to keyword searches; for startUrls the URL's own sort is respected. |
| `minPrice` | integer; minimum=0 | Only return products whose unit price (minimum of the price range) is at or above this value in USD. Applied as an Alibaba URL filter and as a safety re-check on the parsed price. Leave empty for no minimum. |
| `maxPrice` | integer; minimum=0 | Only return products whose unit price (maximum of the price range) is at or below this value in USD. Applied as an Alibaba URL filter and as a safety re-check on the parsed price. Leave empty for no maximum. |
| `minMoq` | integer; minimum=1 | Server-side MOQ floor passed to Alibaba's search URL. Combine with maxMoq to bracket a target MOQ window. Leave empty for no MOQ lower bound. |
| `maxMoq` | integer; minimum=1 | Drop products whose minimum order quantity (MOQ) is above this value (e.g. 100 keeps only products requiring up to 100 pieces minimum). Useful for small-volume sourcing. Applied client-side after extraction; products with unknown MOQ are dropped when this bound is set. Leave empty for no upper bound. |
| `verifiedOnly` | boolean | When enabled, keep only products from Verified or Gold Suppliers (Alibaba's supplier vetting tiers). Filtered products are not billed. Default false. |
| `tradeAssuranceOnly` | boolean | When enabled, keep only products offering Alibaba Trade Assurance (escrow + dispute protection). Filtered products are not billed. Default false. |
| `minSupplierYears` | integer; minimum=0 | Drop products from suppliers with fewer than this many years on Alibaba (e.g. 3 keeps suppliers with 3+ years). Useful to skip brand-new sellers. Products with unknown years are dropped when this bound is set. Filtered products are not billed. Leave empty to keep all. |
| `supplierCountries` | array | Optional whitelist of supplier countries as ISO-3166 alpha-2 codes (e.g. ['CN','VN','IN','PK']). Only products whose supplier is based in one of these countries are kept. Products with unknown supplier country are dropped when this filter is set. Leave empty to allow all countries. |
| `minRating` | integer; minimum=0; maximum=5 | Drop products whose supplier average rating (0–5) is below this value, or whose rating is unknown. Useful to keep only well-reviewed suppliers. Filtered products are not billed. Leave empty to keep all ratings. |
| `minOrders` | integer; minimum=0 | Drop products with fewer than this many recorded orders/transactions, or with unknown order count. Useful to surface proven listings. Filtered products are not billed. Leave empty to keep all. |
| `site` | string; www.alibaba.com | Which Alibaba domain to search. Defaults to the global English site 'www.alibaba.com'. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## thomasnet-suppliers-scraper

Exact owner: `khadinakbar`. Identity: `ZAoqDpC01eOCZ8KdQ`. State: `public_schema_verified`.

Build `1.1.12` / `svfxxkbPDKmcRg9at`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/thomasnet-suppliers-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Free-text searches run on ThomasNet's nsearch (e.g. 'cnc machining', 'sheet metal fabrication', 'plastic injection molding'). Each keyword is searched separately across the entire North America directory and paginated up to maxPagesPerQuery. Use this for product/service-led supplier discovery. NOT a URL — to scrape a specific category, state, or city page use startUrls instead. |
| `startUrls` | array | Direct ThomasNet URLs. Supported: (1) nsearch results URLs — e.g. https://www.thomasnet.com/nsearch.html?cov=NA&searchterm=cnc%20machining (paginated like a search); (2) supplier profile URLs — e.g. https://www.thomasnet.com/company/fruehauf-manufacturing-30088334/profile (scraped as one enriched supplier). NOT supported: /products-suppliers/ or /suppliers/usa/{state} directory URLs (these are subcategory hubs, not supplier listings — use searchQueries with a keyword instead). |
| `maxResults` | integer; minimum=1; maximum=5000 | Hard cap on the total number of suppliers scraped and billed across all queries and URLs. The run stops once this is reached. Defaults to 20; max 5000. Primary cost control — at $0.005/supplier basic, 20 suppliers is about $0.10. With enrichDetails on, double the cost estimate. |
| `maxPagesPerQuery` | integer; minimum=1; maximum=50 | How many listing pages (about 20-30 suppliers each) to paginate through for each keyword or listing URL before moving on. Defaults to 5; max 50. Lower it to sample top results; raise it for deep coverage. Bounded again by maxResults. |
| `enrichDetails` | boolean | When true, every listing supplier is followed to its own ThomasNet profile to add full description, employee count, year founded, annual sales, certifications, products taxonomy, and additional contact details. Slower and costs an extra $0.003 per enriched supplier on top of the base $0.005. Leave false for fast listing-level data (name, phone, website, location, headline) only. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## importyeti-scraper

Exact owner: `khadinakbar`. Identity: `LdxFVnIbSOX7MCEP3`. State: `public_schema_verified`.

Build `0.2.9` / `WYAaetQfWu6YzZVME`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/importyeti-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Free-text company names or product keywords (e.g., 'Patagonia', 'YETI Coolers', 'phone case', 'lithium battery'). Each query is sent to the ImportYeti search API and paginated up to maxResultsPerQuery records. Leave empty if you only have direct profile URLs. |
| `startUrls` | array | Direct ImportYeti profile URLs (https://www.importyeti.com/company/{slug} or https://www.importyeti.com/supplier/{slug}). Each URL is resolved to a single matching record via the search API. NOT a search-results URL — use the canonical profile URL. |
| `maxResultsPerQuery` | integer; minimum=1; maximum=500 | Maximum profiles to return per searchQueries entry. The API returns 10 results per page; the actor paginates internally until this cap is hit or no more pages are available. Bounded 1–500. Default 10. Each pushed profile is billed at the per-profile event price. |
| `countryCode` | string | Optional ISO-3166-1 alpha-2 country code (e.g., 'US', 'CN', 'VN') to restrict results to that country. Applied after fetching — filters out profiles registered in other countries. Leave empty for no country filter. |
| `typeFilter` | string; both, company, supplier | Restrict results to US importers ('company') only, foreign suppliers ('supplier') only, or return both ('both'). Default 'both'. |
| `minShipments` | integer; minimum=0 | Drop records with fewer than this number of total bills-of-lading on file. Use to filter out inactive or tiny companies. Default 0 (no filter). |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## sam-gov-scraper

Exact owner: `khadinakbar`. Identity: `SZC3tSm0Rhoc9KRzO`. State: `public_schema_verified`.

Build `1.0.10` / `A3pyMQQMBWtQe3RrS`; tag `latest`. Required keys: `query`. [Full dated input schema](../schemas/sam-gov-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `query` | string | Use this to search words in the SAM.gov opportunity title, for example cybersecurity or cloud migration. It defaults to no keyword so filters can return all matching opportunities. This is not a full-text search of attached solicitation documents. |
| `noticeTypes` | array | Use this to limit results to published SAM.gov notice-type codes. Select values such as o for Solicitation, k for Combined Synopsis/Solicitation, r for Sources Sought, or a for Award Notice. It defaults to all supported types. This is not a contract award category. |
| `naicsCode` | string | Use this to filter opportunities by one 2-to-6-digit NAICS industry code, for example 541512. It is optional and the official API accepts one code per request. This is not a PSC or a free-text industry name. |
| `setAsideCode` | string | Use this to filter by one SAM.gov set-aside code, for example SBA, 8A, HZC, or SDVOSBC. It is optional and should use the official short code. This is not a description such as 'small business'. |
| `state` | string | Use this to filter the work location by a two-letter state or territory code, for example VA. It is optional and maps to SAM.gov's place-of-performance filter. This is not the contracting agency's state. |
| `agency` | string | Use this to filter by the SAM.gov organization name, for example Department of Defense. It is optional and supports the official organization-name field. This is not a contracting officer's name. |
| `postedFrom` | string | Use this to set the first posted date as YYYY-MM-DD or MM/DD/YYYY, for example 2026-07-01. It defaults to 30 days ago and SAM.gov permits at most one year per search. This is not a response deadline. |
| `postedTo` | string | Use this to set the last posted date as YYYY-MM-DD or MM/DD/YYYY, for example 2026-07-19. It defaults to today and must not precede posted from. This is not an archive date. |
| `responseDueFrom` | string | Use this with response deadline to include only opportunities whose response date is on or after this date. Use YYYY-MM-DD or MM/DD/YYYY, for example 2026-07-20. Both deadline fields are required together. This is not a posted-date filter. |
| `responseDueTo` | string | Use this with response deadline from to include only opportunities whose response date is on or before this date. Use YYYY-MM-DD or MM/DD/YYYY, for example 2026-08-31. Both deadline fields are required together. This is not an award date. |
| `maxResults` | integer; minimum=1; maximum=10000 | Use this to cap validated SAM.gov opportunity records written to the dataset. Enter an integer from 1 through 10000, for example 100. It defaults to 100 and prevents charges beyond this number of returned opportunities. This is not an API page count. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## scrape-public-tenders

Exact owner: `khadinakbar`. Identity: `ByVZasVU6zOzCqXG5`. State: `public_schema_verified`.

Build `0.1.3` / `z3Z5rLL61AYILOyyS`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/scrape-public-tenders.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `keyword` | string | Free-text query matched against notice titles and descriptions, for example 'software' or 'school catering'. TED uses expert FT~ search; UK Contracts Finder uses its keyword index. Leave empty to browse the date window only. This is not a CPV code — put codes in cpvCodes. |
| `sources` | array | Which official registers to query. ted is EU Tenders Electronic Daily. uk-contracts-finder is below-threshold UK notices. uk-find-a-tender is above-threshold UK notices. Default all three. This is not SAM.gov — use sam-gov-scraper for US federal RFPs. |
| `countries` | array | ISO 3166-1 alpha-3 buyer countries for TED only, for example DEU or FRA. Leave empty for all TED countries. UK sources always stay GBR. Do not pass two-letter codes such as DE. |
| `cpvCodes` | array | Common Procurement Vocabulary codes, 2-8 digits, for example 72000000 for IT services. TED prefix-matches so 72 also covers 72000000 children. Leave empty for every sector. This is not a keyword. |
| `statusFilter` | string; open, awarded, all | Which procurement stage to keep. open (default) is active TED notices and Open UK Contracts Finder tenders. awarded is TED contract-award notices and Awarded UK rows. all includes planning. This is not a bid-win probability. |
| `datePreset` | string; last_24_hours, last_7_days, last_30_days, custom | Publication-date window applied to TED, Contracts Finder, and Find a Tender. last_7_days is the default quality sample. Choose custom only when publishedFrom is set. This is publication date, not bid deadline. |
| `publishedFrom` | string | Inclusive publication start date as YYYY-MM-DD, for example 2026-09-01. Used only when datePreset is custom. Ignored for last_7_days and other presets. |
| `publishedTo` | string | Inclusive publication end date as YYYY-MM-DD, for example 2026-09-17. Used only when datePreset is custom. Defaults to today when omitted. |
| `expertQuery` | string | Native TED expert-search expression, for example buyer-country=DEU AND classification-cpv=72000000*. When set, it replaces the TED keyword/country/CPV/date query. Leave empty for normal use. UK sources ignore this field. |
| `maxResults` | integer; minimum=1; maximum=250 | Hard cap on billed dataset rows for the whole run. Default 25. Prefill 5 keeps the quality sample cheap: each saved notice is one $0.005 tender-found event. This is not a page number. |
| `language` | string | TED language code for localized title and buyer fields, default ENG. Falls back to English then the first available translation. UK notices stay English. This is not a country filter. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
