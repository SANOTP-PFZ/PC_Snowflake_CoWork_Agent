import streamlit as st
import pandas as pd


def render_brand_card(brand: dict):
    direction = brand["direction"]
    color = "#3b6d11" if direction == "up" else "#a32d2d"
    bg = "#eaf3de" if direction == "up" else "#fcebeb"
    icon = "↑" if direction == "up" else "↓"

    df = pd.DataFrame({"value": brand["values"]})

    st.markdown(
        f"""
        <div class="brand-card">
            <div class="brand-name">{brand['name']}</div>
            <div class="brand-category">{brand['category']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.line_chart(df, height=60, use_container_width=True)
    st.markdown(
        f'<span class="chip" style="background:{bg};color:{color}">{icon} {brand["trend"]}</span>',
        unsafe_allow_html=True,
    )


def render_category_card(title: str, description: str, count: int, color_scheme: str, key: str):
    if color_scheme == "blue":
        bg = "#e6f1fb"
        tc = "#185fa5"
        icon = "🩺"
    else:
        bg = "#e1f5ee"
        tc = "#0f6e56"
        icon = "🗄️"

    if st.button(
        f"**{title}**\n\n{description}\n\n{count} agents",
        key=f"cat_{key}",
        use_container_width=True,
    ):
        st.session_state["screen"] = key


def render_agent_card(agent: dict, category: str):
    name = agent["name"]
    brand = agent["brand"]
    source = agent.get("source")

    if category == "ta":
        url = agent.get("url")
        if url:
            st.markdown(
                f"""
                <a href="{url}" target="_blank" class="ta-card-link">
                    <div class="ta-agent-card">
                        <div class="ta-agent-name">{name}</div>
                    </div>
                </a>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="ta-agent-card">
                    <div class="ta-agent-name">{name}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        chips_html = f'<span class="chip chip-blue">{brand}</span>'
        if source:
            chips_html += f'<span class="chip chip-teal">{source}</span>'
        chips_html += '<span class="chip chip-green">Active</span>'

        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-card-header">
                    <div class="agent-icon">🤖</div>
                    <div class="agent-name">{name}</div>
                </div>
                <div class="agent-chips">{chips_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    if category != "ta":
        url = agent.get("url")
        if url:
            st.link_button("Launch agent ↗", url, use_container_width=True)
        else:
            if st.button("Launch agent", key=f"launch_{category}_{name}", use_container_width=True):
                st.session_state["screen"] = "agent"
                st.session_state["current_agent"] = agent
                st.session_state["agent_category"] = category


def render_stat_tile(label: str, value: str):
    st.markdown(
        f"""
        <div class="stat-tile">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
