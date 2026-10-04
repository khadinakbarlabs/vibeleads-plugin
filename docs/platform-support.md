# Platform support

One repository contains the shared `skills/` tree and target-specific metadata. Platform manifests do not provide tools by themselves.

| Surface | Package contract | Execution dependency | Evidence |
| --- | --- | --- | --- |
| Claude Code | `.claude-plugin/plugin.json`, skills, optional local marketplace | Host tools and user’s authenticated data access | Native validators passed; source-directory prompt tests exercised prospecting, failover and enrichment. See validation report for observed repairs and limits; cached installation untested. |
| Claude Cowork | Shared skills and compatible plugin metadata | Actual executable/network/filesystem access in that environment | Not tested; imports/planning remain supported instructions. |
| Claude chat | Skills where supported | A local CLI is not available merely by installing skills | Live collection not asserted. |
| OpenAI/Codex | Root Agent Plugins `plugin.json` and `extensions.com.openai` | Suitable host tool access | Portable schema checked; live host install not asserted unless recorded. |
| ChatGPT web/mobile | Target’s actual plugin/skill capability | Existing capable tool; no bundled service | Local CLI execution not asserted. |
| Cursor | `.cursor-plugin/plugin.json`, shared skills | Host shell/tools and user account | Schema checked; UI installation not tested. |
| Other Agent Skills hosts | Whole shared `skills/` tree | Supported resource links and tools | Portable content; host behavior untested. |

Claude documentation: [manifest](https://code.claude.com/docs/en/plugins-reference), [security](https://code.claude.com/docs/en/plugins/security). OpenAI: [packaging](https://developers.openai.com/plugins/build/plugins), [submission](https://developers.openai.com/plugins/deploy/submission). Cursor: [official specification](https://github.com/cursor/plugins). Checked October 5, 2026.

Recurring-work guidance uses each host’s supported scheduler only when available. No real scheduled task was activated or tested in 0.2.0. Context/report files must be reachable from the chosen execution environment; local paths/login do not automatically carry into a cloud run. The attempted 0.2.0 native Claude conversation was blocked by the account usage limit; native manifest validation and independent scenarios passed.

Before release, refresh platform rules, load the final archive in each intended host, check discovered skills and behavior, and complete each vendor’s actual submission requirements. The same source repository can serve all destinations; vendor portals may require different ZIP layouts and listing fields.

Release 0.2.1 adds directory support/privacy/terms/documentation metadata. The current Claude Code validator loads the plugin but warns that these four directory-specific metadata fields are unknown; strict mode treats those metadata-only warnings as errors. The directory portal explicitly requests those fields. Runtime skills are unchanged from 0.2.0.
