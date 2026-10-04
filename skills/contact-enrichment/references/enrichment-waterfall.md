# Lead enrichment and email validation waterfall

Use the source catalog as the preferred route map, refresh live contracts before collection, and follow [Actor failover](../../lead-engine/references/actor-failover.md) when an owned route cannot cover the task or does not work. Preserve source/date/provider per field. Keep a single authorized discovery/enrichment/validation budget.

## Enrich in useful stages

1. **Account identity:** official company/domain, location and business model. Resolve ambiguous brands, subsidiaries and branches before people lookups.
2. **Company evidence:** published industry, office geography, observed size/headcount, technology and initiative signals where the actual source supports them. Public homepage extraction does not establish revenue or licensed firmographics.
3. **Professional roles:** relevant current business roles and public professional profiles. Verify account/employer match; title is not purchasing authority.
4. **Business contact discovery:** official contact page, published role address or supported work-email lookup. Keep published, provider-found and inferred pattern candidates distinct.
5. **Email validation:** syntax/DNS/classification first where useful; a separately configured mailbox-verification route if required and authorized. Keep actual verdict and provider/tier/date, not just an Actor's success flag.
6. **Quality/export:** suppression, exact-grain deduplication, provenance, uncertain/conflicting facts and an email-ready subset. Valid deliverability does not authorize sending.

Stop once the user’s needed fields/contact path are adequately supported. Avoid paying multiple providers for already complete fields. If a provider reports no matching contact, record it; do not invent one. Partial fallback results merge with retained rows, preserving their actual provenance.

## Preferred provided routes and precise limits

| Provided owned route | Useful stage | Important boundary |
| --- | --- | --- |
| Company-by-domain, company finder/profile/details | Company identity and supported professional/account details | Inspect actual fields, dates and employer/entity matching. |
| `zoominfo-alternative` | Bounded public-company-page enrichment and published contacts | Requires `companies`; public pages are not ZoomInfo’s licensed database, guessed contacts or mailbox validation. |
| `clearbit-alternative` | Public company/domain, website and published-contact evidence | Requires `companies`; no implied Clearbit subscription or validated mailbox. |
| `apollo-alternative` | Bounded public professional-role search by company/title/keywords | Not native Apollo licensed lead data, domain firmographics, funding filter or guaranteed verified email. |
| `rocketreach-alternative` | Known-name/employer work-email enrichment or supplied-address verification where configured | Mode and verification availability matter; candidate-only/MX results are not verified mailboxes. |
| `snov-io-alternative`, Lusha/Cognism/Seamless alternatives | Supported company/contact enrichment modes | Verify each current schema/data contract; a comparison title does not establish licensed vendor access. |
| Contact-details, bulk-website-contact and appropriate public-contact routes | Public business contact discovery | Published/found email remains unverified deliverability until actually checked. |
| `email-address-validator` | Syntax, DNS/MX and optional SMTP/classification checks | Required `emails`; cloud SMTP often returns unknown. Basic checks cannot establish mailbox validity. |
| `neverbounce-alternative` | Standard preflight or configured premium verification | Required `emails`; inspect `verificationTier`, supported cap, actual provider verdict and separate charges. Not official NeverBounce access. |
| `zerobounce-alternative` | Standard checks or configured premium provider verification | Required `emails`; premium uses the Actor’s configured owner-managed provider according to its observed schema. Confirm availability/verdict; no implied ZeroBounce subscription. |

Exact identities and safe schema snapshots are in the [catalog](../../lead-engine/references/source-catalog.md). They are dated input-contract evidence, not runtime certification.

## Apollo, ZoomInfo and other actual providers

Support a named provider through an Actor that demonstrably uses the requested authorized vendor source, or analyze a user-provided vendor export with accurate attribution. Prefer an owned implementation when available; a verified third-party implementation may fill the gap. Check required subscription/API entitlement and terms as well as platform authentication. The user's Apify API key alone does not provide Apollo/ZoomInfo or another vendor's licensed access.

If no authorized exact-source route is available, offer a clearly labeled alternative without claiming vendor affiliation. Changing publisher while keeping the same source is allowed within the current envelope; changing the requested underlying source needs agreement. Do not invent an endpoint, install a new server, expose vendor keys in chat, or present a sourced/pattern email as validator-backed.

Apply this source-change gate to an exact required vendor source. When providers are examples or requested “where available,” use the suitable accurately attributed route without another confirmation solely for the alternative label. Preserve external IDs and richer provider details in a companion mapping when using the [quality helper's canonical contract](../../lead-engine/references/record-contract.md).

## Validation output mapping

| Observed evidence | Canonical state / treatment |
| --- | --- |
| Invalid syntax or actual invalid provider verdict | `invalid`; excluded from email-ready files. |
| Syntax/DNS/MX passes without mailbox verdict | `unknown` or `not_checked` for deliverability; retain separate basic-check detail. |
| SMTP blocked/time-out/provider unavailable | `unknown`; disclose unprocessed/inconclusive coverage. |
| Catch-all or uncertain acceptance | `catch_all`; not automatically sendable. |
| Risk/disposable/role warnings requiring review | `risky` unless a more specific actual verdict applies; preserve reason. |
| Actual configured verifier reports mailbox valid | `valid` with exact-address validator evidence, provider and checked time; no guarantee of future delivery/consent. |

Use results of the actual source, not its marketing label. Do not flatten a provider's richer unknown/risky/catch-all outcomes into valid. Keep raw sensitive logs out of exports and redact unrelated data before retaining evidence.

A blocked SMTP attempt is inconclusive. Inspect the actual diagnostics before attributing it to a universal infrastructure rule; do not claim every cloud host blocks SMTP or that a premium tier guarantees a mailbox verdict. Verify live provider availability, batch limits, pricing and actual output. Avoid repeating the same blocked probe without evidence that conditions changed.
