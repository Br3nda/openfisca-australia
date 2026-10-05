# openfisca-australia

An [OpenFisca](https://openfisca.org) rules-as-code model for Australia.

This is a bootstrapped skeleton built from the structure of the
[OpenFisca country template](https://github.com/openfisca/country-template).
It defines the entities (person, household) and a single generic variable
(`age`, computed from `birth`). It contains no Australian legislation yet.

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

## Licence

AGPL-3.0-or-later, as for the OpenFisca country template.
