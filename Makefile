install:
	uv sync --all-packages
build:
	uvx --from build pyproject-build --installer uv
test:
	uv python manage.py test
lint:
	uv python ruff check
lint-fix:
	uv python ruff check --fix