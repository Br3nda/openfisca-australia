install:
	pip install --editable ".[dev]"

test:
	openfisca test --country-package openfisca_australia openfisca_australia/tests

serve-local:
	openfisca serve --country-package openfisca_australia

dev-setup: .git/hooks/pre-commit

# Only runs when the git hook is missing, so repeat runs do nothing.
.git/hooks/pre-commit:
	$(MAKE) install
	pre-commit install
