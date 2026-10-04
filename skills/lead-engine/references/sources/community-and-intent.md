# Community and intent source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

## reddit-search-scraper

Exact owner: `khadinakbar`. Identity: `j1gQL2JlzmGKxrPzJ`. State: `public_schema_verified`.

Build `1.0.5` / `kDtqTaEphsfHAwdfH`; tag `latest`. Required keys: `searchQuery`. [Full dated input schema](../schemas/reddit-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this when the user wants to search public Reddit posts by keyword, topic, brand, phrase, or question. Accepts plain text such as 'OpenAI API pricing' or 'CRM recommendations for startups'. Required; blank strings ret |
| `withinSubreddit` | string | Optional subreddit scope for the search query. Accepts a subreddit name with or without r/ prefix, such as 'learnpython' or 'r/MachineLearning'. Leave blank to search across Reddit. This is not a post URL field. |
| `maxResults` | integer; minimum=1; maximum=10000 | Maximum number of Reddit search result records to return. Each saved result is charged as one result event. Defaults to 25, minimum 1, maximum 10000. Use small values for smoke tests and larger values for monitoring or r |
| `sortBy` | string; relevance, new, top, comments | How to sort Reddit search results. Use 'relevance' for the closest keyword match, 'new' for recent posts, 'top' for highly scored posts, or 'comments' for heavily discussed posts. Defaults to relevance. This affects sear |
| `timeFilter` | string; day, week, month, year, all | Time window for Reddit search results. Use 'day', 'week', 'month', 'year', or 'all'. Defaults to month for useful recent monitoring results. This is a search filter, not a post creation date guarantee. |
| `postDateLimit` | string | Optional post creation cutoff applied after provider search results are returned. Use ISO 8601 format such as '2026-01-01' or '2026-01-01T00:00:00Z'. Leave blank to keep all provider results. Invalid dates are ignored an |
| `includeNsfw` | boolean | When enabled, includes Reddit posts marked NSFW in the dataset. Disabled by default to keep monitoring and business research outputs safer. This does not bypass private, quarantined, deleted, or login-only content. NSFW  |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## reddit-posts-search-scraper

Exact owner: `khadinakbar`. Identity: `hvkaKLQvHrNYLqmgZ`. State: `public_schema_verified`.

Build `0.1.6` / `sMlUVl1QPxO6O8fab`; tag `latest`. Required keys: `queries`. [Full dated input schema](../schemas/reddit-posts-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | Keywords, phrases, brands, competitors, products, pain points, or natural-language topics to search on Reddit. AI agents should put the main user request here. |
| `subreddits` | array | Optional subreddit names or URLs. Leave empty for global Reddit search. When set, every query is searched inside each subreddit. Accepts r/SEO, SEO, or https://www.reddit.com/r/SEO. |
| `sort` | string; relevance, new, top, comments, hot | How Reddit orders matching posts. Relevance is best for research and AI agents, new is best for monitoring, top is best for high-signal historical posts, comments finds active discussions, and hot finds currently trendin |
| `timeRange` | string; hour, day, week, month, year, all | Time window for search results. Use week or month for current market research, year or all for evergreen SEO research. |
| `maxPosts` | integer; minimum=1; maximum=200000 | Maximum number of unique post records to return across all queries and subreddits. Billing stops when this cap is reached. |
| `includeTopComments` | boolean | When true, each post record includes a compact topComments array. Use this for AI summaries and sentiment analysis. Leave off for faster, cheaper post-only extraction. |
| `maxTopCommentsPerPost` | integer; minimum=1; maximum=100 | Maximum number of top comments to embed in each post when includeTopComments is enabled. |
| `postDateLimit` | string | Optional ISO date. Example: 2026-01-01. Posts older than this are skipped after retrieval. |
| `includeNsfw` | boolean | Disabled by default for business research and AI-agent workflows. Enable only when you intentionally need NSFW Reddit content. |
| `proxy` | object | Proxy settings. Defaults to Apify Residential proxies because Reddit often blocks datacenter IPs. Leave unchanged unless you know your target and plan requirements. |
| `redditClientId` | string | Optional Reddit app client ID. Leave blank to use owner-managed access when configured. Create a free app at reddit.com/prefs/apps if you want to use your own credentials. |
| `redditClientSecret` | string | Credential/access field. Use secure authorized setup only if this feature requires it; never include a credential in files or chat. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## reddit-comments-search-scraper

Exact owner: `khadinakbar`. Identity: `LBOeAB0frqbihEMl0`. State: `public_schema_verified`.

Build `1.0.5` / `ppl0DrQemrAAKJ44Z`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/reddit-comments-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | Use this when you need to find public Reddit comments containing one or more phrases. Pass phrases such as "AI coding assistant" or "best standing desk". Defaults to "artificial intelligence" and accepts at most 20 disti |
| `subreddit` | string | Use this to search comments within one public subreddit. Pass a name such as "MachineLearning" or "r/MachineLearning". Defaults to all of Reddit and accepts only one community name. This is not a subreddit URL or a list  |
| `maxComments` | integer; minimum=1; maximum=1000 | Use this to cap unique comments saved across every query. Pass an integer such as 100. Defaults to 100 and accepts 1 through 1000, which also caps comment-event charges. This is not a number of comments per post or a req |
| `sort` | string; relevance, new, top, comments | Use this to choose Reddit's ordering for matching comments. Choose relevance, new, top, or comments; for example, "new" prioritizes recent matches. Defaults to relevance. This does not analyze sentiment or change Reddit' |
| `time` | string; hour, day, week, month, year, all | Use this to restrict comment search to a Reddit time window. Choose hour, day, week, month, year, or all; for example, "month". Defaults to all. This is not an exact date-range filter and Reddit may cap deep search pagin |
| `includeNsfw` | boolean | Use this only when adult-marked public Reddit content is appropriate for the research task. Pass true to retain a result explicitly marked NSFW. Defaults to false. This does not bypass Reddit safety controls or access pr |
| `responseFormat` | string; concise, detailed | Use this to balance agent context size against diagnostic metadata. Choose concise for core text, authorship, score, and links, or detailed for moderation and award fields; for example, "concise". Defaults to concise. Th |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## reddit-subreddit-search-scraper

Exact owner: `khadinakbar`. Identity: `dp0G62SqSsVlv77HJ`. State: `public_schema_verified`.

Build `1.2.4` / `wMPDza8ZIxJGwKARQ`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/reddit-subreddit-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array | Use this when you need to discover public Reddit communities from keywords. Pass one or more phrases such as "machine learning" or "personal finance". Defaults to "artificial intelligence" and accepts at most 20 distinct |
| `maxSubreddits` | integer; minimum=1; maximum=100 | Use this to cap the total unique communities returned across every query. Pass an integer such as 25. Defaults to 25 and accepts 1 through 100, which also caps event charges. This is not a number of posts, comments, or r |
| `minSubscribers` | integer; minimum=0; maximum=1000000000 | Use this to filter out communities below a subscriber threshold. Pass an integer such as 10000. Defaults to 0 and accepts 0 through 1,000,000,000; communities with an unavailable count do not pass a positive threshold. T |
| `sort` | string; relevance, subscribers, activity, newest | Use this to choose how matching communities are ordered after deduplication. Choose relevance, subscribers, activity, or newest; for example, "subscribers" ranks the largest known communities first. Defaults to relevance |
| `includeNsfw` | boolean | Use this only when adult-marked public communities are appropriate for the research task. Pass true to include a community whose Reddit metadata is marked NSFW, for example true. Defaults to false. This does not bypass R |
| `responseFormat` | string; concise, detailed | Use this to balance agent context size against metadata depth. Choose concise for identifiers, counts, URLs, and status, or detailed for descriptions and artwork URLs; for example, "concise". Defaults to concise. This do |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-post-search-scraper

Exact owner: `khadinakbar`. Identity: `yMNWUCINasvKFmMED`. State: `public_schema_verified`.

Build `1.0.11` / `aAGw0s76JbqJnDzJ7`; tag `latest`. Required keys: `query`. [Full dated input schema](../schemas/linkedin-post-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `query` | string | Keyword or phrase to search for in public LinkedIn posts. The actor uses Google-indexed LinkedIn post results via the primary managed public-data route, so results are best-effort and depend on public indexing. Use a foc |
| `datePosted` | string; any, last-hour, last-day, last-week, last-month, last-year | Optional freshness filter applied by the upstream provider to Google-indexed LinkedIn results. Recent windows can be sparse because the provider can only return public posts that Google has indexed. Use last-week or last |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum number of post records to save to the dataset. This is also the hard cap for billable post-found events. Higher values may require multiple provider pages because the primary managed public-data route returns pag |
| `maxProviderPages` | integer; minimum=1; maximum=60 | Advanced safety valve for pagination. Leave at 60 for normal runs. Lower this when you are testing, debugging cursor behavior, or intentionally limiting upstream provider calls. |
| `startCursor` | string | Optional cursor returned by a previous run. Paste the value from the run summary to continue from a later provider page. Leave empty for the first page of results. |
| `includeComments` | boolean | Include the public comments returned by the provider in each dataset record. Disable this for smaller records when you only need post-level metadata and engagement counts. |
| `outputMode` | string; full, compact | Compact mode keeps the most common fields for quick monitoring and LLM workflows. Full mode also includes images, media URLs, provider cursor context, and comments when enabled. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-posts-scraper

Exact owner: `khadinakbar`. Identity: `pcdyX7pdaieYWnLm3`. State: `public_schema_verified`.

Build `0.1.10` / `edHFElgAuXDEYwvpe`; tag `latest`. Required keys: `companyUrls`. [Full dated input schema](../schemas/linkedin-company-posts-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companyUrls` | array | One or more public LinkedIn company page URLs, for example https://www.linkedin.com/company/shopify. |
| `maxPosts` | integer; minimum=1; maximum=1000 | Maximum number of post records to save across all company URLs. |
| `startPage` | integer; minimum=1; maximum=7 | the primary managed public-data route company-post pages are numbered from 1. |
| `maxPagesPerCompany` | integer; minimum=1; maximum=7 | the primary managed public-data route currently exposes up to 7 company-post pages because of LinkedIn public-page limits. |
| `includeCompanyProfile` | boolean | When the managed fallback route is available, attach public company metadata such as name, handle, followers, industry, logo, and website. |
| `enrichPosts` | boolean | Fetch each post detail with the managed fallback route when available to add engagement counts and author/comment previews. This costs one provider request per post. |
| `includeRawData` | boolean | Include compact raw provider payloads for debugging and downstream custom parsing. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-post-comments-engagements-scraper

Exact owner: `khadinakbar`. Identity: `0tcbv4SIYhcPCFteQ`. State: `public_schema_verified`.

Build `0.1.5` / `LFu88nhaYiLPMbPsV`; tag `latest`. Required keys: `postUrls`. [Full dated input schema](../schemas/linkedin-post-comments-engagements-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `postUrls` | array | One or more public LinkedIn post, feed update, or Pulse article URLs. Use this actor when you already know the post URLs and want comments, commenters, and engagement counts. |
| `maxPosts` | integer; minimum=1; maximum=500 | Maximum number of unique post URLs to process from the input list. Use this to cap provider calls and PPE cost for large URL batches. |
| `maxCommentsPerPost` | integer; minimum=0; maximum=1000 | Maximum number of comment rows to save per post. The provider may expose fewer comments than this cap. Set to 0 when you only need post-level engagement rows. |
| `outputMode` | string; both, comments, posts | Choose whether to save post-level engagement summary rows, per-comment rows, or both. Both is recommended for CRM, lead research, and AI-agent workflows. |
| `dedupeComments` | boolean | Remove duplicate comments per post using comment URL, commenter profile URL, and text. Keep enabled for cleaner automation datasets. |
| `includeRawData` | boolean | Attach raw the managed fallback route post/comment payloads to dataset rows. Enable only for debugging or custom downstream parsing because it increases dataset size. |
| `maxConcurrency` | integer; minimum=1; maximum=5 | How many post URLs to process in parallel. Keep the default for reliable provider usage and predictable cost tracking. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## x-twitter-search-scraper

Exact owner: `khadinakbar`. Identity: `6xhgv9qnX0z36Btrv`. State: `public_schema_verified`.

Build `1.1.4` / `pZ39e8acQKkBii6H5`; tag `latest`. Required keys: `queries`. [Full dated input schema](../schemas/x-twitter-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array; minItems=1; maxItems=50 | X/Twitter search queries, hashtags, usernames, or advanced operators. Examples: ai agents, #buildinpublic, from:openai min_faves:100, (marketing OR sales) lang:en. |
| `searchType` | string; Top, Latest, People, Photos, Media | Which X search tab to scrape. Top and Latest return tweet-like results. People returns account-like results. Photos and Media return media-heavy results. |
| `maxResults` | integer; minimum=1; maximum=5000 | Maximum dataset records to save across all queries. This is also the hard cap for billable result events. |
| `maxPagesPerQuery` | integer; minimum=1; maximum=100 | Advanced pagination safety valve. Lower this for quick tests; increase it for deeper searches when the provider returns a next cursor. |
| `startCursor` | string | Optional provider cursor from a previous run. Use this only when continuing one query/search type from RUN_SUMMARY.nextCursors. |
| `includeRaw` | boolean | Attach the raw provider item to each dataset record for debugging field drift. Leave disabled for smaller production datasets. |
| `dedupeResults` | boolean | Skip duplicate tweet/account/list records across pages and queries. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## x-twitter-replies-scraper

Exact owner: `khadinakbar`. Identity: `HcEzBhLB9Aqdhbz5b`. State: `public_schema_verified`.

Build `1.0.7` / `MPsr4DxTzLkK1oRFR`; tag `latest`. Required keys: `tweetUrls`. [Full dated input schema](../schemas/x-twitter-replies-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `tweetUrls` | array; minItems=1; maxItems=50 | Use this when you need public replies from specific X/Twitter posts. Enter full URLs like https://x.com/openai/status/1930000000000000000 or numeric tweet IDs. Defaults to one working public tweet example. This is not fo |
| `rankingMode` | string; Relevance, Recency, Likes | Use this when choosing how X should order replies for each tweet. Relevance returns the default conversation ranking, Recency returns newer replies first, and Likes prioritizes liked replies. Defaults to Relevance. This  |
| `maxReplies` | integer; minimum=1; maximum=5000 | Use this to cap the total reply rows saved across all input tweets. The actor stops before charging beyond this limit. Defaults to 100 and supports up to 5000. This is a hard billing and dataset cap, not a per-tweet targ |
| `maxPagesPerTweet` | integer; minimum=1; maximum=100 | Use this as a pagination safety valve for each tweet conversation. Higher values collect deeper reply pages when the provider returns a next cursor. Defaults to 10 and supports up to 100. This does not override maxReplie |
| `startCursor` | string | Use this when continuing one tweet from a previous RUN_SUMMARY nextCursors value. Paste the cursor string exactly as returned by the actor. Leave blank for a fresh run. This is not a tweet URL or tweet ID field. |
| `includeRaw` | boolean | Use this for debugging provider field drift or building custom parsers. When enabled, each dataset row includes the raw the managed fallback route reply object. Defaults to false for smaller datasets. This is not needed  |
| `dedupeReplies` | boolean | Use this to skip duplicate reply tweets across pages and input tweets. The actor dedupes by reply ID first, then reply URL or text fallback. Defaults to true. Disable only when you need to inspect provider pagination ove |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## search-bluesky-posts

Exact owner: `khadinakbar`. Identity: `ZuuohTEzrMJbFL7VF`. State: `public_schema_verified`.

Build `1.0.8` / `DmrB3q59go6O4v6eZ`; tag `latest`. Required keys: `searchQuery`. [Full dated input schema](../schemas/search-bluesky-posts.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `useUnblockerFallback` | boolean | Retry a blocked public search through Apify Unblocker with at most two requests for transient failures. Defaults to true; set false for direct routes only. Each successful proxy request adds 10 Unblocker units to platfor |
| `searchQuery` | string | Use this when you need posts matching text, a phrase, or supported Lucene-style syntax. Enter a focused query such as 'open source' or '"climate change"'. The field is required and accepts up to 500 characters. This is n |
| `sort` | string; latest, top | Use this when choosing how Bluesky ranks matching posts. Choose 'latest' for newest indexed posts or 'top' for relevance-ranked results. Defaults to 'latest'. This does not sort the finished dataset locally. |
| `maxResults` | integer; minimum=1; maximum=100 | Use this when bounding dataset size and per-post charges. Enter an integer from 1 to 100, such as 100. Defaults to 100 and the Console prefill is 25. Bluesky's public search route currently supports one page per query. |
| `since` | string | Use this when restricting results to posts indexed at or after a date. Enter YYYY-MM-DD or an ISO 8601 timestamp, such as '2026-07-01'. Defaults to no lower date bound. This filter uses Bluesky search time and may differ |
| `until` | string | Use this when restricting results to posts before a date. Enter YYYY-MM-DD or an ISO 8601 timestamp, such as '2026-07-15'. Defaults to no upper date bound and is exclusive. This must be later than Posts since. |
| `lang` | string | Use this when you need posts tagged with one language. Enter a BCP 47 tag such as 'en', 'ja', or 'pt-BR'. Defaults to all languages. This is not a country or proxy location. |
| `author` | string | Use this when limiting search to posts from one public Bluesky account. Enter a handle or DID such as 'jay.bsky.team'; a leading @ is accepted. Defaults to any author. This does not scrape a user's full feed or profile. |
| `mentions` | string | Use this when finding posts that mention one Bluesky account through a rich-text mention facet. Enter a handle or DID such as 'bsky.app'; a leading @ is accepted. Defaults to any mention. Plain text that only resembles a |
| `domain` | string | Use this when finding posts whose facets or embeds link to a hostname. Enter a domain such as 'github.com'; a full https URL is normalized to its hostname. Defaults to any linked domain. This is not a keyword search with |
| `url` | string | Use this when finding posts that link to one absolute web URL. Enter an http or https URL such as 'https://example.com/report'. Defaults to any linked URL. This is not the URL of a Bluesky post to fetch directly. |
| `tags` | array; maxItems=10 | Use this when posts must contain specific hashtags. Enter up to 10 tags without #, such as ['ai', 'opensource']; multiple tags use AND matching. Defaults to no hashtag filter. These are structured hashtag facets, not fre |
| `includeReplies` | boolean | Use this when deciding whether reply posts may appear in the dataset. Set false to drop posts containing Bluesky reply metadata after search. Defaults to true. This does not fetch complete reply threads. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## threads-search-scraper

Exact owner: `khadinakbar`. Identity: `RWcwKI3Xw3RPfS9bv`. State: `public_schema_verified`.

Build `0.2.4` / `nDDSvknDHKli0UA9F`; tag `latest`. Required keys: `queries`. [Full dated input schema](../schemas/threads-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchType` | string; posts, users | What to search Meta Threads for. 'posts' searches the text of public Threads posts by keyword (e.g. 'ai agents'). 'users' searches for public Threads accounts by username keyword (e.g. 'openai'). Defaults to 'posts'. Thi |
| `queries` | array | One or more search terms. For 'posts' these are content keywords or hashtags (e.g. 'ai agents', 'climate tech'); for 'users' these are username fragments (e.g. 'openai'). Each query is searched independently and results  |
| `maxResults` | integer; minimum=1 | Hard cap on total results pushed across all queries, used for cost control. Each result is billed (see pricing). Defaults to 100. The actor stops once this many records are collected. Bounds: 1 and up. |
| `maxResultsPerQuery` | integer; minimum=1; maximum=100 | Cap on results taken from each individual query before moving to the next. The provider search endpoint returns roughly 20-25 items per query, so values above ~25 rarely add more. Defaults to 25. Bounds: 1-100. |
| `startDate` | string | Optional earliest date filter for 'posts' search, format YYYY-MM-DD (e.g. '2026-01-01'). Ignored for 'users' search. Leave empty for no lower bound. Only honored by the primary managed public-data route provider. |
| `endDate` | string | Optional latest date filter for 'posts' search, format YYYY-MM-DD (e.g. '2026-06-30'). Ignored for 'users' search. Leave empty for no upper bound. Only honored by the primary managed public-data route provider. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## quora-scraper

Exact owner: `khadinakbar`. Identity: `sBeeNXEwCMea3jePc`. State: `public_schema_verified`.

Build `0.1.16` / `Rm31hfrbR3tZbUZ7g`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/quora-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | List of Quora URLs to scrape. Each may be a question page (https://www.quora.com/What-is-the-best-way-to-learn-programming), a profile (https://www.quora.com/profile/Adam-DAngelo), a space (https://www.quora.com/q/<space |
| `maxItemsPerTarget` | integer; minimum=1; maximum=1000 | Maximum number of records to return for each URL or keyword. The Actor scrolls to paginate until this cap, then stops, so it doubles as your cost ceiling (each record is one billable event). Defaults to 50. Lower it for  |
| `maxConcurrency` | integer; minimum=1; maximum=10 | How many target pages to scrape in parallel. Higher is faster but uses more proxy IPs and memory; lower is gentler on anti-bot defenses. Defaults to 5 (max 10). Leave default unless you hit blocking. |
| `proxyConfiguration` | object | Proxy settings. Residential proxies are strongly recommended — Quora is protected by Cloudflare and datacenter IPs are often challenged. Defaults to Apify Proxy automatic. Override to select residential proxies or a spec |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## github-deep-scraper

Exact owner: `khadinakbar`. Identity: `VJF7QtGTpSkiFyPli`. State: `public_schema_verified`.

Build `0.1.16` / `MdmZEFHcfPh8q8L0D`; tag `latest`. Required keys: `mode`. [Full dated input schema](../schemas/github-deep-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `mode` | string; repo, repo-search, issues, prs, code-search, contributors, releases, readme, commits, user, trending | Which GitHub surface to scrape. One actor, 11 modes. Pick exactly one. 'repo' = full metadata for one repo (50+ fields). 'repo-search' = keyword/qualifier search. 'issues'/'prs' = list issues/PRs for a repo with comments |
| `repo` | string | GitHub repository in 'owner/name' format (e.g., 'facebook/react'). Required for modes: repo, issues, prs, contributors, releases, readme, commits. Accepts full URL too — 'https://github.com/facebook/react' is normalised. |
| `query` | string | Free-text query with GitHub search qualifiers (e.g., 'language:typescript stars:>1000 web framework'). Used by modes: repo-search, code-search. Supports all GitHub search operators (language:, stars:, forks:, user:, org: |
| `user` | string | GitHub user or organization login (e.g., 'torvalds' or 'apify'). Required for mode 'user'. Returns profile, repos, organizations, and (if available) social accounts. NOT a repo path — for that use 'repo' field. |
| `language` | string | Optional language filter for trending mode (e.g., 'python', 'rust', 'typescript'). Lowercase, hyphenated for multi-word. For repo-search use 'language:python' inside the query field instead. Empty = all languages. |
| `timeframe` | string; daily, weekly, monthly | Time window for trending mode. 'daily' = today's trending repos, 'weekly' = this week, 'monthly' = this month. GitHub publishes these lists at github.com/trending. Only used by mode 'trending'. Default: daily. |
| `state` | string; open, closed, all | Filter issues or PRs by state. 'open' = only open, 'closed' = only closed, 'all' = both. Only used by modes 'issues' and 'prs'. Default: open. GitHub's UI default is open, so leave as 'open' for most agent use. |
| `since` | string | Only return items updated/created at or after this ISO 8601 date (e.g., '2026-01-01' or '2026-01-01T00:00:00Z'). Used by modes 'issues', 'prs', 'commits'. Empty = no lower bound. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of records to return. Each record = one PPE 'result' ($0.005) or 'deep-result' ($0.01) charge. Default 50. Hard cap 1000 to keep one run under $10 for x402 agents. Set lower to control cost; the actor will |
| `includeComments` | boolean | When true, fetches comments for each issue or PR (extra API call per item). Increases run cost but gives the full conversation thread. Only affects modes 'issues' and 'prs'. Default: false. Set true when an agent needs s |
| `includeReviews` | boolean | When true, fetches reviews and review comments for each PR (extra API call per PR). Returns reviewer login, state (APPROVED/REQUEST_CHANGES/COMMENTED), submitted_at, body. Only affects mode 'prs'. Default: false. Set tru |
| `includeFiles` | boolean | When true, includes the list of files changed per commit with additions/deletions/status. Charged as 'deep-result' ($0.01) instead of 'result'. Only affects mode 'commits'. Default: false. Set true when an agent needs to |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## facebook-groups-search-scraper

Exact owner: `khadinakbar`. Identity: `9nSWzeI0pi1GzrycY`. State: `public_schema_verified`.

Build `1.1.2` / `d0aw48rj3AZTtz2Cx`; tag `latest`. Required keys: `searchQueries`. [Full dated input schema](../schemas/facebook-groups-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Use this when you want to discover Google-indexed Facebook groups for one or more topics. Provide short natural-language phrases such as 'real estate investors' or 'small business owners London'. The actor searches Googl |
| `maxResultsPerQuery` | integer; minimum=1; maximum=100 | Use this when you need to cap the number of unique public Facebook groups returned for each search query. Enter an integer from 1 to 100; the default is 20. A lower number reduces both event charges and result-review tim |
| `countryCode` | string | Use this when the group search should be localized to a country. Enter a two-letter uppercase country code such as 'US', 'GB', or 'CA'; the default is 'US'. This affects the search provider's regional results, not Facebo |
| `includeRawData` | boolean | Use this when you need the original provider result alongside the normalized group fields for debugging. Defaults to false to keep dataset rows compact and agent-friendly. Raw response shapes can change without notice an |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## facebook-group-posts-scraper

Exact owner: `khadinakbar`. Identity: `hfPwOw0vcVcuYhJVB`. State: `public_schema_verified`.

Build `1.1.3` / `Ico3d4zjwfHP7Ng0T`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/facebook-group-posts-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `groupUrls` | array | One or more public Facebook group URLs, for example https://www.facebook.com/groups/homemakingtips/. |
| `groupIds` | array | Optional numeric Facebook group IDs. Use this when you know the group ID and do not have a URL. |
| `maxPosts` | integer; minimum=1; maximum=3000 | Maximum number of group post records to save across all groups. |
| `maxPagesPerGroup` | integer; minimum=1; maximum=200 | Provider APIs currently return up to 3 posts per request and paginate with a cursor. |
| `startCursor` | string | Optional provider pagination cursor. Use a cursor from RUN_SUMMARY.nextCursors to resume a group feed. |
| `sortBy` | string; RECENT_ACTIVITY, TOP_POSTS, CHRONOLOGICAL, CHRONOLOGICAL_LISTINGS | Provider-side Facebook group post ordering. |
| `dataSource` | string; auto, provider, browser | Auto tries configured providers first, then browser fallback when enabled. Provider only skips browser fallback. Browser only skips provider APIs. |
| `useBrowserFallback` | boolean | Try a Playwright browser scrape when provider APIs are unavailable, empty, or disabled. |
| `maxBrowserScrolls` | integer; minimum=0; maximum=50 | Maximum page scrolls in browser fallback mode. |
| `facebookCookies` | string | Optional JSON cookie array or raw Cookie header for browser fallback only. Use your own authorized session; do not use this for data you are not allowed to access. |
| `proxy` | object | Proxy settings for browser fallback. |
| `includeRawData` | boolean | Include raw source objects in each dataset row for debugging and custom downstream parsing. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## skool-community-scraper

Exact owner: `khadinakbar`. Identity: `DyVrOeKLG39Fy3vNd`. State: `public_schema_verified`.

Build `0.1.10` / `4qBLo5Nn6uX2UtFfp`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/skool-community-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `communityUrls` | array | Skool community URLs or bare slugs to look up directly (group mode). Accepts full links like 'https://www.skool.com/new-society' or just 'new-society'. Returns the full public profile of each community plus its owner. NO |
| `searchQueries` | array | Keywords to search Skool's public Discovery directory (discovery mode), e.g. 'real estate' or 'ai automation'. Each keyword is paginated and every matched community is returned. Use this to build lists of communities in  |
| `enrichDetails` | boolean | When ON (default), each Discovery result is enriched via the Skool group API to add pricing, post/course counts, join questions, and the owner lead. When OFF, Discovery returns the lean directory card only (name, descrip |
| `maxItems` | integer; minimum=1; maximum=100000 | Hard cap on the total number of communities returned across all inputs, for cost control. Each community is billed at $0.005. Defaults to 100. Set lower for a quick sample or higher to sweep a whole niche (Skool Discover |
| `maxPagesPerQuery` | integer; minimum=1; maximum=34 | Upper bound on how many Discovery pages (30 communities each) to fetch per keyword before moving on. Defaults to 34, the full depth Skool exposes (~1000 results). Lower it to sample only the top results of each keyword.  |
| `proxyConfiguration` | object | Proxy used for requests. Skool's public API is a clean JSON endpoint, so the default Apify Proxy (datacenter, US) is sufficient and cheapest. Override only if you hit regional issues. Residential is rarely needed. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-forums-search-scraper

Exact owner: `khadinakbar`. Identity: `bJHodTCveq8PX7rJC`. State: `public_schema_verified`.

Build `0.7.2` / `aJ5FE94gCBxxUqX2e`; tag `latest`. Required keys: `queries`. [Full dated input schema](../schemas/google-forums-search-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `queries` | array; minItems=1; maxItems=50 | One or more phrases to search in Google's Forums tab. Each query returns public discussion threads only, not ordinary web results. |
| `countryCode` | string | Two-letter lowercase country code used for Google result localization, such as us, gb, or de. |
| `languageCode` | string | Two-letter lowercase Google interface and result language code, such as en, de, or es. |
| `device` | string; desktop, mobile, tablet | Google Forums layout to request. Desktop is the default; mobile can return a different ranking. |
| `maxResultsPerQuery` | integer; minimum=1; maximum=100 | Maximum public thread records to save for each query. The Actor fetches only the pages necessary to reach this cap. |
| `dateRange` | string; anytime, hour, day, week, month, year | Optional Google date filter. This limits Google results by recency; it does not modify the returned date text. |
| `includeAnswerPreviews` | boolean | When Google returns answer previews under a forum result, include their public snippet, link, and labels. Defaults to true. |
| `includeDomains` | array; maxItems=20 | Optional bare domains to include, such as reddit.com or stackoverflow.com. The Actor adds Google site: filters and keeps the original query in output. Do not include URLs, paths, or wildcards. |
| `excludeDomains` | array; maxItems=20 | Optional bare domains to exclude. The Actor adds Google -site: filters. A domain cannot be both included and excluded. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
