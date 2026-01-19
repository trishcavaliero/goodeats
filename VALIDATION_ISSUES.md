Validation Issues and Fields to Fill

Overview
- Repository restructured on 2026-01-19: previous content archived to `archive/2026-01-19/`. New folder structure created under `recipe_indexes/` and `recipes/` with placeholders and recipe files migrated as individual recipe documents. This file now tracks leftover fields or missing data to complete the migration.

Remaining items to fill

- PR001 (Ground Beef Portion): Calories value missing — provide kcal per 5 oz cooked portion if available.
- SF001 (Salmon / Shrimp Bowl): Clarify whether both proteins are included per serving or if one is an option.
- YG002 (Biscoff): `Carbs:` currently set to `carbs vary` — provide carbs or range to standardize.

Next steps I can take:
- Run a validation check to list any recipe files missing `Macros per serving`, `Instructions`, or `Tags` and add placeholders for missing Instructions where sensible.
- Update tag usage across recipes to ensure format `macro/cut | meal/timing | ingredient/core | prep/storage` and 1–2 tags per type.
