RECIPE_SCHEMA — goodeats

Purpose
- Define required fields, macro format, ID rules, tags, and Cut Tier.

Required fields for each recipe
- ID: Two-letter category code + 3 digits, e.g., `BR001`, `YG001`. Regex: `^[A-Z]{2}\d{3}$`.
- Name: Human-readable recipe name.
- Ingredients: Bulleted list of ingredients and quantities.
- Macros: Per serving, formatted exactly as: `Protein: XX g | Carbs: XX g | Fat: XX g | Calories: XXX kcal`.
  - If a value is unknown, leave that portion blank (e.g., `Calories:`).
  - Ranges are allowed (e.g., `40–45 g` or `325–350 kcal`) when exact values are not available.
- Instructions: Preparation or usage notes. Leave blank if unknown.

Optional fields
- Tags: Optional space-separated hashtags. Suggested list: `#high-protein`, `#cut-staple`, `#treat`, `#quick`, `#meal-prep`.
- Cut Tier: Optional value of `Staple`, `Flexible`, or `Treat`. Default: `Flexible` if not specified.

Category rules
- Each recipe must belong to one primary category only (the file under `recipe_indexes/` where it appears).
- Use canonical IDs and avoid duplicates. If moving a recipe between categories, update references and the catalog.

Style rules
- Keep Markdown headings for recipes as: `### ID — Name`.
- Keep `Ingredients:` as a bulleted list under the recipe heading.
- Keep `Macros:` on its own line after `Ingredients` and before `Instructions`.
- Use `Tags:` and `Cut Tier:` lines after `Instructions`.

Examples

### BR001 — Omelet + Bacon + Avocado + Pineapple

Ingredients:
- 3 large eggs (~150 g)
- 1 slice thick-cut bacon (~42 g raw)
- ¼ medium avocado (~50 g)
- Pineapple (~90 g)

Macros: Protein: 30 g | Carbs: 17 g | Fat: 37 g | Calories: 514 kcal

Instructions:

Tags: #breakfast #protein #high-protein

Cut Tier: Flexible
