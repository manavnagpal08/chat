import streamlit as st

st.set_page_config(page_title="ScreenerPro with Tidio Chat")

st.title("💬 ScreenerPro with Tidio Chat")

# Inject Tidio widget
st.markdown("""
<!-- Tidio Chat -->
<script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
""", unsafe_allow_html=True)

st.write("👉 The Tidio chat bubble should appear in the bottom-right corner.")
