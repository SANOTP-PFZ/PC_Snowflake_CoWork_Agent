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


AGENT_ICON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'


def render_agent_card(agent: dict, category: str):
    name = agent["name"]
    url = agent.get("url")
    desc = agent.get("desc", "")

    card_html = f"""
    <div class="ta-agent-card">
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
