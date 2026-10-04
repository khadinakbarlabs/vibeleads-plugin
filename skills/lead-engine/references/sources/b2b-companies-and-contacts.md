# B2B companies and contacts source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

## b2b-lead-finder-enrichment

Exact owner: `khadinakbar`. Identity: `hUKhKQ3mQGtYSfct3`. State: `public_schema_verified`.

Build `1.0.28` / `0EG3uvUWLS1gUkynz`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/b2b-lead-finder-enrichment.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Use this field when the user wants to run multiple searches in one go — e.g. the same business type across multiple cities, or multiple industries in one location. Each entry is a full search query like 'dentists in Miam |
| `searchQuery` | string | Use this field when the user provides a business type, industry, or niche to search for. Examples: 'dentists', 'marketing agencies', 'SaaS companies', 'plumbers', 'law firms'. Do NOT use this field for a specific company |
| `location` | string | Use this field when the user specifies a geographic area such as a city, state, country, or region. Examples: 'Miami, FL', 'New York', 'London', 'Australia'. Leave empty to search globally or let Google Maps use IP geolo |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of business leads to extract from Google Maps per query. Each lead is charged as a PPE event. Prefilled at 3 for fast quality testing — raise to 50, 100, or 500 for real bulk prospecting. Google Maps typic |
| `enableEnrichment` | boolean | Set to true when the user wants email addresses for each lead. When enabled, the actor crawls each business's own website to find their contact email directly — no third-party API needed. This costs more credits (lead-en |
| `proxyConfiguration` | object | HTTP proxy settings for scraping. Leave as default (Apify datacenter proxies, US) for best results. Only change if you need to target a specific country or use residential proxies for higher-trust requests. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## universal-lead-finder

Exact owner: `khadinakbar`. Identity: `qTbWrJckpXQaUe83d`. State: `public_schema_verified`.

Build `1.0.24` / `2282W4PQtddtRbkij`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/universal-lead-finder.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this field when the user provides a keyword or business type to search for (e.g., 'dentists in Miami', 'plumbers Chicago', 'SaaS companies New York'). Use startUrls instead when direct website URLs are provided. |
| `location` | string | City, state, or ZIP code to target (e.g., 'Miami, FL', 'New York, NY', '90210'). Improves search precision. You can also include location directly in the searchQuery above. |
| `startUrls` | array | Use this field when the user provides specific company website URLs to extract contact info from. The actor will crawl each site for emails, phones, and social links. Do NOT use this when the user describes a keyword or  |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of business leads to extract. Each lead counts as one billable event. Default: 50. Max: 1000. |
| `crawlWebsites` | boolean | When enabled, visits each business website to extract email addresses and social media links. Recommended — this is what makes leads actionable. Disable only if you need only phone/address data faster. |
| `includeSubpages` | boolean | Also crawl /contact, /about, /team subpages for better email coverage. Slower but finds more emails. |
| `proxyConfiguration` | object | Proxy settings for scraping. Datacenter proxies (default) work for most sites. Use Residential if you experience blocks. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## lead-finder-pro

Exact owner: `khadinakbar`. Identity: `YXDqLHgkNFKNxyYpo`. State: `public_schema_verified`.

Build `1.1.4` / `w9M13g1WX02W5lb0L`; tag `latest`. Required keys: `searchQueries`. [Full dated input schema](../schemas/lead-finder-pro.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | One to ten business categories or ICP phrases to discover, such as ["web design agencies", "B2B SaaS consultants"]. Each term is combined with Location when supplied. This is not a list of URLs or a person-name lookup. |
| `location` | string | Optional city, state, country, or region that narrows each business search, for example "Austin, TX". Leave blank for location-independent search terms. This is search context, not a precise map-radius filter. |
| `maxResults` | integer; minimum=1; maximum=100 | Maximum number of unique company domains returned across the entire run. Choose an integer from 1 to 100; the default is 10. This cap applies after duplicate and directory filtering, not per search term. |
| `enrichContacts` | boolean | When enabled, visits each discovered business homepage and records public email addresses and a likely contact page link when present. It does not verify deliverability, guess emails, or enrich private personal data. Def |
| `includeDirectories` | boolean | Include results from directories and social networks such as LinkedIn or Yelp. Default is disabled so the output favors the company’s own website. Enable only when directory pages are useful to your workflow. |
| `excludeDomains` | array | Optional domains to omit, for example ["competitor.com", "agency-directory.com"]. Subdomains are also excluded. Do not include URLs, paths, or wildcard syntax. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-search-scraper

Exact owner: `khadinakbar`. Identity: `EmXJMBaKn5SccxM9x`. State: `public_schema_verified`.

Build `0.2.2` / `KmfrdB0JvkVPbVXKJ`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-company-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `keywords` | string | Free-text company-search terms run against public LinkedIn company pages (e.g. 'fintech payments' or 'solar installer'). Combined with the other filters into one Google query. Defaults to empty. NOT a company URL — this  |
| `industry` | string | Industry or sector to match in the company page (e.g. 'Software Development' or 'Renewable Energy'). Quoted automatically so multi-word industries stay intact. Defaults to empty. NOT a free-form description — keep it to  |
| `location` | string | City, region, or country the company is based in (e.g. 'San Francisco' or 'Berlin'). Used both in the search text and as the managed Google search geo hint. Defaults to empty. NOT a country code — use 'Country' for Googl |
| `country` | string | Two-letter country code used to route the Google domain and result language (e.g. 'us', 'gb', 'de'). Defaults to 'us'. NOT a free-text country name — must be an ISO 3166-1 alpha-2 code. |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of unique public company pages to return. Each company returned is billed as one 'company-found' event. Defaults to 25, max 500. Set lower to cap cost on exploratory searches. |
| `enrich` | boolean | When true, each found company is additionally fetched from its public LinkedIn page (industry, employee count, company size, headquarters, website, founded year, followers, specialties, description) via optional company  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-profile-scraper

Exact owner: `khadinakbar`. Identity: `gn2BKbv4n9GIexJKQ`. State: `public_schema_verified`.

Build `0.1.4` / `1aqTkgrWWTHHMqG2s`; tag `latest`. Required keys: `companyUrls`. [Full dated input schema](../schemas/linkedin-company-profile-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyUrls` | array | One or more public LinkedIn company pages to scrape. Each item is either a full URL (e.g. https://www.linkedin.com/company/stripe) or just the vanity name (e.g. stripe). University /school/ and /showcase/ pages are not s |
| `maxCompanies` | integer; minimum=1; maximum=1000 | Maximum number of company profiles to scrape and bill in this run. Accepts 1 to 1000; defaults to 100. Extra input URLs beyond this cap are ignored. Caps your spend at maxCompanies x the per-company price. |
| `includeSimilarCompanies` | boolean | Attach the 'similar / also viewed' company pages LinkedIn lists on the profile (name, url, industry). Defaults to true. Set false for a leaner record. Does not add a separate charge. |
| `includeEmployeesSample` | boolean | Attach a small public sample of employees surfaced on the company page (name, title, profile URL, image). Defaults to false. This is a preview sample, not the full employee roster - for that use the linkedin-company-empl |
| `maxEmployeesSample` | integer; minimum=1; maximum=100 | How many sample employees to include when 'Include sample employees' is on. Accepts 1 to 100; defaults to 10. Ignored when the sample is disabled. |
| `includeRawData` | boolean | Add the compact raw provider payload under rawData for debugging or custom parsing. Defaults to false. Increases record size noticeably; leave off for normal use. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-details-scraper

Exact owner: `khadinakbar`. Identity: `VhnNYP5gZkMlC9n35`. State: `public_schema_verified`.

Build `0.1.9` / `hpOGseaHObswqmByl`; tag `latest`. Required keys: `companyUrls`. [Full dated input schema](../schemas/linkedin-company-details-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyUrls` | array | List of LinkedIn company pages to scrape. Each item is either a full company URL (e.g. 'https://www.linkedin.com/company/shopify') or a bare company slug (e.g. 'shopify'). Defaults to none — at least one is required. NOT |
| `includePosts` | boolean | When true, each company record includes a 'recentPosts' array (post URL, date, text) published by the company page. Defaults to false to keep records small and cheap for AI agents. Does NOT change the per-company price. |
| `maxCompanies` | integer; minimum=1; maximum=1000 | Hard ceiling on how many companies to scrape this run, after de-duplication. Accepts 1 to 1000. Defaults to 100. Caps both work and PPE spend — extra input URLs beyond this limit are ignored. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-by-domain-scraper

Exact owner: `khadinakbar`. Identity: `rIx5BxFR9Pxvbe4wX`. State: `public_schema_verified`.

Build `0.1.9` / `xyECdmQCUaa7iCm3Q`; tag `latest`. Required keys: `domains`. [Full dated input schema](../schemas/linkedin-company-by-domain-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `domains` | array; minItems=1 | One domain or homepage URL per line — e.g. stripe.com, https://www.hubspot.com. Accepts bare domains, www URLs, or https links. |
| `maxResultsPerDomain` | integer; minimum=1; maximum=5 | How many LinkedIn company candidates to return per domain (1–5). Use 1 for enrichment lists; raise it when a domain may map to multiple entities. |
| `includeSerpEvidence` | boolean | Attach the Google Search query, rank, title, and snippet that produced each match — useful for audits and agent debugging. |
| `minConfidence` | number; minimum=0; maximum=1 | Minimum match confidence (0–1) required to bill a row as FOUND. Lower values accept more matches; higher values reduce false positives. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-finder-from-website

Exact owner: `khadinakbar`. Identity: `rs9pkKCfDcdihqtWS`. State: `public_schema_verified`.

Build `0.1.3` / `uL90SHQIcfc0DkvQu`; tag `latest`. Required keys: `websites`. [Full dated input schema](../schemas/linkedin-company-finder-from-website.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `websites` | array; minItems=1; maxItems=100 | Company homepage URLs or domains to resolve to public LinkedIn company pages, e.g. stripe.com or https://www.notion.so. Accepts bare domains, www URLs, or https links. Up to 100 per run. NOT LinkedIn company URLs — for t |
| `maxItems` | integer; minimum=1; maximum=100 | Maximum number of matched LinkedIn company pages to save and bill this run. Default 50. CLEAR / not-found rows do not count toward this cap and are never billed. Prefill is 1 so Apify quality tests finish quickly; raise  |
| `minConfidence` | integer; minimum=40; maximum=95 | Minimum 0-100 confidence required to accept a LinkedIn company page as a match. Default 60. Lower values return more matches with a higher false-positive risk; higher values keep only domain or slug locks. This is not a  |
| `enrichCompany` | boolean | When enabled, each found LinkedIn company page is fetched to add industry, employee count, headquarters, followers, founded year, and description. Enrichment costs an additional $0.02 per successfully enriched company on |
| `maxConcurrency` | integer; minimum=1; maximum=5 | How many website lookups to run in parallel. Default 2 balances speed against provider rate limits. Raise to 5 for large batches; lower to 1 if you see provider rate-limit errors in the run log. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-people-search-scraper

Exact owner: `khadinakbar`. Identity: `S6dSWuZpECzcBhWIc`. State: `public_schema_verified`.

Build `0.1.13` / `3oGg0BNzwWKmiEpdc`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-people-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `jobTitle` | string | Job title to search for, quoted as a phrase on Google (e.g. 'Head of Growth'). Use this when sourcing people by role. Combine with location/company/school to narrow. NOT a free-text bio search — for that use the keywords |
| `location` | string | City, region, or country to filter people by (e.g. 'San Francisco' or 'Germany'). Matched against the public profile's location text in Google results. Leave empty for worldwide. NOT a postal code. |
| `currentCompany` | string | Company name to filter people by (e.g. 'Stripe'). Quoted as a phrase so Google matches it exactly. Best-effort — LinkedIn public pages do not always expose the current employer. NOT a company LinkedIn URL. |
| `school` | string | School or university name to filter alumni (e.g. 'Stanford University'). Quoted as a phrase on Google. Useful for alumni sourcing. NOT a degree or field of study. |
| `keywords` | string | Extra free-text keywords added to the Google query (e.g. 'fintech founder'). Supports Google operators. Use alongside or instead of the structured filters. NOT a LinkedIn profile URL. |
| `profileUrls` | array | Optional list of LinkedIn personal-profile URLs (https://www.linkedin.com/in/<slug>). When provided, search is skipped and these profiles are enriched directly. Use this when you already have URLs and just want full publ |
| `enrichProfiles` | boolean | When true (default), each found profile is fetched for full public data: About section, work history with company links, education entries and follower count. When false, only the fast search-level fields (name, headline |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of people to return (1-500). Caps both search depth and total cost. Defaults to 50. In direct-URL mode it caps how many of the supplied URLs are processed. |
| `resultsRegion` | string | Two-letter country code for the Google search region (e.g. 'US', 'GB', 'DE'). Affects which localized results surface. Defaults to 'US'. NOT the person's location filter — use the location field for that. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-profile-details-scraper

Exact owner: `khadinakbar`. Identity: `96FrUYrH0Zm6SU9K5`. State: `public_schema_verified`.

Build `0.1.4` / `1QM3wMzlohmeldRs4`; tag `latest`. Required keys: `profileUrls`. [Full dated input schema](../schemas/linkedin-profile-details-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `profileUrls` | array; minItems=1; maxItems=1000 | List of public LinkedIn person profiles to scrape. Accepts full URLs (https://www.linkedin.com/in/williamhgates/) or bare vanity handles (williamhgates). Each resolves to one output row. NOT company pages (/company/...)  |
| `maxProfiles` | integer; minimum=1; maximum=1000 | Hard cap on how many profiles to scrape from profileUrls in one run, protecting your budget. Defaults to 1000 (the absolute max). Extra profiles beyond this cap are skipped and noted in the run summary. Does not add resu |
| `outputMode` | string; full, compact | How much per-profile data to return. 'full' (default) returns the complete experience, education, and published-articles arrays. 'compact' returns only the first 3 of each for smaller, agent-friendly records. Pricing is  |
| `includeRawData` | boolean | When true, each output row also includes the unmodified response JSON under rawProfile for debugging or accessing fields not yet mapped. Defaults to false to keep records small and agent-friendly. Turn on only when you n |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-employee-scraper

Exact owner: `khadinakbar`. Identity: `10OSHG9C9mP30WFrN`. State: `public_schema_verified`.

Build `0.3.8` / `OLDjk7Dyzq1DYZNei`; tag `latest`. Required keys: `companyUrls`. [Full dated input schema](../schemas/linkedin-company-employee-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyUrls` | array | LinkedIn company page URLs to scrape. Pass canonical company pages or company subpages, for example https://www.linkedin.com/company/apify/ or https://www.linkedin.com/company/apify/posts/. The actor normalizes each targ |
| `maxEmployees` | integer; minimum=1; maximum=2500 | Global cap across all companies in the run. The actor stops after this many unique employee profile rows have been pushed to the dataset. This is a maximum, not a guarantee, because LinkedIn and provider sources may expo |
| `maxEmployeesPerCompany` | integer; minimum=1; maximum=1000 | Per-company cap for each LinkedIn company URL. This keeps multi-company runs balanced and prevents one large company from consuming the whole global cap. Use it when an agent is comparing several accounts in one run. The |
| `mode` | string; auto, publicSearch, linkedinPeopleTab | Choose how the actor discovers employee profile URLs. Use auto for production workflows because it tries Automatic, the managed fallback route second, authenticated LinkedIn people-tab scraping when LINKEDIN_COOKIES is s |
| `searchQuery` | string | Optional words to add to public-search fallback queries. Use this to guide discovery toward roles, teams, seniority, or functions such as founder, sales, security, recruiter, or engineering. This field mainly affects pub |
| `jobTitles` | array | Optional current-title keywords used to filter or boost visible matches. Examples include CTO, Account Executive, Recruiter, Engineer, Product Manager, or Founder. Rows that match these terms list them in matchedFilters. |
| `locations` | array | Optional location keywords used to filter or boost visible matches. Examples include San Francisco, London, Germany, Remote, or Prague. Location availability depends on the source and may be missing on provider rows. Use |
| `includeProfileDetails` | boolean | Authenticated LinkedIn fallback only. When enabled, the actor visits discovered profile pages to improve visible name, headline, and location extraction. This is slower, uses more compute, and is more likely to hit Linke |
| `maxConcurrency` | integer; minimum=1; maximum=5 | How many companies to process in parallel. Keep this low when using LinkedIn cookies to reduce rate-limit risk and account pressure. Provider-first runs can usually tolerate the default. For AI-agent calls, the default b |
| `proxyConfiguration` | object | Proxy settings for LinkedIn fallback and public search paths. The default uses Apify Residential proxy, which is recommended for reliability. Provider API calls do not need browser proxying, but fallback scraping does. K |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-sales-navigator-scraper

Exact owner: `khadinakbar`. Identity: `VsSYUBBqsszsxMntS`. State: `public_schema_verified`.

Build `0.1.8` / `gflWk5beH8BIqaGaF`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-sales-navigator-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `salesNavigatorUrl` | string | Paste the full URL from the address bar of your LinkedIn Sales Navigator people search (e.g. 'https://www.linkedin.com/sales/search/people?query=...'). The actor decodes the title, company, location, school, industry and |
| `jobTitle` | string | Manual filter used when you are NOT pasting a Sales Navigator URL. Job title quoted as a phrase on Google (e.g. 'Head of Growth'). Combine with location/company/school to narrow. If a salesNavigatorUrl is provided, that  |
| `location` | string | Manual filter: city, region, or country to filter people by (e.g. 'San Francisco' or 'United Kingdom'). Matched against the public profile's location text. Leave empty for worldwide. Overridden by a salesNavigatorUrl whe |
| `currentCompany` | string | Manual filter: company name to filter people by (e.g. 'Stripe'). Quoted as a phrase so Google matches it exactly. Best-effort — public LinkedIn pages do not always expose the current employer. Overridden by a salesNaviga |
| `school` | string | Manual filter: school or university name to filter alumni (e.g. 'Stanford University'). Quoted as a phrase on Google. Useful for alumni sourcing. Overridden by a salesNavigatorUrl. NOT a degree or field of study. |
| `keywords` | string | Manual filter: extra free-text keywords added to the Google query (e.g. 'fintech founder'). Supports Google boolean operators. Use alongside or instead of the structured filters. Merged with a salesNavigatorUrl's decoded |
| `profileUrls` | array | Optional list of LinkedIn personal-profile URLs (https://www.linkedin.com/in/<slug>) — for example a lead list exported from Sales Navigator. When provided (and no salesNavigatorUrl is set), search is skipped and these p |
| `enrichProfiles` | boolean | When true (default), each lead is fetched for full public data: about, experience, education, skills, follower/connection counts. When false, only fast search-level fields (name, headline, location, URL) are returned at  |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of leads to return (1-500). Caps both search depth and total cost. Defaults to 50. In direct-URL mode it caps how many of the supplied URLs are processed. |
| `resultsRegion` | string | Two-letter country code for the Google search region (e.g. 'US', 'GB', 'DE'). Affects which localized results surface. Defaults to 'US'. NOT the person's location filter — use the location field or Sales Navigator URL fo |
| `preferProvider` | string; scrapecreators, sociavault | Which data provider to try first for discovery and enrichment; the other is the automatic fallback if it errors or returns nothing. 'scrapecreators' (default) is broader and usually cheaper; 'sociavault' is the alternati |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-sales-account-scraper

Exact owner: `khadinakbar`. Identity: `52YUfbphiN2IesXUi`. State: `public_schema_verified`.

Build `0.1.3` / `ENPdncsPzjCEdNMQ2`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-sales-account-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `salesNavigatorUrl` | string | Full URL from the address bar of a LinkedIn Sales Navigator Account search, for example https://www.linkedin.com/sales/search/company?query=(filters:List((type:INDUSTRY,values:List((text:Software Development,selectionTyp |
| `industry` | string | Manual filter used when you are NOT pasting a Sales Navigator URL. Industry phrase quoted on Google (e.g. Software Development). Combine with location or companyName to narrow. If salesNavigatorUrl is provided, that URL' |
| `location` | string | Manual filter: city, region, or country to match against public company pages (e.g. San Francisco or United Kingdom). Leave empty for worldwide. Overridden by a salesNavigatorUrl when one is supplied. NOT a postal code l |
| `companyName` | string | Manual filter: company name to search for on public LinkedIn company pages (e.g. Stripe). Quoted as a phrase so Google matches it exactly. Overridden by a salesNavigatorUrl. NOT a LinkedIn company URL — put those in comp |
| `keywords` | string | Manual filter: extra keywords added to the Google query (e.g. fintech payments). Supports Google boolean operators. Merged with a salesNavigatorUrl's decoded keywords. NOT a Sales Navigator URL. |
| `companyUrls` | array | Optional list of public LinkedIn company page URLs (https://www.linkedin.com/company/<slug>). When provided and no salesNavigatorUrl is set, search is skipped and these pages are enriched directly. Use this for an export |
| `enrichAccounts` | boolean | When true (default), each company is fetched for public firmographics: industry, employee count, size, headquarters, website, founded year, followers, description. When false, only search-level fields (name, URL, industr |
| `maxResults` | integer; minimum=1; maximum=250 | Maximum number of company accounts to return (1-250). Caps both search depth and total event cost. Defaults to 25. Prefill is 3 so Apify quality tests finish inside five minutes. In direct-URL mode it caps how many of th |
| `resultsRegion` | string | Two-letter country code for the Google search region (e.g. US, GB, DE). Affects which localized company pages surface. Defaults to US. NOT the company's headquarters filter — use the location field or Sales Navigator URL |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## dnb-companies-scraper

Exact owner: `khadinakbar`. Identity: `QYoGBoZGWKtsoTJCB`. State: `public_schema_verified`.

Build `0.2.4` / `GRmauLexUqVFMQIeb`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/dnb-companies-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Paste Dun & Bradstreet business-directory URLs. Accepts BOTH listing pages (e.g. https://www.dnb.com/business-directory/company-information.software_publishers.us.california.html) AND individual company-profile pages (e. |
| `industryPath` | string | D&B industry slug used for structured search when no startUrls are given (e.g. 'software_publishers'). Find slugs on any industry-analysis URL or via D&B's industry list. Used together with Country and Region. NOT a free |
| `countryIsoCode` | string | Two-letter ISO country code for search mode (e.g. 'us', 'gb', 'de', 'ca'). Defaults to 'us'. Ignored when startUrls are provided. NOT a country name — use the ISO-3166 alpha-2 code. |
| `regionName` | string | Optional state or region to narrow search mode (e.g. 'california', 'texas', 'new_york'). Leave empty to search the whole country. Ignored when startUrls are provided. Use the lowercase underscore form as it appears in dn |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of company records to return across all inputs. D&B caps any single industry+region listing at 1000 companies (20 pages of 50). Defaults to 50. Higher values cost more (see pricing). |
| `enrichDetails` | boolean | When true (default), each company from a listing is enriched with its full profile page (website, industries + NAICS, Fortune ranking, competitor industry, similar companies, contact/principal counts). Adds one extra req |
| `proxyConfiguration` | object | Proxy used for requests. Defaults to Apify datacenter (US). D&B sits behind Cloudflare but is reachable via browser-grade TLS fingerprints; datacenter proxy with IP rotation is normally sufficient. Switch to residential  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## companies-house-uk-scraper

Exact owner: `khadinakbar`. Identity: `IRRvAn8X2ll9zTIgh`. State: `public_schema_verified`.

Build `0.2.4` / `T1CIQjPmVhUPpuQzJ`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/companies-house-uk-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyNumbers` | array; maxItems=100 | Exact UK company numbers to enrich, for example 00000006 or SC123456. Accepts 8-character Companies House numbers with optional SC/NI/OC prefixes. Use this when you already know the register number; do not put free-text  |
| `companyNames` | array; maxItems=50 | Company name phrases to search on Companies House, for example TESCO PLC. Each query returns up to maxSearchResultsPerQuery matches that are then enriched. Use this for discovery when you do not have the company number y |
| `searchQueries` | array; maxItems=50 | Alias of companyNames for agents that prefer a generic searchQueries field. Same company-name search behavior. |
| `officerNames` | array; maxItems=50 | Director or officer names to search, for example Jane Smith. Returns companies linked through officer appointments, then enriches those company profiles. This is not a personal-data enrichment tool beyond the public regi |
| `companyUrls` | array; maxItems=100 | Public Companies House company page URLs. The Actor extracts the company number from paths like /company/00000006. Invalid non-company URLs become INVALID_INPUT warnings. |
| `includeOfficers` | boolean | When true (default), nest active officers on each company row. Turn off to save API quota when you only need the company profile and PSCs. |
| `includePscs` | boolean | When true (default), nest persons with significant control on each company row. Some companies have no published PSC list and return an empty array. |
| `includeResignedOfficers` | boolean | When true, keep resigned directors in the nested officers list. Default false returns currently appointed officers only. |
| `includeCeasedPscs` | boolean | When true, keep ceased persons with significant control. Default false returns active PSC notifications only. |
| `emitOfficerLeadRows` | boolean | When true, also write one billed officer-lead dataset row per nested officer in addition to the company row. Default false keeps one company-shaped row. |
| `maxResults` | integer; minimum=1; maximum=100 | Hard cap on billed company-scraped rows for the run. Default 10 keeps KYB canaries cheap; raise toward 100 for batch enrichment. |
| `maxSearchResultsPerQuery` | integer; minimum=1; maximum=20 | How many company or officer search hits to enrich for each name query before applying maxResults. Default 5. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | Reserved for future parallel enrichment. Current build processes jobs sequentially to respect the Companies House 600 requests / 5 minutes free quota. |
| `companiesHouseApiKey` | string | Credential/access field. Use secure authorized setup only if this feature requires it; never include a credential in files or chat. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## apollo-alternative

Exact owner: `khadinakbar`. Identity: `7chyRbD6rRl5uSvid`. State: `public_schema_verified`.

Build `0.1.9` / `YS3XySo8VViBmdIoe`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/apollo-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `jobTitles` | array; maxItems=10 | One to ten job titles to match in public LinkedIn search results, such as `Head of Growth` or `VP Marketing`. Each value becomes a bounded search plan and duplicates are removed. Use this for people roles, not a list of  |
| `keywords` | array; maxItems=10 | Optional role, skill, or market phrases such as `B2B SaaS` or `demand generation`. They are combined with the public LinkedIn search query and deduplicated. This is not a free-form search of Apollo's proprietary database |
| `companyNames` | array; maxItems=10 | Optional company names to pair with titles or keywords, for example `Stripe` or `HubSpot`. The Actor makes one bounded role-company query per combination, with a maximum of ten query plans. This is not a company-domain e |
| `industry` | string | Optional industry phrase added to every public-search query, such as `cybersecurity` or `healthcare`. Defaults to empty and does not verify NAICS codes or buying intent. Use a short descriptive phrase rather than a locat |
| `location` | string | Optional city, region, or country context such as `San Francisco Bay Area` or `London`. It is retained with the request context; `country` controls Google-market context. This is not a guaranteed residence or employment- |
| `country` | string | Two-letter ISO country code used for public-search market context and the residential proxy, such as `US`, `GB`, or `PK`. Defaults to `US`; it does not guarantee that every profile belongs to this country. Do not enter a |
| `maxResults` | integer; minimum=1; maximum=100 | Hard cap on unique public prospect records persisted for this run. Defaults to 25 and accepts 1 through 100; each persisted record costs $0.02 plus platform usage. Start small to validate relevance before a larger run. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## zoominfo-alternative

Exact owner: `khadinakbar`. Identity: `Y6fgJKtKB3iDq1wbO`. State: `public_schema_verified`.

Build `0.1.12` / `HgXb2c6JGlBLFSNN7`; tag `latest`. Required keys: `companies`. [Full dated input schema](../schemas/zoominfo-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companies` | array; minItems=1; maxItems=100 | One to 100 companies already selected by you, each with a public website domain such as example.com. Optional companyName and externalId are carried into the result to make CRM matching auditable. This is not a free-text |
| `maxCompanies` | integer; minimum=1; maximum=100 | Hard cap on distinct valid company domains processed in this run. Defaults to 25 and accepts 1 to 100, limiting maximum company-enriched event charges to $0.05 per processed company plus platform usage. This is a company |
| `maxPagesPerCompany` | integer; minimum=1; maximum=3 | How many standard public pages to inspect for each supplied domain: the homepage, then optional /about and /contact routes. Defaults to 3 and accepts 1 to 3, keeping collection bounded and source URLs reviewable. This do |
| `includePublishedContacts` | boolean | Return business emails and telephone links visibly published on the company pages that were fetched. Defaults to true and preserves the exact source URLs for review. It does not guess email patterns, unmask protected dat |
| `includeTechnologySignals` | boolean | Return a small list of named technologies whose public asset or script signatures were observed in fetched HTML. Defaults to true and labels each result as an observed website signal rather than a complete technology inv |
| `requestTimeoutSecs` | integer; minimum=5; maximum=60 | Maximum wait for each direct or fallback public-page request. Defaults to 20 seconds and accepts 5 to 60. Transient direct failures receive one bounded retry; this setting does not extend the overall Actor timeout. |
| `useApifyUnblockerFallback` | boolean | After direct requests are clearly blocked or transiently unavailable, try the same public page once through Apify Unblocker. Defaults to true for higher reachability. Unblocker is Apify platform usage paid by the caller, |
| `preferApifyUnblocker` | boolean | Send each configured public page through Apify Unblocker first. If that one attempt is temporarily unavailable, the Actor makes one direct recovery attempt. Defaults to false. Use this higher-platform-usage mode only for |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## rocketreach-alternative

Exact owner: `khadinakbar`. Identity: `kFR5TDChnXFhWBRu0`. State: `public_schema_verified`.

Build `0.2.8` / `GkiimjuMkL0bKc4ow`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/rocketreach-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `operation` | string; work_email_enrichment, public_profile_search | Choose work_email_enrichment for caller-supplied known contacts, or public_profile_search for a bounded public professional-profile search. Public-profile search is available only after its separately priced event become |
| `contacts` | array; minItems=1; maxItems=200 | Required for work_email_enrichment: one to 200 contacts you already know, each with fullName and companyDomain. An optional externalId is preserved for CRM matching and optional linkedInUrl is stored only as supplied pro |
| `publicProfileSearch` | object | Required for public_profile_search: provide a professional search query or a public LinkedIn company URL, with optional title and location filters. Results are public profile name, headline, URL, and location only; no em |
| `maxProfiles` | integer; minimum=1; maximum=25 | For public_profile_search, process one to 25 returned public profiles. Each accepted complete profile is charged only after the separately priced public-profile event has become active. Defaults to 10. |
| `enrichmentMode` | string; find_and_verify, verify_supplied_email, candidate_only | Choose find_and_verify to find a work email from the known name and employer domain, verify_supplied_email to validate contact.email, or candidate_only for DNS-backed conventional patterns. The default uses the owner-con |
| `fallbackPolicy` | string; strict, dns_candidate | Choose strict to fail truthfully without billing when the required verification provider is unavailable. Choose dns_candidate to return the MX-backed candidate route when provider verification cannot complete. The defaul |
| `maxResults` | integer; minimum=1; maximum=200 | Hard cap on contacts processed in one run. Defaults to 25 and accepts 1 to 200 contacts, limiting maximum event charges to $0.12 per completed enrichment plus platform usage. This is not a search-result page limit becaus |
| `maxCandidatesPerContact` | integer; minimum=1; maximum=5 | Number of common work-email patterns returned for an MX-capable employer domain. Defaults to 3 and accepts 1 to 5 patterns, ordered by conventional pattern priority. This does not verify that a specific mailbox exists or |
| `includeMxValidatedCandidates` | boolean | Return candidate work-email strings only when the supplied company domain advertises an MX mail host. Defaults to true; turning it off still returns the enrichment status and DNS provenance without email strings. This is |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## clearbit-alternative

Exact owner: `khadinakbar`. Identity: `SDthf1Y3UTZJYbtfr`. State: `public_schema_verified`.

Build `1.0.6` / `4DMeQ8BIyAdvLTAUs`; tag `latest`. Required keys: `companies`. [Full dated input schema](../schemas/clearbit-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companies` | array; minItems=1; maxItems=100 | Provide one to 100 companies you already selected, each with a public website domain such as apify.com. Optional companyName and externalId are carried through for an auditable CRM join. This is not a free-text person se |
| `maxCompanies` | integer; minimum=1; maximum=100 | Set the hard cap on distinct valid company domains in this run, from 1 through 100. It defaults to 10, so company-enriched event charges cannot exceed the selected count plus platform usage. This is a result cap, not a r |
| `maxPagesPerCompany` | integer; minimum=1; maximum=4 | Choose how many standard public routes to inspect: the homepage and then /about, /contact, and /team. It defaults to 3 and accepts 1 through 4 so source URLs stay bounded and reviewable. It does not enter portals, logins |
| `includePublishedContacts` | boolean | When enabled, return business email and phone links visibly published on the fetched public company pages. It defaults to true and preserves supporting source URLs for review. It never guesses email patterns, unmask prot |
| `includeTechnologySignals` | boolean | When enabled, return a small list of technologies whose public HTML asset signatures were observed during the fetch. It defaults to true and labels these as page-level observations, not a complete technology inventory. I |
| `useProxyFallback` | boolean | Allow one Apify Residential proxy retry only after the direct request is blocked or transiently unavailable. It defaults to true to improve resilience while keeping direct public-site collection as the primary route. Pro |
| `requestTimeoutSecs` | integer; minimum=5; maximum=40 | Set the timeout for one public webpage request, from 5 through 40 seconds. It defaults to 20 seconds and is applied independently to every bounded route and retry. This does not extend the overall Actor timeout or allow  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## lusha-alternative

Exact owner: `khadinakbar`. Identity: `n7oPOKjLe1OLcfC5Q`. State: `public_schema_verified`.

Build `0.1.5` / `SJ8VLbuKsBuJpQ3lZ`; tag `latest`. Required keys: `contacts`. [Full dated input schema](../schemas/lusha-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `contacts` | array; minItems=1; maxItems=25 | Provide 1 to 25 people you already know, each with a full name and the employer’s public website domain. Optional companyName and externalId are carried through so the returned evidence can join back to your CRM or sprea |
| `maxContacts` | integer; minimum=1; maximum=25 | Hard cap on distinct valid contacts processed in one run. Defaults to 25 and accepts 1 to 25, limiting public-page collection and the maximum public-contact-found event charge. Duplicate name-and-domain entries are skipp |
| `maxPagesPerContact` | integer; minimum=1; maximum=3 | How many public company-owned pages to inspect per contact, from 1 to 3. The Actor tries caller-provided source URLs first, then bounded standard public routes. Defaults to 3 to make the evidence set small and reviewable |
| `requestTimeoutSecs` | integer; minimum=5; maximum=20 | Maximum wait for each direct or fallback public-page request. Defaults to 10 seconds and accepts 5 to 20 seconds, keeping a single run bounded. A transient or blocked direct request gets one short retry and, if enabled,  |
| `responseFormat` | string; detailed, concise | Choose detailed to include a short surrounding role snippet for every name match, or concise to omit snippets while keeping source URLs and structured evidence. Defaults to detailed for human review. The setting does not |
| `useApifyUnblockerFallback` | boolean | After a direct request is blocked or transiently unavailable, make one bounded retry through Apify Unblocker. Defaults to true to improve public-page reachability while preserving the same domain and redirect checks. Unb |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## cognism-alternative

Exact owner: `khadinakbar`. Identity: `3vN9tAAV1lCR8vorN`. State: `public_schema_verified`.

Build `0.8.3` / `dMnMN74v3CVMayDas`; tag `latest`. Required keys: `accounts`. [Full dated input schema](../schemas/cognism-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `accounts` | array; minItems=1; maxItems=20 | Provide one to 20 known B2B company records to research from their public website. Each item needs companyDomain such as example.com and can retain a caller label, record ID, and up to five role keywords. The default is  |
| `maxAccounts` | integer; minimum=1; maximum=20 | Safety cap for valid account records after normalization and duplicate removal. Enter an integer such as 5; values range from 1 to 20. The default 5 keeps first runs bounded. This is not the number of pages or an instruc |
| `maxPagesPerAccount` | integer; minimum=1; maximum=5 | Bound the fixed public-page set checked for each account: homepage, contact, about, team, then leadership. Enter 1 through 5; the default is 3 pages. Lower values reduce runtime and event-charge exposure. This is not a s |
| `requestTimeoutSecs` | integer; minimum=5; maximum=30 | Maximum time allowed for one public-page HTTP request before it is classified for retry or a truthful source outcome. Enter seconds such as 15; supported values are 5 through 30. The default balances first-run reliabilit |
| `useApifyUnblockerFallback` | boolean | Enable one Apify Unblocker recovery attempt only when a direct public-page request is blocked or transiently unavailable. The default is false, preserving direct collection as the primary route. Apify proxy usage may add |
| `preferApifyUnblocker` | boolean | Start with Apify Unblocker when a permitted public website has repeatedly blocked direct requests. It only applies when the fallback option is also enabled, and defaults to false. Direct collection remains the standard l |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## seamless-ai-alternative

Exact owner: `khadinakbar`. Identity: `wptNZi3zSlTeqJTfx`. State: `public_schema_verified`.

Build `0.1.7` / `5ItbszGqfiJpC45jC`; tag `latest`. Required keys: `contacts`. [Full dated input schema](../schemas/seamless-ai-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `contacts` | array; minItems=1; maxItems=25 | 1–25 caller-supplied contacts. companyDomain is required. fullName helps locate a public mention on the company site, but is optional. |
| `maxContacts` | integer; minimum=1; maximum=25 | Safety cap applied after validation. Use a lower number for a small canary run. |
| `maxPagesPerContact` | integer; minimum=1; maximum=4 | The Actor tries the homepage, /contact, /about, and /team in a fixed bounded order. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=45 | Time limit for each public-page request. |
| `useApifyUnblockerFallback` | boolean | When enabled, a single Apify Unblocker retry is attempted only after a direct fetch is blocked or transiently unavailable. This can add Apify proxy usage charges. |
| `preferApifyUnblocker` | boolean | Off by default. Enable only if a customer-authorized site consistently blocks direct public requests. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## snov-io-alternative

Exact owner: `khadinakbar`. Identity: `8WS1icazgH7IGOhK7`. State: `public_schema_verified`.

Build `0.1.7` / `hCdFs1Q001s8rsXnS`; tag `latest`. Required keys: `targets`. [Full dated input schema](../schemas/snov-io-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `targets` | array; minItems=1; maxItems=25 | Provide 1 to 25 public company domains you are authorized to research. Each item accepts a hostname such as 'example.com' and optional known business context. This reads the homepage plus directly linked same-site contac |
| `maxTargets` | integer; minimum=1; maximum=25 | Safety cap for accepted domain targets. Use 1 for a quick canary, and use up to 25 for one bounded batch. The default is 10 and values outside 1 to 25 are constrained. This is not a result-count or page-depth setting. |
| `maxPagesPerTarget` | integer; minimum=1; maximum=5 | Maximum number of public same-site pages to inspect after the homepage, including the homepage. The Actor follows only directly linked contact, about, team, legal, privacy, or terms pages. The default is 3 and values are |
| `requestTimeoutSecs` | integer; minimum=5; maximum=45 | Time limit for one public page request, for example 20 seconds. The default is 20 and values are bounded from 5 to 45 seconds. Lower values make runs fail faster on unresponsive sites. This is not the whole-run timeout c |
| `useApifyUnblockerFallback` | boolean | Enable one Apify Unblocker retry only after a public direct request is blocked or transiently unavailable. The default is true and may add Apify proxy usage charges. Disable it for direct-only testing. This is not a guar |
| `preferApifyUnblocker` | boolean | When true, try Apify Unblocker first for every public page; direct access remains the recovery route if proxy creation fails. The default is false because direct public HTTP is cheaper and preferred. Enable only for an a |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
