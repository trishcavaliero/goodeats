#!/usr/bin/env python3
"""Validate recipe files for required fields and formatting.
Exits with non-zero when issues are found.
Writes a 'validation-report.txt' file at repo root summarizing issues.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPE_DIR = ROOT / "recipes"
TAGS_FILE = ROOT / "TAGS.md"
REPORT = ROOT / "validation-report.txt"

# Helpers
macro_re = re.compile(r"Protein:\s*[^|]+\|\s*Carbs:\s*[^|]+\|\s*Fat:\s*[^|]+\|\s*Calories:\s*[^\n]+", re.I)
placeholder_re = re.compile(r"\[ADD")


def load_allowed_tags():
    if not TAGS_FILE.exists():
        return set()
    tags = set()
    section = None
    def norm(s):
        return s.lower().replace('-', ' ').replace('_', ' ').strip()
    for line in TAGS_FILE.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            section = line
            continue
        if line.startswith("-"):
            entry = line[1:].strip()
            # split on commas and bars
            parts = re.split(r"[,|]", entry)
            for p in parts:
                t = p.strip()
                if not t:
                    continue
                # handle 'cut-tier: staple | flexible | treat'
                if t.startswith("cut-tier:"):
                    opts = t.split(":", 1)[1]
                    for o in opts.split("|"):
                        tags.add(norm(o))
                else:
                    tags.add(norm(t))
    return tags


allowed_tags = load_allowed_tags()

issues = []
files_checked = 0

for p in RECIPE_DIR.rglob("*.md"):
    files_checked += 1
    text = p.read_text()
    lines = text.splitlines()
    name = p.relative_to(ROOT)

    # Check Category
    if not re.search(r"^Category:\s*", text, re.I | re.M):
        issues.append((str(name), "Missing 'Category:' line"))

    # Check Tags
    m = re.search(r"^Tags:\s*(.+)$", text, re.I | re.M)
    if not m:
        issues.append((str(name), "Missing 'Tags:' line"))
    else:
        tags_line = m.group(1).strip()
        # Expect groups separated by '|'
        groups = [g.strip() for g in tags_line.split("|")]
        for i, g in enumerate(groups, start=1):
            if not g:
                issues.append((str(name), f"Empty tag group #{i}"))
                continue
            # split tags by comma
            tags = [t.strip() for t in re.split(r"[,\s]+", g) if t.strip()]
            if len(tags) > 2:
                issues.append((str(name), f"Tag group #{i} has >2 tags (found {len(tags)}): {tags}"))
            # check against allowed tags where possible (normalize dashes/underscores)
            for t in tags:
                base = t.lower().replace("-", " ").replace("_", " ")
                # if allowed tags list not empty, do a loose match
                if allowed_tags and not any(base == a or base in a or a in base for a in allowed_tags):
                    issues.append((str(name), f"Tag '{t}' in group #{i} not recognized"))

    # Check Ingredients
    if not re.search(r"^Ingredients:\s*", text, re.I | re.M):
        issues.append((str(name), "Missing 'Ingredients:' section"))

    # Check Macros
    if not macro_re.search(text):
        issues.append((str(name), "Missing or malformed 'Macros per serving' line"))
    else:
        mac = macro_re.search(text).group(0)
        if placeholder_re.search(mac):
            issues.append((str(name), "Macros contain placeholder values"))

    # Check Instructions
    if not re.search(r"^Instructions:\s*", text, re.I | re.M):
        issues.append((str(name), "Missing 'Instructions:' section"))
    else:
        # ensure at least one instruction step or line after header
        parts = re.split(r"^Instructions:\s*$", text, flags=re.I | re.M)
        if len(parts) > 1:
            after = parts[1].strip()
            if not after or after.splitlines()[0].strip() == "":
                issues.append((str(name), "'Instructions:' section appears empty"))

    # Placeholder checks
    if placeholder_re.search(text):
        issues.append((str(name), "Contains placeholder token '[ADD'"))

# Write report
with REPORT.open("w") as fh:
    fh.write(f"Recipe validation report\nFiles checked: {files_checked}\n\n")
    if not issues:
        fh.write("No issues found.\n")
        print("No issues found.")
        exit(0)
    fh.write("Issues found:\n")
    for f, msg in issues:
        fh.write(f"- {f}: {msg}\n")
    print(f"Validation completed: {len(issues)} issues found. See {REPORT}")
    exit(1)
