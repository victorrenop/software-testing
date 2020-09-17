## Requirements

.PHONY: requirements-test
requirements-test:
	@python3PATH=. python3 -m pip install -r requirements.test.txt

.PHONY: requirements-lint
requirements-lint:
	@python3PATH=. python3 -m pip install -r requirements.lint.txt

.PHONY: minimum-requirements
minimum-requirements:
	@python3PATH=. python3 -m pip install -U -r requirements.txt

.PHONY: requirements
## install all requirements
requirements: requirements-test requirements-lint minimum-requirements

## Style Checks

.PHONY: style-check
style-check:
	@echo ""
	@echo "Code Style"
	@echo "=========="
	@echo ""
	@python3 -m black --check -t py36 --exclude="build/|buck-out/|dist/|_build/|pip/|\.pip/|\.git/|\.hg/|\.mypy_cache/|\.tox/|\.venv/" . && echo "\n\nSuccess" || echo "\n\nFailure\n\nRun \"make black\" to apply style formatting to your code"
	@echo ""

.PHONY: check-flake8
check-flake8:
	@echo ""
	@echo "Flake 8"
	@echo "======="
	@echo ""
	@-python3 -m flake8 assignments/ && echo "assignments module success"
	@-python3 -m flake8 tests/ && echo "tests module success"
	@echo ""

.PHONY: checks
checks:
	@echo ""
	@echo "Code Style & Flake 8"
	@echo "--------------------"
	@echo ""
	@make style-check
	@make check-flake8
	@echo ""

.PHONY: black
black:
	@python3 -m black -t py36 --exclude="build/|buck-out/|dist/|_build/|pip/|\.pip/|\.git/|\.hg/|\.mypy_cache/|\.tox/|\.venv/" .

## Tests

.PHONY: tests
tests:
	@python3 -m coverage run --source=$(ARGS) --branch -m pytest $(ARGS)

.PHONY: report
report:
	@make tests
	@python3 -m coverage report

.PHONY: report-html
report-html:
	@make tests
	@python3 -m coverage html
