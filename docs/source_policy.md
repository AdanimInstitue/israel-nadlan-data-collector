# Source Policy

This repository includes only sources the public project is willing to name and process publicly.

Each registered source declares:

- stable `source_id`
- display name
- public homepage
- terms or license pointer where available
- access method
- source class
- attribution requirement flag
- conservative redistribution note

## Current Admission Rules

A source belongs in this repository only if all of the following are true:

1. It can be named publicly.
2. The collector can describe its role in public documentation.
3. Attribution handling is documented.
4. The repository is comfortable treating its use as public-safe.

## Current Sources

- `nadlan_gov_il`
- `cbs_table49`
- `cbs_api`
- `boi_hedonic`
- `data_gov_il_locality_registry`

The machine-readable registry lives in [`src/rent_collector/source_registry.py`](../src/rent_collector/source_registry.py).
