# Creators and agencies source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

## instagram-niche-influencer-finder

Exact owner: `khadinakbar`. Identity: `LHCEKswaihgmShn5p`. State: `public_schema_verified`.

Build `1.0.6` / `6mVmtexfF84TBIfYe`; tag `latest`. Required keys: `topics`. [Full dated input schema](../schemas/instagram-niche-influencer-finder.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `topics` | array | Use this to describe the niche each influencer should match. Enter one or more plain phrases such as 'vegan skincare', 'home coffee brewing', or 'trail running gear'. The actor searches public Instagram profiles for each |
| `maxInfluencers` | integer; minimum=1; maximum=500 | Use this to cap the ranked influencer shortlist and its billable rows. Enter a whole number from 1 to 500; the default is 25. The actor enriches candidates until this many influencers pass the follower, engagement, and c |
| `minFollowers` | integer; minimum=0 | Use this to exclude small or spammy accounts from the shortlist. Enter a whole number such as 5000; the default is 1000, a common nano-influencer floor. Influencers below the threshold are filtered out before anything is |
| `maxFollowers` | integer; minimum=1 | Use this to keep the shortlist inside an affordable creator tier. Enter a whole number such as 100000; the default is 500000, which includes most mid-tier creators. Influencers above the threshold are filtered out before |
| `minEngagementRatePct` | number; minimum=0; maximum=100 | Use this to drop creators whose audience rarely interacts. Enter a percentage such as 1.5; the default is 0, which keeps every influencer. The rate is average likes plus comments per recent post divided by followers. Rec |
| `requireEmail` | boolean | Use this when outreach-ready contacts are required. Enable it to keep only influencers that expose an email in their public business contact field or biography; the default is off. The actor reads public data only and ca |
| `requireVerified` | boolean | Use this when the blue check is a campaign requirement. Enable it to keep only publicly verified accounts; the default is off. Verified status comes from the public profile metadata returned by the data provider. It does |
| `sortBy` | string; engagement-rate, followers, niche-score | Use this to choose the order of the ranked shortlist. Choose engagement-rate for average interaction per follower, followers for raw audience size, or niche-score for the combined relevance ranking; the default is engage |
| `postsPerInfluencer` | integer; minimum=6; maximum=24 | Use this to tune how many recent posts feed the engagement average. Enter 6 to 24; the default is 12, about one page of posts. More posts give a steadier engagement rate but each extra page adds provider time and platfor |
| `maxSearchPagesPerTopic` | integer; minimum=1; maximum=10 | Use this advanced control to bound profile-search depth for each topic. Enter an integer from 1 to 10; the default is computed from maxInfluencers so the actor usually gathers about two to three candidates per saved infl |
| `outputMode` | string; full, compact | Use this when selecting concise agent-friendly records or fuller research records. Choose compact for core scoring, count, and contact fields, or full for biography, links, and provider provenance fields; the default is  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## instagram-user-search-scraper

Exact owner: `khadinakbar`. Identity: `oUoYvWUxieBb8HVE1`. State: `public_schema_verified`.

Build `1.1.4` / `TAYvcGgqU1jEghIG9`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/instagram-user-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array; maxItems=50 | Keywords used to find public Instagram users, one keyword phrase per entry (e.g., "fitness coach" or "vegan bakery london"). Plain natural-language phrases work best; avoid hashtags and URLs. Runs each keyword independen |
| `maxResultsPerQuery` | integer; minimum=1; maximum=100 | Upper bound on unique users saved for each keyword after filters are applied. Defaults to 20 and cannot exceed 100. Lower it to cap Pay per event charges for exploratory runs. |
| `maxResults` | integer; minimum=1; maximum=1000 | Global cap on unique users saved across all keywords in one run. Defaults to 200. The actor stops early once this many users have been saved, even if keywords remain. |
| `minimumFollowers` | integer; minimum=0 | Excludes users with fewer than this many followers, e.g., 10000 keeps accounts with 10K or more. Defaults to 0, which keeps everyone. Use with maximumFollowers to define an audience-size band. |
| `maximumFollowers` | integer; minimum=0 | Excludes users with more than this many followers, e.g., 100000 keeps accounts under 100K. Defaults to 0, which sets no upper bound. Useful for finding micro-influencers instead of celebrities. |
| `verifiedOnly` | boolean | Keeps only Instagram-verified accounts (blue check) in the results. Defaults to false so unverified niche accounts are included. Turn on when assembling brand-safe partnership shortlists. |
| `accountType` | string; any, personal, business, professional | Filters by Instagram account class: any keeps all, personal keeps non-professional profiles, business keeps business accounts, professional keeps creator and professional accounts. Defaults to any. Category detail for pr |
| `includePrivateProfiles` | boolean | Also saves private (locked) accounts when they match the keyword. Defaults to false because private accounts hide most public data. Turn on only when the username itself is the deliverable. |
| `parseContacts` | boolean | Extracts public email addresses and phone numbers found in each user's bio text and bio links into separate contact fields. Defaults to true; parsing is text-only and never guesses missing values. Contacts are optional n |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## instagram-profile-stats-scraper

Exact owner: `khadinakbar`. Identity: `N3rc0uhS4SJcNE9fb`. State: `public_schema_verified`.

Build `0.0.3` / `N5e7DuSInN8GUvrHE`; tag `latest`. Required keys: `usernames`. [Full dated input schema](../schemas/instagram-profile-stats-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `usernames` | array | Look up public Instagram stats for these profiles. Accepts bare usernames (natgeo), @handles (@nasa), or full profile URLs (https://www.instagram.com/instagram/). Each value becomes one dataset row. |
| `deduplicate` | boolean | Collapse repeated handles to a single request after normalization. Keep this on for CRM lists that repeat the same creator. |
| `maxItems` | integer; minimum=1 | Process at most this many input tokens, in list order, before stopping. Use it as the run-wide cost ceiling for a bulk roster. |
| `maxRequestRetries` | integer; minimum=0; maximum=10 | Extra attempts per profile when Instagram returns a transient empty or challenge response. Default 2 keeps bulk runs moving. |
| `requestTimeoutSecs` | integer; minimum=10; maximum=120 | Seconds allowed for one profile stats request before the next retry. Default 30 is enough for the public web profile endpoint. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## instagram-contact-scraper

Exact owner: `khadinakbar`. Identity: `TtmjIptjSXepkD0fP`. State: `public_schema_verified`.

Build `0.1.6` / `xtKDyccsoDaEJvLjb`; tag `latest`. Required keys: `usernames`. [Full dated input schema](../schemas/instagram-contact-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `usernames` | array | One or more Instagram accounts to extract contact info from. Accepts bare usernames ('nike'), @-handles ('@nasa'), or full profile URLs ('https://instagram.com/hubspot'). Business and creator accounts are most likely to  |
| `onlyWithContact` | boolean | When true, only profiles that have at least one email or phone number are pushed to the dataset. Profiles with no contact data are silently skipped (not billed). Useful for lead-gen pipelines where you only want actionab |
| `maxItems` | integer; minimum=1 | Stop after processing this many profiles. Useful for budget control on large lists. Defaults to unlimited (all supplied usernames). |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## tiktok-user-search-scraper

Exact owner: `khadinakbar`. Identity: `HrqooIYLDycsbyGEP`. State: `public_schema_verified`.

Build `0.1.4` / `XemQURVi5Ph7zKaq7`; tag `latest`. Required keys: `searchQueries`. [Full dated input schema](../schemas/tiktok-user-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Use this when you want to find TikTok users or creators by keyword, brand, niche, or person name. Accepts one query per line, for example Taylor Swift, beauty creator, or soccer coach. Defaults to the prefilled example f |
| `maxProfilesPerQuery` | integer; minimum=1; maximum=10000 | Use this to cap how many creator profile rows are saved for each search query. Accepts integers from 1 to 10000. Defaults to 50 and the prefill is 10 for fast tests. This is the main per-query billing guard. |
| `maxPagesPerQuery` | integer; minimum=1; maximum=500 | Use this as a safety cap for provider pagination on each TikTok user search. Accepts integers from 1 to 500. Defaults to 10 and the prefill is 1 for quick checks. Not a result limit by itself. |
| `maxTotalProfiles` | integer; minimum=1; maximum=50000 | Use this to cap the whole run across all search queries. Accepts integers from 1 to 50000. Defaults to 5000 and the prefill is 50. This prevents accidental overbilling on large keyword batches. |
| `minFollowerCount` | integer; minimum=0 | Use this to keep only creator profiles at or above a follower threshold. Accepts 0 or any positive integer, for example 10000 for micro-influencer discovery. Defaults to 0, which keeps all returned profiles. This filter  |
| `verifiedOnly` | boolean | Use this when you only want TikTok profiles that are marked verified or have a provider verification label. Defaults to false so discovery is broad. Set true for brand safety, public figures, or official creator research |
| `excludePrivateAccounts` | boolean | Use this to skip profiles marked private by TikTok or the provider response. Defaults to false because private-account metadata can still help discovery workflows. Set true when you only want public creator candidates. T |
| `trim` | boolean | Use this to request smaller provider payloads when supported. Defaults to false so profile fields such as bio and verification are preserved. Turn it on only for speed tests where compact profile rows are acceptable. Thi |
| `includeRawData` | boolean | Use this when you need the original provider response attached to each dataset row. It helps debug field drift or build custom parsers. Defaults to false. Not recommended for AI-agent runs because raw payloads are large. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## tiktok-shop-creators-scraper

Exact owner: `khadinakbar`. Identity: `HN6feG9AqX0gYuhy2`. State: `public_schema_verified`.

Build `0.1.4` / `4Zwf6UUWLcWvRa0Fp`; tag `latest`. Required keys: `searchQueries`. [Full dated input schema](../schemas/tiktok-shop-creators-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Use this when you want to find TikTok creators by niche, product category, brand, or creator style. Accepts one query per line, for example tiktok shop finds, beauty creator, or kitchen gadgets. Defaults to the prefilled |
| `maxProfilesPerQuery` | integer; minimum=1; maximum=10000 | Use this to cap how many TikTok user-search profiles are inspected for each query. Accepts integers from 1 to 10000. Defaults to 50 and the prefill is 25 for fast tests. This is a scan cap, not the final saved creator co |
| `maxPagesPerQuery` | integer; minimum=1; maximum=500 | Use this as a safety cap for provider pagination on each TikTok user search. Accepts integers from 1 to 500. Defaults to 10 and the prefill is 1 for quick checks. Not a result limit by itself. |
| `maxProfilesScanned` | integer; minimum=1; maximum=50000 | Use this to cap public showcase checks across the whole run. Accepts integers from 1 to 50000. Defaults to 500 and the prefill is 25. This is the main billing guard for showcase lookup costs. |
| `maxTotalCreators` | integer; minimum=1; maximum=50000 | Use this to cap saved TikTok Shop creator rows across all queries. Accepts integers from 1 to 50000. Defaults to 50 and the prefill is 10. This prevents accidental overbilling on broad keyword batches. |
| `requireShowcaseProducts` | boolean | Use this to save only creators with public TikTok Shop showcase products. Defaults to true because this actor is for TikTok Shop creator discovery. Set false to save searched creator profiles even when no showcase produc |
| `minFollowerCount` | integer; minimum=0 | Use this to keep only creator profiles at or above a follower threshold. Accepts 0 or any positive integer, for example 10000 for micro-influencer discovery. Defaults to 0, which keeps all returned profiles. This filter  |
| `verifiedOnly` | boolean | Use this when you only want TikTok profiles marked verified or with a provider verification label. Defaults to false so discovery is broad. Set true for brand safety, public figures, or official creator research. Not all |
| `excludePrivateAccounts` | boolean | Use this to skip profiles marked private by TikTok or the provider response. Defaults to true because private accounts are weak TikTok Shop outreach candidates. Set false if private-account metadata still helps your rese |
| `maxShowcaseProductsPerCreator` | integer; minimum=1; maximum=50 | Use this to cap showcase products attached to each creator. Accepts integers from 1 to 50. Defaults to 5 for campaign shortlisting. This controls row size and does not change how many profiles are checked. |
| `maxShowcasePagesPerCreator` | integer; minimum=1; maximum=5 | Use this to cap provider pagination for each creator showcase. Accepts integers from 1 to 5. Defaults to 1 for predictable cost. Increase only when you need more public product examples per creator. This is not a product |
| `showcaseRegion` | string; US, GB, DE, FR, IT, ID, MY, MX, PH, SG, ES, TH, VN, BR, JP, IE | Use this to choose the TikTok Shop region for public showcase product enrichment. Accepts supported shop regions such as US, GB, DE, FR, IT, ID, MY, MX, PH, SG, ES, TH, VN, BR, JP, or IE. Defaults to US. Not a creator-lo |
| `trim` | boolean | Use this to request smaller user-search payloads when supported. Defaults to false so profile fields such as bio and verification are preserved. Turn it on only for speed tests where compact profile rows are acceptable.  |
| `includeRawData` | boolean | Use this when you need the original user-search provider response attached to each dataset row. It helps debug field drift or build custom parsers. Defaults to false. Not recommended for AI-agent runs because raw payload |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## youtube-channel-search-scraper

Exact owner: `khadinakbar`. Identity: `vlAeQZCl9NzbiAwAU`. State: `public_schema_verified`.

Build `0.1.3` / `f9TNe3N5aaz0X5b0y`; tag `latest`. Required keys: `searchQueries`. [Full dated input schema](../schemas/youtube-channel-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Free-text YouTube search terms used to find public channels, for example 'personal finance' or 'fitness coach'. Each query is searched independently and unique channels are merged. Prefills one example query. This is not |
| `searchUrls` | array | Optional youtube.com/results URLs that already contain a search_query, for example 'https://www.youtube.com/results?search_query=lofi'. The Actor extracts the keyword and runs a channel-only search. Defaults to empty. Th |
| `maxResultsPerQuery` | integer; minimum=1; maximum=200 | Maximum unique channels saved for each search query after pagination. Example: 10. Range 1–200; default 10. This is not a global run cap — see maxResultsTotal. |
| `maxResultsTotal` | integer; minimum=1; maximum=500 | Hard cap on unique channels billed and saved across every query in this run. Example: 50. Range 1–500; default 50. Extra matches after the cap are skipped. This is not the per-query limit. |
| `minSubscribers` | integer; minimum=0; maximum=1000000000 | Keep channels whose public subscriber count is at least this number, for example 10000. Default 0 (no floor). Channels that hide subscriber counts are kept. This is not a YouTube API quota. |
| `maxSubscribers` | integer; minimum=0; maximum=1000000000 | Keep channels whose public subscriber count is at most this number, for example 1000000. Default 0 means no ceiling. Hidden counts are kept. This is not a billing cap. |
| `verifiedOnly` | boolean | When true, keep only search cards that show YouTube's verified badge. Default false returns verified and unverified public channels. This does not confirm official brand ownership beyond the public badge. |
| `country` | string | Two-letter ISO country code used as YouTube geo context (gl) and residential proxy country, for example 'US' or 'GB'. Defaults to 'US'. This is not a language code — see language. |
| `language` | string | Two-letter ISO language code used as YouTube interface language (hl), for example 'en' or 'es'. Defaults to 'en'. This is not a country code — see country. |
| `enrichProfiles` | boolean | When true, each found channel is fetched for About-page fields (description, total views, joined date, country, links) and billed as one extra channel-enriched event. Default false returns search-card fields only. Leave  |
| `fallbackMode` | string; auto, never, always | Controls when the managed fallback runs after direct YouTube HTTP. 'auto' (default) uses residential YouTube first and falls back only if blocked. 'never' stays on direct HTTP. 'always' skips direct scraping. This is not |
| `proxyConfiguration` | object | Proxy settings for the direct YouTube HTTP scrape. Residential proxies are enabled by default because datacenter IPs are blocked. Country follows the country field unless overridden. This is not the managed fallback. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## youtube-channel-scraper

Exact owner: `khadinakbar`. Identity: `BGuQRhPiGRWOZzqyr`. State: `public_schema_verified`.

Build `0.1.9` / `agbHdcVyROAG7D0bi`; tag `latest`. Required keys: `channelUrls`. [Full dated input schema](../schemas/youtube-channel-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `channelUrls` | array | Use this when you know the YouTube channels to inspect. Accepts full URLs, @handles, /channel IDs, or bare handles such as @Apify. Defaults to one small Apify channel test. Not for keyword search; use youtube-search-scra |
| `maxVideosPerChannel` | integer; minimum=0; maximum=100 | Use this to include recent regular videos from each channel. Set 0 for channel profile only, 5 for fast agent calls, or up to 100 for deeper exports. Defaults to 5. Not a global row limit; it applies separately to each c |
| `includeShorts` | boolean | Use this when Shorts are part of the channel audit. If true, the actor also requests Shorts up to maxShortsPerChannel. Defaults to false for faster health checks. Not for global Shorts discovery; use youtube-shorts-scrap |
| `maxShortsPerChannel` | integer; minimum=0; maximum=50 | Use this to cap Shorts collected when includeShorts is true. Accepts 0 to 50 and defaults to 0. Keep it small for MCP calls. Not used when includeShorts is false. |
| `sortVideosBy` | string; latest, popular | Use this to choose how channel videos are listed. Accepted values are latest or popular, with latest as the default. The setting applies to regular videos and provider-backed Shorts when supported. Not a relevance search |
| `providerMode` | string; auto, direct, providerOnly | Use this to control the managed provider path. auto tries managed public-data routes when the owner secret is configured and falls back to direct YouTube. direct skips providers. providerOnly soft-exits if no provider ke |
| `country` | string | Use this to localize YouTube responses with a two-letter country code. Example: US, GB, PK, or DE. Defaults to US. Not a filter for channels by country. |
| `language` | string | Use this to localize text labels returned by YouTube. Example: en, es, de, or fr. Defaults to en. Not a translation feature for channel descriptions. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## youtube-channel-email-extractor

Exact owner: `khadinakbar`. Identity: `IRx3DJZeQdk6DhAtn`. State: `public_schema_verified`.

Build `1.2.4` / `ae64IIxg0JUbgobaa`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/youtube-channel-email-extractor.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `channelUrls` | array | Use this field when the user provides specific YouTube channel names, handles, or URLs (e.g. '@mkbhd', 'youtube.com/@MrBeast', a list of creators). Accepts @handle URLs, /channel/ID URLs, or video URLs. Each URL = 1 chan |
| `searchQueries` | array | Use this field when the user describes a niche, topic, or industry instead of specific channels (e.g. 'fitness influencers', 'tech reviewers', 'cooking YouTube channels'). The actor searches YouTube and auto-discovers ma |
| `maxResults` | integer; minimum=1; maximum=10000 | How many YouTube channels to extract contact data from in total (across all URLs and search queries combined). Set to 10–20 for a quick test. Set to 500–5000 for bulk influencer outreach lists. A channel with a public em |
| `scrapeWebsite` | boolean | When enabled, the actor visits the website linked on each channel's About page and scrapes it for additional email addresses and contact info. This is the most powerful feature — many creators list their business email o |
| `followLinkAggregators` | boolean | When enabled, the actor follows link aggregator pages (Linktree, Beacons.ai, Bio.link, Campsite, Bento, etc.) found in channel About sections. These pages often contain business emails, booking links, and all social prof |
| `proxyConfiguration` | object | HTTP proxy settings. The actor uses Apify Residential proxies by default — these are required for reliable YouTube access. Only change this if you have a specific proxy provider or want to use your own proxies. Leave def |
| `unlockBusinessInquiryEmail` | boolean | Most users leave this OFF. Default public scrape already reads About text, mailto links, websites, and Linktree-style pages. Turn this ON only when the user explicitly wants the business inquiry email behind YouTube's "V |
| `youtubeSessionCookies` | string | Required only when unlockBusinessInquiryEmail is true. Paste a logged-in YouTube/Google session as a Cookie header string (for example SAPISID=…; __Secure-3PSID=…; LOGIN_INFO=…) or a JSON object of {cookieName: value}. U |
| `maxInquiryUnlocksPerRun` | integer; minimum=1; maximum=50 | Maximum number of channels for which the optional View-email unlock may be attempted in this run (only when unlock is on and the public path found no email). Use 1–5 for tests. Raise only when the user asks for bulk gate |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## social-media-influencer-scraper

Exact owner: `khadinakbar`. Identity: `qN3wwWqgKBCBEty0P`. State: `public_schema_verified`.

Build `0.6.3` / `0kGNpmugjlHDxuRUx`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/social-media-influencer-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `platforms` | array | Use this to choose which public social platforms to search. Select any combination of instagram, tiktok, and youtube; all three are the default. Discovery runs separately on each selected platform. This is not an account |
| `searchQueries` | array | Use this when you want to discover public creators by niche, name, or brand query. Enter one query per line, for example 'fitness coach' or 'Miami food creator'. Leave it empty when enriching known profile URLs; an empty |
| `profileUrls` | array | Use this when you already know public creator profiles to enrich. Accepts profile URLs or tagged handles such as 'instagram:@natgeo' and 'youtube:@Apify'. Leave it empty for keyword discovery. This does not accept post,  |
| `maxProfilesPerQuery` | integer; minimum=1; maximum=50 | Use this to cap returned profiles for every query-platform pair. Choose 5 for fast agent runs or up to 50 for deeper discovery. Defaults to 10 and is applied before the global run cap. This is not a follower-count filter |
| `maxTotalProfiles` | integer; minimum=1; maximum=500 | Use this to set a hard ceiling on profiles saved and charged in this run. Choose a number from 1 to 500; the default is 100. The actor stops gracefully when it reaches this cap. This is not a request-page count. |
| `minFollowerCount` | integer; minimum=0; maximum=2147483647 | Use this to keep creators with at least a specified public follower or subscriber count. Enter a whole number such as 5000; 0 keeps every returned public profile. Defaults to 0 and applies after provider retrieval. This  |
| `verifiedOnly` | boolean | Use this when a platform verification signal is required for the shortlist. Set true to keep only profiles whose provider response marks them verified. Defaults to false because verification coverage differs by platform. |
| `excludePrivateAccounts` | boolean | Use this to remove profiles explicitly marked private by a data provider. It defaults to true so output remains useful for public influencer research. A missing privacy flag does not imply that an account is public. This |
| `countryCode` | string | Use this to localize YouTube creator discovery with a two-letter country code. Enter values such as US, GB, or PK; the default is US. It affects YouTube search results only. This is not a creator-location filter. |
| `includeRawData` | boolean | Use this only for provider-schema diagnostics when you need the original public response alongside normalized fields. It defaults to false to keep dataset records compact for agents and CSV exports. Raw payloads can chan |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
