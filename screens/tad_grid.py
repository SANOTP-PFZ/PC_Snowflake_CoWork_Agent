import streamlit as st
import base64
from pathlib import Path

from data.agents import TAD_SHIPMENT_AGENTS, TAD_ADMINS_AGENTS


AGENT_ICON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'


def _render_agent_card(agent: dict, highlighted: bool):
    name = agent["name"]
    url = agent.get("url")
    desc = agent.get("desc", "")
    highlight_class = "ta-agent-card-highlight" if highlighted else ""

    card_html = f"""
    <div class="ta-agent-card {highlight_class}">
        <div class="ta-card-title">{name}</div>
        <div class="ta-card-desc">{desc}</div>
    </div>
    """

    if url:
        st.markdown(
            f'<a href="{url}" target="_blank" class="ta-card-link">{card_html}</a>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(card_html, unsafe_allow_html=True)


def render():
    st.markdown("## Therapy Area & Data Source")
    st.markdown(
        "<p style='color:#1a5296;font-size:14px;margin-top:-8px'>Agents wired to a specific data source for grounded, source-level answers — ideal for deep-dives into shipment, claims, or market data.</p>",
        unsafe_allow_html=True,
    )

    # Flowchart images
    img_dir = Path(__file__).parent.parent
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        st.image(str(img_dir / "shipment_flow.png"), use_container_width=True)
        st.markdown("<p style='text-align:center;font-size:13px;font-weight:600;color:var(--text-2);margin-top:4px'>Shipment Flow</p>", unsafe_allow_html=True)
    with col_img2:
        st.image(str(img_dir / "supply_chain.png"), use_container_width=True)
        st.markdown("<p style='text-align:center;font-size:13px;font-weight:600;color:var(--text-2);margin-top:4px'>Supply Chain</p>", unsafe_allow_html=True)

    # AI disclaimer
    st.warning(
        "Answers from these agents are produced by AI and may be incomplete or inaccurate. "
        "For complex or business-critical outputs, please verify with the relevant ZS team to validate the underlying logic and code before making decisions.",
        icon="⚠️",
    )

    # Shipment Data agents section
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Shipment Data</div>", unsafe_allow_html=True)

    # Filter chips
    if "shipment_filter" not in st.session_state:
        st.session_state["shipment_filter"] = "All"

    chip_options = ["All", "CDC", "DDD", "867"]
    cols = st.columns([1, 1, 1, 1, 5])
    for i, option in enumerate(chip_options):
        with cols[i]:
            is_active = st.session_state["shipment_filter"] == option
            btn_type = "primary" if is_active else "secondary"
            if st.button(option, key=f"chip_{option}", use_container_width=True, type=btn_type):
                st.session_state["shipment_filter"] = option
                st.rerun()

    shipment_filter = st.session_state["shipment_filter"]

    filtered_shipment = [a for a in TAD_SHIPMENT_AGENTS if shipment_filter == "All" or a.get("tag") == shipment_filter]

    if not filtered_shipment:
        st.caption("No agents match the selected filter.")
    else:
        rows = [filtered_shipment[i : i + 3] for i in range(0, len(filtered_shipment), 3)]
        for row in rows:
            cols = st.columns(3)
            for i, agent in enumerate(row):
                with cols[i]:
                    _render_agent_card(agent, False)
            st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    # Admins Data agents section
    st.markdown("<hr style='border:none;border-top:1px solid rgba(0,47,108,0.08);margin:28px 0 8px'>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Administrations Data</div>", unsafe_allow_html=True)

    # Data source filter
    if "admins_source_filter" not in st.session_state:
        st.session_state["admins_source_filter"] = "All"

    source_options = [("All", "All"), ("eLAAD", "Elaad"), ("Optum", "Optum"), ("Health Verity", "Health Verity")]
    src_cols = st.columns([1.5, 1, 1, 1, 1.5, 4])
    with src_cols[0]:
        st.markdown("<div style='font-size:14px;font-weight:600;color:var(--text-2);padding-top:6px'>Data source</div>", unsafe_allow_html=True)
    for i, (label, value) in enumerate(source_options):
        with src_cols[i + 1]:
            is_active = st.session_state["admins_source_filter"] == value
            btn_type = "primary" if is_active else "secondary"
            if st.button(label, key=f"adm_src_{value}", use_container_width=True, type=btn_type):
                st.session_state["admins_source_filter"] = value
                st.rerun()

    # Market filter
    if "admins_market_filter" not in st.session_state:
        st.session_state["admins_market_filter"] = "All"

    market_options = [("All", "All"), ("RSV", "Rsv"), ("PCV", "Pcv"), ("COVID", "Covid"), ("Flu", "Flu")]
    mkt_cols = st.columns([1.5, 1, 1, 1, 1, 1, 3.5])
    with mkt_cols[0]:
        st.markdown("<div style='font-size:14px;font-weight:600;color:var(--text-2);padding-top:6px'>Market</div>", unsafe_allow_html=True)
    for i, (label, value) in enumerate(market_options):
        with mkt_cols[i + 1]:
            is_active = st.session_state["admins_market_filter"] == value
            btn_type = "primary" if is_active else "secondary"
            if st.button(label, key=f"adm_mkt_{value}", use_container_width=True, type=btn_type):
                st.session_state["admins_market_filter"] = value
                st.rerun()

    # Agent grid
    admins_source = st.session_state["admins_source_filter"]
    admins_market = st.session_state["admins_market_filter"]

    filtered_admins = [
        a for a in TAD_ADMINS_AGENTS
        if (admins_source == "All" or a.get("source") == admins_source)
        and (admins_market == "All" or a.get("market") == admins_market)
    ]

    if not filtered_admins:
        st.caption("No agents match the selected filters.")
    else:
        rows = [filtered_admins[i : i + 3] for i in range(0, len(filtered_admins), 3)]
        for row in rows:
            cols = st.columns(3)
            for i, agent in enumerate(row):
                with cols[i]:
                    _render_agent_card(agent, False)
            st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    from data.agents import TAD_OAC_AGENTS, TAD_MIGRAINE_AGENTS, TAD_NPA_AGENTS, TAD_COPAY_AGENTS

    # OAC agents section
    st.markdown("<hr style='border:none;border-top:1px solid rgba(0,47,108,0.08);margin:28px 0 8px'>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Oral Anticoagulant (OAC)</div>", unsafe_allow_html=True)

    rows = [TAD_OAC_AGENTS[i : i + 3] for i in range(0, len(TAD_OAC_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                _render_agent_card(agent, False)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    # Migraine agents section
    st.markdown("<hr style='border:none;border-top:1px solid rgba(0,47,108,0.08);margin:28px 0 8px'>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Migraine</div>", unsafe_allow_html=True)

    rows = [TAD_MIGRAINE_AGENTS[i : i + 3] for i in range(0, len(TAD_MIGRAINE_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                _render_agent_card(agent, False)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    # NPA agents section
    st.markdown("<hr style='border:none;border-top:1px solid rgba(0,47,108,0.08);margin:28px 0 8px'>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>National Prescription Audit (NPA)</div>", unsafe_allow_html=True)

    rows = [TAD_NPA_AGENTS[i : i + 3] for i in range(0, len(TAD_NPA_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                _render_agent_card(agent, False)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    # CoPay agents section
    st.markdown("<hr style='border:none;border-top:1px solid rgba(0,47,108,0.08);margin:28px 0 8px'>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>CoPay</div>", unsafe_allow_html=True)

    rows = [TAD_COPAY_AGENTS[i : i + 3] for i in range(0, len(TAD_COPAY_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                _render_agent_card(agent, False)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)


