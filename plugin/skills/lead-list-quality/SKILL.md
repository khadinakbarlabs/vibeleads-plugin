---
name: lead-list-quality
description: Clean, suppress, deduplicate, score, and export an evidence-backed company or business-contact list. Use for CSV hygiene, prioritization, unknown deliverability, or CRM-ready files.
---

# Lead List Quality

Apply the [shared operating contract](../lead-engine/references/operating-contract.md) before acting.


Read [record contract](../lead-engine/references/record-contract.md) and prospecting framework. Agree account/contact/branch grain from the request. Inspect actual file structure and deliberately map source fields. Do not assume every source’s `url` is the company website or every email is deliverable.

Normalize domains and exact emails, preserve distinct contacts/branches, apply suppression/disqualifiers, resolve conflicts and check evidence/date coverage. Missing domain/address remains in manual review. Do not deduplicate unrelated businesses by similar names. Do not mix summary/error records into leads.

Use the optional offline helper with canonical records:

```sh
python3 <skill-directory>/scripts/lead_quality.py input.json --grain contact --suppression suppression.json --output report.json --csv leads.csv
```

Inspect help first. Omitting `--csv` writes only JSON; `--sendable-only` restricts CSV to validator-backed valid emails. Python is optional: if unavailable, perform the same checks manually and write equivalent outputs with the host’s tools. The helper makes no network calls and does not verify addresses.

Preserve required external IDs and provider-specific enrichment/validation detail in a companion mapping before the helper drops unsupported fields. Join by reviewed stable identity after deduplication, never row position; include that mapping in enrichment/CRM handoffs.

Review notes/evidence for irrelevant private data before exporting. Escape formula-leading cells in CSV. Report qualified/review/excluded counts, duplicates, suppressed rows, email-quality distribution, scoring rationale and missing fields. Preserve original source files.
