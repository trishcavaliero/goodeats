Validation Issues and Fields to Fill

Overview
- Repository restructured on 2026-01-19: previous content archived to `archive/2026-01-19/`. New folder structure created under `recipe_indexes/` and `recipes/` with placeholders and recipe files migrated as individual recipe documents. This file now tracks leftover fields or missing data to complete the migration.

Remaining items to fill

- PR001 (Ground Beef Portion): **Resolved** — values updated from user input: 5 oz cooked ≈ 360 kcal; Protein ≈ 34 g; Fat ≈ 24 g; Carbs ≈ 0 g.
- SF001 (Salmon / Shrimp Bowl): **Resolved** — Protein updated to 43 g and notes updated to indicate both salmon and shrimp are included per serving.
- YG002 (Biscoff): **Resolved** — `Carbs` set to 16 g based on provided cookie nutrition (2 cookies ≈ 16 g carbs, 3 g fat, 2 g protein, 160 kcal).

Validation summary:
- All recipe files include `Category`, `Tags`, `Ingredients`, `Macros per serving` and `Instructions` fields now.
- Placeholders were added where numeric values were missing (see above).

Next steps I can take:
- If you provide missing numeric values, I will update recipes and remove placeholders.
- I can run an enforcement check for tag group formatting and limit tags per category if you'd like.
