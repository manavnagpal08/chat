import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro with Tidio")

st.title("💬 ScreenerPro with Tidio")

# Run Tidio script in a hidden div (no visible iframe)
components.html("""
<div id="tidio-chat-widget"></div>
<script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
""", height=0, width=0)
