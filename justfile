default:
  @just --choose

dev:
  uv run fastapi dev src/app/interface/api/main.py

type-check:
  uvx ty check .

format:
  uvx ruff check --fix .
  uvx ruff format .

pre-commit: format type-check
