# VibeLeads: B2B Lead Finder

Find the right companies, understand why they might buy, and prepare a lead list you can trust.

VibeLeads is a skills-only plugin for your AI assistant. It brings the prospecting process together: ideal customer profiles, source selection, buying signals, company research, company and public contact enrichment, email validation, qualification, list hygiene, account plans, and outreach drafts. It also reuses scoped business context, improves targeting from deliberate feedback, resumes sessions, prepares bounded recurring research and produces private visual reports.

**An Apify API key is required for live collection.** Use your own account; data collection is billed there. Planning and working with files need no data connection. Setup details belong in the [connection guide](skills/lead-engine/references/connection-guide.md).

## Start with a normal request

- “I sell SEO to dentists. Find 25 independent clinics in Austin with evidence of a website or reputation problem.”
- “Find SaaS companies hiring their first growth marketer. Show the job date and the company behind it.”
- “Find Product Hunt launches relevant to my onboarding service, then research the teams.”
- “I asked for Apollo data. Tell me which exact route you can use before running anything.”
- “Enrich these companies and contacts, prefer my Actors, and use a suitable fallback where needed.”
- “Validate these business emails and separate actual mailbox verdicts from basic syntax and MX checks.”
- “Clean this CSV, preserve distinct contacts at one company, and flag unverified emails.”
- “Draft three personal opening lines for the strongest accounts. Leave them ready for review.”
- “Remember this business brief in my chosen workspace, then continue from it next session.”
- “These leads are mostly chains. Improve the targeting and explain what you changed.”
- “Make a visual report with evidence, uncertain emails, changes since last session and next actions.”
- “Prepare a weekly review of my saved prospects. Use the host scheduler only when available.”

The assistant uses existing context, asks only for material missing information, and prepares a small search plan. It explains the sources, exclusions, output, and any collection cost before a billable search. It respects previously authorized budgets.

## What you receive

A ranked company or contact list with source links, dates, fit reasons, buying signals, contact status, confidence, exclusions, and the next useful action. CSV exports escape spreadsheet formulas. A successful search with zero matching companies is reported as an empty result. Partial coverage and unknown email deliverability stay visible.

## Workflows

| Workflow | Skill |
| --- | --- |
| Guided prospecting from an offer to a lead list | `lead-engine` |
| Understand the business and reuse a scoped brief | `business-context` |
| Choose a useful next search from evidence and feedback | `adaptive-prospecting` |
| Learn preferences from deliberate feedback | `feedback-learning` |
| Resume sessions without repeating work or resetting spend | `session-continuity` |
| Bounded recurring research and weekly reviews | `scheduled-prospecting` |
| Interactive reports, comparisons and feedback download | `lead-reporting` |
| ICP, territory, pains, disqualifiers, offer hypotheses | `ideal-customer-profile` |
| Select sources and disclose coverage gaps | `source-planning` |
| Local businesses and service opportunities | `local-business-prospecting` |
| B2B companies and decision makers | `b2b-prospecting` |
| Startups, launches, software and app ecosystems | `startup-prospecting` |
| Jobs, hiring and expansion | `hiring-signals` |
| Public problem and demand signals | `community-intent` |
| Reviews, competitors and replacement opportunities | `review-opportunities` |
| Ad activity and technology evidence | `competitive-signals` |
| Merchants, suppliers and public tenders | `commerce-prospecting` |
| Events, communities and channel partnerships | `partnership-prospecting` |
| Creator businesses and agencies | `creator-prospecting` |
| Account and decision-maker enrichment | `company-enrichment` |
| Mailbox validation and honest quality states | `email-validation` |
| Public business contacts and email quality | `contact-enrichment` |
| Account research and buying committee | `account-research` |
| Qualification, suppression, deduplication and exports | `lead-list-quality` |
| Evidence-based outreach drafts | `outreach-drafting` |
| Pipeline handoff and prospecting experiments | `pipeline-handoff` |

See the [source coverage guide](skills/lead-engine/references/source-coverage.md) and [source catalog](skills/lead-engine/references/source-catalog.md). Your Actors are preferred. If they are unavailable, do not cover the task, or fail, the assistant can use a verified Actor from another publisher, explain why, and stay within the remaining authorized budget. See [fallback guidelines](skills/lead-engine/references/actor-failover.md).

Cataloged schemas describe availability at inspection time; they do not prove every route produces working lead data. Apollo, ZoomInfo and similar branded databases are not implied by similarly named alternatives.

## Better decisions across sessions

VibeLeads uses the current host model to research your business and form a narrow, editable search hypothesis. It separates confirmed facts from assumptions, learns from explicit corrections, and recommends the next useful action. Saved business briefs and handoffs live in your chosen workspace; the plugin does not create invisible memory or need another model API key.

The visual report includes search, quality filters, expandable evidence, budget status, session comparisons, deliberate feedback download and print/save-PDF. It recalculates qualification from canonical evidence. [Reporting guide](skills/lead-reporting/references/report-guide.md) · [Context guide](skills/business-context/references/context-protocol.md).

Scheduled research uses the host’s supported scheduler with explicit scope, timezone, run/period allowance and stop rules. No schedule starts on installation. Local credentials do not automatically work in a cloud runner. [Scheduling guide](skills/scheduled-prospecting/references/schedule-contract.md).

## Install from the same repository

Claude Code: install from GitHub with `/plugin marketplace add khadinakbarlabs/vibeleads-plugin`, then `/plugin install vibeleads-b2b@vibeleads-local`. For local development, test with `claude --plugin-dir /absolute/path/to/vibeleads/plugin`, then use `/vibeleads-b2b:lead-engine` or natural language. For a local marketplace, run `/plugin marketplace add /absolute/path/to/vibeleads` followed by `/plugin install vibeleads-b2b@vibeleads-local` in Claude Code.

Codex/OpenAI: use the portable release package with the host’s supported installation flow. Use the host’s supported local plugin flow. The package cannot make a local executable available to a cloud chat that lacks shell access.

Cursor: use the shared portable package with Cursor’s plugin workflow. Load through the host’s supported plugin workflow. Other Agent Skills hosts can discover the shared `skills/` directory; keep the whole directory together because the skills share resources.

See [platform support](https://github.com/khadinakbarlabs/vibeleads-plugin/blob/main/docs/platform-support.md) for tested and untested surfaces. Loading skills, connecting data, and marketplace approval are separate checks.

## Optional local tools

Python 3.10+ is needed only for the optional offline quality and reporting helpers. These helpers read specified files and produce local outputs. Read the [record contract](skills/lead-engine/references/record-contract.md) before mapping source data.

## Trust

[Privacy](PRIVACY.md), [terms](TERMS.md), [security](SECURITY.md), [support](SUPPORT.md), [inspiration and attribution](THIRD-PARTY-NOTICES.md).

The source is published at [khadinakbarlabs/vibeleads-plugin](https://github.com/khadinakbarlabs/vibeleads-plugin). Tagged packages are available from [GitHub Releases](https://github.com/khadinakbarlabs/vibeleads-plugin/releases). Vendor directory review and approval are separate from GitHub availability; see the [submission handoff](https://github.com/khadinakbarlabs/vibeleads-plugin/blob/main/docs/submission-handoff.md) for observed status.
