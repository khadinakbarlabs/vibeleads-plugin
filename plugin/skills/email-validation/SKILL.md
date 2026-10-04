---
name: email-validation
description: Validate business email lists with the provided validator Actors or a verified fallback, preserving syntax, MX, mailbox, catch-all, risky and unknown outcomes. Use before email-ready export or to check contact-list quality.
---

# Email Validation

Apply the [shared operating contract](../lead-engine/references/operating-contract.md), read the [enrichment waterfall](../contact-enrichment/references/enrichment-waterfall.md) and preserve the [record contract](../lead-engine/references/record-contract.md).

1. Start with relevant business addresses and provenance. Normalize exact email strings, deduplicate and apply suppression before paid validation. Discovery or a pattern guess is not a validation result.
2. Prefer the provided email-address-validator, NeverBounce alternative or ZeroBounce alternative route whose current tier actually supports the desired verification. Inspect required `emails`, supported batch limits and optional tier/SMTP fields. Independent alternatives are not the branded vendor service. Additional setup and premium validation charges must fit the authorized envelope.
3. Distinguish basic syntax/DNS/disposable/role checks from a configured mailbox-verification provider. The basic email-address-validator and standard alternative tiers do not inherently prove mailbox deliverability. An attempted cloud SMTP probe can be blocked/unknown. Premium tiers need an actual observed provider verdict; selecting premium or completing a run is not itself a valid verdict.
4. On unavailable/failed owned validation, verify a suitable other-publisher Actor through the failover guide. Preserve unprocessed addresses and charged usage, validate only missing coverage, and retain actual provider/tier/date/outcome. Do not upgrade uncertain results merely because the fallback succeeded as a job.
5. Map valid/invalid/risky/catch_all/unknown/not_checked from actual observed semantics. Save validator evidence matched to the exact address for `valid`; it remains a point-in-time check, not a guarantee of delivery, ownership, employment or consent. Unknown/catch-all/risky addresses remain outside the email-ready export. Report stale results and suggest revalidation only within authorization.

Deliver per-address status and reason, check type/tier/provider, checked time and run/evidence reference; summary counts, unprocessed items, cost/remaining budget, and a separately filtered email-ready file when requested. No messages are sent and no mailbox probe is represented as an outreach email.

Keep richer verification details in the companion mapping described in the record contract when using the quality helper. Its canonical evidence supports classification but does not retain arbitrary provider/tier/reason/run fields. Do not omit these details from the final validation handoff.

Blocked SMTP without another actual verdict is `unknown`; do not relabel it catch-all/risky. Do not recommend sending unverified addresses for warmup or manual tests as a validation workaround. Use only actual email counts; company-row counts are not email denominators. Preserve missing provider/tier as unknown rather than inventing them from check names.
