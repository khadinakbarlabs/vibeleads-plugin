# Local businesses source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [qualified business/contact-use gate](../contact-use.md). Provider result bounds are not recommended audience sizes; optional contact extraction must be disabled during discovery.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## google-maps-leads-scraper

Exact owner: `khadinakbar`. Identity: `9XVfT1vIqqL4fiS4q`. State: `public_schema_verified`.

Build `1.8.3` / `ZPuzdOapj4wKYPHBL`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/google-maps-leads-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | The local business type to find on Google Maps. Enter a plain-language category such as 'dentists', 'roofing contractors', or 'Italian restaurants'. Use it with Location for a focused territory search. This is not a Google Maps URL; use Start URLs for direct Maps pages. |
| `location` | string | The city, region, or country that limits the business search. Use a clear place such as 'Austin, TX' or 'London, UK'. It defaults to the location encoded in a direct Maps URL when Start URLs are used. It is not a radius or latitude-longitude field. |
| `startUrls` | array | One or more public Google Maps search or place URLs to process directly. Paste a URL such as 'https://www.google.com/maps/search/dentists+in+Austin'. When supplied, these URLs are processed alongside any category search. Do not provide website URLs here; use the category and location fields for discovery. |
| `maxResults` | integer; minimum=1; maximum=5000 | The maximum number of business lead records to return and bill as place-scraped events. The allowed range is 1 to 5000 and the actor stops once it reaches this limit. This is not a page count, because Maps result pages contain a variable number of businesses. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `enrichEmails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `requireEmail` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `requireWebsite` | boolean | Keep only businesses whose Google Maps listing includes a website URL. This is useful when the next workflow step needs a reachable domain for enrichment or audit. It defaults to false so listing-only local prospects can still be returned. It does not test whether the website is currently online. |
| `minLeadScore` | integer; minimum=0; maximum=100 | The minimum 0–100 contactability score a lead must have to be returned. For example, 70 prioritizes leads with several public contact signals while 0 keeps all records. It defaults to 0 and only filters after the complete lead record is assembled. This is not a prediction of purchase intent or a credit score. |
| `maxReviews` | integer; minimum=0; maximum=100 | The number of recent Google reviews to include for each returned business. Set 0 to omit review text and keep results compact. The allowed range is 0 to 100 and reviews do not change the lead score. This is not the total review count, which is always returned as review_count. |
| `language` | string; en, es, fr, de, it, pt, nl, pl, ru, ja, ko, zh-CN, ar, tr, hi | The Google Maps interface language used while collecting the listing. Select 'en' for English or another supported language such as 'es' or 'de'. It defaults to 'en' and can influence category and address text. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `minRating` | number; minimum=0; maximum=5 | The minimum 0–5 Google Maps rating a business must have before it is returned. For example, 4.2 filters out lower-rated listings while 0 includes all listings. It defaults to 0 and records with no rating do not pass a positive threshold. This is not a review-count filter or a measure of business quality. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-maps-extractor

Exact owner: `khadinakbar`. Identity: `c77y9zjyEMnlRbaZH`. State: `public_schema_verified`.

Build `1.0.5` / `Myp6EbsjRona75P5V`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/google-maps-extractor.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this when you want to search Google Maps by business type or keyword. Accepted format is plain text such as 'dentists' or 'coffee shops'. Defaults to 'dentists' when no URLs are provided. This is not a Google Maps URL; paste URLs into Google Maps URLs. |
| `location` | string | Use this when the search query needs a city, region, or country. Accepted format is 'Miami, FL', 'London, UK', or another natural Maps location. Defaults to 'Miami, FL' for health checks. Leave empty only when every Google Maps URL already contains the target area. |
| `startUrls` | array | Use this when you already have Google Maps search or place URLs. Accepted entries are objects with a url field, such as {'url':'https://www.google.com/maps/search/dentists+Miami'}. Defaults to an empty list. This is not for normal website URLs outside Google Maps. |
| `maxResults` | integer; minimum=1; maximum=2000 | Use this to cap how many Google Maps places are returned and charged. Defaults to 20. This is not a page-count setting; one result means one place record. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `minRating` | number; minimum=0; maximum=5 | Use this to keep only places at or above a Google rating threshold. Accepted values are 0 through 5, for example 4.2. Defaults to 0, which keeps unrated and rated places. This is not a review-count filter. |
| `skipClosedPlaces` | boolean | Use this to avoid businesses Google marks as permanently closed. Accepted value is true or false. Defaults to true for lead and market research freshness. This does not remove places that are only closed outside business hours. |
| `includeWebsiteContacts` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `language` | string; en, es, fr, de, it, pt, nl, pl, ru, ja, ko, zh-CN, ar, tr, hi | Use this to choose the Google Maps interface language for names, categories, and addresses. Accepted examples include 'en', 'es', 'fr', 'de', and 'ja'. Defaults to 'en'. This does not translate data after extraction. |
| `countryCode` | string | Accepted format is a two-letter ISO code such as 'US', 'GB', or 'DE'. Defaults to 'US'. This is not a location filter; use Location for the search area. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-maps-email-extractor

Exact owner: `khadinakbar`. Identity: `Kl05x3ga1ptGJ8IX8`. State: `public_schema_verified`.

Build `1.1.14` / `bKTlrvrqvv5aVBxqd`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/google-maps-email-extractor.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Business type or niche to search Google Maps for (e.g., 'dentists', 'real estate agents', 'plumbers'). Combined with the location below into a Google Maps query. Defaults to 'dentists'. NOT a Google Maps URL — paste a URL into the 'Google Maps URLs' field instead. |
| `location` | string | City, region, or country to search in (e.g., 'Miami, FL' or 'London, UK'). Simple 'City, Country' or 'City, State' formats work best. Defaults to 'Miami, FL'. Leave empty only if pasting a full Google Maps URL that already contains the area. |
| `maxResults` | integer; minimum=1; maximum=2000 | Maximum number of businesses to extract per search. Lower = faster and cheaper. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `skipWithoutEmail` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `minRating` | number; minimum=0; maximum=5 | Only include businesses with a Google rating >= this value (1.0 to 5.0). Set to 0 to include all businesses regardless of rating. Businesses with no rating are included when this is 0 and excluded otherwise. |
| `skipClosedPlaces` | boolean | Skip businesses marked as 'Permanently closed' on Google Maps. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `language` | string; en, es, fr, de, it, pt, nl, pl, ru, ja, ko, zh-CN, ar, tr, hi | Language code for the Google Maps interface — affects business names, categories, and addresses. Use 'en' for English, 'es' for Spanish, 'fr' for French, etc. Only affects Google Maps UI, not the email extraction step. |
| `startUrls` | array | Paste HTTPS Google Maps search or place URLs on google.com, www.google.com, or maps.google.com with a /maps path. Regional Google domains and shortlinks are not supported; expand them to a supported full URL first. Credentials and custom ports are rejected. Each URL replaces one keyword search. Leave empty if using keyword + city. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## yelp-scraper-all-in-one

Exact owner: `khadinakbar`. Identity: `LqTt06VgB01NP5ZOa`. State: `public_schema_verified`.

Build `1.9.7` / `JcwwZrXQ6mAkzdvEU`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/yelp-scraper-all-in-one.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this when the user provides a keyword, business type, or category (e.g. 'restaurants', 'dentists', 'coffee shops', 'auto repair'). Do NOT use this when the user provides specific Yelp URLs — use Start URLs for that instead. |
| `location` | string | City, state, ZIP code, or address to search in. Examples: 'New York, NY', 'Los Angeles, CA', '90210', 'Chicago Downtown'. Paired with Search Query. Ignored when Start URLs are provided. |
| `startUrls` | array | Use this when the user provides direct Yelp business page URLs (e.g. https://www.yelp.com/biz/joes-pizza-new-york). Do NOT use this for keyword searches — use Search Query instead. Accepts multiple URLs. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of businesses to scrape and return. Each business = 1 billable event at $0.003. Start with 10–50 to test before scaling. |
| `includeReviews` | boolean | Extract up to N recent user reviews per business. Each review contains: author name, star rating, date, and review text. Adds 1–2 seconds per business but significantly enriches the output. |
| `maxReviewsPerBusiness` | integer; minimum=1; maximum=20 | How many reviews to extract per business page (1–20). Only applies when Include Reviews is enabled. Reviews are returned newest-first as shown on Yelp. |
| `proxyType` | string; datacenter, residential, none | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## yellow-pages-us-scraper

Exact owner: `khadinakbar`. Identity: `LKAk6HaLHNFVSk6eo`. State: `public_schema_verified`.

Build `0.1.12` / `eiW41dJRZLK7ggN3T`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/yellow-pages-us-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchTerms` | string | Business type or name to search (e.g. "plumber", "pizza", "auto repair"). Combine with "location" for best results. |
| `location` | string | City, state, or ZIP code to narrow the search (e.g. "Los Angeles, CA", "90210"). Leave blank to search nationwide. |
| `startUrls` | array | Direct yellowpages.com search URLs or business profile URLs (/mip/...). Overrides searchTerms + location when provided. |
| `maxResults` | integer; minimum=1; maximum=5000 | Maximum number of business listings to return. Each result costs $0.005. |
| `maxPagesPerSearch` | integer; minimum=1; maximum=40 | Max search result pages to paginate through (~30 businesses/page). Increase for broader coverage. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## yellow-pages-uae-scraper

Exact owner: `khadinakbar`. Identity: `ZhcyPyawv0MsNJmht`. State: `public_schema_verified`.

Build `0.1.5` / `j2NfdZLbJ5nLryJvS`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/yellow-pages-uae-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `categories` | array | Business categories to scrape from yello.ae, as slugs or plain names (e.g. 'restaurants', 'estate-agents', 'doctors and clinics'). Each is resolved to a yello.ae category listing and paginated. Leave empty if you provide Start URLs instead. NOT a free-text keyword search - use a real directory category. |
| `city` | string; , dubai, abu-dhabi, sharjah, ajman, ras-al-khaimah, fujairah, umm-al-quwain, al-ain, jebel-ali-free-zone | Optional emirate or city to restrict category results to (applied as a yello.ae city filter). Pick one value; leave empty to scrape all of the UAE. Only applies to the Categories input above, not to direct company Start URLs. Example: 'dubai'. |
| `startUrls` | array | Direct yello.ae URLs to scrape, one per line: category pages (https://www.yello.ae/category/<slug>), location pages (https://www.yello.ae/location/<emirate>), or company pages (https://www.yello.ae/company/<id>/<slug>). Category and location URLs are paginated; company URLs are scraped directly. Use this for precise control. NOT for non-yello.ae domains. |
| `maxResults` | integer; minimum=1 | Maximum number of business records to return across the whole run (hard cap on billing). The run stops and finishes gracefully once this many businesses are scraped. Defaults to 1000; set lower for a quick test. Counts final business records, not intermediate listing pages. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## apple-maps-business-scraper

Exact owner: `khadinakbar`. Identity: `cvmZbYW6v9NUYbzsz`. State: `public_schema_verified`.

Build `0.1.7` / `G2qrILku3Afhlp0y7`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/apple-maps-business-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Business category or keyword to search on Apple Maps, such as coffee shops or dentists. Combine with location or latitude/longitude for best coverage. Prefer a short category phrase over a full sentence. This is Apple Maps search, not Google Maps — use google-maps-leads-scraper for Google. |
| `searchQueries` | array | Optional list of additional Apple Maps search keywords processed in the same run. Merged with searchQuery after dedupe. Use for related categories in one city (for example cafes and bakeries). Each unique place is still billed once. |
| `location` | string | City, region, or address text that centers the Apple Maps search, such as San Francisco, CA. Used with searchQuery when latitude/longitude are not set. Leave empty when providing exact coordinates or Apple Maps search URLs. Improves local NAP coverage for territory lists. |
| `latitude` | number | Optional map center latitude in decimal degrees. Pair with longitude for precise geocentering without relying on geocoded location text. When set with searchQuery, adaptiveGrid can expand nearby cells. Ignored for place URL lookups that already include coordinates. |
| `longitude` | number | Optional map center longitude in decimal degrees. Pair with latitude for precise geocentering. Use WGS84 values from Apple Maps share links or a known venue. Leave empty when location text or searchUrls already define the area. |
| `placeUrls` | array | Direct Apple Maps place links (maps.apple.com/place or place-id/auid query params). Each valid place is fetched and billed as place-scraped when persisted. Invalid non-Apple URLs are skipped with a warning. Prefer place URLs when you already have listing links. |
| `searchUrls` | array | Apple Maps search share URLs that include a query (and optional center/span). The Actor extracts the query and optional map center, then runs MapKit search. Place URLs pasted here are treated as place lookups. Non-Apple URLs are ignored. |
| `maxResults` | integer; minimum=1; maximum=500 | Hard cap on unique places saved after dedupe and filters. Defaults to 20. Prefill 5 keeps quality tests fast and cheap. Maximum 500. Each persisted place costs $0.004 as place-scraped. |
| `enrichEmails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `requireWebsite` | boolean | When true, keep only places that expose a website URL in the MapKit payload. Useful for outbound lists that need a domain before enrichment. Defaults to false so phone-only listings remain. Filtered-out places are not billed. |
| `requirePhone` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `adaptiveGrid` | boolean | When true and a map center is known, expand search across nearby grid cells to improve coverage for dense categories. Defaults to true. Disable for a single-point probe or when searchUrls already encode a tight span. Extra cells stop once maxResults is reached. |
| `language` | string | Locale for MapKit requests, such as en-US. Affects category and address language when Apple returns localized fields. Defaults to en-US. Use a BCP-47 style tag Apple Maps accepts for your market. |
| `countryCode` | string | ISO country hint for MapKit search, such as US. Helps disambiguate city names that exist in multiple countries. Defaults to US. Does not replace location or coordinates when those are set. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## yandex-maps-scraper

Exact owner: `khadinakbar`. Identity: `nvSVDwQpjExZEGdUn`. State: `public_schema_verified`.

Build `0.1.12` / `eD6PZ4QE2NIGNV8R6`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/yandex-maps-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Free-text search run on Yandex Maps, exactly as you would type it in the search box (e.g. 'coffee Moscow' or 'дантист Казань'). Combine a business type and a place for best results. Leave empty if you instead use category + city or startUrls. NOT a URL — paste URLs into 'Start URLs' instead. |
| `category` | string | Business type to search for, used together with 'City' when you do not supply a full search query (e.g. 'restaurant', 'gym', 'автосервис'). Combined internally as '<category> <city>'. Ignored if 'Search query' is set. Optional. |
| `city` | string | City or area to search within, paired with 'Category' (e.g. 'Saint Petersburg', 'Ankara'). Only used when 'Search query' is empty. Yandex auto-geocodes the place name. Optional. |
| `startUrls` | array | Yandex Maps URLs to scrape directly: a search-results URL (.../maps/?text=...) scrapes its listing, an organisation URL (.../maps/org/<id>/) scrapes that one business. Use this when you already have specific Yandex Maps links. Accepts the standard Apify URL list. Leave empty when using a search query. |
| `maxPlaces` | integer; minimum=1; maximum=1000 | Maximum number of unique businesses to return across all queries/URLs. Each place is billed once. Defaults to 50; range 1–1000. Yandex caps a single listing around a few hundred results, so very large targets need multiple narrower queries. |
| `includeReviews` | boolean | When enabled, each place also gets its visible Yandex reviews scraped (author, rating, text, date) and billed per review. Adds significant runtime, so keep it off for fast lead lists. Defaults to false. Use 'Max reviews per place' to cap volume. |
| `maxReviewsPerPlace` | integer; minimum=0; maximum=200 | Upper limit of reviews fetched per business when 'Include reviews' is on. Defaults to 20; range 0–200. Set to 0 to disable reviews even if the toggle is on. Ignored entirely when 'Include reviews' is off. |
| `language` | string; ru_RU, en_US, tr_TR | Yandex locale used for the search and for field text. 'ru_RU' uses yandex.ru (best coverage for Russia/CIS), 'en_US' uses yandex.com (English UI), 'tr_TR' uses yandex.com.tr (Turkey). Defaults to ru_RU. Does not translate review text — that stays in the original language. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## naver-map-scraper

Exact owner: `khadinakbar`. Identity: `fAkwN2B29fxeiIf7I`. State: `public_schema_verified`.

Build `0.1.23` / `PqxSc7d12TCpf3o6m`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/naver-map-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Free-text Naver Map searches, one place list per query (e.g. "강남 맛집", "홍대 카페", "Gangnam hair salon"). Korean queries return the richest results because Naver Map is a Korean service. Leave empty if you are using the Category + Location fields or Place URLs instead. This is NOT a place URL — put URLs in the Place URLs field. |
| `placeType` | string; restaurant, beauty | Which Naver category route to search. "restaurant" is the broadest and covers food, cafes, bakeries, bars, and desserts — use it for most keyword searches. Pick "beauty" for hair salons, nail, and skincare. Applies to Search queries and Category + Location; ignored for Place URLs. |
| `location` | string | A Korean area, district, or landmark to search within (e.g. "강남구", "제주도", "Seoul Hongdae"). Combined with the Category field and Place type into one Naver search. Leave empty if you already provide full Search queries. Example: "성수동". |
| `category` | string | A category or business keyword appended to Location, such as "카페", "치과", "pilates". Only used when Location is set. Leave empty to search the Location alone. Example: "치과". |
| `startUrls` | array | Direct Naver place URLs or numeric place IDs to look up individually (e.g. "https://m.place.naver.com/restaurant/1188590985/home" or "1188590985"). Each returns one place record with best-effort menu/detail enrichment. Use this for single-place lookups; use Search queries for discovery. naver.me short links cannot be resolved — paste the expanded URL. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxPlaces` | integer; minimum=1; maximum=2000 | Hard cap on total places scraped (and billed) across all queries and URLs in this run. Prevents runaway cost. Defaults to 100; maximum 2000. One Naver keyword search server-renders roughly 50-70 places. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## gelbe-seiten-scraper

Exact owner: `khadinakbar`. Identity: `Mm0GVaQ4tzorXYpIO`. State: `public_schema_verified`.

Build `1.0.5` / `XYPkG3yTaQ7UZnvbQ`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/gelbe-seiten-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searches` | array | Business-type and location pairs to search on Gelbe Seiten. Example: [{"query":"Zahnarzt","location":"Berlin"}]. Defaults to a Berlin dentist search. This is not a list of URLs; use Gelbe Seiten URLs for an existing results or business page. |
| `startUrls` | array | Existing Gelbe Seiten search-result or business-detail URLs. Example: https://www.gelbeseiten.de/branchen/zahnarzt/berlin. Use this to preserve a search URL's filters; URLs outside gelbeseiten.de are rejected. |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum unique business records to return across every input. Example: 50. Defaults to 50 and accepts 1 through 500. This is a business-row cap, not a page count, and it also caps billable business-found events. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## bbb-scraper

Exact owner: `khadinakbar`. Identity: `Ieo7Fq8mBluwRqGGA`. State: `public_schema_verified`.

Build `0.1.6` / `GfZxpr8eagYAGW9cq`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/bbb-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchKeyword` | string | Business type or name to search on bbb.org, e.g. 'plumber', 'hvac contractor', or a company name. Combine with 'location' to scope by city. Leave empty if you instead pass profile URLs in 'startUrls'. NOT a URL — for a single known business use 'startUrls'. |
| `location` | string | Geographic area to scope the search, formatted as 'City, ST' for the US or 'City, Province' for Canada, e.g. 'Los Angeles, CA'. Optional — omit for a nationwide search. Ignored when only profile 'startUrls' are provided. NOT a ZIP code on its own. |
| `country` | string; US, CA | Country directory to search: US (bbb.org USA) or CA (Canada). Defaults to US. Does not affect direct profile 'startUrls', which already encode their country. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `startUrls` | array | Direct bbb.org business profile URLs to scrape in depth, e.g. https://www.bbb.org/us/ca/los-angeles/profile/plumber/example-1216-907682 . Use instead of, or alongside, a keyword search. NOT search or category URLs — only '/profile/' pages are scraped here. |
| `maxResults` | integer; minimum=1; maximum=5000 | Maximum number of businesses to return across the whole run. Defaults to 100. A single keyword+location search caps at 225 results on bbb.org; raise this and add more locations to collect more. Controls cost — you are billed per returned business. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `minRating` | string; Any, A+, A, B, C, D, F | Only return businesses with at least this BBB letter rating (A+ is highest, F lowest). Defaults to 'Any' (no filter). Businesses with no published rating are excluded when a minimum is set. Applied after scraping each business. |
| `accreditedOnly` | boolean | When true, return only BBB-Accredited businesses and skip the rest. Defaults to false (return all). Useful for lead lists that require accreditation. Applied after each business is scraped. |
| `storeRawSample` | boolean | Developer/debug option. When true, the first search and profile page's raw embedded JSON is saved to the key-value store for inspection. Defaults to false. Leave off for normal runs — it does not change the dataset output. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## houzz-scraper

Exact owner: `khadinakbar`. Identity: `iEvCUyjKXa3tCUGe2`. State: `public_schema_verified`.

Build `0.1.15` / `JUJJembpofHSbb3gq`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/houzz-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `category` | string | The Houzz professional type to search, e.g. 'general contractor', 'interior designer', 'kitchen and bathroom remodeler', 'architect', 'landscape architect'. Free text — slugified automatically to the Houzz directory. Leave blank only if you pass startUrls instead. |
| `location` | string | City and state/region to filter professionals, e.g. 'New York, NY' or 'Austin, TX'. Encoded to Houzz's 'City--ST' URL form automatically. Leave blank for a nationwide search. Ignored when startUrls are supplied. |
| `startUrls` | array | Optional list of exact Houzz URLs to scrape directly: professional directory listings (/professionals/...) or individual pro profiles (/professionals/...-pfvwus-pf~ID). When provided, these override category/location. Accepts plain strings or {"url": "..."} objects. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxResults` | integer; minimum=1; maximum=2000 | Hard cap on the number of professionals pushed (and charged) in one run. Range 1-2000, default 50. The run stops and never charges beyond this number. Use a small value first to preview output and cost. |
| `proxyCountry` | string | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `maxRequestRetries` | integer; minimum=1; maximum=15 | Range 1-15. Higher values raise reliability but also compute cost on hard blocks. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## checkatrade-scraper

Exact owner: `khadinakbar`. Identity: `NDA7wKRcFeIfwfdjz`. State: `public_schema_verified`.

Build `1.4.2` / `tw6z8KVCVAaUX8yZ4`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/checkatrade-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `trade` | string | The Checkatrade trade to find, such as 'Plumber' or 'Electrician'. Pair it with a UK location to create a Checkatrade search URL. Defaults to 'Plumber'. This is not a profile URL; use directUrls for existing profiles. |
| `location` | string | The UK town, city, postcode, or postcode area to search, such as 'London' or 'SW1A'. Combined with trade unless searchUrls is supplied. Defaults to 'London'. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `searchUrls` | array | Optional Checkatrade search-result URLs copied from a browser, for example 'https://www.checkatrade.com/Search/Plumber/in/London'. Each URL is crawled and paginated. Leave empty to use trade and location. Do not paste profile URLs here; put those in directUrls. |
| `directUrls` | array | Optional individual Checkatrade tradesperson profile URLs, such as 'https://www.checkatrade.com/trades/exampleltd'. Each is scraped directly and bypasses search discovery. Leave empty for a trade/location search. Do not include URLs from other directories. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum validated tradesperson records to return across the entire run. Each persisted record is one billable tradesperson event. Defaults to 100 and accepts 1 through 1000. This is not a page limit because one page can contain multiple profiles. |
| `scrapeDetails` | boolean | Keep explicitly disabled during company discovery. Detailed profile/contact expansion is available only for named qualified businesses under the contact-use gate. Direct profile inputs that always expand details are unavailable for broad discovery; verify actual build controls or decline that route. |
| `extractReviews` | boolean | Include up to ten visible recent review objects for each returned profile. This adds review body, author when public, rating, and date when available. Defaults to false to keep items compact. This does not claim to return a profile's complete review history. |
| `requirePhone` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `minRating` | number; minimum=0; maximum=10 | Minimum public Checkatrade rating from 0 to 10. Profiles without a rating or below this threshold are excluded when a value above zero is used. Defaults to 0. This is not a star rating out of five. |
| `minReviews` | integer; minimum=0; maximum=100000 | Minimum number of public reviews a profile must show before it is returned. Profiles without enough reviews are excluded when this is above zero. Defaults to 0. This is a filter, not the number of review objects to extract. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## angi-home-services-scraper

Exact owner: `khadinakbar`. Identity: `Q8bDbhf70u3tFVEkz`. State: `public_schema_verified`.

Build `0.1.6` / `wL9IRrlHdqQbK8Elb`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/angi-home-services-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `category` | string | Angi trade slug used in companylist URLs, for example plumbing, electrical, hvac, or roofing. Pair with city and state, or with zipCodes. Ignored when startUrls alone drive the run. NOT a free-text Google query. |
| `city` | string | US city for the Angi directory page, for example austin or New York. Requires state. Prefer this over ZIP for accurate companylist URLs. Ignored when only profile startUrls are supplied. |
| `state` | string | Two-letter US state code, for example tx, ca, or ny. Required with city. Case-insensitive. |
| `zipCodes` | array | Optional US 5-digit ZIPs. Each ZIP is resolved to a city/state listing URL when category is set. Angi ZIP query params are often non-filtering — city slug remains authoritative. |
| `startUrls` | array | Direct angi.com companylist pages and/or business profile URLs (/business/..., companyreviews.htm?spid=, or *-reviews-{id}.htm). Overrides structured search when present. Non-angi URLs are ignored. |
| `maxResults` | integer; minimum=1; maximum=2000 | Cap on unique billed provider rows for the run. Default 100. Prefill 3 keeps quality checks fast and cheap. You are billed per persisted provider. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `includeReviews` | boolean | Attach up to maxReviewsPerProvider public review excerpts when Angi exposes them. Not a full review archive. Default false. |
| `maxReviewsPerProvider` | integer; minimum=0; maximum=25 | Maximum review excerpts to attach when includeReviews is true. Default 5. |
| `minRating` | number; minimum=0; maximum=5 | Skip providers below this average star rating (0–5). Default 0 (no filter). Providers with no published rating are excluded when a minimum is set. |
| `requirePhone` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxPagesPerListing` | integer; minimum=1; maximum=50 | Maximum companylist pages to paginate per seed URL. Default 5. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `storeRawSample` | boolean | Developer/debug option. Saves the first listing and profile HTML plus __NEXT_DATA__ to the key-value store. Leave off for normal runs. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-local-services-ads-scraper

Exact owner: `khadinakbar`. Identity: `x5gKZkXwagh1WR6sK`. State: `public_schema_verified`.

Build `1.7.6` / `ahqoUcbXeNxgyoQsp`; tag `latest`. Required keys: `queries`, `locationName`, `dataCid`. [Full dated input schema](../schemas/google-local-services-ads-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | One to ten supported Local Services category queries, for example ["electrician", "plumber"]. Enter the service only; set the market separately with locationName and dataCid. Each completed category and city-CID request is billed once. |
| `locationName` | string | Caller-provided readable label for the same United States city or district represented by dataCid, for example "Austin, Texas, United States". dataCid is the authoritative provider market selector; this matching label is carried into every output record for CRM and agent workflows. |
| `dataCid` | string | Required decimal Google CID for the requested city or district, not a business CID or a Google Place ID. Use it exactly as a string to preserve all digits. Example: Austin, Texas is "6745062158417646970". The Actor validates it so it never substitutes a different market. |
| `maxResults` | integer; minimum=1; maximum=20 | Maximum public advertiser records to save for each category query. The dedicated source can return up to 20 cards per category; this cap controls dataset size, not the number of billed category queries. |
| `languageCode` | string | Two-to-five-letter Google interface language code, such as "en" or "es". It defaults to en and is included in the provider request. |
| `countryCode` | string; us | The dedicated Google Local Services provider source currently supports United States city and district CIDs. Keep this set to us. |
| `jobType` | string | Optional supported Local Services job-type identifier, for example "restore_power" with electrician. Leave blank to collect the category-level advertiser list. The same job type applies to all queries in this run. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-local-pack-api

Exact owner: `khadinakbar`. Identity: `YpwdWR0SnyI3jTWx6`. State: `public_schema_verified`.

Build `0.2.3` / `F9orP0ImyrO1kBlMr`; tag `latest`. Required keys: `queries`, `locations`. [Full dated input schema](../schemas/google-local-pack-api.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array; minItems=1; maxItems=100 | Local-intent searches to snapshot, such as ['dentist near me', 'emergency dentist']. Each query runs at every supplied location. Provide 1–100 non-empty queries; this Actor does not generate keywords. |
| `locations` | array; minItems=1; maxItems=25 | Each location must specify exactly one of locationCode, locationName, or locationCoordinate. Coordinates are best for a precise neighborhood snapshot and must be latitude,longitude,radius in metres. Maximum 25 locations and 500 total query/location snapshots per run. |
| `languageCode` | string | the keyword-data API Google language code, e.g. en or es. Defaults to en; it controls the SERP language, not the location. |
| `device` | string; desktop, mobile | Google result layout to request. Local-pack appearance can vary by device. |
| `seDomain` | string | Optional Google domain such as google.com, google.co.uk, or google.de. Leave blank to let the keyword-data API choose a domain for the selected language and location. |
| `maxLocalPackResults` | integer; minimum=1; maximum=20 | Maximum local-pack businesses to return from each Google SERP block. Defaults to 3 to match the common local 3-pack; use up to 20 only when the provider returns more businesses in the local-pack block. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## 2gis-places-scraper

Exact owner: `khadinakbar`. Identity: `s12YodiOzxwNenTJ6`. State: `public_metadata_unavailable`.

Live metadata/schema unavailable at inspection. Treat as a coverage gap until a fresh read verifies it; do not run from assumptions.
