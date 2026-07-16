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
    st.markdown(
        "<p style='color:#1a5296;font-size:14px;margin-top:-8px'>Agents wired to a specific data source for grounded, source-level answers — ideal for deep-dives into shipment, claims, or market data.</p>",
        unsafe_allow_html=True,
    )

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

    rows = [filtered_shipment[i : i + 3] for i in range(0, len(filtered_shipment), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                _render_agent_card(agent, False)
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    # Admins Data agents section
    st.markdown("<hr style='border:none;border-top:1px solid rgba(0,47,108,0.08);margin:28px 0 8px'>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>Admins Data</div>", unsafe_allow_html=True)

    # Data source filter
    if "admins_source_filter" not in st.session_state:
        st.session_state["admins_source_filter"] = "All"

    source_options = ["All", "Elaad", "Optum", "Health Verity"]
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

    market_options = ["All", "Rsv", "Pcv", "Covid", "Flu"]
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

    filtered_admins = [
        a for a in TAD_ADMINS_AGENTS
        if (admins_source == "All" or a.get("source") == admins_source)
        and (admins_market == "All" or a.get("market") == admins_market)
    ]

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
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>OAC</div>", unsafe_allow_html=True)

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
    st.markdown("<div style='margin-top:24px;margin-bottom:12px;font-size:18px;font-weight:700'>NPA</div>", unsafe_allow_html=True)

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


