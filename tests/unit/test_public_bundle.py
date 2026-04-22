from __future__ import annotations

import json
from pathlib import Path

from rent_collector.public_bundle import validate_public_bundle
from rent_collector.provenance import write_manifest, write_source_inventory_csv


def test_validate_public_bundle_detects_missing_manifest(tmp_path: Path) -> None:
    assert validate_public_bundle(tmp_path) == ["manifest.json is missing"]


def test_write_manifest_uses_relative_paths(tmp_path: Path) -> None:
    root_dir = tmp_path
    bundle_dir = tmp_path / "data" / "public_bundle"
    bundle_dir.mkdir(parents=True)
    inventory_path = bundle_dir / "source_inventory.csv"
    write_source_inventory_csv(inventory_path)

    manifest = write_manifest(
        root_dir=root_dir,
        output_path=bundle_dir / "manifest.json",
        artifact_paths=[inventory_path],
        row_counts={"source_inventory.csv": 5},
        collector_version="0.2.0",
    )

    stored = json.loads((bundle_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["files"][0]["relative_path"] == "data/public_bundle/source_inventory.csv"
    assert stored["files"][0]["relative_path"] == "data/public_bundle/source_inventory.csv"
