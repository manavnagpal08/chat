import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro with Tidio")

st.title("💬 ScreenerPro with Tidio")

# Inject only the script, no iframe visible
components.html(
    """
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    """,
    height=0,  # no height
    width=0    # no width
)
