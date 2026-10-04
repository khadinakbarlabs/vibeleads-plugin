---
name: scheduled-prospecting
description: Prepare or manage bounded recurring lead research, saved-list refreshes, signal monitors and weekly reports using the host's supported scheduler. Use for daily leads, weekly reviews, reminders, monitoring or scheduled prospecting.
---

# Scheduled Prospecting

Apply the [shared contract](../lead-engine/references/operating-contract.md), [schedule contract](references/schedule-contract.md) and [host guide](references/host-scheduling.md).

First distinguish a report on existing files, a source monitor with paid collection, and a reminder. The user's request to add scheduling capability to this plugin does not activate a real job. For an actual recurring request, reuse an applicable existing job rather than duplicate it; obtain only missing scope/timezone/allowance/destination details and prepare a concrete short contract.

Inspect the current host's scheduling tools, tool execution, secure credentials and persistence/file access. A local authenticated executable does not automatically exist in a cloud sandbox. Use the supported host scheduler when available and authorized; do not create a daemon, shell cron workaround or remote service from plugin instructions. If capability is absent, deliver the ready prompt/contract and say it is inactive. Never fabricate a scheduled job ID.

Each run loads the same scoped business context and checks expiry, permitted actions, suppression, cumulative budget and overlap/pending runs before collection. Reconcile ambiguous launches; reserve unresolved charges. Process only new/missing coverage with the proper date field and half-open window. Commit the cursor only after all required partitions for that window complete; partial usable rows can be retained and deduped for recovery.

Apply the owned-first/fallback rules within the remaining run/period envelope. No automatic enrichment tier, source change, paid subscription, outreach, CRM upload or extra spend outside the contract. Stop new paid work at expiry, absent scope/access or exhausted allowance. Sequential tasks or a trustworthy atomic reservation are required when several jobs share a budget; if that cannot be enforced, do not launch concurrent paid jobs.

Report useful new/changed prospects and actual source failures/coverage gaps. Stay quiet on unchanged/non-actionable polls unless a scheduled digest was requested. Keep notifications in the host/task; sending to email/Slack or another destination requires that explicit authorization. Provide job ID, next run/timezone and scope only after the host confirms them; pause/edit/delete through the host's supported controls.
