from __future__ import annotations

import runpy

from click.testing import CliRunner

from rent_collector.cli import main


def test_probe_command_returns_success(monkeypatch) -> None:
    monkeypatch.setattr(
        "rent_collector.pipeline.probe_all",
        lambda: {
            "nadlan": {"ok": True},
            "cbs-table49": {"ok": False},
        },
    )

    result = CliRunner().invoke(main, ["--probe"])

    assert result.exit_code == 0
    assert "1/2 sources reachable." in result.output


def test_full_command_exits_nonzero_when_pipeline_returns_empty(monkeypatch, tmp_path) -> None:
    import pandas as pd

    monkeypatch.setattr("rent_collector.pipeline.run_pipeline", lambda **_: pd.DataFrame())

    result = CliRunner().invoke(main, ["--output", str(tmp_path / "out.csv")])

    assert result.exit_code == 1
    assert "No data collected." in result.output


def test_dry_run_empty_does_not_exit_nonzero(monkeypatch, tmp_path) -> None:
    import pandas as pd

    monkeypatch.setattr("rent_collector.pipeline.run_pipeline", lambda **_: pd.DataFrame())

    result = CliRunner().invoke(main, ["--dry-run", "--output", str(tmp_path / "out.csv")])

    assert result.exit_code == 0


def test_module_main_invokes_click_entrypoint(monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["rent_collector.cli", "--help"])

    try:
        runpy.run_module("rent_collector.cli", run_name="__main__")
    except SystemExit as exc:
        assert exc.code == 0
