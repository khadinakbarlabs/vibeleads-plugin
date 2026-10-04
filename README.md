# VibeLeads: B2B Lead Finder

Find the right companies, understand why they might buy, and prepare a lead list you can trust.

VibeLeads is a skills-only plugin for your AI assistant. It brings the prospecting process together: ideal customer profiles, source selection, buying signals, company research, public contact enrichment, qualification, list hygiene, account plans, and outreach drafts.

**An Apify API key is required for live collection.** Use your own account; data collection is billed there. Planning and working with files need no data connection. Setup details belong in the [connection guide](skills/lead-engine/references/connection-guide.md).

## Start with a normal request

- “I sell SEO to dentists. Find 25 independent clinics in Austin with evidence of a website or reputation problem.”
- “Find SaaS companies hiring their first growth marketer. Show the job date and the company behind it.”
- “Find Product Hunt launches relevant to my onboarding service, then research the teams.”
- “I asked for Apollo data. Tell me which exact route you can use before running anything.”
- “Clean this CSV, preserve distinct contacts at one company, and flag unverified emails.”
- “Draft three personal opening lines for the strongest accounts. Leave them ready for review.”

The assistant uses existing context, asks only for material missing information, and prepares a small search plan. It explains the sources, exclusions, output, and any collection cost before a billable search. It respects previously authorized budgets.

## What you receive

A ranked company or contact list with source links, dates, fit reasons, buying signals, contact status, confidence, exclusions, and the next useful action. CSV exports escape spreadsheet formulas. A successful search with zero matching companies is reported as an empty result. Partial coverage and unknown email deliverability stay visible.

## Workflows

| Workflow | Skill |
| --- | --- |
| Guided prospecting from an offer to a lead list | `lead-engine` |
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
| Public business contacts and email quality | `contact-enrichment` |
| Account research and buying committee | `account-research` |
| Qualification, suppression, deduplication and exports | `lead-list-quality` |
| Evidence-based outreach drafts | `outreach-drafting` |
| Pipeline handoff and prospecting experiments | `pipeline-handoff` |

See the [source coverage guide](skills/lead-engine/references/source-coverage.md) and [source catalog](skills/lead-engine/references/source-catalog.md). Cataloged schemas describe availability at inspection time; they do not prove every route produces working lead data. Apollo, ZoomInfo and similar branded databases are not implied by similarly named alternatives.

## Install from the same repository

Claude Code: test with `claude --plugin-dir /absolute/path/to/vibeleads`, then use `/vibeleads:lead-engine` or natural language. For a local marketplace, run `/plugin marketplace add /absolute/path/to/vibeleads` followed by `/plugin install vibeleads@vibeleads-local` in Claude Code.

Codex/OpenAI: the root `plugin.json` uses the portable Agent Plugins format. Use the host’s supported local plugin flow. The package cannot make a local executable available to a cloud chat that lacks shell access.

Cursor: the repository includes `.cursor-plugin/plugin.json`. Load through the host’s supported plugin workflow. Other Agent Skills hosts can discover the shared `skills/` directory; keep the whole directory together because the skills share resources.

See [platform support](docs/platform-support.md) for tested and untested surfaces. Loading skills, connecting data, and marketplace approval are separate checks.

## Development and testing

Python 3.10+ is needed only for the optional offline quality helper and maintainer tools. No installation hooks, service, daemon, bundled data client, or background scheduler.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_package.py
claude plugin validate --strict .
python3 scripts/package_release.py --output /absolute/path/to/export-directory
```

The quality helper processes canonical, evidence-mapped records; it does not guess arbitrary source fields. Read the [record contract](skills/lead-engine/references/record-contract.md) before using it.

## Trust

[Privacy](PRIVACY.md), [terms](TERMS.md), [security](SECURITY.md), [support](SUPPORT.md), [inspiration and attribution](THIRD-PARTY-NOTICES.md).

This release is a local build. Public repository publication, marketplace submissions and vendor approval have their own release gates.
