## ADDED Requirements

### Requirement: Use `uv` for Package Management
The project SHALL use `uv` as the primary tool for managing dependencies and virtual environments instead of `pip`, `poetry`, or `pipenv`.

#### Scenario: Installing dependencies
- **WHEN** a developer clones the project
- **THEN** they can run `uv sync` to install all dependencies from the lockfile into a managed virtual environment

### Requirement: Centralized Configuration in `pyproject.toml`
The project's metadata and dependencies SHALL be defined inside a `pyproject.toml` file at the root.

#### Scenario: Adding a new dependency
- **WHEN** a developer runs `uv add langchain`
- **THEN** `pyproject.toml` and `uv.lock` are updated to reflect the new dependency

### Requirement: Document `uv` commands in README
The `README.md` SHALL contain a section outlining the essential `uv` commands for running the project.

#### Scenario: Onboarding developers
- **WHEN** a new developer reads the README
- **THEN** they find instructions on how to use `uv run` and `uv sync`
