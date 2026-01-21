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

# Fixer helpers
import argparse

def normalize_tag(t: str) -> str:
    return t.lower().strip()

def parse_tags_line(line: str):
    # returns list of groups, each group is list of tags
    groups = [g.strip() for g in line.split('|')]
    result = []
    for g in groups:
        if not g:
            result.append([])
            continue
        tags = [normalize_tag(t) for t in re.split(r"[,\s]+", g) if t.strip()]
        result.append(tags)
    return result

def format_tags_line(groups):
    # enforce up to 2 tags per group
    parts = []
    for tags in groups:
        if not tags:
            parts.append("")
            continue
        parts.append(', '.join(tags[:2]))
    return ' | '.join(parts)


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

# If fixer mode enabled, attempt auto-fix of tags line
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate recipes. Use --fix to auto-fix simple tag formatting and write files.')
    parser.add_argument('--fix', action='store_true', help='Automatically fix simple formatting issues (Tags line formatting)')
    parser.add_argument('--create-pr', action='store_true', help='After --fix, create a branch with fixes and open a PR (requires gh CLI)')
    args = parser.parse_args()

    if args.fix:
        fixed_files = []
        for p in RECIPE_DIR.rglob("*.md"):
            text = p.read_text()
            m = re.search(r"^Tags:\s*(.+)$", text, re.I | re.M)
            if not m:
                continue
            tags_line = m.group(1).strip()
            groups = parse_tags_line(tags_line)
            new_line = format_tags_line(groups)
            if new_line != tags_line:
                new_text = re.sub(r"^Tags:\s*.+$", f"Tags: {new_line}", text, flags=re.I | re.M)
                p.write_text(new_text)
                fixed_files.append(str(p.relative_to(ROOT)))
        if fixed_files:
            print(f"Auto-fixed Tags in {len(fixed_files)} files:")
            for f in fixed_files:
                print(f" - {f}")
            # create git branch and commit changes
            import subprocess, datetime
            branch = f"fix/format-tags-{datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
            subprocess.check_call(["git", "checkout", "-b", branch])
            subprocess.check_call(["git", "add"] + fixed_files)
            subprocess.check_call(["git", "commit", "-m", "chore: auto-format Tags fields across recipes"]) 
            subprocess.check_call(["git", "push", "-u", "origin", branch])
            print(f"Pushed branch {branch} with fixes.")
            if args.create_pr:
                # try to create PR using gh if available
                try:
                    subprocess.check_call(["gh", "pr", "create", "--fill"])
                    print("Created PR via gh CLI.")
                except Exception:
                    print("Could not create PR via gh CLI; please open a PR for the branch manually if desired.")
        else:
            print("No automatic fixes necessary.")

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
