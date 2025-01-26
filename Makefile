install:
	uv sync
package-install:
	uv tool install dist/*.whl --reinstall
test:
	uv run pytest
build:
	uv build
lint:
	uv run ruff check gendiff
