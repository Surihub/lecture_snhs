import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="iframe 삽입 예시", layout="wide")
st.title("iframe 삽입 실습")

# HTML iframe 삽입
components.html(
    """
    <iframe src="https://example.com" width="800" height="600" style="border:none;"></iframe>
    """,
    height=600,
)
