#!/usr/bin/env bash

set -e
set -x

uv run ty check src
uv run ruff check src
uv run ruff format src --check