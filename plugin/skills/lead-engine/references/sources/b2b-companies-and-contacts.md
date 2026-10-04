# B2B companies and contacts source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [qualified business/contact-use gate](../contact-use.md). Provider result bounds are not recommended audience sizes; optional contact extraction must be disabled during discovery.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## b2b-lead-finder-enrichment

Exact owner: `khadinakbar`. Identity: `hUKhKQ3mQGtYSfct3`. State: `public_schema_verified`.

Build `1.0.28` / `0EG3uvUWLS1gUkynz`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/b2b-lead-finder-enrichment.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Use this field when the user wants to run multiple searches in one go — e.g. the same business type across multiple cities, or multiple industries in one location. Each entry is a full search query like 'dentists in Miami' or 'law firms in Chicago'. When provided, this takes priority over searchQuery. Examples: ['dentists in Miami', 'dentists in Orlando', 'dentists in Tampa']. Leave empty to use the single searchQuery field instead. |
| `searchQuery` | string | Use this field when the user provides a business type, industry, or niche to search for. Examples: 'dentists', 'marketing agencies', 'SaaS companies', 'plumbers', 'law firms'. Do NOT use this field for a specific company name — this is for category-level searches that return many results. |
| `location` | string | Use this field when the user specifies a geographic area such as a city, state, country, or region. Examples: 'Miami, FL', 'New York', 'London', 'Australia'. Leave empty to search globally or let Google Maps use IP geolocation. Do NOT put the business type here — use searchQuery for that. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of business leads to extract from Google Maps per query. Each lead is charged as a PPE event. Google Maps typically returns up to ~120 results per query before pagination stops. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `enableEnrichment` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## universal-lead-finder

Exact owner: `khadinakbar`. Identity: `qTbWrJckpXQaUe83d`. State: `public_schema_verified`.

Build `1.0.24` / `2282W4PQtddtRbkij`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/universal-lead-finder.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this field when the user provides a keyword or business type to search for (e.g., 'dentists in Miami', 'plumbers Chicago', 'SaaS companies New York'). Use startUrls instead when direct website URLs are provided. |
| `location` | string | City, state, or ZIP code to target (e.g., 'Miami, FL', 'New York, NY', '90210'). Improves search precision. You can also include location directly in the searchQuery above. |
| `startUrls` | array | Use this field when the user provides specific company website URLs to extract contact info from. The actor will crawl each site for emails, phones, and social links. Do NOT use this when the user describes a keyword or niche — use searchQuery for that. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of business leads to extract. Each lead counts as one billable event. Default: 50. Max: 1000. |
| `crawlWebsites` | boolean | When enabled, visits each business website to extract email addresses and social media links. Recommended — this is what makes leads actionable. Disable only if you need only phone/address data faster. |
| `includeSubpages` | boolean | VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

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
| `enrichContacts` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `includeDirectories` | boolean | Include results from directories and social networks such as LinkedIn or Yelp. Default is disabled so the output favors the company’s own website. Enable only when directory pages are useful to your workflow. |
| `excludeDomains` | array | Optional domains to omit, for example ["competitor.com", "agency-directory.com"]. Subdomains are also excluded. Do not include URLs, paths, or wildcard syntax. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-search-scraper

Exact owner: `khadinakbar`. Identity: `EmXJMBaKn5SccxM9x`. State: `public_schema_verified`.

Build `0.2.2` / `KmfrdB0JvkVPbVXKJ`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-company-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `keywords` | string | Free-text company-search terms run against public LinkedIn company pages (e.g. 'fintech payments' or 'solar installer'). Combined with the other filters into one Google query. Defaults to empty. NOT a company URL — this searches for companies, it does not enrich a known page. |
| `industry` | string | Industry or sector to match in the company page (e.g. 'Software Development' or 'Renewable Energy'). Quoted automatically so multi-word industries stay intact. Defaults to empty. NOT a free-form description — keep it to a short industry phrase. |
| `location` | string | City, region, or country the company is based in (e.g. 'San Francisco' or 'Berlin'). Used both in the search text and as the managed Google search geo hint. Defaults to empty. NOT a country code — use 'Country' for Google domain routing. |
| `country` | string | Two-letter country code used to route the Google domain and result language (e.g. 'us', 'gb', 'de'). Defaults to 'us'. NOT a free-text country name — must be an ISO 3166-1 alpha-2 code. |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of unique public company pages to return. Each company returned is billed as one 'company-found' event. Defaults to 25, max 500. Set lower to cap cost on exploratory searches. |
| `enrich` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-profile-scraper

Exact owner: `khadinakbar`. Identity: `gn2BKbv4n9GIexJKQ`. State: `public_schema_verified`.

Build `0.1.4` / `1aqTkgrWWTHHMqG2s`; tag `latest`. Required keys: `companyUrls`. [Full dated input schema](../schemas/linkedin-company-profile-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyUrls` | array | One or more public LinkedIn company pages to scrape. Each item is either a full URL (e.g. https://www.linkedin.com/company/stripe) or just the vanity name (e.g. stripe). University /school/ and /showcase/ pages are not supported. Not a LinkedIn person profile - for people use the linkedin-profile-details-scraper actor. |
| `maxCompanies` | integer; minimum=1; maximum=1000 | Maximum number of company profiles to scrape and bill in this run. Accepts 1 to 1000; defaults to 100. Extra input URLs beyond this cap are ignored. Caps your spend at maxCompanies x the per-company price. |
| `includeSimilarCompanies` | boolean | Attach the 'similar / also viewed' company pages LinkedIn lists on the profile (name, url, industry). Defaults to true. Set false for a leaner record. Does not add a separate charge. |
| `includeEmployeesSample` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxEmployeesSample` | integer; minimum=1; maximum=100 | How many sample employees to include when 'Include sample employees' is on. Accepts 1 to 100; defaults to 10. Ignored when the sample is disabled. |
| `includeRawData` | boolean | Add the compact raw provider payload under rawData for debugging or custom parsing. Defaults to false. Increases record size noticeably; leave off for normal use. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-details-scraper

Exact owner: `khadinakbar`. Identity: `VhnNYP5gZkMlC9n35`. State: `public_schema_verified`.

Build `0.1.9` / `hpOGseaHObswqmByl`; tag `latest`. Required keys: `companyUrls`. [Full dated input schema](../schemas/linkedin-company-details-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyUrls` | array | List of LinkedIn company pages to scrape. Each item is either a full company URL (e.g. 'https://www.linkedin.com/company/shopify') or a bare company slug (e.g. 'shopify'). Defaults to none — at least one is required. NOT for personal profiles, posts, or schools; use the matching profile/posts actor for those. |
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
| `websites` | array; minItems=1; maxItems=100 | Company homepage URLs or domains to resolve to public LinkedIn company pages, e.g. stripe.com or https://www.notion.so. Accepts bare domains, www URLs, or https links. Up to 100 per run. NOT LinkedIn company URLs — for those use LinkedIn Company Profile Scraper. |
| `maxItems` | integer; minimum=1; maximum=100 | Maximum number of matched LinkedIn company pages to save and bill this run. Default 50. CLEAR / not-found rows do not count toward this cap and are never billed. Prefill is 1 so Apify quality tests finish quickly; raise it for production batches. |
| `minConfidence` | integer; minimum=40; maximum=95 | Minimum 0-100 confidence required to accept a LinkedIn company page as a match. Default 60. Lower values return more matches with a higher false-positive risk; higher values keep only domain or slug locks. This is not a LinkedIn login threshold. |
| `enrichCompany` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | How many website lookups to run in parallel. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-people-search-scraper

Exact owner: `khadinakbar`. Identity: `S6dSWuZpECzcBhWIc`. State: `public_schema_verified`.

Build `0.1.13` / `3oGg0BNzwWKmiEpdc`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-people-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `jobTitle` | string | Job title to search for, quoted as a phrase on Google (e.g. 'Head of Growth'). Use this when sourcing people by role. Combine with location/company/school to narrow. NOT a free-text bio search — for that use the keywords field. |
| `location` | string | City, region, or country to filter people by (e.g. 'San Francisco' or 'Germany'). Matched against the public profile's location text in Google results. Leave empty for worldwide. NOT a postal code. |
| `currentCompany` | string | Company name to filter people by (e.g. 'Stripe'). Quoted as a phrase so Google matches it exactly. Best-effort — LinkedIn public pages do not always expose the current employer. NOT a company LinkedIn URL. |
| `school` | string | School or university name to filter alumni (e.g. 'Stanford University'). Quoted as a phrase on Google. Useful for alumni sourcing. NOT a degree or field of study. |
| `keywords` | string | Extra free-text keywords added to the Google query (e.g. 'fintech founder'). Supports Google operators. Use alongside or instead of the structured filters. NOT a LinkedIn profile URL. |
| `profileUrls` | array | Optional list of LinkedIn personal-profile URLs (https://www.linkedin.com/in/<slug>). When provided, search is skipped and these profiles are enriched directly. Use this when you already have URLs and just want full public data. NOT company or post URLs. |
| `enrichProfiles` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of people to return (1-500). Caps both search depth and total cost. Defaults to 50. In direct-URL mode it caps how many of the supplied URLs are processed. |
| `resultsRegion` | string | Two-letter country code for the Google search region (e.g. 'US', 'GB', 'DE'). Affects which localized results surface. Defaults to 'US'. NOT the person's location filter — use the location field for that. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-profile-details-scraper

Exact owner: `khadinakbar`. Identity: `96FrUYrH0Zm6SU9K5`. State: `public_schema_verified`.

Build `0.1.4` / `1QM3wMzlohmeldRs4`; tag `latest`. Required keys: `profileUrls`. [Full dated input schema](../schemas/linkedin-profile-details-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `profileUrls` | array; minItems=1; maxItems=1000 | List of public LinkedIn person profiles to scrape. Accepts full URLs (https://www.linkedin.com/in/williamhgates/) or bare vanity handles (williamhgates). Each resolves to one output row. NOT company pages (/company/...) — those are skipped; for companies use the LinkedIn Company scrapers. |
| `maxProfiles` | integer; minimum=1; maximum=1000 | Hard cap on how many profiles to scrape from profileUrls in one run, protecting your budget. Defaults to 1000 (the absolute max). Extra profiles beyond this cap are skipped and noted in the run summary. Does not add results that were not supplied in profileUrls. |
| `outputMode` | string; full, compact | How much per-profile data to return. 'full' (default) returns the complete experience, education, and published-articles arrays. 'compact' returns only the first 3 of each for smaller, agent-friendly records. Pricing is identical in both modes. |
| `includeRawData` | boolean | When true, each output row also includes the unmodified response JSON under rawProfile for debugging or accessing fields not yet mapped. Defaults to false to keep records small and agent-friendly. Turn on only when you need fields the normalized schema does not expose yet. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-employee-scraper

Exact owner: `khadinakbar`. Identity: `10OSHG9C9mP30WFrN`. State: `public_schema_verified`.

Build `0.3.8` / `OLDjk7Dyzq1DYZNei`; tag `latest`. Required keys: `companyUrls`. [Full dated input schema](../schemas/linkedin-company-employee-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyUrls` | array | LinkedIn company page URLs to scrape. Pass canonical company pages or company subpages, for example https://www.linkedin.com/company/apify/ or https://www.linkedin.com/company/apify/posts/. The actor normalizes each target to /company/<slug>/ and deduplicates repeated companies. Use this field when an agent already knows the target accounts. |
| `maxEmployees` | integer; minimum=1; maximum=2500 | Global cap across all companies in the run. The actor stops after this many unique employee profile rows have been pushed to the dataset. This is a maximum, not a guarantee, because LinkedIn and provider sources may expose fewer visible employees. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `maxEmployeesPerCompany` | integer; minimum=1; maximum=1000 | Per-company cap for each LinkedIn company URL. This keeps multi-company runs balanced and prevents one large company from consuming the whole global cap. Use it when an agent is comparing several accounts in one run. The actor can still return fewer rows when visible data is limited. |
| `mode` | string; auto, publicSearch, linkedinPeopleTab | Use publicSearch only after verifying the actual build respects the source access gate and disables automatic recovery. The auto and linkedinPeopleTab modes are unavailable in VibeLeads. |
| `searchQuery` | string | Optional words to add to public-search fallback queries. Use this to guide discovery toward roles, teams, seniority, or functions such as founder, sales, security, recruiter, or engineering. This field mainly affects publicSearch mode and the final public-search fallback in auto mode. Leave it blank for broader provider-first company discovery. |
| `jobTitles` | array | Optional current-title keywords used to filter or boost visible matches. Examples include CTO, Account Executive, Recruiter, Engineer, Product Manager, or Founder. Rows that match these terms list them in matchedFilters. Use this when an agent needs a role-focused employee list instead of a broad company sample. |
| `locations` | array | Optional location keywords used to filter or boost visible matches. Examples include San Francisco, London, Germany, Remote, or Prague. Location availability depends on the source and may be missing on provider rows. Use this for geo-focused research, but keep filters broad when recall matters. |
| `includeProfileDetails` | boolean | Unavailable for enablement in VibeLeads. Keep disabled; gated profile collection is unsupported. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | How many companies to process in parallel. Provider-first runs can usually tolerate the default. For AI-agent calls, the default balances speed and reliability. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-sales-navigator-scraper

Exact owner: `khadinakbar`. Identity: `VsSYUBBqsszsxMntS`. State: `public_schema_verified`.

Build `0.1.8` / `gflWk5beH8BIqaGaF`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-sales-navigator-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `salesNavigatorUrl` | string | Paste the full URL from the address bar of your LinkedIn Sales Navigator people search (e.g. 'https://www.linkedin.com/sales/search/people?query=...'). The actor decodes the title, company, location, school, industry and keyword filters from the URL and finds matching PUBLIC profiles via Google — no LinkedIn login or Sales Navigator seat is used. SN-only filters (headcount, seniority, function, intent) cannot be honored by public search and are skipped with a notice. NOT a profile URL — for that use 'profileUrls'. |
| `jobTitle` | string | Manual filter used when you are NOT pasting a Sales Navigator URL. Job title quoted as a phrase on Google (e.g. 'Head of Growth'). Combine with location/company/school to narrow. If a salesNavigatorUrl is provided, that URL's filters take precedence. NOT a free-text bio search — use the keywords field for that. |
| `location` | string | Manual filter: city, region, or country to filter people by (e.g. 'San Francisco' or 'United Kingdom'). Matched against the public profile's location text. Leave empty for worldwide. Overridden by a salesNavigatorUrl when one is supplied. NOT a postal code. |
| `currentCompany` | string | Manual filter: company name to filter people by (e.g. 'Stripe'). Quoted as a phrase so Google matches it exactly. Best-effort — public LinkedIn pages do not always expose the current employer. Overridden by a salesNavigatorUrl. NOT a company LinkedIn URL. |
| `school` | string | Manual filter: school or university name to filter alumni (e.g. 'Stanford University'). Quoted as a phrase on Google. Useful for alumni sourcing. Overridden by a salesNavigatorUrl. NOT a degree or field of study. |
| `keywords` | string | Manual filter: extra free-text keywords added to the Google query (e.g. 'fintech founder'). Supports Google boolean operators. Use alongside or instead of the structured filters. Merged with a salesNavigatorUrl's decoded keywords. NOT a LinkedIn profile URL. |
| `profileUrls` | array | Optional list of LinkedIn personal-profile URLs (https://www.linkedin.com/in/<slug>) — for example a lead list exported from Sales Navigator. When provided (and no salesNavigatorUrl is set), search is skipped and these profiles are enriched directly. Use when you already have URLs and just want full public data. NOT company or post URLs. |
| `enrichProfiles` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of leads to return (1-500). Caps both search depth and total cost. Defaults to 50. In direct-URL mode it caps how many of the supplied URLs are processed. |
| `resultsRegion` | string | Two-letter country code for the Google search region (e.g. 'US', 'GB', 'DE'). Affects which localized results surface. Defaults to 'US'. NOT the person's location filter — use the location field or Sales Navigator URL for that. |
| `preferProvider` | string; scrapecreators, sociavault | 'scrapecreators' (default) is broader and usually cheaper; 'sociavault' is the alternative. Leave on default unless you specifically want to route through SociaVault first. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-sales-account-scraper

Exact owner: `khadinakbar`. Identity: `52YUfbphiN2IesXUi`. State: `public_schema_verified`.

Build `0.1.3` / `ENPdncsPzjCEdNMQ2`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-sales-account-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `salesNavigatorUrl` | string | Full URL from the address bar of a LinkedIn Sales Navigator Account search, for example https://www.linkedin.com/sales/search/company?query=(filters:List((type:INDUSTRY,values:List((text:Software Development,selectionType:INCLUDED))))). The actor decodes industry, location, company name, and keywords, then finds matching PUBLIC company pages via Google. SN-only filters such as headcount and revenue are skipped with a notice. NOT a people-search URL and NOT a /sales/company/{id} detail link. |
| `industry` | string | Manual filter used when you are NOT pasting a Sales Navigator URL. Industry phrase quoted on Google (e.g. Software Development). Combine with location or companyName to narrow. If salesNavigatorUrl is provided, that URL's industry filter takes precedence. NOT a NAICS code. |
| `location` | string | Manual filter: city, region, or country to match against public company pages (e.g. San Francisco or United Kingdom). Leave empty for worldwide. Overridden by a salesNavigatorUrl when one is supplied. NOT a postal code lookup. |
| `companyName` | string | Manual filter: company name to search for on public LinkedIn company pages (e.g. Stripe). Quoted as a phrase so Google matches it exactly. Overridden by a salesNavigatorUrl. NOT a LinkedIn company URL — put those in companyUrls. |
| `keywords` | string | Manual filter: extra keywords added to the Google query (e.g. fintech payments). Supports Google boolean operators. Merged with a salesNavigatorUrl's decoded keywords. NOT a Sales Navigator URL. |
| `companyUrls` | array | Optional list of public LinkedIn company page URLs (https://www.linkedin.com/company/<slug>). When provided and no salesNavigatorUrl is set, search is skipped and these pages are enriched directly. Use this for an exported account list you already have. NOT personal /in/ profiles and NOT /sales/company/{id} seat URLs. |
| `enrichAccounts` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `maxResults` | integer; minimum=1; maximum=250 | Maximum number of company accounts to return (1-250). Caps both search depth and total event cost. Defaults to 25. Prefill is 3 so Apify quality tests finish inside five minutes. In direct-URL mode it caps how many of the supplied URLs are processed. |
| `resultsRegion` | string | Two-letter country code for the Google search region (e.g. US, GB, DE). Affects which localized company pages surface. Defaults to US. NOT the company's headquarters filter — use the location field or Sales Navigator URL for that. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## dnb-companies-scraper

Exact owner: `khadinakbar`. Identity: `QYoGBoZGWKtsoTJCB`. State: `public_schema_verified`.

Build `0.2.4` / `GRmauLexUqVFMQIeb`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/dnb-companies-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Paste Dun & Bradstreet business-directory URLs. Accepts BOTH listing pages (e.g. https://www.dnb.com/business-directory/company-information.software_publishers.us.california.html) AND individual company-profile pages (e.g. https://www.dnb.com/business-directory/company-profiles.apple_inc.<hash>.html). The actor auto-detects each URL type. Leave empty to use the industry/country/region search fields instead. |
| `industryPath` | string | D&B industry slug used for structured search when no startUrls are given (e.g. 'software_publishers'). Find slugs on any industry-analysis URL or via D&B's industry list. Used together with Country and Region. NOT a free-text industry name — it must be the underscore slug exactly as it appears in a dnb.com URL. |
| `countryIsoCode` | string | Two-letter ISO country code for search mode (e.g. 'us', 'gb', 'de', 'ca'). Defaults to 'us'. Ignored when startUrls are provided. NOT a country name — use the ISO-3166 alpha-2 code. |
| `regionName` | string | Optional state or region to narrow search mode (e.g. 'california', 'texas', 'new_york'). Leave empty to search the whole country. Ignored when startUrls are provided. Use the lowercase underscore form as it appears in dnb.com listing URLs. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of company records to return across all inputs. D&B caps any single industry+region listing at 1000 companies (20 pages of 50). Defaults to 50. Higher values cost more (see pricing). |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## companies-house-uk-scraper

Exact owner: `khadinakbar`. Identity: `IRRvAn8X2ll9zTIgh`. State: `public_schema_verified`.

Build `0.2.4` / `T1CIQjPmVhUPpuQzJ`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/companies-house-uk-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyNumbers` | array; maxItems=100 | Exact UK company numbers to enrich, for example 00000006 or SC123456. Accepts 8-character Companies House numbers with optional SC/NI/OC prefixes. Use this when you already know the register number; do not put free-text company names here. |
| `companyNames` | array; maxItems=50 | Company name phrases to search on Companies House, for example TESCO PLC. Each query returns up to maxSearchResultsPerQuery matches that are then enriched. Use this for discovery when you do not have the company number yet. |
| `searchQueries` | array; maxItems=50 | Alias of companyNames for agents that prefer a generic searchQueries field. Same company-name search behavior. |
| `officerNames` | array; maxItems=50 | Director or officer names to search, for example Jane Smith. Returns companies linked through officer appointments, then enriches those company profiles. This is not a personal-data enrichment tool beyond the public register. |
| `companyUrls` | array; maxItems=100 | Public Companies House company page URLs. The Actor extracts the company number from paths like /company/00000006. Invalid non-company URLs become INVALID_INPUT warnings. |
| `includeOfficers` | boolean | When true (default), nest active officers on each company row. Turn off to save API quota when you only need the company profile and PSCs. |
| `includePscs` | boolean | When true (default), nest persons with significant control on each company row. Some companies have no published PSC list and return an empty array. |
| `includeResignedOfficers` | boolean | When true, keep resigned directors in the nested officers list. Default false returns currently appointed officers only. |
| `includeCeasedPscs` | boolean | When true, keep ceased persons with significant control. Default false returns active PSC notifications only. |
| `emitOfficerLeadRows` | boolean | When true, also write one billed officer-lead dataset row per nested officer in addition to the company row. Default false keeps one company-shaped row. |
| `maxResults` | integer; minimum=1; maximum=100 | Hard cap on billed company-scraped rows for the run. Default 10 keeps KYB canaries cheap; raise toward 100 for batch enrichment. |
| `maxSearchResultsPerQuery` | integer; minimum=1; maximum=20 | How many company or officer search hits to enrich for each name query before applying maxResults. Default 5. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | Reserved for future parallel enrichment. Current build processes jobs sequentially to respect the Companies House 600 requests / 5 minutes free quota. |
| `companiesHouseApiKey` | string | Optional. The caller/user must supply their own Companies House Public Data API key for this run when they want the official API path. When omitted, the Actor uses the free public HTML register (zero-config). The value is never written to the dataset, output, or logs. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## apollo-alternative

Exact owner: `khadinakbar`. Identity: `7chyRbD6rRl5uSvid`. State: `public_schema_verified`.

Build `0.1.9` / `YS3XySo8VViBmdIoe`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/apollo-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `jobTitles` | array; maxItems=10 | One to ten job titles to match in public LinkedIn search results, such as `Head of Growth` or `VP Marketing`. Each value becomes a bounded search plan and duplicates are removed. Use this for people roles, not a list of profile URLs or an email-search request. |
| `keywords` | array; maxItems=10 | Optional role, skill, or market phrases such as `B2B SaaS` or `demand generation`. They are combined with the public LinkedIn search query and deduplicated. This is not a free-form search of Apollo's proprietary database or a Boolean-email verifier. |
| `companyNames` | array; maxItems=10 | Optional company names to pair with titles or keywords, for example `Stripe` or `HubSpot`. The Actor makes one bounded role-company query per combination, with a maximum of ten query plans. This is not a company-domain enrichment or account-intent filter. |
| `industry` | string | Optional industry phrase added to every public-search query, such as `cybersecurity` or `healthcare`. Defaults to empty and does not verify NAICS codes or buying intent. Use a short descriptive phrase rather than a location or job title. |
| `location` | string | Optional city, region, or country context such as `San Francisco Bay Area` or `London`. It is retained with the request context; `country` controls Google-market context. This is not a guaranteed residence or employment-location filter or verification. |
| `country` | string | Defaults to `US`; it does not guarantee that every profile belongs to this country. Do not enter a full country name here. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `maxResults` | integer; minimum=1; maximum=100 | Hard cap on unique public prospect records persisted for this run. Defaults to 25 and accepts 1 through 100; each persisted record costs $0.02 plus platform usage. Start small to validate relevance before a larger run. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## zoominfo-alternative

Exact owner: `khadinakbar`. Identity: `Y6fgJKtKB3iDq1wbO`. State: `public_schema_verified`.

Build `0.1.12` / `HgXb2c6JGlBLFSNN7`; tag `latest`. Required keys: `companies`. [Full dated input schema](../schemas/zoominfo-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companies` | array; minItems=1; maxItems=100 | One to 100 companies already selected by you, each with a public website domain such as example.com. Optional companyName and externalId are carried into the result to make CRM matching auditable. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `maxCompanies` | integer; minimum=1; maximum=100 | Hard cap on distinct valid company domains processed in this run. Defaults to 25 and accepts 1 to 100, limiting maximum company-enriched event charges to $0.05 per processed company plus platform usage. This is a company-list cap, not a web crawl depth setting. |
| `maxPagesPerCompany` | integer; minimum=1; maximum=3 | How many standard public pages to inspect for each supplied domain: the homepage, then optional /about and /contact routes. Defaults to 3 and accepts 1 to 3, keeping collection bounded and source URLs reviewable. This does not crawl the public web, customer portals, or login-protected pages. |
| `includePublishedContacts` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `includeTechnologySignals` | boolean | Return a small list of named technologies whose public asset or script signatures were observed in fetched HTML. Defaults to true and labels each result as an observed website signal rather than a complete technology inventory. It does not infer subscriptions, spending, or buyer intent. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=60 | Maximum wait for each direct or fallback public-page request. Defaults to 20 seconds and accepts 5 to 60. Transient direct failures receive one bounded retry; this setting does not extend the overall Actor timeout. |
| `useApifyUnblockerFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `preferApifyUnblocker` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## rocketreach-alternative

Exact owner: `khadinakbar`. Identity: `kFR5TDChnXFhWBRu0`. State: `public_schema_verified`.

Build `0.2.8` / `GkiimjuMkL0bKc4ow`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/rocketreach-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `operation` | string; work_email_enrichment, public_profile_search | Choose work_email_enrichment for caller-supplied known contacts, or public_profile_search for a bounded public professional-profile search. Public-profile search is available only after its separately priced event becomes active; it never returns email or phone data. |
| `contacts` | array; minItems=1; maxItems=200 | Required for work_email_enrichment: one to 200 contacts you already know, each with fullName and companyDomain. An optional externalId is preserved for CRM matching and optional linkedInUrl is stored only as supplied provenance. Leave empty for public_profile_search. |
| `publicProfileSearch` | object | Required for public_profile_search: provide a professional search query or a public LinkedIn company URL, with optional title and location filters. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `maxProfiles` | integer; minimum=1; maximum=25 | For public_profile_search, process one to 25 returned public profiles. Each accepted complete profile is charged only after the separately priced public-profile event has become active. Defaults to 10. |
| `enrichmentMode` | string; find_and_verify, verify_supplied_email, candidate_only | VibeLeads allows verify_supplied_email only, for known lawfully held business emails. Address-pattern generation and finder modes are unavailable. Verify actual build behavior and source/use rights before execution. |
| `fallbackPolicy` | string; strict, dns_candidate | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `maxResults` | integer; minimum=1; maximum=200 | Hard cap on contacts processed in one run. Defaults to 25 and accepts 1 to 200 contacts, limiting maximum event charges to $0.12 per completed enrichment plus platform usage. This is not a search-result page limit because the Actor does not search a people database. |
| `maxCandidatesPerContact` | integer; minimum=1; maximum=5 | Candidate-address generation is unavailable in VibeLeads. This provider field is retained as structural metadata only; do not activate a candidate mode. |
| `includeMxValidatedCandidates` | boolean | Unavailable for enablement. Explicitly disable candidate-address output and verify the actual build, or decline the route. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## clearbit-alternative

Exact owner: `khadinakbar`. Identity: `SDthf1Y3UTZJYbtfr`. State: `public_schema_verified`.

Build `1.0.6` / `4DMeQ8BIyAdvLTAUs`; tag `latest`. Required keys: `companies`. [Full dated input schema](../schemas/clearbit-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companies` | array; minItems=1; maxItems=100 | Provide one to 100 companies you already selected, each with a public website domain such as apify.com. Optional companyName and externalId are carried through for an auditable CRM join. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `maxCompanies` | integer; minimum=1; maximum=100 | Set the hard cap on distinct valid company domains in this run, from 1 through 100. It defaults to 10, so company-enriched event charges cannot exceed the selected count plus platform usage. This is a result cap, not a request to crawl the wider web. |
| `maxPagesPerCompany` | integer; minimum=1; maximum=4 | Choose how many standard public routes to inspect: the homepage and then /about, /contact, and /team. It defaults to 3 and accepts 1 through 4 so source URLs stay bounded and reviewable. It does not enter portals, logins, or unrelated sites. |
| `includePublishedContacts` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `includeTechnologySignals` | boolean | When enabled, return a small list of technologies whose public HTML asset signatures were observed during the fetch. It defaults to true and labels these as page-level observations, not a complete technology inventory. It does not infer contracts, spending, buyer intent, or internal systems. |
| `useProxyFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=40 | Set the timeout for one public webpage request, from 5 through 40 seconds. It defaults to 20 seconds and is applied independently to every bounded route and retry. This does not extend the overall Actor timeout or allow unbounded retries. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## lusha-alternative

Exact owner: `khadinakbar`. Identity: `n7oPOKjLe1OLcfC5Q`. State: `public_schema_verified`.

Build `0.1.5` / `SJ8VLbuKsBuJpQ3lZ`; tag `latest`. Required keys: `contacts`. [Full dated input schema](../schemas/lusha-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `contacts` | array; minItems=1; maxItems=25 | Provide 1 to 25 people you already know, each with a full name and the employer’s public website domain. Optional companyName and externalId are carried through so the returned evidence can join back to your CRM or spreadsheet. Optional sourceUrls must be HTTPS pages on that same employer domain and are checked before standard public pages. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `maxContacts` | integer; minimum=1; maximum=25 | Hard cap on distinct valid contacts processed in one run. Defaults to 25 and accepts 1 to 25, limiting public-page collection and the maximum public-contact-found event charge. Duplicate name-and-domain entries are skipped before collection. Apify platform usage is billed separately to the caller. |
| `maxPagesPerContact` | integer; minimum=1; maximum=3 | How many public company-owned pages to inspect per contact, from 1 to 3. The Actor tries caller-provided source URLs first, then bounded standard public routes. Defaults to 3 to make the evidence set small and reviewable. It never crawls a whole website or follows a redirect to another domain. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=20 | Maximum wait for each direct or fallback public-page request. Defaults to 10 seconds and accepts 5 to 20 seconds, keeping a single run bounded. This does not extend the overall Actor timeout. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `responseFormat` | string; detailed, concise | Choose detailed to include a short surrounding role snippet for every name match, or concise to omit snippets while keeping source URLs and structured evidence. Defaults to detailed for human review. The setting does not change which pages are fetched. It does not infer a title, email, or phone number when evidence is absent. |
| `useApifyUnblockerFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## cognism-alternative

Exact owner: `khadinakbar`. Identity: `3vN9tAAV1lCR8vorN`. State: `public_schema_verified`.

Build `0.8.3` / `dMnMN74v3CVMayDas`; tag `latest`. Required keys: `accounts`. [Full dated input schema](../schemas/cognism-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `accounts` | array; minItems=1; maxItems=20 | Provide one to 20 known B2B company records to research from their public website. Each item needs companyDomain such as example.com and can retain a caller label, record ID, and up to five role keywords. The default is one stable public example and maxAccounts applies after validation. This is not a company-name search, contact-database lookup, or permission to submit private network targets. |
| `maxAccounts` | integer; minimum=1; maximum=20 | Safety cap for valid account records after normalization and duplicate removal. Enter an integer such as 5; values range from 1 to 20. The default 5 keeps first runs bounded. This is not the number of pages or an instruction to discover additional companies. |
| `maxPagesPerAccount` | integer; minimum=1; maximum=5 | Bound the fixed public-page set checked for each account: homepage, contact, about, team, then leadership. Enter 1 through 5; the default is 3 pages. Lower values reduce runtime and event-charge exposure. This is not a site-wide crawl depth or a request to follow arbitrary links. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=30 | Maximum time allowed for one public-page HTTP request before it is classified for retry or a truthful source outcome. Enter seconds such as 15; supported values are 5 through 30. The default balances first-run reliability and bounded compute. This is not the total Actor timeout or an unlimited retry setting. |
| `useApifyUnblockerFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `preferApifyUnblocker` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

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
| `useApifyUnblockerFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `preferApifyUnblocker` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## snov-io-alternative

Exact owner: `khadinakbar`. Identity: `8WS1icazgH7IGOhK7`. State: `public_schema_verified`.

Build `0.1.7` / `hCdFs1Q001s8rsXnS`; tag `latest`. Required keys: `targets`. [Full dated input schema](../schemas/snov-io-alternative.json).

This is an independently supplied alternative, not licensed access to the named vendor database or an official integration. Attribute its actual source and results accurately.

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `targets` | array; minItems=1; maxItems=25 | Provide 1 to 25 public company domains you are authorized to research. Each item accepts a hostname such as 'example.com' and optional known business context. This reads the homepage plus directly linked same-site contact, about, team, legal, privacy, or terms pages. It is not a personal-email list, private database query, or mailbox login. |
| `maxTargets` | integer; minimum=1; maximum=25 | Safety cap for accepted domain targets. Use 1 for a quick canary, and use up to 25 for one bounded batch. The default is 10 and values outside 1 to 25 are constrained. This is not a result-count or page-depth setting. |
| `maxPagesPerTarget` | integer; minimum=1; maximum=5 | Maximum number of public same-site pages to inspect after the homepage, including the homepage. The Actor follows only directly linked contact, about, team, legal, privacy, or terms pages. The default is 3 and values are bounded from 1 to 5. This does not crawl a site broadly or invent URL paths. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=45 | Time limit for one public page request, for example 20 seconds. The default is 20 and values are bounded from 5 to 45 seconds. Lower values make runs fail faster on unresponsive sites. This is not the whole-run timeout configured by Apify. |
| `useApifyUnblockerFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `preferApifyUnblocker` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
