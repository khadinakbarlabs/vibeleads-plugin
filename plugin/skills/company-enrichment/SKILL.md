---
name: company-enrichment
description: Enrich B2B company and decision-maker records with source-backed business details and contact routes. Use for enrichment waterfalls, Apollo or ZoomInfo source requests, and completing account lists.
---

# Company Enrichment

Apply the [shared operating contract](../lead-engine/references/operating-contract.md) and read the [enrichment waterfall](../contact-enrichment/references/enrichment-waterfall.md).

1. Inspect the imported/discovered account or contact grain. Resolve the official company/domain and preserve external record IDs. Establish which missing fields matter: industry, size, geography, website/technology, relevant roles or public business contact paths. Unknown facts remain unknown.
2. Prefer the provided owned Actors whose actual contracts cover those fields. Company/domain/profile routes answer different questions; inspect live schemas before mapping inputs. A company-enrichment Actor is not necessarily a people finder or mailbox validator.
3. Use verified third-party Actors when owned coverage is unavailable, unsuitable or fails. Follow the failover guide and preserve the underlying requested data source. Apollo/ZoomInfo requests may use a demonstrably authorized vendor-backed Actor or a user export; a similarly named alternative must be attributed to its actual public/provider data.
4. Run the minimum useful waterfall within the shared budget. Apply suppression and deduplication before billable lookups. Retain existing strong facts; fill missing fields and flag conflicts instead of overwriting them silently. Reconcile partial/failed stages before failover.
5. Route address discovery to contact-enrichment and deliverability to email-validation. No company/profile/source-confidence score proves mailbox deliverability or purchasing authority.

Deliver enriched records plus field-level source/date/provider, original identity, unresolved fields, conflicts, contact status and actual stage charges when known. Report how many records were enhanced and which fallback was used. Do not manufacture headcount, revenue or job authority to fill a column.

For the optional quality helper, follow the [record contract](../lead-engine/references/record-contract.md): preserve original external IDs and richer enrichment details in a companion mapping or custom export before normalization. The helper drops unsupported fields; include the mapping in the final handoff.
