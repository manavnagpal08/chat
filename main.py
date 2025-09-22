import streamlit as st
import streamlit.components.v1 as components

# Your Tidio JavaScript code with your unique key
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# Inject the script directly into the Streamlit app
# The Tidio widget handles its own fixed positioning.
components.html(tidio_script, height=0)

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
st.text("." * 1000)
