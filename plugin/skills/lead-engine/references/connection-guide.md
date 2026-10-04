# Data connection and Apify CLI execution

Before collection or recovery, apply the [source access gate](access-safety.md). Catalog/schema verification is not execution permission. Denied underlying source access is excluded from Actor failover and automatic retries.

VibeLeads supplies skills, not an executable data engine. The agent uses the independently installed official Apify CLI or a capable existing authenticated integration. An Apify API key is required; each user uses their own account. The publisher’s account and keys are never shipped.

## First-run check

1. Inspect the host’s existing tools. Reuse an authenticated integration only if it can inspect exact Actor identity/schema/pricing, start within a supported charge envelope, read run state and paginate results. Do not install/register an MCP server just to enable the plugin.
2. Otherwise check `apify --version` and installed command help. The build-time check used CLI 1.8.0; current documentation may describe newer flags. Missing executable: explain official installation and authentication, and continue preparing the plan. Do not change global tools without the user’s setup authorization.
3. Use `apify info` for account presence; never use `apify auth token` or inspect `~/.apify/auth.json`. If login is needed, have the user use the official supported login or host secret configuration. Do not paste `APIFY_TOKEN` into chat or commands. Confirm account identity without displaying credentials.
4. If the host has neither shell nor capable integration, retain the exact source plan and offer a user-supplied export. Cloud ChatGPT and Claude chat cannot necessarily invoke your local CLI.

## Inspect before execution

Current help is authoritative for installed syntax. `apify actors info` may include nested source files/environment in authenticated metadata: parse internally and emit only id, name, username, isPublic, selected build id/number, public pricing, required input keys and safe schema. Never save/print entire metadata/build responses.

```sh
apify actors info <exact-verified-id> --input
apify api --describe 'actors/{actorId}/runs'
apify api --help
apify runs info --help
apify datasets get-items --help
```

Prefer the owned catalog; use the [Actor failover guide](actor-failover.md) to discover and verify another publisher when needed. Confirm exact identity and actual publisher for every route. Catalog snapshots under `schemas/` are credential-free references with defaults/prefills removed. Refresh against the current default build. Do not pull private source or deploy changes. IDs are cataloged; friendly titles and lookalike names do not establish equivalence.

Create an input file using the current required fields, enums, bounds and cross-field conditions. Read the Actor’s README for semantic validation such as “search mode requires a query.” Add only supported item limits and optional flags; platform query controls do not belong in Actor input. Unknown input fields may be ignored, so validate rather than relying on apparent acceptance. Public URLs must not point to loopback, private networks, credential-bearing URLs or local files. Required provider credentials mean additional setup, never permission to share another secret.

## Bounded execution

Do not start without an authorized total spend and stage allocation. Inspect pricing for startup/minimum fees, pay-per-event meters, platform usage and optional enrichment. Platform charge caps are spending controls, not fixed-price guarantees; termination can lag. A user’s hard ceiling must not be represented as a mathematically exact cap if the platform cannot enforce it.

The installed CLI accepts authenticated requests with stdin JSON. After verifying current endpoint parameters and user authorization:

```sh
apify api POST 'acts/<exact-verified-id>/runs' --body - --params '<verified-limit-query-JSON>' < input.json
```

`verified-limit-query-JSON` must contain supported `maxTotalChargeUsd` and `timeout`, plus a selected verified build when appropriate. Verify units and permitted build/memory values. Do not copy placeholder text into a real command. Use exact IDs and files through argument arrays; use the shell only with correct quoting. Default optional enrichment off. If a minimum charge exceeds the allocation, stop and revise the plan with the user.

An alternative `apify actors start` is suitable only if its installed options can enforce the same envelope. An existing MCP connection alone does not prove this. Never invoke an uncapped tool as fallback.

Record run ID immediately; ambiguous start failures need readback, not an automatic retry. Poll using `apify runs info <run-id> --json` with bounded waits. Filter summaries internally. Save a resumable state if work remains running; do not endlessly poll or announce it complete.

## Collect and inspect

```sh
apify datasets get-items <dataset-id> --format json --limit 100 --offset 0
```

Continue with offset 100, 200, etc., to the authorized output limit or exhausted dataset. Report truncation. Inspect keys in the run’s actual key-value store and collect `OUTPUT`/`RUN_SUMMARY` when present; do not assume both exist. Keep diagnostic/summary/error rows out of the lead table. A successful empty dataset plus upstream errors is a coverage failure, not evidence of zero market demand.

Map the observed fields to the [record contract](record-contract.md) before quality checks. Preserve the original source URLs, timestamps, observed fields and validation status. Report aggregate actual charges if available, remaining budget and incomplete pages; do not expose unrelated run/customer records.

## Troubleshooting

| Problem | Response |
| --- | --- |
| CLI missing | Give official setup link; finish a source plan or analyze an import. |
| Key expired or wrong account | Request reauthentication through secure settings/login; no credential echo. |
| Preferred owned Actor unavailable or unsuccessful | Verify a suitable fallback and continue within the remaining authorized budget; explain the publisher switch. |
| Live schema differs | Rebuild input and validate; do not reuse the old request silently. |
| Additional source key required | Explain setup requirement; optional feature stays off. |
| Cap below minimum | Stop; do not raise the cap on your own. |
| Start timed out after possible creation | Reconcile matching run metadata before another start. |
| Source blocked or data incomplete | Preserve usable rows; disclose partial coverage and a concrete next step. |

Sources checked October 5, 2026: [CLI reference](https://docs.apify.com/cli/docs/reference), [run endpoint](https://docs.apify.com/api/v2/actors-runs-post), installed CLI help. These instructions do not install or connect anything automatically.
