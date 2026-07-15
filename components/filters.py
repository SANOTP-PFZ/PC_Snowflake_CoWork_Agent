import streamlit as st


def render_brand_filter(options: list[str], key: str = "brand_filter") -> str:
    selected = st.pills("Brand", options, default="All", key=key)
    return selected or "All"


def render_source_filter(options: list[str], key: str = "source_filter") -> str:
    selected = st.pills("Data source", options, default="All sources", key=key)
    return selected or "All sources"
