# Ecommerce sellers source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

## shopify-all-in-one-scraper

Exact owner: `khadinakbar`. Identity: `pOI3iJZfm6l7C6xPD`. State: `public_schema_verified`.

Build `1.1.4` / `4pgXeXgzx9YGFiuSy`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/shopify-all-in-one-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `storeUrls` | array | Use this field when the user provides a Shopify store URL or domain name. Accepts full URLs (https://gymshark.com) or bare domains (gymshark.com). Add multiple stores for batch scraping. Use this for specific known store |
| `scrapeProducts` | boolean | Use this when the user wants product data: titles, prices, discounts, variants, stock status, images, SKUs, or barcodes. Enables product extraction from /products.json. Charged at $0.003 per product. |
| `scrapeCollections` | boolean | Use this when the user wants product categories, collections, or store taxonomy. Extracts all collection handles, titles, descriptions, and product counts from /collections.json. Charged at $0.001 per collection. |
| `scrapeReviews` | boolean | Use this when the user wants customer reviews, star ratings, verified buyer status, or review text. Auto-detects review platform (Judge.me, Yotpo). Each review is charged separately at $0.001. Use maxReviewsPerProduct to |
| `scrapeContactInfo` | boolean | Use this when the user wants merchant emails, phone numbers, or social media links for B2B outreach, lead generation, or sales prospecting. Extracts live contact data from the store's pages. Charged at $0.005 per store ( |
| `maxProductsPerStore` | integer; minimum=1 | Maximum number of products to extract from each store. Default 50 for quick tests; use higher values for full catalog extraction. |
| `maxCollectionsPerStore` | integer; minimum=1 | Maximum number of collections to extract from each store when scrapeCollections is enabled. Default 250 for most stores; large fashion/home stores may have thousands. |
| `maxReviewsPerProduct` | integer; minimum=1 | Maximum reviews to fetch per product when scrapeReviews is enabled. Applies per product, not total. Start with 50 for a sample; use higher values for full sentiment analysis. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## ecommerce-store-scraper

Exact owner: `khadinakbar`. Identity: `43imkJ5nkiEbP4281`. State: `public_schema_verified`.

Build `1.0.21` / `8dDNoge0ejeq187ma`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/ecommerce-store-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | One or more ecommerce URLs to scrape. Paste a store homepage (e.g. 'https://allbirds.com') to crawl its entire catalog, or paste individual product page URLs for targeted extraction. Supports Shopify, WooCommerce, and ge |
| `maxProducts` | integer; minimum=1; maximum=10000 | Upper limit on the number of products returned in this run. Accepts integers from 1 to 10000. Defaults to 50. Each product counts as one billable 'product-scraped' event at $0.003. Set high for full catalog extraction. |
| `includeVariants` | boolean | If true, every product record includes a 'variants' array with individual size/color/style entries, each with its own price, SKU, and availability. If false, the 'variants' array is always empty. Defaults to true. Does N |
| `includeDescription` | boolean | If true, every record includes the full product description text (HTML stripped to plain text). If false, the 'description' field is set to null. Defaults to true. Disable this for smaller payloads when you only care abo |
| `proxyConfiguration` | object | Advanced: Apify proxy configuration. Leave as default unless you have a specific proxy requirement. Residential proxies are enabled by default for best compatibility with anti-bot systems. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## woocommerce-product-scraper

Exact owner: `khadinakbar`. Identity: `wNKFSEi4wb1iXE87g`. State: `public_schema_verified`.

Build `0.1.6` / `hMlwcz7bayZY1t0UQ`; tag `latest`. Required keys: `storeUrls`. [Full dated input schema](../schemas/woocommerce-product-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `storeUrls` | array | Use this when you need a public WooCommerce store catalog, such as 'https://porterandyork.com'. Add a homepage URL or a store installed in a subdirectory, and the actor calls its public Store API. The actor extracts publ |
| `maxProducts` | integer; minimum=1; maximum=10000 | Use this to set one hard product cap across every requested store, such as 100. It accepts whole numbers from 1 through 10,000 and defaults to 100. Billing and Store API pagination stop after this many validated product  |
| `search` | string | Use this to ask the WooCommerce Store API for products matching a text phrase, such as 'organic coffee'. It accepts up to 200 characters and is empty by default, which returns the full catalog. Store search behavior is s |
| `categoryIds` | array | Use this to limit output to public WooCommerce category IDs, for example [12, 27]. It accepts positive numeric IDs and defaults to an empty list, which applies no category filter. IDs are store-specific, so obtain them f |
| `stockStatuses` | array | Use this to return products in one or more public stock states, such as 'instock'. It accepts instock, outofstock, and onbackorder and defaults to an empty list, which applies no stock filter. Multiple values are sent to |
| `onSale` | boolean | Use this when you need only products that the public Store API marks as on sale. Set true to apply the filter; false is the default and leaves the catalog unfiltered by sale status. The value is sent directly to the Stor |
| `featured` | boolean | Use this when you need only catalog items that WooCommerce marks as featured. Set true to apply the filter; false is the default and leaves the catalog unfiltered by featured status. The flag is read from the public Stor |
| `sortBy` | string; date, price, popularity, rating | Use this to choose the Store API sorting field, for example price. It accepts date, price, popularity, or rating and defaults to date. Set sortOrder separately to choose ascending or descending results. It does not sort  |
| `sortOrder` | string; asc, desc | Use this to choose ascending or descending order for the selected Store API sort field. It accepts asc or desc and defaults to desc. The setting applies to the target API before pagination begins. It is not a way to orde |
| `proxyConfiguration` | object | Use this only if a public Store API blocks the default direct request path. Set useApifyProxy to true and optionally choose a proxy group or two-letter country code. It defaults to direct HTTP requests because the public |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## amazon-seller-scraper

Exact owner: `khadinakbar`. Identity: `vzyaCFYKCjXkDp7DK`. State: `public_schema_verified`.

Build `0.3.5` / `2nbUhta2xJ0UP8ynO`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/amazon-seller-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `sellerIds` | array | Amazon seller (merchant) IDs, 13–14 uppercase chars, e.g. ['A1ODG4ICFE5MU3','AN9M05X8SIK1X']. Each is resolved on the selected marketplace's /sp?seller= profile page. NOT an ASIN (10 chars) — for products use 'asins'. NO |
| `startUrls` | array | Amazon URLs to scrape: seller profile ('/sp?seller=ID'), storefront ('/s?me=ID'), or product ('/dp/ASIN') pages. Product URLs are resolved to the seller(s) in their buy box. The domain in each URL overrides the 'country' |
| `asins` | array | Product ASINs (10 chars, e.g. ['B007ADJ4JI']) whose third-party seller(s) you want to find. The actor opens each product, reads the 'Sold by' seller(s), then scrapes their profile. NOT a seller ID (13–14 chars) — for sel |
| `country` | string; US, UK, DE, FR, CA, ES, IT, JP, AU, IN, MX, BR, NL, SE, PL, TR, AE, SG | Which Amazon marketplace to use for sellerIds and asins. Ignored when a startUrl already contains a specific Amazon domain. Defaults to US (amazon.com). |
| `includeFeedback` | boolean | When true, the seller record includes a 'recentFeedback' array of the most recent buyer comments rendered on the profile (rating, comment, author, date). Turn off for a leaner record focused on business details and ratin |
| `maxFeedback` | integer; minimum=0; maximum=100 | Maximum recent feedback comments to capture per seller (only the comments rendered on the profile page; Amazon shows ~5–10 without pagination). Ignored when 'includeFeedback' is off. |
| `includeStorefrontProducts` | boolean | When true, the actor also opens the seller's storefront ('/s?me=ID') and lists their products into a 'products' array on the seller record. Each product is billed at $0.003. Adds time and cost — leave off if you only nee |
| `maxStorefrontProducts` | integer; minimum=1; maximum=2000 | Maximum products to list from each seller's storefront. Only applies when 'includeStorefrontProducts' is on. Each product returned is billed as one 'storefront-product' event. |
| `maxStorefrontPages` | integer; minimum=1; maximum=20 | Maximum storefront result pages to paginate per seller (~48 products per page). Only applies when 'includeStorefrontProducts' is on. Amazon caps most listings at ~7 pages. |
| `proxyConfiguration` | object | Apify Proxy settings. Defaults to automatic proxy. Amazon blocks datacenter IPs aggressively on heavy use — for reliable, large runs switch this to RESIDENTIAL. Seller profile pages tolerate datacenter better than search |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## amazon-seller-email-scraper

Exact owner: `khadinakbar`. Identity: `F9WSyqdmOnC76yM4h`. State: `public_schema_verified`.

Build `1.0.19` / `wss1RFnVlmp328n4b`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/amazon-seller-email-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `sellerIds` | array | Use this when you know Amazon merchant IDs. Enter 13–14 uppercase characters such as A1ODG4ICFE5MU3. The selected marketplace determines the seller profile URL. This is not a 10-character ASIN or a website domain. |
| `startUrls` | array | Use this when you already have Amazon URLs. Accepted examples include https://www.amazon.com/sp?seller=A1ODG4ICFE5MU3, storefront URLs with me=, and product /dp/ASIN URLs. Product pages resolve their third-party seller b |
| `marketplace` | string; US, UK, DE, FR, CA, ES, IT, JP, AU, IN, MX, BR, NL, SE, PL, TR, AE, SG | Use this for seller IDs that do not include an Amazon URL. Select the marketplace, for example DE for amazon.de; a supplied Amazon URL always overrides it. Defaults to US. This setting is not a proxy-country selector. |
| `discoverWebsiteEmails` | boolean | Use this to follow a seller website that Amazon itself links, or a matching URL supplied in companyWebsites, when the seller page has no email. The Actor scans the homepage and a few same-site contact pages. Defaults to  |
| `companyWebsites` | array | Use this to supply an official company website for a specific seller ID when Amazon does not link one. Each item needs a sellerId and a full HTTPS URL, for example {"sellerId":"A1ODG4ICFE5MU3","url":"https://example.com" |
| `maxResults` | integer; minimum=1; maximum=100 | Use this to cap the number of Amazon seller profiles inspected in one run. Enter a whole number from 1 to 100; each returned public email is charged at $0.20 and the actor stops adding new seller work at this cap. Defaul |
| `maxContactPages` | integer; minimum=1; maximum=5 | Use this to limit extra official-site crawling for a seller without an Amazon-page email. The homepage is included, followed by same-site contact, support, imprint, or legal pages. Defaults to 3 and accepts 1–5. This doe |
| `proxyConfiguration` | object | Use this to configure Apify Proxy for Amazon access. Automatic Apify Proxy is the default; residential proxies are recommended for larger or blocked runs. The Actor keeps a session consistent across requests. This field  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## etsy-shop-details-scraper

Exact owner: `khadinakbar`. Identity: `ZAe4FkllNBm4EwWe0`. State: `public_schema_verified`.

Build `0.2.4` / `FpnUfL4VXgpCjKvHj`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/etsy-shop-details-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `shopUrls` | array | Use this when you have full Etsy shop URLs. Each item must look like https://www.etsy.com/shop/HunchbackLeather. URLs are deduplicated case-insensitively and combined with shopNames. Do not provide Etsy listing, search,  |
| `shopNames` | array | Use this when you know Etsy shop handles instead of URLs. Enter values such as HunchbackLeather, without spaces or an @ prefix. Names are combined with shopUrls and deduplicated. Do not enter product keywords; this field |
| `maxShops` | integer; minimum=1; maximum=100 | Use this to cap the number of shop profiles processed and billed. One successfully stored profile costs $0.015, so 10 shops cap shop-detail events at $0.15. The default is 10 and the hard maximum is 100. This limit does  |
| `includeShopSections` | boolean | Use this to include public shop-section names when an upstream route exposes them. The default is true; unavailable sections remain null instead of becoming a fabricated empty list. Set false for the leanest profile shap |
| `proxyConfiguration` | object | Kept for backward compatibility with saved tasks created before version 0.2. The rebuilt actor uses managed provider routes and does not send this configuration to Etsy. Leave the default unchanged. This field does not s |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## tiktok-shop-scraper

Exact owner: `khadinakbar`. Identity: `CsvGzdxkpcqmRf3FM`. State: `public_schema_verified`.

Build `0.1.18` / `ssJT7sR1kRYcfZYgT`; tag `latest`. Required keys: `productUrls`. [Full dated input schema](../schemas/tiktok-shop-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `productUrls` | array | Direct TikTok Shop product page URLs to scrape, one per line. Accepts shop.tiktok.com/view/product/<id> and shop.tiktok.com/<region>/pdp/<slug>/<id>. Returns full product details + variants + seller. Multiple URLs run in |
| `includeReviews` | boolean | When true, scrapes reviews for each product (capped by maxReviewsPerProduct). Adds $0.001 per review to the cost. Defaults to false. Set to true only when review text/ratings are needed downstream. |
| `maxReviewsPerProduct` | integer; minimum=1; maximum=1000 | Cap on reviews extracted per product when includeReviews=true (1-1000). Reviews are returned newest-first. Defaults to 30. Ignored when includeReviews=false. |
| `proxyConfiguration` | object | Apify proxy. Defaults to Residential US — required for reliable TikTok Shop scraping. Override only if you know your proxy passes TikTok's anti-bot. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
