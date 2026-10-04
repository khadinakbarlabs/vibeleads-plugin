---
name: lead-reporting
description: Present lead research as an evidence-backed visual brief, quality dashboard, session comparison or printable report with honest counts and budget status. Use for reports, charts, weekly reviews, presentation or clearer lead-list handoffs.
---

# Lead Reporting

Apply the [shared contract](../lead-engine/references/operating-contract.md) and [report guide](references/report-guide.md).

Lead with the business result: best prospects, why they fit/why now, completeness and the next action. For a small result, a concise table is enough. For larger/recurring work, create a private interactive HTML brief plus readable Markdown and structured JSON when useful. Default cards show company, score, evidence and uncertainty; minimize exposed contact data and keep full mappings separate.

Use actual canonical input records, observed coverage and attributed actual spend/reserved allowances. The optional offline helper recalculates quality through the shared lead-quality engine, rather than trusting imported scores or `email_sendable` claims. Never equate company counts with email counts, job success with complete source coverage, or score with conversion probability.

For session comparisons, use the same grain/scope and reviewed prior canonical rows. Label new, retained, changed and not observed; missing from partial coverage does not establish disappearance. Rich provider detail/original IDs remain in the companion mapping. Source-domain counts describe evidence coverage, not independent-provider reliability or revenue attribution.

Use the bundled helper if Python is available:

```sh
python3 <skill-directory>/scripts/lead_report.py canonical.json --grain account --summary summary.json --previous previous-canonical.json --suppression suppression.json --html brief.html --markdown brief.md --json brief.json
```

Read help first. Optional inputs can be omitted. Outputs must be outside the plugin, distinct from inputs, and do not replace existing files unless `--overwrite` is explicitly intended. The HTML has search, bucket filters, expandable evidence, deliberate feedback selections/download and print/save-PDF; no remote assets, tracking, network collection or sender. Feedback remains page-local until the user downloads it and asks the host to apply it in context. If Python/HTML is unavailable, generate equivalent Markdown/host visuals with the same evidence and counts.

Open/show the finished local report through a supported host artifact tool. Do not claim a queued tab is visible or a Markdown-only output is an interactive report. Review before sharing/exporting: user business information may be sensitive. Saving a requested private artifact is routine; publishing it or sending it externally needs that authorization.
