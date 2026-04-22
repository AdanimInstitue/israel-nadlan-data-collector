# israel-nadlan-data-collector

Public-safe collector for Israeli housing-rent benchmark data.

This repository fetches and normalizes named public sources, writes a public bundle with provenance metadata, and avoids any coupling to non-public workflows or repositories.

## Supported Sources

The public collector currently ships adapters for these public-facing sources:

| `source_id` | Publisher | Public role |
| --- | --- | --- |
| `nadlan_gov_il` | Israeli government real-estate portal | locality rent observations |
| `cbs_table49` | Central Bureau of Statistics | district and city benchmark observations |
| `cbs_api` | Central Bureau of Statistics | public metadata and API-discoverable series support |
| `boi_hedonic` | Bank of Israel | modeled fallback estimates derived from published source material |
| `data_gov_il_locality_registry` | data.gov.il / CBS | locality metadata and crosswalk support |

Source metadata, terms pointers, and attribution posture are documented in [docs/source_policy.md](docs/source_policy.md).

## What The Collector Produces

`build-public-bundle` writes a bundle under `data/public_bundle/` containing:

- `rent_benchmarks.csv`
- `locality_crosswalk.csv`
- `source_inventory.csv`
- `manifest.json`

The bundle is designed to feed the public dataset repository, but this repository remains self-contained and does not require a sibling checkout to run.

## Install

```bash
python -m pip install -e ".[dev]"
```

Requires Python 3.11 or newer.

## CLI

```bash
indc --help
indc --probe
indc --source nadlan --validate
indc sources list
indc build-public-bundle
indc validate-public-bundle
indc write-manifest
```

The legacy `rent-collector` and `rent-collect` entry points remain available as aliases.

## Repository Layout

```text
src/rent_collector/
  cli.py
  source_registry.py
  provenance.py
  public_bundle.py
  pipeline.py
  collectors/
  utils/
configs/
  pipelines/public_release.yaml
  sources/
docs/
tests/
```

## Public Scope

- Public-facing source adapters only.
- Synthetic or public-safe test fixtures only.
- Rights-aware source metadata and provenance records.
- No references to non-public systems or storage layouts.

## Development

```bash
pytest
ruff check src tests
mypy src
```
