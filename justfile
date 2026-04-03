default:
  @just --choose

dev:
  uv run fastapi dev src/app/interface/api/main.py
