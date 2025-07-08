#!/usr/bin/env bash

set -e
set -x

uv run coverage run --source=app -m pytest
uv run coverage report --show-missing
uv run coverage html --title "${@-coverage}"