# Hiring and expansion source guide

Read the relevant prospecting playbook and shared operating contract. Source titles/IDs do not establish data-use rights. “Verified” below means metadata/input schema verified, not lead quality or runtime health. Refresh the schema and pricing before execution.

Apply the [qualified business/contact-use gate](../contact-use.md). Provider result bounds are not recommended audience sizes; optional contact extraction must be disabled during discovery.

Apply the [source access gate](../access-safety.md) before execution. Provider recovery recommendations are replaced by VibeLeads restrictions; structural field names/types/bounds remain references.

## linkedin-jobs-scraper

Exact owner: `khadinakbar`. Identity: `TBxNczWNXst8K72z2`. State: `public_schema_verified`.

Build `0.2.6` / `I4bCoGSSCm8pznVUq`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/linkedin-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Use this field when the user provides job titles, roles, or keywords to search. E.g. ['Software Engineer', 'Product Manager']. Use startUrls instead when the user provides direct LinkedIn search URLs. Supports multiple queries — each is run against every location. |
| `locations` | array | List of locations to search in. Each query is cross-searched against each location. Use city names, states, or countries. E.g. ['New York', 'Remote', 'London']. Use 'United States' for nationwide US results. |
| `startUrls` | array | Use this field instead of searchQueries when the user provides direct LinkedIn job search URLs (e.g. copied from linkedin.com/jobs/search). Open linkedin.com/jobs in an incognito window, apply your filters, and paste the URL here. Overrides searchQueries + locations when provided. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of job listings to return across all queries and locations combined. LinkedIn limits each search to ~1000 results. Use multiple queries to get more. |
| `datePosted` | string; any, r86400, r604800, r2592000 | Filter jobs by how recently they were posted. 'Any time' returns all available jobs. Use 'Past 24 hours' for fresh postings. |
| `jobType` | array | Filter by employment contract type. Leave empty to return all types. F=Full-time, P=Part-time, C=Contract, T=Temporary, I=Internship. |
| `experienceLevel` | array | Filter by required experience level. Leave empty to return all levels. 1=Internship, 2=Entry level, 3=Associate, 4=Mid-Senior, 5=Director, 6=Executive. |
| `workType` | array | Filter by on-site, remote, or hybrid work arrangement. Leave empty to return all. 1=On-site, 2=Remote, 3=Hybrid. |
| `salaryBase` | string; 40000, 60000, 80000, 100000, 120000 | Filter to only show jobs above a minimum annual salary. Note: LinkedIn only shows salary on a subset of postings. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## linkedin-company-jobs-scraper

Exact owner: `khadinakbar`. Identity: `jo4IhcXBcbcD0GC3r`. State: `public_schema_verified`.

Build `0.1.5` / `HVOzgiE9qHRdGmwMI`; tag `latest`. Required keys: `company`. [Full dated input schema](../schemas/linkedin-company-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `company` | string | The LinkedIn company whose job postings you want. Accepts a company URL (e.g. 'https://www.linkedin.com/company/stripe'), a bare slug ('stripe'), or a numeric LinkedIn company ID ('51737071'). A URL or slug is resolved to the numeric ID via the primary managed public-data route (primary) then the managed fallback route (fallback). NOT a job-search keyword and NOT a personal profile URL — for keyword job search use the linkedin-jobs-scraper actor. |
| `keywords` | string | Optional free-text filter applied to the company's postings (e.g. 'engineer', 'product manager'). Matches LinkedIn's job-title search. Leave empty to return all open roles at the company. This filters WITHIN one company, it does not search across companies. |
| `location` | string | Optional geographic filter such as 'United States', 'London', or 'Remote'. Maps to LinkedIn's job location facet. Leave empty for all locations. This is a job-location filter, not the company headquarters. |
| `datePosted` | string; any, month, week, day | Limit results by how recently a job was posted. 'any' returns all open postings; 'month'/'week'/'day' restrict to the last 30/7/1 days. Defaults to 'any'. |
| `jobType` | string; any, full-time, part-time, contract, temporary, internship | Filter by employment type. 'any' returns all types. Maps to LinkedIn's job-type facet (F/P/C/T/I). Defaults to 'any'. |
| `experienceLevel` | string; any, internship, entry, associate, mid-senior, director, executive | Filter by seniority. 'any' returns all levels. Maps to LinkedIn's experience facet. Defaults to 'any'. |
| `remoteOnly` | boolean | When true, returns only roles LinkedIn flags as remote. Defaults to false (all workplace types: on-site, hybrid, remote). |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of job postings to return. LinkedIn's guest endpoint caps near 1000 per company-query. Defaults to 50. Each returned job is billed at the per-job rate. |
| `enrichJobDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `enrichCompany` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## indeed-job-scraper

Exact owner: `khadinakbar`. Identity: `archZrc8GyycLrX2i`. State: `public_schema_verified`.

Build `1.1.8` / `UZ22KcZUExgWyBWa4`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/indeed-job-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this field when the user provides a job title, skill, keyword, or role to search for (e.g. 'software engineer', 'nurse', 'marketing manager', 'data analyst'). Use startUrls instead when the user provides a direct Indeed.com search URL. |
| `location` | string | City, state, ZIP code, or 'Remote' to filter jobs geographically (e.g. 'Austin, TX', 'New York', 'Remote', '10001'). Leave empty to search all locations. |
| `startUrls` | array | Use this field when the user provides specific Indeed.com job search URLs (e.g. https://www.indeed.com/jobs?q=nurse&l=Chicago). Do NOT use this when the user provides keywords or a role name — use searchQuery for that instead. |
| `maxResults` | integer; minimum=1; maximum=1000 | Maximum number of job listings to scrape and return. Each result costs $0.002 (= $2 per 1,000 jobs). Default is 50. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `country` | string; www, uk, ca, au, in, de, fr, sg, nz | Which Indeed country site to scrape. Use 'www' for United States (default). Change for country-specific job markets. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## google-jobs-scraper

Exact owner: `khadinakbar`. Identity: `QSfNn2wwDEBa69WGO`. State: `public_schema_verified`.

Build `0.2.15` / `aG13n0OXxgfxTjB8i`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/google-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQueries` | array | Use this field when the user provides job titles, skills, or keyword phrases to search. Accepts multiple queries — the actor runs them all in one go. Example: ["software engineer New York", "product manager remote"]. Use startUrls instead when the user provides a direct Google Jobs URL. |
| `startUrls` | array | Use this field when the user provides a specific Google Jobs URL (e.g. https://www.google.com/search?q=nurse&ibp=htl;jobs). Do NOT use this when the user describes a job role or keyword — use searchQueries instead. |
| `maxResults` | integer; minimum=1; maximum=500 | Maximum total number of job listings to extract across all queries. Must be between 1 and 500. Default: 50. Each result costs $0.003 — so 100 results costs $0.30. |
| `datePosted` | string; any, today, 3days, week, month | Filter jobs by how recently they were posted. 'any' returns all results. 'today' returns jobs posted in the last 24 hours. 'week' returns jobs from the past 7 days. |
| `employmentType` | string; any, FULLTIME, PARTTIME, CONTRACTOR, INTERN | Filter by job type. Use 'FULLTIME' for permanent full-time roles, 'PARTTIME' for part-time, 'CONTRACTOR' for contract/freelance work, 'INTERN' for internships. Use 'any' to return all types. |
| `remoteOnly` | boolean | When enabled, appends 'remote' to all search queries and marks all results as is_remote: true. Enable this when the user asks specifically for remote, work-from-home, or WFH jobs. |
| `proxyCountry` | string | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## wellfound-jobs-scraper

Exact owner: `khadinakbar`. Identity: `ddBZbnGzOvViKbPY5`. State: `public_schema_verified`.

Build `1.3.2` / `59vx5hCUWBi1ANIgs`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/wellfound-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `role` | string | Use this when you want Wellfound startup jobs for a specific role. Enter a plain job title such as 'software engineer' or 'product manager'. Defaults to 'software engineer'. This is not a Wellfound URL; paste URLs into Start URLs instead. |
| `location` | string | Use this when you want jobs in a city, country, or startup hub. Enter Wellfound-style text such as 'san francisco', 'new york', or 'united states'. Defaults to blank when Remote only is enabled. This is not a country code field. |
| `remoteOnly` | boolean | Use this when you only want remote Wellfound jobs for the selected role. When true, the actor uses Wellfound remote role pages such as /role/r/software-engineer. Defaults to true for a reliable small health-check run. This does not guarantee every company hires in every country. |
| `startUrls` | array | Use this when you already have Wellfound role, location, remote, or job-detail URLs. Accepts URLs like https://wellfound.com/role/l/software-engineer/san-francisco or https://wellfound.com/jobs/1234567. When set, Role, Location, and Remote only are ignored. This is not for LinkedIn, Indeed, or Google Jobs URLs. |
| `maxItems` | integer; minimum=1; maximum=50000 | Use this to cap the number of Wellfound jobs returned and billed in one run. Accepts 1 to 50000; the default is 20 and the health-check prefill is 1. The actor stops before charging past this limit. This is not a page count. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `maxConcurrency` | integer; minimum=1; maximum=10 | Use this to tune how many Wellfound pages are open in parallel. Accepts 1 to 10; the default is 2 and the health-check prefill is 1 for safer session consistency. Lower it if the run hits blocks, raise it only for healthy large exports. This is not the result limit. |
| `debugDumpHtml` | boolean | Use this only for troubleshooting extractor drift. When enabled, raw HTML snapshots are saved to the key-value store under DEBUG keys. Defaults to false. This is not needed for normal exports. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## glassdoor-jobs-scraper

Exact owner: `khadinakbar`. Identity: `gDgmwzoi4dAD2ZFMm`. State: `public_schema_verified`.

Build `1.1.2` / `cyBiyxQVBpRnlyDDI`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/glassdoor-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | Use this when you already have Glassdoor jobs search URLs (for example a copied https://www.glassdoor.com/Job/...SRCH_IL...htm results page). Each item is scraped directly and takes priority over searchQuery/location. Leave empty to build a search from the query and location below. This is not for company review or salary pages. |
| `searchQuery` | string | Use this when you want Glassdoor jobs matching a role, skill, or company. Accepts plain text such as "software engineer", "nurse practitioner", or "data analyst". Defaults to "software engineer" for small health-check runs. This is not a company reviews, interview, or salary-only search. |
| `location` | string | Use this when you need jobs near a city, state, country, or remote-style location label. Accepted examples include "New York, NY", "San Francisco, CA", "London", or "Remote". Defaults to "New York, NY" for predictable canaries. This is not a postal address or radius field. |
| `country` | string | Use this to label the requested country in output records and summaries. Use a two-letter code such as "US", "GB", "CA", or "AU". Defaults to "US". Search targeting is primarily controlled by the location text. |
| `maxResults` | integer; minimum=1; maximum=1000 | Use this to cap how many job records and billable job-scraped events can be returned. Accepts 1 to 1000, with default 50. The actor stops charging and pushing data at this number. This is not a page count. |
| `daysOld` | integer; minimum=1; maximum=30 | Use this when you only want recent Glassdoor jobs. Accepts 1 to 30, for example 7 for jobs posted in the last week. Leave empty to let the backend return its default date range. This is not a timestamp or exact date. |
| `includeNoSalaryJobs` | boolean | Use this when jobs without visible salary ranges are still useful. Defaults to true because many Glassdoor listings omit pay. Set false for compensation-only datasets. This does not estimate missing salary values. |
| `deduplicate` | boolean | Use this to skip repeated Glassdoor jobs returned by the backend. Defaults to true and dedupes by job ID, URL, or a title-company-location hash. Set false only when you need raw backend-level evidence. This does not merge with old datasets from previous runs. |
| `debug` | boolean | Use this only for troubleshooting. Defaults to false. This does not change which jobs are scraped. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## greenhouse-jobs-scraper

Exact owner: `khadinakbar`. Identity: `VWE9UWysLxkHbOETu`. State: `public_schema_verified`.

Build `1.0.4` / `K0GUwfWQ8sNrfmLf2`; tag `latest`. Required keys: `boardTokens`. [Full dated input schema](../schemas/greenhouse-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `boardTokens` | array | Enter one public Greenhouse board token or board URL per line, such as stripe or https://job-boards.greenhouse.io/stripe. The actor extracts the token and accepts up to 25 unique boards. This is required and is not a company website URL, login URL, individual job URL, or application form. |
| `maxResultsPerBoard` | integer; minimum=1; maximum=1000 | Caps validated job records returned for each Greenhouse board. Enter an integer such as 100. It defaults to 100 and accepts 1 through 1,000. This is a per-board result cap, not a page count or a global budget across every board. |
| `titleIncludes` | string | Optionally keep only jobs whose public title contains this text, such as engineer. Matching is case-insensitive and uses literal text. Leave blank to keep all titles. This is not a Boolean query or a full-text search across descriptions. |
| `locationIncludes` | string | Optionally keep only jobs whose public Greenhouse location contains this text, such as remote or london. Matching is case-insensitive and uses the location text supplied by the board. Leave blank to keep every location. This does not geocode jobs or search office addresses. |
| `departmentIncludes` | string | Optionally keep only jobs assigned to a public Greenhouse department containing this text, such as engineering. Matching is case-insensitive across the public department names. Leave blank to keep all departments. This does not infer a department from the job description. |
| `includeDescriptions` | boolean | Controls whether each output record includes the public Greenhouse description in HTML and clean text. Set true for detailed recruiting and research data or false for a smaller, faster result. It defaults to true. This does not retrieve private hiring notes, candidates, or application answers. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## lever-jobs-scraper

Exact owner: `khadinakbar`. Identity: `zThhdw9tYfPAM6GEz`. State: `public_schema_verified`.

Build `1.1.2` / `aNetkIWIcaOUdHVAt`; tag `latest`. Required keys: `boardTokens`. [Full dated input schema](../schemas/lever-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `boardTokens` | array | Use this when you know a company's public Lever board, for example lever or https://jobs.lever.co/lever. Enter up to 25 unique board tokens or root public board URLs. This field is required. It is not a company website, an individual job URL, a login page, or an application form. |
| `maxResultsPerBoard` | integer; minimum=1; maximum=1000 | Use this to cap validated jobs returned from each supplied Lever board. Enter an integer such as 100. It defaults to 100 and accepts 1 through 1,000. This is a per-board result cap, not a page count or a global charge budget. |
| `titleIncludes` | string | Use this when you need jobs whose public title contains literal text, for example engineer. Matching is case-insensitive. Leave it blank to retain every public title. This is not Boolean search and does not search the description. |
| `locationIncludes` | string | Use this when you need jobs whose public Lever location contains literal text, for example remote or london. Matching is case-insensitive across the primary and alternate public locations. Leave it blank to retain every location. This does not geocode a job or infer location from its description. |
| `teamIncludes` | string | Use this when you need a public Lever team containing literal text, for example engineering. Matching is case-insensitive against Lever's public team category. Leave it blank to retain every team. This does not infer a team from title words or job description text. |
| `commitmentIncludes` | string | Use this when you need a public Lever commitment such as full-time, contract, or internship. Matching is case-insensitive against the board's commitment field. Leave it blank to retain every employment type. This is not a date filter or a candidate availability filter. |
| `includeDescriptions` | boolean | Use this to include the public Lever description and additional text in HTML and clean-text fields. Set true for detailed recruiting and research output or false for a smaller result. It defaults to true. This does not retrieve private hiring notes, candidate data, or application responses. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## ashby-jobs-scraper

Exact owner: `khadinakbar`. Identity: `UnbMttEkpRV4otgC9`. State: `public_schema_verified`.

Build `1.0.9` / `KisofuMwdTCpIQhdN`; tag `latest`. Required keys: `boardTokens`. [Full dated input schema](../schemas/ashby-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `boardTokens` | array | Enter one public Ashby board token or jobs URL per line, such as notion or https://jobs.ashbyhq.com/notion. The actor extracts and deduplicates up to 25 boards. This is required and is not a company website URL, individual job URL, application form, or Ashby admin URL. |
| `maxResultsPerBoard` | integer; minimum=1; maximum=1000 | Caps validated job records returned for each Ashby board. Enter an integer such as 100. It defaults to 100 and accepts 1 through 1,000. This is a per-board output cap, not a page count or a global budget across every board. |
| `titleIncludes` | string | Optionally keep only jobs whose public title contains this text, such as engineer. Matching is case-insensitive and uses literal text. Leave blank to keep all titles. This is not a Boolean query or a full-text search across job descriptions. |
| `locationIncludes` | string | Optionally keep only jobs whose public primary or secondary location contains this text, such as remote or london. Matching is case-insensitive against text supplied by Ashby. Leave blank to keep every location. This does not geocode jobs or search office addresses. |
| `departmentIncludes` | string | Optionally keep only jobs whose public Ashby department contains this text, such as engineering. Matching is case-insensitive against the department field. Leave blank to keep all departments. This does not infer departments from job titles or descriptions. |
| `remoteOnly` | boolean | Keeps only jobs Ashby marks remote or with workplace type Remote. Set true for remote-role research or false to retain all listed roles. It defaults to false. This does not infer remote eligibility from a job description or location text. |
| `includeDescriptions` | boolean | Controls whether each output record includes public Ashby description HTML and clean text. Set true for detailed recruiting and research data or false for smaller results. It defaults to true. This does not retrieve private hiring notes, candidates, or application answers. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## workable-jobs-scraper

Exact owner: `khadinakbar`. Identity: `cetk6UriLHVw6AIVY`. State: `public_schema_verified`.

Build `1.0.5` / `av3wVaTZ0Eof8yGmZ`; tag `latest`. Required keys: `companies`. [Full dated input schema](../schemas/workable-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `companies` | array | Enter one Workable company slug or public careers URL per line, such as recurly or https://apply.workable.com/recurly/. The actor extracts up to 25 unique slugs. This is required and is not an arbitrary company website, login page, individual application form, or private ATS URL. |
| `maxJobsPerCompany` | integer; minimum=1; maximum=30 | Caps validated job records returned for each Workable company board. Enter an integer such as 25. It defaults to 30 and accepts 1 through 30 because Workable's current public Markdown listing route returns a bounded set. This is a per-company result cap, not a page count or global collection budget. |
| `searchQuery` | string | Optional text passed to Workable's public jobs listing route, for example engineer. Use it to narrow a large board before extraction. Leave blank to request the board's current public listing. This is not a Boolean expression or a cross-company Workable search. |
| `titleIncludes` | string | Optionally retain only jobs whose public title contains this text, such as engineer. Matching is case-insensitive literal text and happens before a dataset record is written or billed. Leave blank to keep all titles. This does not search private application data or description text. |
| `locationIncludes` | string | Optionally retain only jobs whose public Workable location contains this text, such as remote or london. Matching is case-insensitive literal text against the board's location column. Leave blank to keep all locations. This does not geocode roles or search office addresses. |
| `departmentIncludes` | string | Optionally retain only jobs whose public Workable department contains this text, such as engineering. Matching is case-insensitive literal text and occurs before write and billing. Leave blank to keep all departments. This does not infer departments from a description. |
| `includeDescriptions` | boolean | Controls whether the actor reads each matched public Workable job detail route for description, requirements, benefits, workplace type, and apply URL. Set false for a smaller, faster listing-level dataset. It defaults to true. This does not access candidates, hiring notes, or application answers. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## workday-jobs-scraper

Exact owner: `khadinakbar`. Identity: `NkmOXS1fYASEW98Lz`. State: `public_schema_verified`.

Build `1.1.2` / `0FxlRseKLdh3YLeAv`; tag `latest`. Required keys: `careerSiteUrls`. [Full dated input schema](../schemas/workday-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `careerSiteUrls` | array | Use this when you know the public Workday board to scrape. Provide one or more HTTPS myworkdayjobs.com URLs, for example 'https://baincapital.wd1.myworkdayjobs.com/External_Public'. The default is one public example board and at most 25 boards are accepted. This is not a company homepage, login URL, or private Workday tenant endpoint. |
| `searchText` | string | Use this when the public Workday board should be narrowed by job keywords. Enter ordinary search text, for example 'senior data analyst', or leave it blank to collect the board's available jobs. The default is blank and the maximum length is 160 characters. This is not a Boolean expression, location filter, or job URL. |
| `maxResultsPerSite` | integer; minimum=1; maximum=500 | Use this when you need to cap records and pay-per-event charges for each board. Enter an integer from 1 to 500, for example 50; the default is 25. The run-start message shows the maximum job-event cost across all supplied boards. This is not a page count and does not allow more than 500 records from one board. |
| `includeJobDetails` | boolean | Use this when you want fuller public job descriptions, work type, and apply URLs from each Workday detail endpoint. Set true for richer hiring data or false to retain only search-result fields more quickly. The default is true. This does not bypass a login wall or access applicant, employee, or internal-recruiting data. |
| `useApifyProxy` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## career-site-job-scraper

Exact owner: `khadinakbar`. Identity: `NyFhPz1Vq9CMJzn7u`. State: `public_schema_verified`.

Build `1.2.3` / `pY5RXHv58oBU7vmpS`; tag `latest`. Required keys: `startUrls`. [Full dated input schema](../schemas/career-site-job-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `startUrls` | array | One or more company career-page URLs to scrape. Paste any career/jobs page and the actor auto-detects the ATS behind it — Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Recruitee, or Workable (e.g. 'https://boards.greenhouse.io/stripe', 'https://jobs.ashbyhq.com/posthog', 'https://acme.wd5.myworkdayjobs.com/en-US/careers', or a custom domain like 'https://careers.stripe.com' — it sniffs the embedded ATS). Accepts plain URL strings, one per line. NOT a job-board aggregator query (Indeed/LinkedIn) — this reads a single company's own career page. |
| `maxResultsPerSite` | integer; minimum=1; maximum=20000 | Upper bound on how many job listings to return from each career page. Accepts a whole number (e.g. 200). Defaults to 200; set to a high value like 5000 to pull an entire board. Applied per URL, so total cost scales with URL count times this cap. |
| `enrichDescriptions` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `descriptionFormat` | string; text, html, both, none | How to render the job description field. 'text' returns clean plain text (best for AI agents and resume-matching), 'html' returns the raw HTML, 'both' returns plain text plus a separate descriptionHtml field, and 'none' omits descriptions for the smallest, fastest output. Defaults to 'text'. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## hiringcafe-jobs-scraper

Exact owner: `khadinakbar`. Identity: `xaNQkBxhf0brOpk7z`. State: `public_schema_verified`.

Build `1.3.2` / `eQyT7ODHTfAWINBoS`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/hiringcafe-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Free-text terms sent to HiringCafe, for example 'senior data engineer'. Use a role, skill, or phrase; the default is 'software engineer'. It accepts up to 120 characters. This is not a job URL or an employer-only lookup. |
| `searchUrls` | array | Optional public HiringCafe search URLs, for example 'https://hiringcafe.com/?searchState=%7B%22searchQuery%22%3A%22data%20engineer%22%7D'. When supplied, these URLs override the keyword field and preserve the filters selected on HiringCafe. Leave this empty for the standard keyword mode. This is not for individual job or external application URLs. |
| `maxResults` | integer; minimum=1; maximum=200 | Hard cap on persisted job records and job-record event charges. Enter an integer from 1 to 200, for example 25. The default is 25 and collection stops once the cap is reached. This is not a page count and cannot return more than 200 records. |
| `maxPages` | integer; minimum=1; maximum=10 | Maximum HiringCafe result pages examined for each search URL, for example 3. The default is 3 and each page is fetched sequentially to keep collection bounded. Raise it only when the result cap requires more coverage. This is not a request-concurrency control. |
| `useUnblockerFallback` | boolean | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## remote-jobs-aggregator

Exact owner: `khadinakbar`. Identity: `aLeztUWQhTlb3jbpa`. State: `public_schema_verified`.

Build `0.1.3` / `kdnVXduxbI4zopyXR`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/remote-jobs-aggregator.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Optional keyword filter applied to title, company, tags, location, and snippet. Example: 'python developer'. Every word must match. Leave empty for the latest listings. This is not a LinkedIn Jobs URL. |
| `sources` | array | Public remote-job boards to query. Default is all seven. Omit the field to use every board. An empty array is invalid. These are specialty remote boards, not LinkedIn or Indeed. |
| `maxItems` | integer; minimum=1; maximum=500 | Hard cap on unique dataset rows for this run. Default 25 keeps MCP calls cheap. Each saved job is one remote-job event. This is a cost ceiling, not pagination into a previous run. |
| `postedWithinDays` | integer; minimum=0; maximum=365 | Keep jobs whose posted date is within this many days. 0 (default) disables the filter. Rows without a parseable date are dropped when this filter is on. This is not a board-native freshness SLA. |
| `jobTypes` | array | Keep normalized employment types such as full-time or contract. Empty means every type. Jobs without a type are dropped when this filter is set. This is not visa or salary filtering. |
| `locationKeywords` | array | Keep jobs whose location mentions at least one term, such as Europe, USA, or Germany. Worldwide/remote locations always pass. Leave empty for no geo filter. This is eligibility text from the board, not a work-authorization check. |
| `excludeKeywords` | array | Drop jobs containing any of these terms in title, company, tags, location, or snippet. Example: 'unpaid'. Excluded rows are never billed. This is a client-side filter, not a board search operator. |
| `includeDescription` | boolean | When off (default), each row keeps a 500-character descriptionSnippet for agent token budgets. Turn on to add descriptionText up to 4,000 characters. Boards that omit descriptions still return the other fields. |
| `dedupe` | boolean | When on (default), the same title+company on several boards becomes one row. The richer copy wins and the others appear in alsoFoundOn. Turn off to emit every board copy separately. Duplicate rows are never billed twice when this is on. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## multiple-job-board-scraper

Exact owner: `khadinakbar`. Identity: `bSGPfloZAg10KGSna`. State: `public_schema_verified`.

Build `0.1.6` / `RlyLDuH1jEc8BV3Bt`; tag `latest`. Required keys: `searchQuery`. [Full dated input schema](../schemas/multiple-job-board-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Use this when you want matching role or skill keywords. |
| `location` | string | Use this to prefer jobs whose location text matches; Remote is accepted. |
| `sources` | array | Use this to choose public job boards. Unavailable boards return a partial result without discarding other data. |
| `maxResults` | integer; minimum=1; maximum=500 | Use this to cap saved results and billable job events. |
| `includeDescription` | boolean | Use this to include a cleaned, capped job description. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## jobs-sh-scraper

Exact owner: `khadinakbar`. Identity: `eEmG7ByAaXJgmUPHY`. State: `public_schema_verified`.

Build `1.0.3` / `6nD47SyLKqTJ7Kn7j`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/jobs-sh-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Keyword search sent to Jobs SHZ, for example 'Pflegefachkraft' or 'Softwareentwickler'. The site matches its public vacancy index and accepts German job terms. Leave blank to collect the newest listings across the board. This is not a URL or an applicant name. |
| `startUrls` | array | Optional public Jobs SHZ search or job-detail URLs to collect, for example 'https://jobs.shz.de/jobs?search=Pflege'. The actor uses these instead of Job search query when provided. Up to 20 URLs are accepted. Do not provide login, applicant, or employer-admin pages. |
| `maxResults` | integer; minimum=1; maximum=200 | Maximum number of validated vacancy records to return. Enter an integer from 1 to 200; the default is 20. The per-vacancy event charges stop at this cap, keeping event costs bounded. This is not a page count. |
| `includeJobDetails` | boolean | Whether to open each public vacancy page for its description and additional fields. Keep enabled for recruitment research and detailed records. Default is true; disabling it returns listing-level fields faster. This does not access private applicant data. |
| `responseFormat` | string; concise, detailed | Controls the maximum public description length in every dataset record. Choose 'concise' for short agent-friendly records or 'detailed' for up to 8,000 characters of job text. Defaults to concise. This does not translate or summarize the original German content. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## bayt-jobs-scraper

Exact owner: `khadinakbar`. Identity: `BtSz4YwJNYSzjDEUY`. State: `public_schema_verified`.

Build `0.6.7` / `TxhSp9Z16hCgvQoPl`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/bayt-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchQuery` | string | Free-text job search keyword to run on Bayt.com (e.g., 'senior accountant', 'odoo developer'). Used with `country` to build the listing URL. Defaults to 'software engineer'. NOT a Bayt category slug — for category-based scraping leave this empty and set `jobCategory`. |
| `country` | string; international, uae, saudi-arabia, qatar, kuwait, bahrain, oman, egypt, lebanon, jordan, iraq, morocco, tunisia, algeria | Bayt MENA market to search. Determines locale and currency in results. Defaults to 'international' (cross-region). Country-specific slugs hit each country's localized Bayt subsite. Ignored when `startUrls` is set. |
| `jobCategory` | string | Optional Bayt category slug for category-based scraping (e.g., 'accounting', 'sales', 'engineering'). When set, overrides `searchQuery`. Leave empty to use keyword search. NOT a free-text field — must be a real Bayt category slug. |
| `startUrls` | array | Optional list of Bayt listing or job-detail URLs to scrape directly. When provided, overrides `searchQuery`, `country`, and `jobCategory`. Each URL must be a Bayt.com page (e.g., https://www.bayt.com/en/uae/jobs/sales-jobs/). Listing URLs auto-paginate up to `maxResults`; detail URLs extract a single job. |
| `maxResults` | integer; minimum=1; maximum=500 | Hard cap on jobs returned per run. Pricing is billed per job-found. Defaults to 50. Maximum 500. Set lower for budget caps; set higher for backfills. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## gulftalent-job-scraper

Exact owner: `khadinakbar`. Identity: `WACeEQaJHjjAi4vsj`. State: `public_schema_verified`.

Build `1.0.10` / `0MHbfXB6d1GNQFghi`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/gulftalent-job-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `searchUrls` | array | Use this when you already have a public GulfTalent search page with filters set in the site. Add up to 10 https://www.gulftalent.com/jobs/... URLs. These URLs override Keyword and are not direct individual-job lookups. |
| `keyword` | string | Use this when you want the actor to build a standard public GulfTalent search. Enter one role or skill phrase, for example software engineer. This is ignored only when GulfTalent search URLs are supplied. |
| `maxResults` | integer; minimum=1; maximum=200 | Use this when you need a predictable billable-result cap. The actor stores at most this many unique validated job records across all search pages; default 20 and maximum 200. |
| `maxPages` | integer; minimum=1; maximum=20 | Use this when Keyword builds the search URLs automatically. The actor requests no more than this many public result pages; this field is ignored when GulfTalent search URLs are supplied. |
| `includeJobDetails` | boolean | Use this when you need each job's public description, disclosed salary, experience, and other page-level fields. Disable only for a faster search-card export with less complete data. |
| `proxyCountry` | string; AE, SA, QA, KW, BH, OM | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## naukri-jobs-scraper

Exact owner: `khadinakbar`. Identity: `m5Iff4MjzhrwevpOm`. State: `public_schema_verified`.

Build `1.6.5` / `Fl5VmC4Cf1TtqEqnb`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/naukri-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `keyword` | string | Use this when you want to search Naukri by role, skill, or title. Enter a query such as 'software engineer', 'data analyst', or 'sales manager'. Defaults to 'software engineer'. This is not a Naukri URL, paste URLs into Start URLs instead. |
| `location` | string | Use this to restrict the Naukri search to a city, region, or remote-style location phrase. Enter values like 'bengaluru', 'mumbai', 'delhi ncr', or 'remote'. Defaults to 'bengaluru'. Leave empty to search all locations. |
| `startUrls` | array | Use this when you already have Naukri search-result pages or job-detail URLs to scrape. Accepts links from naukri.com search pages and /job-listings- detail pages. When provided, Keyword, Location, Experience, and Date posted are ignored for the first page. Do not paste non-Naukri URLs here. |
| `experience` | string; any, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | Use this to filter jobs by required years of experience. Choose 'any' or a starting year from 0 to 15, matching Naukri's search filter. Defaults to 'any'. This is not the extracted experience field returned in each job record. |
| `jobAge` | string; any, 1, 3, 7, 15, 30 | Use this to restrict results to recently posted jobs. Allowed values are 'any', '1', '3', '7', '15', and '30', representing days back on Naukri search. Defaults to 'any'. This is a search filter, not the returned postedAgo text. |
| `jobType` | string; any, full-time, part-time, contract, internship | Use this to keep Naukri jobs whose employment type matches 'any', 'full-time', 'part-time', 'contract', or 'internship'. Naukri's search URL uses jobPostType for company vs consultant, not employment type, so this Actor filters the returned jobType/employmentType (and title) after a normal search. Defaults to 'any'. This is a search filter, not the returned jobType field on each row. |
| `workMode` | string; any, office, hybrid, remote | Use this to restrict Naukri results by workplace. Choose 'any', 'office', 'hybrid', or 'remote'. Defaults to 'any'. This is a search filter mapped to Naukri wfhType, not the extracted workMode field. |
| `company` | string | Use this to restrict the search to one hiring company name when Naukri exposes that filter. Example: 'Infosys'. Leave empty for any company. This is not a Naukri company profile URL. |
| `maxItems` | integer; minimum=1; maximum=100000 | Use this to cap how many job postings the actor returns and bills for. Defaults to 50 and stops cleanly when the limit is reached. One returned job costs $0.006 plus the tiny run-start event. Do not use this as a page count. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `maxConcurrency` | integer; minimum=1; maximum=10 | Use this to control how many browser pages run at once. This is not the result limit. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `debugDumpHtml` | boolean | Internal troubleshooting flag that saves raw Naukri pages to the key-value store. Use this only when extraction returns zero jobs or the site layout changes. Defaults to false. Normal users should leave it disabled. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## seek-job-scraper

Exact owner: `khadinakbar`. Identity: `8N1Ho85C9Y6Cy5Tib`. State: `public_schema_verified`.

Build `1.6.1` / `yW9vwPQ9tvhYau7Od`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/seek-job-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `keywords` | string | Use this when you want the actor to build a SEEK search from a role or skill query. Enter ordinary search text such as software engineer or data analyst. It defaults to software engineer and can be combined with Location. Do not use this for a job URL or Boolean syntax that SEEK itself does not support. |
| `location` | string | Use this to narrow a keyword search to a SEEK place name. Enter a location such as Melbourne VIC or Auckland. It is optional and defaults to an Australia-wide or New Zealand-wide search when blank. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `country` | string; AU, NZ | Use this to choose the public SEEK site searched by structured keywords. Choose AU for seek.com.au or NZ for seek.co.nz. It defaults to AU. This does not override the host of a supplied direct SEEK search URL. |
| `searchUrls` | array | Use this when you already configured filters on a public SEEK results page. Enter one URL per line, such as https://www.seek.com.au/jobs?keywords=data+analyst. It is optional; when present it takes precedence over Job keywords and Location. Do not enter individual job pages, login pages, or URLs from other job boards. |
| `sortBy` | string; relevance, date | Use this to choose how a keyword-built SEEK search is ordered. Choose relevance or date, for example date. It defaults to relevance. This setting does not rewrite the filters or sort order embedded in a Direct SEEK search URL. |
| `maxResults` | integer; minimum=1; maximum=200 | Use this to cap the number of validated job records written to the dataset. Enter an integer such as 25. It defaults to 25 and accepts 1 through 200. This is not a page count; the actor stops before writing or charging more job rows than this limit. |
| `includeDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyCountry` | string; AU, NZ | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.

## stepstone-jobs-scraper

Exact owner: `khadinakbar`. Identity: `RRD6DxpNDigqXfwWu`. State: `public_schema_verified`.

Build `1.0.8` / `zg06WQsRnTkNslc10`; tag `latest`. Required keys: Check mode-specific conditions. [Full dated input schema](../schemas/stepstone-jobs-scraper.json).

Relevant input fields (schema guidance, not a ready-to-run request):

| Field | Type/mode/bounds | Meaning |
| --- | --- | --- |
| `keyword` | string | Free-text job search run on StepStone.de (e.g. 'data engineer' or 'pflegefachkraft'). Builds the search URL /work/{keyword}/in-{location}. Defaults to 'data engineer' when empty and no Start URLs are given. This is NOT a StepStone job-detail URL — paste those into Start URLs instead. |
| `location` | string | City or region in German spelling (e.g. 'Berlin', 'München', 'Nordrhein-Westfalen'). Combined with Keyword to build /work/{keyword}/in-{location}. Defaults to all of Germany ('deutschland') when empty. Ignored when Start URLs is provided. |
| `startUrls` | array | Optional list of StepStone.de search-result or job-detail URLs to scrape as-is. When set, Keyword, Location, and the filters below are ignored. Accepts /jobs/... and /work/... search pages and /stellenangebote--...-inline.html detail links. Example: https://www.stepstone.de/work/java/in-berlin. |
| `postedWithin` | string; any, 1, 3, 7, 14, 30 | Restrict results to jobs posted within the last N days, applied as StepStone's age facet. Allowed values: 'any', '1', '3', '7', '14', '30'. Defaults to 'any' (no date limit). Ignored when Start URLs is provided. |
| `workFromHomeOnly` | boolean | When enabled, returns only jobs that offer remote / work-from-home, using StepStone's wfh facet. Defaults to false (all jobs). Applies only to keyword/location searches, not to Start URLs. |
| `maxItems` | integer; minimum=1; maximum=100000 | Maximum number of job postings to return and bill for in this run (1 job = $0.003). Defaults to 100. The run stops once this many jobs are collected, even across multiple result pages. VibeLeads scope: qualify companies first. Optional contact extraction stays disabled in discovery; enable only a reviewed, relevant contact stage for named qualified businesses under the contact-use gate. Provider bounds are not recommended volumes or permission. |
| `enrichDetails` | boolean | VibeLeads scope: keep optional contact/detail extraction explicitly disabled during company discovery. A relevant stage for named qualified businesses requires verified actual build controls, source/use rights and suppression under the contact-use gate. Decline inseparable audience collection. |
| `proxyConfiguration` | object | VibeLeads restriction: enablement is unsupported. Verify a documented disabled/direct/public mode and actual build behavior before execution; otherwise decline this route. See the source access gate. |
| `maxConcurrency` | integer; minimum=1; maximum=50 | Maximum number of pages fetched in parallel. Defaults to 10. Most users should leave this at the default. Use only permitted direct/public or licensed API access verified against the actual build. Stop on access denial or rate limits; see the source access gate. |
| `debugDumpHtml` | boolean | Internal debugging flag. When enabled, raw HTML and parsed JSON candidates are saved to the key-value store for extraction troubleshooting. Leave off for normal runs. |

Verify actual output rows before mapping. Preserve company identity, source URL, event/collection date, contact state and evidence. Modes and optional enrichments can affect setup/cost; inspect conditions and current pricing. Summary/error rows are not leads.
