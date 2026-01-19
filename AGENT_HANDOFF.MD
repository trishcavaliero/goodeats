# Agent Handoff — Nutrition Tracking & Documentation System

## Purpose
This document defines the **required structure and rules** for nutrition tracking during a fat-loss (cut) phase. Any agent continuing work on this project must follow this structure to ensure consistency, low cognitive load, and long-term reusability of data.

The system prioritizes:
- protein-first tracking
- minimal daily friction
- reusable recipes
- clear historical reference

---

## Core Principle (Non‑Negotiable)

> **Foods/recipes are defined once, indexed, and reused. Daily logs reference the index.**

Do **NOT** recreate ingredient lists or macros inside daily logs.
Do **NOT** organize primarily by day-made or chronological cooking order.

---

## Canonical Structure

### 1. Recipe / Food Index (Static)

**Purpose:** Single source of truth for all repeat foods.

Each entry MUST include:
- Name
- Ingredients with measurements
- Macros per serving (subtitle-style)
- Notes (optional: tags, flexibility, protein anchor)

Format example:
# Agent Handoff — Nutrition Tracking & Documentation System

## Purpose
This document defines the **required structure and rules** for nutrition tracking during a fat-loss (cut) phase. Any agent continuing work on this project must follow this structure to ensure consistency, low cognitive load, and long-term reusability of data.

The system prioritizes:
- protein-first tracking
- minimal daily friction
- reusable recipes
- clear historical reference

---

## Core Principle (Non‑Negotiable)

> **Foods/recipes are defined once, indexed, and reused. Daily logs reference the index.**

Do **NOT** recreate ingredient lists or macros inside daily logs.
Do **NOT** organize primarily by day-made or chronological cooking order.

---

## Canonical Structure

### 1. Recipe / Food Index (Static)

**Purpose:** Single source of truth for all repeat foods.

Each entry MUST include:
- Name
- Ingredients with measurements
- Macros per serving (subtitle-style)
- Notes (optional: tags, flexibility, protein anchor)

Format example:
```md
### Berry Protein Yogurt Bowl
*~325 kcal | 50 g protein | 21 g carbs | 5 g fat*
- 8 oz Greek yogurt
- 1 scoop protein powder
- 95 g frozen berries
Tags: #post-gym #office-friendly #high-protein
```

Rules:
- Recipes are reusable across weeks and future cuts
- Variations are either:
  - separate indexed recipes, or
  - noted as optional swaps

---

### 2. Daily Log (Dynamic)

**Purpose:** Track intake quickly without duplication.

Daily logs MUST:
- Reference foods by name or ID from the index
- Track quantity/servings only
- Avoid re-listing ingredients or macros

Format example:
```md
## 2026-01-20

Breakfast:
- Omelet + Bacon + Avocado + Pineapple (1 serving)

Post-gym:
- Berry Protein Yogurt Bowl (1 serving)

Lunch:
- Ground Beef Portion (5 oz cooked) + free veg

Snack:
- Peanut Butter Ball x1
```

Rules:
- Non-starchy vegetables may be logged as "free veg"
- Protein portions must be explicit
- Carb portions must be explicit when relevant

---

## Tracking Rules

### Always Track
- Protein sources (meat, eggs, yogurt, protein powder)
- Primary carb sources (rice, potatoes, fruit, sweet potatoes)

### Optional / Free Tracking
- Non-starchy vegetables (lettuce, carrots, onions, green beans)
- Herbs, spices, zero-cal flavorings

### Measurement Standards
- Proteins: cooked weight preferred unless noted
- Carbs: cooked or raw, but must be consistent per recipe
- Fats: measured when added intentionally (oil, butter, nut butters)

---

## Portioning Philosophy

- Proteins are pre-portioned to enforce consistency
- Portions are interchangeable unless explicitly labeled otherwise
- No meal is locked to a time of day

Example:
- Ground beef portions are **not** labeled lunch/dinner
- Any portion may be used when protein is needed

---

## Variability Without Chaos

Allowed variability includes:
- flavor swaps (sauces, spices)
- vegetable swaps
- carb swaps within the same macro category

Not allowed:
- unindexed “one-off” meals without documentation
- silent macro changes without updating the index

---

## Long-Term Intent

This system must support:
- future cut phases
- comparison across weeks
- fast re-entry after breaks
- minimal decision fatigue

If a decision conflicts with **simplicity + reuse**, it is incorrect.

---

## Agent Instructions

Any agent continuing this work must:
1. Add new foods to the Recipe Index first
2. Reference foods from the index in daily logs
3. Keep daily logs short and scannable
4. Preserve protein-first logic
5. Avoid restructuring unless explicitly requested
6. Classify sweet recipes by ingredient: if a recipe contains Greek yogurt, keep it in the Greek Yogurt / Dessert index; otherwise place sweet/ dessert items in the Sweet Treats index. Always prefer a single canonical entry per recipe and reference its ID from logs and other indexes.

Failure to follow this structure degrades tracking quality and user adherence.

---

## Status
This document is **authoritative** for nutrition tracking in this repository.
