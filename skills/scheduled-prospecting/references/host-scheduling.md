# Scheduling belongs to the host

Checked October 5, 2026. Host plans, versions and tool access vary; inspect available tools/settings again before creation. Package metadata does not make a scheduler or authenticated data runtime appear.

| Host | Supported path to inspect | Key execution check |
| --- | --- | --- |
| Codex desktop | Exposed native automation/task tools; use thread follow-ups where supported | Current project/thread, chosen local workspace, secure data access and confirmed task ID. Follow tool instructions for heartbeat/standalone choice. |
| Claude Code | Native scheduled tools, session loops, or supported Desktop/cloud tasks | Session loops and durable jobs differ; check lifetime, timezone, tool permissions and actual runtime. |
| Claude/Cowork | Native Scheduled tasks where available in the current plan | A remote session does not inherit local files/executables/login; verify connected resources and supported data access. |
| Cursor | Supported Automations workflow | Cloud execution, account usage and configured tools/credentials; local context is not automatically synced. |
| Another skills host | Its actual exposed scheduler | If absent, provide an inactive prompt/contract rather than invent a tool or silently install cron. |

Official references: [Claude Code scheduling](https://code.claude.com/docs/en/scheduled-tasks), [Claude scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork), [Cursor Automations](https://cursor.com/docs/cloud-agent/automations).

Current documentation distinguishes session-scoped Claude loops from persistent scheduling, and remote Claude/Cursor execution from local execution. Avoid hard-coding a lifetime, billing rate or machine-on rule for every host. Observe the selected host's actual creation result; state next fire/expiry only when confirmed. For private-local-data reports, choose a runtime that can reach that workspace or explicitly prepare a permitted synced input. Never copy keys/contact datasets to a cloud job just to make it work.
