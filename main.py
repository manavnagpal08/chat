import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro with Tidio")

st.title("💬 ScreenerPro with Tidio")

components.html("""
<!DOCTYPE html>
<html>
  <body>
    <!-- Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
  </body>
</html>
""", height=0, width=0)
