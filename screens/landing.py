import streamlit as st

from data.agents import BRANDS, TA_AGENTS


def _sparkline_svg(values: list, color: str) -> str:
    """Generate an inline SVG sparkline from a list of values."""
    max_val = max(values) if values else 1
    min_val = min(values) if values else 0
    span = max_val - min_val or 1
    width = 100
    height = 28
    step = width / (len(values) - 1) if len(values) > 1 else width
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
    st.caption("Summaries sourced from NPA data source")

    cols = st.columns(5)
    for i, brand in enumerate(BRANDS):
        with cols[i]:
            direction = brand["direction"]
            line_color = "#3b6d11" if direction == "up" else "#a32d2d"
            chip_class = "green" if direction == "up" else "red"
            icon = "↑" if direction == "up" else "↓"

            svg = _sparkline_svg(brand["values"], line_color)
            st.markdown(
                f"""
                <div class="brand-card">
                    <div class="brand-name">{brand['name']}</div>
                    <div class="brand-category">{brand['category']}</div>
                    {svg}
                    <span class="chip chip-{chip_class}">{icon} {brand['trend']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Main heading
    st.markdown("<h1 style='text-align:center;margin-bottom:4px'>Choose an agent category</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center;color:#5f5e5a;font-size:15px'>One place to discover and launch your CoCo agents.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("<div style='margin-bottom:24px'></div>", unsafe_allow_html=True)

    # Category cards
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("<div style='font-size:18px;font-weight:600'>Therapy area agents</div>", unsafe_allow_html=True)
            st.markdown("Agents scoped to a single therapy area and all available data sources for domain and data focused questions.")
            st.markdown(f'<span class="chip chip-blue">6 agents</span>', unsafe_allow_html=True)
            if st.button("Explore →", key="go_ta", use_container_width=True):
                st.session_state["screen"] = "ta"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("<div style='font-size:18px;font-weight:600'>Therapy area & Data source agents</div>", unsafe_allow_html=True)
            st.markdown("Therapy area agents wired to a specific data source for grounded answers.")
            st.markdown(f'<span class="chip chip-teal">9 agents</span>', unsafe_allow_html=True)
            if st.button("Explore →", key="go_tad", use_container_width=True):
                st.session_state["screen"] = "tad"
                st.rerun()

    # Stats tiles
    st.markdown("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total agents", "14")
    with c2:
        st.metric("Therapy areas", "7")
    with c3:
        st.metric("Data sources", "4")
