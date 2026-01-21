validate:
	python3 scripts/validate_recipes.py

fix-tags:
	python3 scripts/validate_recipes.py --fix

.PHONY: validate fix-tags
