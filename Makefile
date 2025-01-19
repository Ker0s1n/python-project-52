install:
	uv sync --all-packages
dev:
	uv run python manage.py runserver
build:
	./build.sh
test:
	uv run python manage.py test
lint:
	uv run python ruff check
lint-fix:
	uv python ruff check --fix
start:
	uv run gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker