from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class SourceDescriptor:
    source_id: str
    display_name: str
    source_class: str
    homepage_url: str
    terms_url: str | None
    license_url: str | None
    access_method: str
    record_grain: str
    expected_refresh_pattern: str
    citation_text: str
    attribution_required: bool
    redistribution_note: str
    status: str

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


PUBLIC_SOURCE_REGISTRY: tuple[SourceDescriptor, ...] = (
    SourceDescriptor(
        source_id="nadlan_gov_il",
        display_name="nadlan.gov.il settlement rent pages",
        source_class="public_safe",
        homepage_url="https://www.nadlan.gov.il/",
        terms_url=None,
        license_url=None,
        access_method="public_website_and_json_endpoint",
        record_grain="locality_room_bucket_period",
        expected_refresh_pattern="irregular_public_updates",
        citation_text="Israeli government real-estate portal (nadlan.gov.il).",
        attribution_required=True,
        redistribution_note="Use conservative, source-aware attribution.",
        status="active",
    ),
    SourceDescriptor(
        source_id="cbs_table49",
        display_name="CBS Table 4.9 average monthly rent",
        source_class="public_safe",
        homepage_url="https://www.cbs.gov.il/",
        terms_url="https://www.cbs.gov.il/en/Pages/Enduser-license.aspx",
        license_url=None,
        access_method="direct_download",
        record_grain="district_or_city_room_bucket_period",
        expected_refresh_pattern="monthly_publication_cycle",
        citation_text="Central Bureau of Statistics Table 4.9.",
        attribution_required=True,
        redistribution_note="Preserve CBS attribution and terms references.",
        status="active",
    ),
    SourceDescriptor(
        source_id="cbs_api",
        display_name="CBS public API",
        source_class="public_safe",
        homepage_url="https://api.cbs.gov.il/",
        terms_url="https://www.cbs.gov.il/en/Pages/Enduser-license.aspx",
        license_url=None,
        access_method="public_api",
        record_grain="series_observation",
        expected_refresh_pattern="source_specific",
        citation_text="Central Bureau of Statistics public API.",
        attribution_required=True,
        redistribution_note=(
            "Treat series-level outputs conservatively and cite the API family used."
        ),
        status="experimental_public",
    ),
    SourceDescriptor(
        source_id="boi_hedonic",
        display_name="Bank of Israel hedonic rent model source material",
        source_class="public_safe",
        homepage_url="https://www.boi.org.il/",
        terms_url="https://www.boi.org.il/en/terms-of-use/",
        license_url=None,
        access_method="public_pdf",
        record_grain="modeled_locality_room_bucket_period",
        expected_refresh_pattern="paper_or_model_revision",
        citation_text="Bank of Israel rent-model source material.",
        attribution_required=True,
        redistribution_note=(
            "Identify modeled outputs as derived estimates, not direct official tables."
        ),
        status="active",
    ),
    SourceDescriptor(
        source_id="data_gov_il_locality_registry",
        display_name="data.gov.il / CBS locality registry",
        source_class="public_safe",
        homepage_url="https://data.gov.il/dataset/citiesandsettelments",
        terms_url=None,
        license_url=None,
        access_method="ckan_api",
        record_grain="locality_reference_record",
        expected_refresh_pattern="periodic_registry_update",
        citation_text="data.gov.il / CBS locality registry.",
        attribution_required=True,
        redistribution_note="Retain source attribution for geography metadata.",
        status="active",
    ),
)


def list_sources() -> list[SourceDescriptor]:
    return list(PUBLIC_SOURCE_REGISTRY)


def get_source(source_id: str) -> SourceDescriptor:
    for source in PUBLIC_SOURCE_REGISTRY:
        if source.source_id == source_id:
            return source
    raise KeyError(source_id)
