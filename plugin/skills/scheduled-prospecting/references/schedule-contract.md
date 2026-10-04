# Recurring research contract

Apply the [source access gate](../../lead-engine/references/access-safety.md) before every pilot, fallback or resumed window. Access-denied, challenged or rate-limited sources do not qualify for automatic recovery; preserve partial rows and pause that source until permitted access is restored.

A recurring prompt is a durable action request, not unlimited permission. Use human-readable task instructions; never place keys in scheduler prompts or records.

## Fields to resolve

Business/profile + chosen context workspace; actual goal and exact data sources; account/contact/branch grain; filters/exclusions/suppression; cadence and IANA timezone; per-run cap and shared period cap/currency; period boundaries/renewal and expiry; result and runtime limits; included enrichment/validation stages; output file destination; notification trigger/destination; allowed action set; pause/stop conditions; resume/dedup/window policy.

Reuse explicit existing values. For missing required constraints ask one grouped question; continue with preparation meanwhile. A “weekly report” may analyze saved files without paid discovery. A zero collection allowance can be explicitly used for report-only mode; host model/scheduling usage may still incur charges under the user's plan. Do not present a report-only host job as universally free.

## Ready prompt pattern

Read the chosen business brief and current handoff for this profile. Run only the listed research/report actions within the stated sources, limits and expiry. Before any paid work reconcile cumulative actual spend, unresolved/in-flight reservations and other jobs sharing the period allowance. Do not reset budget on retries or session creation. Reuse preferred owned routes; verify suitable same-source fallback only for actual gaps/failure. Apply suppression and exact-grain deduplication before paid lookups. Retain partial usable records, and report COMPLETE/VALID_EMPTY/PARTIAL/failure truthfully. Never send messages, upload contacts or enroll outreach unless specifically included with a destination. Write the private report/handoff to the chosen workspace. Notify only on a meaningful change/failure or at the requested digest cadence. Stop new paid work when any required constraint, access or allowance is missing; return a useful status.

## Windows, recovery and overlapping runs

Use `[start, end)` in a declared timezone converted to UTC. The event/posting/launch date is not the collection date. A configured lookback overlaps old records deliberately; dedupe by stable entity + event identity, not only row position. Do not claim sources support date pagination merely because a date field exists; inspect actual schema/coverage.

The committed cursor advances only when all required source/query partitions for that window are complete. On partial/upstream failure, keep usable rows, record the failed window/partitions and retain the last complete cursor. Resume the same failed window's missing coverage within remaining allowance. Dataset pagination reads existing results; it does not revive a terminal failed collection run.

Sequential execution is the default for shared caps. Prevent duplicate jobs, overlapping scope and duplicate billable starts; where no reliable shared reservation/lock exists, do not promise a hard cross-process spending guarantee. Use a single sequential monitor or report-only mode. For a period reset, use the explicitly defined timezone/boundaries and first reconcile older in-flight exposure; do not automatically forgive unresolved charges.

## Good recurring uses

| Goal | Output | Useful trigger |
| --- | --- | --- |
| Weekly prospect review on saved files | Visual brief, feedback changes, next segment | Requested weekly digest |
| New relevant hiring/launch signal | Dated company evidence and fit reason | New qualified signal, not every raw job |
| Public local-business opportunity refresh | New/changed account issue with provenance | Material change; avoid re-paying for unchanged fields |
| Email-status refresh | Actual updated verifier outcomes | Configured stale-validation rule, inside included allowance |
| Source/coverage recovery | Resumable partial status, failure explanation | Failure or missing access; no endless paid retries |

Do not schedule nagging “come back” prompts solely to increase sessions. More use should follow useful recurring business changes.
