---
name: business-context
description: Understand the user's business, offer, buyers and constraints from available context, then create or refresh a reusable prospecting brief. Use for onboarding, personalization, a changed offer or avoiding repeated questions.
---

# Business Context

Apply the [shared contract](../lead-engine/references/operating-contract.md) and [context protocol](references/context-protocol.md).

Start from the current conversation, the user's selected workspace brief and supplied business website/documents. Research available public business information through permitted host tools before asking the user to describe what is already visible. The host's model performs synthesis; this plugin does not require another model API key. Public website positioning is evidence of the published offer, not proof of customer outcomes.

Build a short brief: what they sell, to whom, geography, likely value, observable buying/problem signals, exclusions, preferred lead grain, output style and success criterion. Separate user-confirmed facts, public observations, working hypotheses and unresolved questions. Prefer the latest explicit human correction over an older saved brief; check that the profile belongs to this business before reuse. Do not mix two clients' contexts.

Ask at most one grouped material question when the missing offer/market blocks useful work. Otherwise propose an editable brief and move into planning. Do not interrogate the user about every field or require them to invent keywords/source choices. Private priorities and spend belong to the user; research cannot infer authorization.

When saving is requested or an established workspace is already chosen, update its readable context files with version/date and a small change note. Otherwise offer the brief inline and resolve the storage destination only if persistence is needed. Keep facts, feedback and action permissions separate. Never save secrets, raw transcripts or an API key; credentials belong in secure host configuration.

Deliver the brief, important uncertainty and the next useful search. Use [adaptive-prospecting](../adaptive-prospecting/SKILL.md) to choose that search and [session-continuity](../session-continuity/SKILL.md) for the next session.
