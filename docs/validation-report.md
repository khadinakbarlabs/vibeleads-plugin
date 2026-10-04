# VibeLeads 0.2.0 validation — October 5, 2026

## Observed result

One skills-only plugin, 26 skills, three platform manifests and no bundled agent personas/service/scheduler. Revision 0.2.0 adds business-context, adaptive-prospecting, feedback-learning, session-continuity, scheduled-prospecting and lead-reporting. Context/feedback use deliberate scoped workspace files; recurring jobs use actual host capabilities. No claim of a measured tenfold conversion or productivity gain.

## Current verification

| Check | Observed result |
| --- | --- |
| Automated suite | 68 passed: 28 lead-quality, 29 reporting and 11 release tests. New coverage includes actual email denominators, suppression, grain identities, full canonical/evidence changes, newly excluded versus absent, historical suppression, unknown budget, reserved charges, overspend, input protection, safe HTML/Markdown, opaque feedback references and three-format CLI output. |
| Independent code/security review | Accuracy, privacy, XSS, path safety, feedback behavior and accessible focus were reviewed. Findings repaired and rechecked. No remaining blocker in reviewed scope. |
| Independent forward evaluation | Six realistic fictional scenarios produced useful briefs/handoffs/feedback/recovery artifacts: no allowance reset, small-sample caution, untrusted feedback rejection, partial monitor cursor/reservation recovery, absent-runtime inactive schedule, and deliberate scoped feedback without telemetry. |
| Real browser interactions | Chrome via Playwright: search, quality filter, empty state, displayed exclusion search, selected-feedback label search, explicit feedback download and clearing on reload passed. No remote request or browser error. |
| Responsive/visual | No horizontal overflow at 1440, 820, 390 and 320 pixels. Desktop/mobile reports visually inspected. Preview and downloadable HTML/Markdown/JSON/PDF use clearly fictional records. |
| Skill scaffolds | All 26 passed Skill Creator frontmatter/naming/scaffold validation. |
| Native Claude manifests | Plugin and local marketplace passed strict validation separately. |
| Portable/OpenAI and Cursor | Current manifests passed the included official schema snapshots; display/subtitle/starter limits passed package checks. |
| Native Claude v0.2 prompt evaluation | Attempted context/feedback/schedule scenario, but the account session usage limit blocked execution immediately. Not counted as a passed behavioral test or plugin failure. |
| Packaging | Root and enclosing-folder archives validated after extraction and matched source bytes. Final hashes are in the export directory's archive-report.json. |

Independent review found incomplete changed-field detection, observed exclusions counted as absent, retroactive prior suppression, indistinguishable same-company contact/branch cards, and low focus contrast. Regression tests repaired these. The feedback UI then exposed search matching unselected option labels; substantive record search and selected-label search were fixed and checked in the actual browser. User-facing reason codes are translated into plain language, while canonical JSON retains exact reasons.

## Prior evidence and scope limits

The [0.1.1 validation history](validation-history-0.1.1.md) records earlier native Claude prospecting/enrichment checks, source inspection and initial repairs. The source map still has 14 detailed families and 152 preferred routes: 149 public metadata/default schemas inspected, three public HTTP-404 gaps. No route is labeled runtime-tested. This revision did not spend on lead collection or perform another full live inventory/schema refresh.

No actual recurring job was activated or run; no paid Actor run, outreach, CRM upload, background service, public repository publication or vendor submission occurred. Host scheduling references were refreshed from official Claude/Cursor docs, but installed runtime/secure data access must be checked in each intended host. Local credentials and files do not automatically exist in a remote job. Recurring budget/cursor/locking rules are host workflow instructions, not an executable distributed spend controller.

The independent evaluation and automated/browser tests establish confidence in their recorded scope. They do not establish real conversion lift, future source health, cross-host installation, cached marketplace loading, cloud-task execution, SMTP/provider deliverability or vendor approval. Saved context is scoped readable files or optionally enabled host memory, not hidden training or automatic cross-host sync. A local feedback download is not a message sent to the developer.

## Reproduce

Run `python3 -m unittest discover -s tests -v`, `python3 scripts/validate_package.py`, separate native manifest validators and `python3 scripts/package_release.py --output <directory-outside-source>`. Official schema checks use the maintainer's jsonschema library; user-facing helpers need only Python's standard library.

Create the fictional report with `python3 plugin/skills/lead-reporting/scripts/lead_report.py tests/fixtures/report-demo.json --summary tests/fixtures/report-demo-summary.json --html <outside-source>/brief.html --markdown <outside-source>/brief.md --json <outside-source>/brief.json`. Check search/filter/feedback/print in a current browser; feedback should not upload, survive reload or include full contact rows. Model behavior cases live in tests/behavior-cases.json; not every listed future scenario was run. Raw host outputs and independent artifacts remain outside the public release tree.

Revision 0.2.2 distribution check: 69 tests pass (including the new installable-scope assertion). All 250 skill/resource files are byte-identical after the move. Root and portable archives contain 261 runtime files, all 26 skills and both offline helpers; maintainer tests/tools/docs and marketing preview are excluded. The four valid directory URL fields still warn on the installed older Claude validator; see the current official manifest reference for the v2.1.281 acceptance threshold.
