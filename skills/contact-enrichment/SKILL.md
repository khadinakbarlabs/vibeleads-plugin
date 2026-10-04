---
name: contact-enrichment
description: Enrich qualified companies with public business contacts and honest email-quality states. Use for finding company contact routes, mapping professional roles, or validating an existing business email list.
---

# Contact Enrichment

Apply the [shared operating contract](../lead-engine/references/operating-contract.md) before acting.


Read [enrichment waterfall](references/enrichment-waterfall.md), then [contact playbook](references/playbook.md) and [record contract](../lead-engine/references/record-contract.md). Begin with resolved official domains/companies, not an unfiltered mass list. Use the least intrusive public business route: contact page, role address or professional business contact with provenance.

Keep candidate address, discovery URL/date and deliverability state separate. A pattern guess is not a found email. Syntax-only validation cannot produce `valid`. Catch-all, risky, unknown and not_checked stay distinct. Validator services may require extra credentials and paid stages; default them off unless the user’s envelope includes them. Never share secrets just because an input schema allows a key.

Only enrich within authorized counts and remaining budget. Account/person match must be supported; a title match alone is insufficient. Apply suppression before extra lookups. Invalid emails stay excluded from email-ready exports; research accounts may remain useful.

Deliver public business routes, role mapping, validation provider/date/outcome where actually checked, missing data and any additional setup needed. Preserve separate contacts at the same company.

Use [company-enrichment](../company-enrichment/SKILL.md) for missing account fields and [email-validation](../email-validation/SKILL.md) for separate deliverability checks. Basic email-address-validator/MX results remain unknown until an actual mailbox verifier supplies a verdict.
