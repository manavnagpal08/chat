import streamlit as st

st.set_page_config(layout="wide")

tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# Embed the Tidio script directly into the Streamlit app's HTML.
# WARNING: Using unsafe_allow_html=True can be a security risk if the HTML comes from untrusted sources.
# Ensure you trust the Tidio script entirely.
st.markdown(tidio_script, unsafe_allow_html=True)

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
st.text("." * 1000)
