import streamlit as st

from data.agents import TAD_SHIPMENT_AGENTS, TAD_ADMINS_AGENTS


def _render_agent_card(agent: dict, highlighted: bool):
    name = agent["name"]
    url = agent.get("url")
    highlight_class = "ta-agent-card-highlight" if highlighted else ""

    if url:
        st.markdown(
            f"""
            <a href="{url}" target="_blank" class="ta-card-link">
                <div class="ta-agent-card {highlight_class}">
                    <div class="ta-agent-name">{name}</div>
                    <div class="ta-launch-text">Launch now ↗</div>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="ta-agent-card {highlight_class}">
                <div class="ta-agent-name">{name}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render():
    st.markdown("**Home** / Therapy area & Data source agents")
    st.markdown("## Therapy area & Data source agents")

    # AI disclaimer
    st.warning(
        "Answers from these agents are produced by AI and may be incomplete or inaccurate. "
        "For complex or business-critical outputs, please verify with the relevant ZS team to validate the underlying logic and code before making decisions.",
        icon="⚠️",
    )

    # Shipment Data agents section
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Shipment Data agents</div>", unsafe_allow_html=True)

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
    filter_active = shipment_filter != "All"

    if filter_active:
        st.markdown("<div class='tad-filter-active'>", unsafe_allow_html=True)

    rows = [TAD_SHIPMENT_AGENTS[i : i + 3] for i in range(0, len(TAD_SHIPMENT_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                highlighted = filter_active and (agent.get("tag") == shipment_filter)
                _render_agent_card(agent, highlighted)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    if filter_active:
        st.markdown("</div>", unsafe_allow_html=True)

    # Admins Data agents section
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Admins Data agents</div>", unsafe_allow_html=True)

    # Data source filter
    if "admins_source_filter" not in st.session_state:
        st.session_state["admins_source_filter"] = "All"

    source_options = ["All", "ELAAD", "OPTUM", "HEALTH VERITY"]
    src_cols = st.columns([1.5, 1, 1, 1, 1.5, 4])
    with src_cols[0]:
        st.markdown("<div style='font-size:13px;color:#5f5e5a;padding-top:4px'>Data source</div>", unsafe_allow_html=True)
    for i, option in enumerate(source_options):
        with src_cols[i + 1]:
            is_active = st.session_state["admins_source_filter"] == option
            btn_type = "primary" if is_active else "secondary"
            if st.button(option, key=f"adm_src_{option}", use_container_width=True, type=btn_type):
                st.session_state["admins_source_filter"] = option
                st.rerun()

    # Market filter
    if "admins_market_filter" not in st.session_state:
        st.session_state["admins_market_filter"] = "All"

    market_options = ["All", "RSV", "PCV", "COVID", "OAC", "FLU"]
    mkt_cols = st.columns([1.5, 1, 1, 1, 1, 1, 1, 1.5])
    with mkt_cols[0]:
        st.markdown("<div style='font-size:13px;color:#5f5e5a;padding-top:4px'>Market</div>", unsafe_allow_html=True)
    for i, option in enumerate(market_options):
        with mkt_cols[i + 1]:
            is_active = st.session_state["admins_market_filter"] == option
            btn_type = "primary" if is_active else "secondary"
            if st.button(option, key=f"adm_mkt_{option}", use_container_width=True, type=btn_type):
                st.session_state["admins_market_filter"] = option
                st.rerun()

    # Agent grid
    admins_source = st.session_state["admins_source_filter"]
    admins_market = st.session_state["admins_market_filter"]
    admins_filter_active = admins_source != "All" or admins_market != "All"

    if admins_filter_active:
        st.markdown("<div class='tad-filter-active'>", unsafe_allow_html=True)

    rows = [TAD_ADMINS_AGENTS[i : i + 3] for i in range(0, len(TAD_ADMINS_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                source_match = admins_source == "All" or agent.get("source") == admins_source
                market_match = admins_market == "All" or agent.get("market") == admins_market
                highlighted = admins_filter_active and source_match and market_match
                _render_agent_card(agent, highlighted)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    if admins_filter_active:
        st.markdown("</div>", unsafe_allow_html=True)

    # Migraine agents section
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Migraine agents</div>", unsafe_allow_html=True)

    from data.agents import TAD_MIGRAINE_AGENTS
    rows = [TAD_MIGRAINE_AGENTS[i : i + 3] for i in range(0, len(TAD_MIGRAINE_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                _render_agent_card(agent, False)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    # Back to home
    st.divider()
    if st.button("← Back to Home", key="tad_home"):
        st.session_state["screen"] = "landing"
        st.rerun()
