from __future__ import annotations

from rent_collector.collectors.cbs_table49 import _extract_table49_entities
from rent_collector.models import DataSource, RentObservation, RoomGroup
from rent_collector.pipeline import _merge_observations


def test_merge_observations_prefers_higher_priority_source() -> None:
    observations = [
        RentObservation(
            locality_code="5000",
            locality_name_he="תל אביב - יפו",
            locality_name_en="Tel Aviv - Yafo",
            room_group=RoomGroup.R3_0,
            avg_rent_nis=7100,
            rent_nis=7100,
            source=DataSource.CBS_TABLE49,
            year=2025,
            quarter=2,
        ),
        RentObservation(
            locality_code="5000",
            locality_name_he="תל אביב - יפו",
            locality_name_en="Tel Aviv - Yafo",
            room_group=RoomGroup.R3_0,
            median_rent_nis=7999,
            rent_nis=7999,
            source=DataSource.NADLAN,
            year=2025,
            quarter=2,
        ),
    ]

    merged = _merge_observations(observations)

    assert len(merged) == 1
    assert merged.iloc[0]["source"] == DataSource.NADLAN
    assert merged.iloc[0]["rent_nis"] == 7999


def test_extract_table49_entities_uses_latest_value_column() -> None:
    import pandas as pd

    df = pd.DataFrame(
        [
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, 2025, None],
            [None, "I-III", None],
            [None, "Average\nprice ", None],
            [None, None, None],
            ["Big cities", None, None],
            ["Tel Aviv - 5000", None, None],
            ["1-2", 5400, None],
            ["2.5-3", 7000, None],
            ["3.5-4", 8600, None],
            ["4.5-6", 10900, None],
        ]
    )

    extracted = _extract_table49_entities(df, value_col=1, year=2025, quarter=1)

    assert extracted["city"].tolist() == ["Tel Aviv", "Tel Aviv", "Tel Aviv", "Tel Aviv"]
    assert extracted["room_group"].tolist() == ["2.0", "3.0", "4.0", "5+"]
    assert extracted["avg_rent_nis"].tolist() == [5400.0, 7000.0, 8600.0, 10900.0]
