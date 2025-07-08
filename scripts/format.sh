#!/bin/sh -e
set -x

uv run ruff check src --fix
uv run ruff format src
