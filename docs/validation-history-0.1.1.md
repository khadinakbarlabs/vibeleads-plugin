# VibeLeads 0.1.1 validation — October 5, 2026

## Outcome

Local skills-only source and two archive layouts built. Revision 0.1.1 adds company/contact enrichment, email validation and owned-first routing with verified other-publisher fallback when needed. 20 skills, 14 detailed source-family guides, 152 selected owned routes: 149 public metadata/default input schemas verified; 3 routes returned public HTTP 404 and remain explicit coverage gaps. Public schema visibility does not prove live source health. No paid Actor collection, outreach, CRM upload, scheduling, deployment or marketplace submission occurred.

## Verification

| Check | Observed result |
| --- | --- |
| Offline lead qualification and release tests | 39 passed: evidence scoring, status separation, suppression, account/contact/branch grains, stronger duplicate selection, matching contact-route evidence, malformed input, CSV formulas, private/ambiguous URLs, private release files, manifest path escape, symlinks, missing resources/assets, archive round-trip. |
| Skill Creator validation | All 20 skills passed frontmatter/naming/scaffold checks. |
| Native Claude manifest validation | Plugin and local marketplace both passed `claude plugin validate --strict` on Claude Code 2.1.165. They were validated separately because a marketplace file can take precedence when validating a directory. |
| Portable/OpenAI schema | Root manifest passed the retrieved Agent Plugins 1.0 JSON Schema. Presentation name/subtitle/prompts fit current limits. |
| Cursor schema | Compatibility manifest passed Cursor’s official plugin schema. |
| Native Claude source-planning test | Explicit skill invocation loaded successfully. Exact Apollo request with no Apollo subscription disclosed the source gap; strict Series A/date qualification required actual financing evidence. No tool for live collection was enabled. |
| Native Claude natural-language test | A request for 15 independent Austin dental practices activated VibeLeads guidance and produced an editable ICP and useful plan without fabricated clinic records or collection. |
| Independent forward tests | Exact source, Product Hunt + financing, untrusted imported commands, unknown deliverability, suppression and distinct contacts were exercised in an isolated fictional workspace. Findings were repaired and rechecked. |
| Independent 0.1.1 enrichment/failover tests | Four read-only scenarios passed: charged partial failure retains rows and remaining budget; valid-empty avoids automatic spend; syntax/MX with blocked SMTP stays non-sendable; exact vendor source requires authorized access. Fictional 8+6 overlap merge retained eight originals and produced 12 unique accounts; a companion mapping retained original ID and validator details. |
| Final native Claude email-validation check | Passed the targeted offline scenario: eight company rows did not become eight emails/qualified accounts; blocked SMTP stayed `unknown`; no unverified warmup sends were advised; email-ready set remained empty; fallback reused $2 remaining; original IDs/provider detail used a companion mapping. No collection tool was enabled. |
| Third-party discovery smoke | Read-only catalog searches returned four Google Maps and three email-validation candidates from other publishers. This establishes discovery, not suitability, runtime health or live fallback delivery. |
| Offline CLI fixture | Canonical fictional records: qualified=1, review=2, excluded=1. Only the validator-backed qualified email entered the sendable CSV. |
| Assets | Existing owner’s VibeLeads mark rendered as 512×512 PNG, 16,055 bytes; visually inspected and included. |
| Distribution | Root-layout and enclosing-folder ZIPs extracted and matched source byte-for-byte; hashes in exported archive-report.json. |

The first native source-plan evaluation exposed excess implementation detail and unverified rate references in its draft. The shared contract was tightened to keep technical records separate and forbid quoting schema/example prices as current rates. The subsequent natural-language test stayed in business/plan language. Independent review found and repaired duplicate ordering, contact provenance, malformed disqualifiers, keyword/public-token guide descriptions, private-file packaging, unsafe manifest names and ambiguous URL qualification.

The first 0.1.1 native offline prompt exposed redundant approvals for optional provider examples and included premium validation, ambiguous failed-run resume language, and an overgeneralized SMTP explanation. Shared contracts were repaired: exact required sources are distinct from examples/“where available”; included enrichment/validation reuses the authorized remaining envelope; reading a dataset does not restart a terminal failed run; blocked SMTP is inconclusive. Independent review also repaired two stale owned-only sentences and made companion mappings explicit for external IDs and richer validation details. A subsequent native test correctly reused authorization and preserved mappings but still invented email denominators from company counts and suggested sending unverified addresses for warmup. The contract now explicitly requires actual counts, blocked-SMTP state `unknown`, and verification rather than warmup sends. This evidence is retained as a model-behavior limitation, not hidden as a passed test.

## Limits and remaining release gates

- CLI 1.8.0 presence/help and authenticated owned inventory were checked. Catalog/schema reads used public endpoints with TLS verification. No new Actor run or runtime output delivery was tested; none of the 149 routes is labeled runtime-tested.
- The three unavailable public routes are 2GIS Places, Acquire.com and Luma. They remain in the preferred map as gaps, not available production sources; a suitable verified other-publisher route can fill missing coverage.
- Claude source-directory loading was exercised. Cached marketplace installation, Cowork/cloud-shell access, Codex/OpenAI plugin installation and Cursor UI installation were not exercised. Same-repository packaging is established; each host’s execution dependency still needs a host check.
- The source and archives are local. No public repository publication, public policy/support URLs, publisher verification, country/commerce declarations, portal scans, attestations, vendor review or live directory availability has been claimed.
- Models can vary in routing and verbosity; schema/text validation cannot prove all prospecting outcomes. Scenario tests improve confidence within the recorded scope, not perfection.

## Reproduce

From the source root, run `python3 -m unittest discover -s tests -v`, `python3 scripts/validate_package.py`, the native Claude validators, and `python3 scripts/package_release.py --output <directory-outside-source>`. Schema checks require the maintainer’s `jsonschema` library; the user-facing offline helper has only standard-library dependencies. Behavioral prompts live in `tests/behavior-cases.json`. Raw native-host evaluation output is outside the release tree; it is not included in archives or vault notes.
