A monorepo template for a Python project using uv.

This project includes:

- [core](./src/core): The core package for the project.
- [api](./src/api): An API server built with FastAPI.


## Why you might consider using this template:
While there are some great monorepo templates out there, there are no major ones that are specifically designed for general-purpose use. This template is designed to be an easy-to-use, general-purpose monorepo and is compatible with IDEs like VSCode.

# Development

Navigate to the target package and refer to the README.md for more information.  
Generally, you should run `uv sync --all-packages` first to create a virtual environment and install the dependencies.

To check linting errors or format the code, run `./scripts/lint.sh` and `./scripts/format.sh`.

# Testing

Run `./scripts/test.sh` to run the tests.
