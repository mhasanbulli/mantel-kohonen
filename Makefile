.PHONY: help install clean hooks check format pyright pre-commit
# Default target
help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: pre-commit ## Install the package with all dependencies
	uv sync --all-extras

clean: ## Clean up build artifacts and virtual environment
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	rm -rf .venv/

hooks: ## Run pre-commit git hooks on all files
	uv run pre-commit run --color=always --all-files --hook-stage pre-push

check: export SKIP=test ## Run format, lint and type check
check: hooks

format: export SKIP=test,pyright ## Run format and lint
format: hooks

pyright: ## Run type checking
	PYRIGHT_PYTHON_IGNORE_WARNINGS=1 uv run pyright

pre-commit: ## Install pre-push hooks
	uv run pre-commit install --install-hooks -t pre-push