Validation Issues and Fields to Fill

Overview
- I found that several markdown files are wrapped inside fenced code blocks which prevents normal rendering and active links. I can un-fence them automatically, but I want your confirmation before making wide edits across recipe files.

Per-file issues and fields for you to fill

1) AGENT_HANDOFF.MD
- Issue: None after un-fencing (already un-fenced).
- Fill: None.

2) RECIPE_CATALOG.md
- Issue: Wrapped in code fence (links inactive).
- Fill: Confirm that the category list and relative paths are correct. If you want different display text for links, list them here.

3) recipe_indexes/breakfast_index.md
- Issue: Wrapped in code fence (links/rendering inactive).
- Inconsistencies to fill:
  - Verify the macro accuracy for `BR001` (kcal/protein/carbs/fat).
  - Confirm serving weights (eggs, bacon) if you track cooked vs raw.
- Tag suggestions added: `#breakfast #protein #high-protein` (edit if different tags desired).

4) recipe_indexes/proteins_index.md
- Issue: Wrapped in code fence.
- Inconsistencies to fill:
  - `PR001` missing kcal value; macros show protein/fat but kcal missing.
  - Confirm whether macros should include kcal and carbs explicitly.
- Tag suggestions: `#protein #portion #meat`.

5) recipe_indexes/seafood_index.md
- Issue: Wrapped in code fence.
- Inconsistencies to fill:
  - Clarify the composition of `SF001` (it lists both salmon patty and shrimp — is this two proteins per serving or an either/or?).
  - Rice portion listed as ~½ cup cooked; confirm cooked/raw standard.
  - Macros include kcal but fat seems low relative to protein — please verify.
- Tag suggestions: `#seafood #bowl #high-protein`.

6) recipe_indexes/treats_index.md
- Issue: Wrapped in code fence and contains editorial notes ("Source: moved from yogurt index" and a question about canonical ID).
- Inconsistencies to fill:
  - Confirm canonical ID (`ST001`) and whether editorial notes should be moved to a changelog.
  - Verify per-ball macros and batch yield.
- Tag suggestions: `#treat #snack #protein-packed`.

7) recipe_indexes/yogurt_index.md
- Issue: Wrapped in code fence.
- Inconsistencies to fill:
  - `YG002`: macros show ranges and "carbs vary" — please provide concrete values or allowed range.
  - `YG003`: raspberry preserves weight per serving needs confirmation.
- Tag suggestions:
  - `YG001`: `#yogurt #post-gym #high-protein`
  - `YG002`: `#yogurt #dessert #treat`
  - `YG003`: `#yogurt #cheesecake #berry`

Global style inconsistencies for you to decide
- Recipe ID format: currently mixed but mostly `^[A-Z]{2}\d{3}$`. Confirm this as canonical.
- Macro line format: Some have `~kcal | X g protein | Y g carbs | Z g fat`; others omit kcal or show ranges. Decide whether to always include kcal and use exact vs range.
- Editorial notes: Move to `CHANGELOG.md` or keep inline? Recommend separate changelog.
- Tags: Decide required tag set (category, meal-time, protein-anchor, other). I added suggestions; tell me which to apply.

Next steps I can take after you confirm:
- Un-fence all markdown files so links render.
- Insert `Tags:` lines using the suggested tags and leave them editable.
- Create or update `CHANGELOG.md` with the editorial notes moved from recipe files.
- Normalize macro lines according to your chosen format.

If you want me to proceed and apply the un-fencing and tag insertions now, reply "Apply changes" and I'll proceed (I'll also commit the changes locally). If you'd like to review or change the suggested tags/fields first, tell me the edits you'd prefer.
