import streamlit as st
import dataiku

from data.agents import TA_AGENTS


DATASET_NAME = "SQL_EARNINGS_REPORT_MASTER_DATASET_SF"

BRAND_CONFIG = [
    {"name": "Prevnar", "market": "PCV", "brand_db": "PREVNAR"},
    {"name": "Abrysvo", "market": "RSV", "brand_db": "ABRYSVO"},
    {"name": "Comirnaty", "market": "COVID_VACCINES", "brand_db": "COMIRNATY"},
    {"name": "Eliquis", "market": "OAC", "brand_db": "ELIQUIS"},
    {"name": "Nurtec", "market": "OCGRP", "brand_db": "NURTEC"},
]


@st.cache_data(ttl=3600)
def _load_data():
    """Load full dataset from Dataiku."""
    dataset = dataiku.Dataset(DATASET_NAME)
    return dataset.get_dataframe()


def _get_brand_trend(df, brand_db, metric="TRX MARKET SHARE"):
    """Extract QoQ trend values for a brand."""
    filtered = df[
        (df["BRAND"] == brand_db)
        & (df["METRICS"] == metric)
        & (df["YR_QTR_TXT"] >= "2024Q1")
    ].sort_values("YR_QTR_TXT")
    if filtered.empty:
        return None
    return filtered["VALUE"].tolist()


def _sparkline_svg(values: list, color: str) -> str:
    """Generate an inline SVG sparkline from a list of values."""
    if not values or len(values) < 2:
        return ""
    max_val = max(values)
    min_val = min(values)
    span = max_val - min_val or 1
    width = 100
    height = 28
    step = width / (len(values) - 1)
    points = " ".join(
        f"{i * step:.1f},{height - ((v - min_val) / span) * (height - 4) - 2:.1f}"
        for i, v in enumerate(values)
    )
    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="32" '
        f'preserveAspectRatio="none" style="display:block;margin:4px 0">'
        f'<polyline points="{points}" fill="none" stroke="{color}" '
        f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    )


def render():
    # National Brand Summary
    st.markdown("#### National Brand Summary")
    st.caption("QoQ TRX Market Share trends from 2024Q1 onwards")

    # Load data from Dataiku
    try:
        df = _load_data()
    except Exception:
        df = None

    st.markdown('<div style="margin-bottom:12px"></div>', unsafe_allow_html=True)
    cols = st.columns(5)
    for i, brand in enumerate(BRAND_CONFIG):
        with cols[i]:
            values = _get_brand_trend(df, brand["brand_db"], "TRX MARKET SHARE") if df is not None else None

            if values and len(values) >= 2:
                latest = f"{values[-1]:.1f}%"
                direction = "up" if values[-1] >= values[0] else "down"
            else:
                values = [50, 50, 50, 50]
                latest = "—"
                direction = "up"

            line_color = "#0093D0" if direction == "up" else "#a32d2d"

            svg = _sparkline_svg(values, line_color)
            st.markdown(
                f"""
                <div class="brand-trend-box">
                    <div class="brand-name">{brand['name']}</div>
                    <div class="brand-category">{brand['market']} · TRX {latest}</div>
                    {svg}
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Main heading
    st.markdown("<h1 style='text-align:center;margin-bottom:4px'>Choose an agent category</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center;color:#4a5568;font-size:15px'>One place to discover and launch your agents.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("<div style='margin-bottom:24px'></div>", unsafe_allow_html=True)

    # Category cards
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown(
                """
                <div style="border-left:4px solid #0093D0;padding-left:12px">
                    <div style="font-size:18px;font-weight:600">🧬 Therapy area agents</div>
                    <div style="font-size:13px;color:#4a5568;margin-top:6px">Agents scoped to a single therapy area and all available data sources for domain and data focused questions.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Explore →", key="go_ta", use_container_width=True):
                st.session_state["screen"] = "ta"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown(
                """
                <div style="border-left:4px solid #0093D0;padding-left:12px">
                    <div style="font-size:18px;font-weight:600">📊 Therapy area & Data source agents</div>
                    <div style="font-size:13px;color:#4a5568;margin-top:6px">Therapy area agents wired to a specific data source for grounded answers.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Explore →", key="go_tad", use_container_width=True):
                st.session_state["screen"] = "tad"
                st.rerun()
