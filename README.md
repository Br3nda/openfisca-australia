# openfisca-australia

An experimental pilot of rules as code for Australia, built on [OpenFisca](https://openfisca.org).

This is a bootstrapped skeleton built from the structure of the
[OpenFisca country template](https://github.com/openfisca/country-template).
It defines the entities (person, household) and a single generic variable
(`age`, computed from `birth`). It contains no Australian legislation yet.

**Status: experimental.** This is a pilot. The scope, structure and results can change
without notice, and nothing here should be relied on as an authoritative statement of
the law or of anyone's entitlements.

## Setup

Requires Python 3.9 to 3.11 (the range supported by openfisca-core).

```sh
python -m venv .venv
. .venv/bin/activate
make install
make test
make serve-local   # web API at http://localhost:5000
```

## Layout

- `openfisca_australia/entities.py` - person and household entities
- `openfisca_australia/variables/` - variables (one module per topic)
- `openfisca_australia/parameters/` - legislation parameters (YAML, with a source reference for each)
- `openfisca_australia/tests/` - YAML tests

## Adding rules

Each parameter and variable should cite the primary source (the Act, regulation
or agency guidance) in its `reference` field.

## Working with AI agents

Guidance for AI coding agents (setup, commands, CI and conventions) is in
[AGENTS.md](AGENTS.md). Human contributors will find it a useful summary too.

## Licence

AGPL-3.0-or-later, as for the OpenFisca country template.
