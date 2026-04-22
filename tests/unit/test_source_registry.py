from __future__ import annotations

import pytest

from rent_collector.source_registry import get_source, list_sources


def test_list_sources_is_public_safe_and_non_empty() -> None:
    sources = list_sources()
    assert sources
    assert all(source.source_class == "public_safe" for source in sources)


def test_get_source_returns_named_descriptor() -> None:
    source = get_source("cbs_table49")
    assert source.display_name.startswith("CBS Table 4.9")
    assert source.as_dict()["status"] == "active"


def test_get_source_raises_for_unknown_source() -> None:
    with pytest.raises(KeyError):
        get_source("missing")
