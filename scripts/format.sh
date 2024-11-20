#!/bin/sh -e
set -x

ruff check src --fix
ruff format src
