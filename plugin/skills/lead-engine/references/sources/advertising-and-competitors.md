# Advertising and competitors source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [qualified business/contact-use gate](../contact-use.md). Provider result bounds are not recommended audience sizes; optional contact extraction must be disabled during discovery.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## meta-ad-library-scraper

Exact owner: `khadinakbar`. Identity: `B4RRM07yZQi5eczJG`. State: `public_schema_verified`.

Build `1.3.4` / `FF1QthHpneLKSXV5O`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/meta-ad-library-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Keyword or phrase to search in Meta Ad Library. Finds all ads mentioning this term across Facebook, Instagram, and Messenger. Example: 'nike running shoes', 'weight loss', 'crypto'. For MCP/API: pass a plain string. |
| `searchQueries` | array | Run several keyword searches in one go. Each keyword is scraped separately and results are merged. Example: ["nike", "adidas", "puma"]. Leave empty if using the single keyword above. |
| `metaAccessToken` | string | Your Meta Graph API access token with ads_read permission. Without it the actor uses web scraping mode (slower, fewer fields). Get a free token at: https://developers.facebook.com/tools/explorer/ Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `countries` | array | Countries where the ads were shown. Use ISO 3166-1 alpha-2 codes. Examples: US, GB, AU, CA, DE, FR, IN, BR. Default is US. For MCP: pass as array of strings, e.g. ["US", "GB"]. |
| `adStatus` | string; ALL, ACTIVE, INACTIVE | ACTIVE = ads currently running (best for competitor research). INACTIVE = stopped ads. ALL = both active and inactive. |
| `adType` | string; ALL, POLITICAL_AND_ISSUE_ADS, HOUSING_ADS, EMPLOYMENT_ADS, CREDIT_ADS | Type of ads to include. ALL covers standard commercial ads and works without a token. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `mediaType` | string; ALL, IMAGE, VIDEO, MEME, NONE | Filter by creative format. IMAGE = photo ads only. VIDEO = video ads only. ALL = no filter. |
| `startDate` | string | Only include ads that were running on or after this date. Format: YYYY-MM-DD. Example: 2024-01-01. Leave empty for no date filter. |
| `endDate` | string | Only include ads that were running on or before this date. Format: YYYY-MM-DD. Example: 2024-12-31. Leave empty for no date filter. |
| `maxResults` | integer; minimum=1; maximum=50000 | Maximum number of ad records to fetch. 50 = quick sample. 100 = standard run. 500–1000 = deep competitive analysis. Higher = more cost. Default: 100. |
| `sortBy` | string; impressions_desc, most_recent | How to order returned ads. impressions_desc = highest-reach ads first (best for finding what's working). most_recent = newest ads first. |
| `enrichAds` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `providerFallbackEnabled` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `onlyCount` | boolean | Returns only the total number of matching ads without downloading records. Use this to check how many ads exist before running a full scrape. Very fast and cheap. |
| `advertiserPageIds` | array | Get all ads from specific Facebook Pages by their Page ID. To find a Page ID: go to the page on Facebook → About → Page ID at the bottom. Example: ["123456789", "987654321"]. Use this instead of searchQuery to get all ads from a known brand. |
| `startUrls` | array | Paste URLs directly from facebook.com/ads/library after setting your filters in the browser. The actor extracts all filter parameters automatically. Also accepts Facebook Page URLs to scrape all ads from that page. |
| `adId` | string | Look up one specific ad by its Meta Ad Library ID (a real working example: 820508563651991). Use this to monitor a single ad or verify it still exists. Works with or without a Meta API token; a nonexistent or taken-down ad ID finishes with an INVALID_INPUT warning instead of data. |
| `contentLanguages` | array | Only return ads written in these languages. Use ISO 639-1 codes: en (English), es (Spanish), de (German), fr (French), pt (Portuguese). Leave empty for all languages. |
| `publisherPlatforms` | array | Filter by which Meta platform the ad ran on. Options: facebook, instagram, messenger, audience_network, threads. Default includes Facebook and Instagram. |
| `searchType` | string; KEYWORD_UNORDERED, KEYWORD_EXACT_PHRASE | KEYWORD_UNORDERED = all words must appear but in any order (broader). KEYWORD_EXACT_PHRASE = words must appear exactly as typed (narrower). |
| `metaAccessTokens` | array | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `proxyUrls` | array | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## facebook-ads-library-scraper

Exact owner: `khadinakbar`. Identity: `2yvvGyBDQXi41nPrW`. State: `public_schema_verified`.

Build `1.0.8` / `UOSk7cpC6C9BmnWO9`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/facebook-ads-library-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `mode` | string; auto, search, companyAds, adDetails | Choose how to find ads. Auto uses ad IDs first, then company inputs, then keyword search. |
| `searchTerms` | array | Keywords or exact phrases to search in the Meta Ad Library. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `companyPageIds` | array | Facebook Ad Library page IDs. Use the page_id returned by company search or provider docs examples. |
| `companyNames` | array | Company names to resolve to Facebook Ad Library page IDs before scraping ads. Page IDs are more reliable when you have them. |
| `adIds` | array | Meta Ad Library archive IDs for direct detail lookup. |
| `adUrls` | array | Direct public Facebook Ad Library URLs such as https://www.facebook.com/ads/library?id=3557423444566854. Login-only, restricted, or authorization-gated ads are skipped without being saved or billed. |
| `country` | string | Two-letter country code such as US, GB, DE, or ALL. Meta Ad Library provider APIs accept one country per request. |
| `status` | string; ACTIVE, INACTIVE, ALL | Whether to return active, inactive, or all ads. |
| `mediaType` | string; ALL, IMAGE, VIDEO, MEME, IMAGE_AND_MEME, NONE | Filter by creative media type exposed by the provider. |
| `adType` | string; all, political_and_issue_ads | Search all ads or only political and issue ads. |
| `searchType` | string; keyword_unordered, keyword_exact_phrase | Use unordered keyword matching for broad discovery or exact phrase matching for precise research. |
| `sortBy` | string; total_impressions, relevancy_monthly_grouped | Sort keyword results by estimated impressions or recent relevance. |
| `language` | string | Optional two-letter language code such as EN, ES, or FR. Mostly useful for company ads. |
| `startDate` | string | Optional impression start date in YYYY-MM-DD format. |
| `endDate` | string | Optional impression end date in YYYY-MM-DD format. |
| `maxResults` | integer; minimum=1; maximum=5000 | Maximum number of ad records to save. This is the primary cost cap; each saved ad charges the ad-scraped event. |
| `maxPagesPerSearch` | integer; minimum=1; maximum=100 | Maximum provider result pages per keyword, page ID, or company. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `includeRawData` | boolean | Debug option. Includes the raw provider payload on each dataset item. Leave disabled for normal runs to keep output small. |
| `requestTimeoutSecs` | integer; minimum=5; maximum=120 | Per-provider request timeout in seconds. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-ads-transparency-scraper

Exact owner: `khadinakbar`. Identity: `dCA5Hpf4BCQX094ZD`. State: `public_schema_verified`.

Build `1.5.7` / `raiLYK7Ov5mqBD4Xf`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/google-ads-transparency-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this field when the user provides a company domain (e.g. 'nike.com') or brand name (e.g. 'Nike'). Do NOT use this when passing a direct Ads Transparency URL — use startUrls instead. This is the primary way to find all ads a specific advertiser is running on Google. |
| `searchType` | string; domain, advertiserName | Use 'domain' when searchQuery is a website domain like 'example.com'. Use 'advertiserName' when searchQuery is a brand name like 'Nike'. Domain search is more precise; name search is broader. |
| `countryCode` | string | Filter ads shown in this country. Uses ISO 2-letter country codes. Default is 'US'. Use 'ANY' to see ads from all regions. |
| `adFormat` | string; ALL, TEXT, IMAGE, VIDEO | Filter by ad creative format. 'ALL' returns every format. 'TEXT' returns text-only search ads. 'IMAGE' returns display/banner ads. 'VIDEO' returns YouTube video ads. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of ads to extract per run. Each ad is one billable event at $0.003. Set to 50 for a quick competitive snapshot. Set to 200+ for comprehensive analysis. |
| `startUrls` | array | Use this field instead of searchQuery when you have specific Google Ads Transparency Center URLs for known advertisers (e.g. https://adstransparency.google.com/advertiser/AR12345). Leave empty to use the searchQuery field instead. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-ad-library-search-scraper

Exact owner: `khadinakbar`. Identity: `fdwr0hBXBdg5ya6tc`. State: `public_schema_verified`.

Build `1.1.3` / `DvyT54eRLuQCD6DKN`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-ad-library-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `advertisers` | array | Use this when you know the company or advertiser whose public ads you want to review. Enter a list of display names such as Microsoft or HubSpot. Defaults to Microsoft only when neither advertisers nor keywords is supplied. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `keywords` | array | Use this when you want public ads whose creative matches a phrase instead of one known advertiser. Enter plain keywords such as CRM software or data warehouse. Defaults to no keyword searches, and each keyword becomes an independent search. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `countries` | array | Use this when results should be limited to countries reported by the Ad Library. Enter ISO alpha-2 codes such as US, DE, or GB. Defaults to no country filter, while supplied codes are sent together to each search. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `startDate` | string | Use this when limiting ads by the beginning of their reported run window. Enter an ISO date such as 2026-01-01. Defaults to no lower date boundary and may be used with or without an end date. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `endDate` | string | Use this when limiting ads by the end of their reported run window. Enter an ISO date such as 2026-06-30. Defaults to no upper date boundary and must not be before startDate when both are supplied. This is not an expiry estimate or a relative date phrase. |
| `maxResults` | integer | Use this to cap the number of normalized ad records saved and billed in this run. Enter an integer such as 20 between 1 and 100. Defaults to 20, which also caps the primary event charge before platform usage. This is not a page number or a guarantee that the Ad Library contains that many matches. |
| `maxPagesPerSearch` | integer | Use this to bound provider pagination for every advertiser or keyword search. Enter an integer such as 2 between 1 and 10. Defaults to 1 page so the actor remains fast and cost-predictable. This is not an overall record limit because maxResults controls persisted ads. |
| `fetchAdDetails` | boolean | Use this when you need a second verified provider call per saved ad for richer public transparency data. Set true to request details and false to use the normalized search response only. Defaults to true and adds the documented detail-enrichment event only after a successful detail fetch. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `responseFormat` | string; concise, detailed | Use this to choose the token budget of each saved ad record. Select concise for core creative and transparency fields or detailed for bounded media and targeting arrays. Defaults to concise for agent-friendly output under the normal result cap. This is not a raw-provider-payload option and never exposes credentials. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## tiktok-ads-library-scraper

Exact owner: `khadinakbar`. Identity: `x5x84HE8Hq7EJ9VmS`. State: `public_schema_verified`.

Build `1.1.6` / `WVfQFRuKr95yYzE5J`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/tiktok-ads-library-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `libraryUrl` | string | Use this when you already have a filtered https://library.tiktok.com/ads URL to reproduce exactly. Paste a URL containing region, date range, and advertiser or keyword filters, for example https://library.tiktok.com/ads?region=DE&adv_name=adidas&query_type=1. Its filters override the individual search fields. Do not paste a TikTok profile, ad-detail, Creative Center, or Ads Manager URL. |
| `country` | string; AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK | Use this when building a public Ads Library search rather than pasting libraryUrl. Select an EEA country, Switzerland, or the United Kingdom where TikTok exposes the ad record, for example DE for Germany. Defaults to DE and also selects a matching residential browser session. This is not the country where your own company is located. |
| `searchQuery` | string | Use this when searching the public library by advertiser name or words in an ad, for example adidas. It accepts one phrase and defaults to adidas for a working health-check search. Choose searchType to say whether the phrase is a keyword or advertiser-name search. This is not an ad ID, TikTok handle, or profile URL. |
| `searchType` | string; keyword, advertiser | Use this to tell TikTok whether searchQuery is a keyword or an advertiser name. Choose keyword for words appearing in creatives and advertiser for a brand, for example adidas AG. Defaults to keyword and only changes the public library search interpretation. It does not perform an exact business-ID lookup; use advertiserBusinessId for that. |
| `advertiserBusinessId` | string | Use this when you know TikTok's advertiser business ID and need an exact advertiser filter. Enter digits such as 6885261436319171329; it can be combined with searchQuery. Leave blank when you only know a brand name or keyword. This is not an ad ID or a TikTok user ID. |
| `dateFrom` | string | Use this to set the inclusive beginning of the public-library date range in YYYY-MM-DD format, for example 2026-01-01. If omitted, the actor uses the preceding 90 days to keep searches bounded and predictable. Use an earlier date only when the target country and advertiser need historical coverage. This is not a time zone, timestamp, or an ad creation-date guarantee. |
| `dateTo` | string | Use this to set the inclusive end of the public-library date range in YYYY-MM-DD format, for example 2026-03-31. If omitted, the actor uses the time the run starts. It must be on or after dateFrom. This is not a duration, a relative date phrase, or a future schedule. |
| `maxResults` | integer; minimum=1; maximum=200 | Use this to cap validated Ads Library records written to the dataset. Enter an integer from 1 to 200; the default is 20 and each saved record charges the ad-scraped event. Keep it small for a quick check and raise it only for a bounded research job. This is not a page count or a guarantee that TikTok has that many matches. |
| `includeDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `requestTimeoutSecs` | integer; minimum=20; maximum=120 | Use this to set the navigation and public-library request timeout in seconds. Increase it only for a slow target response, not to bypass an access block. This is not the overall Apify run timeout. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## pinterest-ads-library-scraper

Exact owner: `khadinakbar`. Identity: `oKsJ4mO6RAVbvcrnz`. State: `public_schema_verified`.

Build `1.0.3` / `4cDVUHEfZN7whC0ko`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/pinterest-ads-library-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `country` | string; AT, BE, BG, BR, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, NO, PL, PT, RO, SK, SI, ES, SE, TR | Select the supported Pinterest repository market used to find disclosed ads, for example FR for France. Use a two-letter country code from the list. Defaults to FR for a working public repository search. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `startDate` | string | Set the inclusive beginning of the public repository window in YYYY-MM-DD format, for example 2026-08-01. Defaults to seven days before the run begins when omitted. The maximum window is 31 calendar days. This is not a relative date phrase or an ad creation-date guarantee. |
| `endDate` | string | Set the inclusive end of the public repository window in YYYY-MM-DD format, for example 2026-08-10. Defaults to the run date when omitted. It must be on or after startDate and within the 31-day window. This is not an overall Actor timeout. |
| `advertiserName` | string | Optionally narrow the public repository to a disclosed advertiser name, for example Tommy Hilfiger. Leave blank to browse the selected market and date window. Names are matched by Pinterest's repository and may not be exact. This is not a Pinterest username, ad ID, or private account ID. |
| `category` | string; ALL, ANIMALS, ARCHITECTURE, ART, BEAUTY, CHILDRENS_FASHION, DESIGN, DIY_AND_CRAFTS, EDUCATION, ELECTRONICS, ENTERTAINMENT, EVENT_P | Optionally filter by Pinterest's public ad category, for example HOME_DECOR. Defaults to ALL and only controls the repository filter. Use it for category-level creative research, not to classify the returned creative yourself. This is not a free-text keyword search. |
| `gender` | string; ALL, FEMALE, MALE, UNSPECIFIED | Optionally apply the repository's disclosed gender filter: ALL, FEMALE, MALE, or UNSPECIFIED. Defaults to ALL. It reflects Pinterest's public ad-library filter rather than inferred user demographics. This is not a guarantee that every returned ad targets only that gender. |
| `age` | string; ALL, AGE_18_24, AGE_25_34, AGE_35_44, AGE_45_49, AGE_50_54, AGE_55_64, AGE_65_PLUS | Optionally apply Pinterest's public age-bucket filter, for example AGE_25_34. Defaults to ALL. Use the public filter values exactly as shown. This is not an inferred audience-age estimate or a free-text age range. |
| `maxResults` | integer; minimum=1; maximum=24 | Cap the validated public ad records saved to the dataset. Enter an integer from 1 to 24; the default is 24 and each saved record charges the ad-scraped event. Keep it low for a quick evidence check. This is not a guarantee that Pinterest has that many matches. |
| `requestTimeoutSecs` | integer; minimum=20; maximum=120 | Set the browser navigation and public repository request timeout in seconds. Enter 20 to 120; the default is 60. Increase it only for a slow public response, not to bypass access controls. This is not the whole Actor run timeout. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
