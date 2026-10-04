---
name: pipeline-handoff
description: Prepare a prospecting handoff, CRM field mapping, source-quality report, or measurable pipeline experiment. Use after lead qualification, for import files, or for comparing lead-source performance.
---

# Pipeline Handoff

Apply the [shared operating contract](../lead-engine/references/operating-contract.md) before acting.


Read [handoff playbook](references/playbook.md). Keep account, contact, branch and opportunity grains explicit. Produce a local import file and mapping for the user’s destination without writing to the CRM unless explicitly authorized and a suitable tool exists.

Include identity key, owner if supplied, stage, source/date, score rationale, public business contact status, suppression status, next action and unresolved facts. Never invent pipeline value or opportunities from raw leads. Preserve provenance in a supported notes/custom-field mapping rather than losing it in a minimal CSV.

Measure source yield with consistent denominators and attributed cost. Report overlapping accounts without double-counting them. Use cost per qualified account, evidence coverage, contactability, stale/invalid rows and manual research time. Replies/meetings/opportunities require actual observed user/tool data, not estimates.

Propose a small segment experiment with hypothesis, success criterion, budget, sample and review date. Scheduling, sending and CRM upload are separate actions; no background work is bundled. Deliver the file, mapping, quality report and next action.

Use [lead-reporting](../lead-reporting/SKILL.md) for a visual brief and [session-continuity](../session-continuity/SKILL.md) for a concise reusable handoff. [Feedback-learning](../feedback-learning/SKILL.md) separates explicit preference changes from outcome hypotheses. An actual recurring request can be handled through [scheduled-prospecting](../scheduled-prospecting/SKILL.md) using an available host scheduler and applicable authorization; a proposed review date alone is not an active schedule.
