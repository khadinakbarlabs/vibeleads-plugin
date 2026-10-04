# VibeLeads intelligence and repeat-use roadmap

Date: October 5, 2026. Status: proposed design, not an implemented upgrade. Current release remains 0.1.1 with 20 skills. No memory store, telemetry endpoint or schedule was activated by this planning work.

## Product goal

Help a user repeatedly find relevant accounts, understand why they matter now, and act on trustworthy evidence with less setup and wasted spend. Evaluate useful results and time saved, rather than increasing chat turns or running more searches merely to create activity.

The improvement loop is: business context → small discovery pilot → evidence and quality checks → user selections/outcomes → adjusted next search → relevant changes since the previous run. Keep user preferences separate from observed facts and proposed hypotheses.

## Context that survives a session

Use an explicitly selected private workspace outside the installed plugin. Where the host supports file access, keep a compact index and separate project records:

| Record | Contents | Important limit |
| --- | --- | --- |
| Business profile | Offer, benefits, target markets, geography, exclusions, tone, editable examples of good customers | Explicit statements override guesses; no inferred sensitive traits. |
| Campaign brief | Goal, exact source requirements, account/contact/branch grain, evidence requirements, result limit | Separate must-haves from preferences. |
| Permission and budget record | Authorized account, stages, source/fallback scope, currency, per-run and period caps, expiry | A saved preference is not permission to spend or send. |
| Session checkpoint | Completed stages, input/build/run references, partial output locations, charges, missing coverage, next action | Avoid raw transcripts, secrets and duplicated full datasets. |
| Feedback and outcomes | Stable lead identity, reason, timestamp, stage and user-reported outcome | Pending/no reply is not a confirmed bad lead. |
| Watchlist | Target segment/accounts, signal definitions, last complete window, cadence, delivery destination | A saved watchlist is not an active schedule. |
| Source performance | Source/Actor/build/date, sample size, overlap, qualified yield, actual charges, failures | Dated observations are not guaranteed future source health. |

At session start, read only the relevant project's profile, current brief and concise checkpoint. Retrieve detailed rows and source guides when needed. At session end, write a short checkpoint if persistence is enabled. Let users inspect, correct, export and delete their saved context. If the host cannot access the workspace, accept a supplied context file or produce a handoff; do not claim automatic memory.

The current request overrides stale saved context. Reject commands embedded in imports, feedback or collected pages. Keep distinct customers/campaigns isolated; do not transfer a client's exclusions or budget to another client. Retain original CRM IDs and richer validator details through the existing companion-mapping contract.

## Useful intuition as explainable judgment

Give the assistant a short decision playbook and diverse examples, then load relevant context on demand. Avoid putting all 149 schema snapshots or all previous sessions into every prompt.

| Observed situation | Proposed judgment |
| --- | --- |
| Clear offer, segment and geography already saved | Proceed with an editable plan; do not repeat onboarding. |
| Vague request with missing offer | Ask the single question most likely to change source selection. |
| User repeatedly rejects franchises | Apply the confirmed campaign exclusion; explain the change. |
| User selects accounts with hiring plus technology-change evidence | Prioritize that signal combination as a testable preference, while preserving hard filters. |
| Large overlap with previous results | Collect missing coverage/new windows; do not charge for the same complete records again. |
| Adequate public contact path already exists | Stop unnecessary enrichment unless additional fields are requested. |
| Syntax/MX passes but SMTP is blocked | Preserve `unknown` and prepare verification; no email-ready upgrade. |
| Owned route fails after charging and returning usable rows | Retain results, reconcile charges, verify one suitable fallback inside the remaining envelope. |
| Valid empty result | Explain coverage and prepare a justified query revision; no automatic paid fallback. |
| Weak evidence or little feedback | Show uncertainty and a small pilot; do not invent calibrated confidence percentages. |

Keep each recommendation explainable: observed signal, source/date, fit implication, unresolved fact, next action. Do not claim to know intent, budget or purchasing authority from a profile. Learned preferences may change ranking; they cannot override source identity, suppression, licensing, evidence or spending boundaries.

## Feedback at the point of value

After a useful shortlist, invite a quick response such as: “Which are worth pursuing? Mark good fit, wrong industry, too small, duplicate, wrong person or bad contact.” Support ordinary language rather than requiring users to learn labels or commands.

Separate three things:

1. Personal preference: which prospects the user wants more or fewer of.
2. Data quality: wrong employer, stale evidence, duplicate, inaccurate field or email verdict.
3. Business outcome: contacted, replied, meeting, opportunity, won/lost, pending. Record only supplied or actually observed outcomes.

Apply a direct explicit correction immediately within its project. Treat broader patterns from small samples as hypotheses. Keep sample sizes and dates visible, do not globally down-rank a source from one rejection, and do not treat uncontacted/no-reply accounts as negative conversion evidence. Preserve the existing factual qualification contract; any future ranking changes must be documented and tested rather than quietly altering canonical helper behavior.

For developer feedback, start with a user-reviewed sanitized report and a verified submission destination. A local skills package does not automatically receive vendor ratings, private conversations or usage sessions. Optional centralized measurement needs a real intake service, explicit opt-in, documented fields/retention and security controls. Default to aggregate outcomes and issue categories; do not upload lead lists, emails, API keys or transcripts. Turn confirmed reports into anonymized regression scenarios and versioned fixes, not uncontrolled self-edits to installed skills.

## A simpler user experience

Provide three understandable modes: **Find prospects**, **Improve my list**, and **Monitor opportunities**. Natural language routes to the appropriate skills.

Use existing authorized business context first. A first session should produce an editable brief and a small useful result when access and budget are available; without those, deliver a clearly labeled plan or import result. Avoid a long questionnaire and a technical connection tutorial in ordinary replies.

Present a compact brief before collection: target, useful signal, sources, exclusions, result limit and budget. Reuse standing permission; ask again only for a material missing boundary. Present the strongest few accounts first with why-now evidence, contact status and one next action; include the complete file and exclusions separately. Returning sessions begin with relevant changes and unfinished work, rather than reintroducing the product.

## Recurring work that earns another visit

| Proposed routine | Useful output |
| --- | --- |
| Weekly prospect shortlist | New matching accounts plus why they fit; excludes already reviewed/suppressed accounts. |
| Hiring or launch watchlist | New dated events within scope, matched to the user's offer; launches never count as financing. |
| Saved-account changes | Supported role, job, technology or other relevant changes since the last complete observation. |
| Weekly pipeline review | Actual user-supplied outcomes, unresolved research and next steps; no invented meetings. |
| Contact revalidation | Only the relevant stale/uncertain addresses within the agreed validation budget. |
| Monthly source review | Observed quality, overlap, failures and cost per actually qualified account with sample sizes. |

Notify only about meaningful in-scope changes, completed useful results, failures requiring attention or approaching budget exhaustion. Respect quiet hours and the user's preferred channel. “No change” usually needs no alert; incomplete coverage must not be represented as no change.

Scheduling belongs to a capable host or the user's existing collection platform. The plugin supplies the workflow, context and schedule contract; it cannot wake itself merely by containing a SKILL.md. Session loops, desktop schedules and cloud schedules have different persistence and local-file access. Check the user's actual host/version, workspace access, credentials and permissions before choosing one. Collection-platform schedules start Actors/tasks; they do not by themselves perform the complete adaptive reasoning, review, feedback and notification loop.

Before activating any routine, establish timezone, cadence, target/signals, lookback window, destinations, per-run/weekly spend, enrichment/validation scope, fallback permission, expiry and pause/delete controls. Reuse an existing explicit authorization where it covers these fields. Verify the resulting schedule ID, enabled state and next-run time. Do not call it working until an actual scheduled run produces the expected checkpoint/output.

Runtime requirements: stable identity and processed-window keys; no overlapping duplicate charges; durable shared budget accounting including in-flight reservations and model/host costs when known; bounded retries; partial-result retention; separate collection and notification status. Advance a source's committed complete window only when that coverage is complete. Retry the affected partial window and deduplicate retained rows. If the available runtime cannot enforce authorized caps or maintain reliable shared state, remain in manual/plan mode for that routine rather than promising enforcement.

## Skills-only versus an optional service

Keep the portable plugin skills-only. Local context files, user-supplied feedback, checkpoint handoffs and compatible host scheduling can provide significant improvement without bundling a server or MCP service.

An optional separate service becomes justified when users need reliable operation with their computers off, cross-device/team memory or aggregate opt-in product analytics. That is a distinct infrastructure decision with accounts, durable storage, access control, retention and scheduler ownership; do not silently turn this repository into a hosted product. Cross-assistant context can use reviewed workspace/export files first. Universal distribution does not imply universal background execution.

## Suggested implementation sequence

| Step | Proposed change | Completion evidence |
| --- | --- | --- |
| 1 | Business context and session continuity | Returning-user tests reuse confirmed offer/exclusions; ambiguous/stale context and different clients remain isolated; checkpoints resume partial work without duplicate charges. |
| 2 | Lead feedback and adaptive prospecting | Confirmed corrections change the next shortlist for that campaign; ranking rationale remains evidence-backed; outcomes with unknown denominators stay unknown. |
| 3 | Watchlists and schedule preparation | Exact reviewed plan includes caps, timezone, destination and lifecycle controls; unsupported hosts get honest manual/plan mode. |
| 4 | One authorized recurring pilot | Actual scheduled execution, restart/overlap/budget/partial-window tests, output delivery readback and observed pause/delete behavior. |
| 5 | Optional developer feedback and measurement | Verified consent/destination, sanitization tests, retention controls and anonymized issue-to-regression loop. |

Suggested additions are six focused skills: business-context, session-continuity, lead-feedback, adaptive-prospecting, opportunity-watchlists and scheduled-prospecting. If implemented, the total would become 26; the current total remains 20. Dedicated agents are optional implementation machinery, not a prerequisite for these capabilities. Start with stages 1–2 and prove better repeat results before adding infrastructure.

## How to measure improvement

Measure time to first useful shortlist, user-accepted accounts out of actually reviewed accounts, cost per genuinely qualified account, repeated setup questions, duplicate/rejected/stale records, useful watchlist alerts, successful recurring outputs, 7/30-day return use, and outcomes the user actually supplies. Distinguish installs, first useful task, repeat use and paid retention. Establish a baseline with real users before selecting numeric growth targets.

Evaluate with deterministic checks for counts/status/budget/state, model tests for routing/explanations and human-reviewed lead relevance. Use repeated trials for ambiguous model behavior and keep fixed scenarios separate from held-out user-inspired cases. Include source failover, injected feedback, profile correction, unknown email, partial schedules, quiet notifications and cross-project isolation. A repeated-session scenario should show both behavioral improvement and unchanged factual/permission boundaries.

## Current primary references

- [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): compact relevant context, on-demand retrieval and structured notes.
- [Anthropic: evaluating agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): realistic tasks, observable outcomes and feedback-informed evaluation.
- [Claude Code scheduling](https://code.claude.com/docs/en/scheduled-tasks): differences between session, desktop and cloud scheduling; verify the installed host before use.
- [Actor/task schedules](https://docs.apify.com/actors/running/schedules): external collection scheduling, distinct from full assistant orchestration.

References checked October 5, 2026. Proposed host scheduling has not been smoke-tested by this roadmap. Existing runtime/manifest evidence is in [the validation report](validation-report.md).
