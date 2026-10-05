# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, GitHub Copilot, and others) when working with code in
this repository. `CLAUDE.md` and `.github/copilot-instructions.md` point here so the guidance lives in one place.

## What this repository is

An experimental pilot of rules as code for Australia, built on [OpenFisca](https://openfisca.org), in the Python package
`openfisca_australia`. Expect the scope and structure to change. It was bootstrapped from the structure of the OpenFisca
country template and currently has the person and household entities and one generic variable (`age`, from `birth`). It contains no Australian legislation yet. Rules are added as
variables (`openfisca_australia/variables/`) and parameters (`openfisca_australia/parameters/`), with YAML tests in
`openfisca_australia/tests/`.

## Setup

Needs Python 3.9 to 3.11 (the range openfisca-core supports). `mise.toml` pins 3.11 and creates `.venv`.

```sh
make dev-setup   # installs the package with dev extras and the pre-commit git hook (skipped if already installed)
```

## Commands

- `make install` - editable install with dev extras
- `make test` - run the YAML tests with `openfisca test`
- `make serve-local` - run the web API on http://localhost:5000
- `pre-commit run --all-files` - ruff (lint and format) and yamllint

## CI

`.github/workflows/ci.yaml` runs on pushes to `main` and on pull requests. It tests on Python 3.9, 3.10 and 3.11, running
`make install`, `make test` and `pre-commit run --all-files`.

## Deployment

The package is intended to be published as a Python package. There is no release process yet: the version in
`pyproject.toml` is a placeholder (`0.0.1`) and nothing has been published.

## Gotchas

- openfisca-core does not support the newest Python versions. Use the 3.11 venv, not the system Python.
- The class `CountryTaxBenefitSystem` in `openfisca_australia/__init__.py` must keep that name; OpenFisca tooling looks it up.
- Never invent rules, rates or thresholds. Each variable and parameter needs a `reference` to a primary source (the Act,
  regulation or agency guidance). If a source can't be found, say so rather than guessing.
- Keep the model neutral: describe what the legislation says, with no commentary on it.
- `openfisca_australia/parameters/` only holds a `.gitkeep` for now.
- `docs/agents/triage-labels.md` is referenced below but doesn't exist yet.

## Agent skills

### Issue tracker

Use the github issues for this repo

### Triage labels

The default five-label vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`.
See `docs/agents/triage-labels.md`.

## Contributing

- Branch from `main` and open a pull request. CI must pass.
- Run `make dev-setup` so pre-commit checks run on each commit.
- Add a YAML test for every new or changed rule.
- Note AI involvement in commits and pull requests with a trailer such as `Assisted-by: Claude Code:<model>`.
