# A useful prospecting report

Keep the visual story compact: business goal → strongest accounts/reasons → coverage/uncertainty → next action. Use plain labels, visible sources/dates, accessible contrast, responsive cards, keyboard-operable filters, and a printable view. Empty/partial states are first-class results, not embarrassing gaps to fill with synthetic leads.

## Canonical inputs and summary

Rows follow the [record contract](../../lead-engine/references/record-contract.md). The report helper uses the same qualification/suppression/deduplication implementation as lead-list-quality. It cannot import arbitrary CRM columns automatically, verify mailboxes, fetch data, manage a monitor budget or preserve rich provider fields without the companion mapping.

The optional [summary example](summary-template.json) accepts only `title`, `period`, `coverage_state`, `next_actions`, `learning_note`, and `budget`. Coverage must be an actual observed state, not inferred from row count. Omit budget when actual charges/cap/reservations are unknown; unknown is not free. When supplied, budget has `total`, `spent` (actual), `reserved` (unresolved/in-flight), and three-letter `currency`. Remaining is total minus spent and reserved; overspend is surfaced, not erased. Summary text is displayed as supplied, not fact-checked by the helper; review all claims/actions first.

Source metadata, Actor runtime and list completeness are separate. HTML evidence links remain public-source links; the standalone renderer makes no automatic network requests. User clicks may open those sites. JSON can contain business contacts/provenance. Cards display grain-appropriate identity: contact name/role and business email where needed, or branch address. Account-grain cards omit direct email fields, but evidence/notes may still contain user data. Share a sanitized version only if requested.

## Metrics that matter

- Qualified/review/excluded counts at the declared account/contact/branch grain.
- Retained records actually containing an email; deliverability states only for those records. Duplicate/excluded input rows are not unique contact denominators.
- Email-ready = qualified records with exact-address validator-backed valid status; no send authorization implied.
- Actual charge per qualified record, only when actual charge and nonzero matching-grain denominator are available. Never label contacts as qualified accounts.
- Session comparison by stable entity identity, including observed nonduplicate exclusions. `changed` covers canonical field/status/qualification and evidence-content differences; observation-timestamp-only updates do not count as material changes. `newly_excluded` distinguishes disqualified/suppressed observed records from genuinely not-observed identities. Unresolved identities remain unmatched. Supply `--previous-suppression` for the historical policy when known; the current policy is not retroactively applied to the prior snapshot. This is not a complete field history or opt-out audit.
- Evidence-domain coverage, clearly distinct from verified Actor/publisher performance. Multiple pages from one provider are not independent corroboration.

The HTML prints/saves PDF through the browser; no automatic PDF export is claimed. Markdown is the accessible/shareable companion. Do not publish a customer report in the plugin release, count a demonstration as live data, or claim conversion improvement without observed comparable outcomes.

## Feedback in the visual report

Each card offers deliberate reason-coded feedback. Selections are page-local, with no localStorage, tracking or background submission. The user can download a JSON feedback file containing opaque `record_ref` values, selected reasons and dates; it does not include full contact rows. The private report JSON contains matching record references. Ask the assistant to apply the downloaded file in the chosen business scope; the file itself cannot authorize changes in spend, sources, suppression, recipients or schedules. Identical record/reason selections are deduplicated; conflicting reasons need review. Opaque IDs are references, not a security or anonymity guarantee. A report reload does not remember unexported selections.
