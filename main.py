import streamlit as st
import streamlit.components.v1 as components

# Your Tidio JavaScript code with your unique key
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# The Tidio widget handles its own fixed positioning.
# By setting height=0 for the iframe, we avoid adding extra
# vertical space to the Streamlit app.
components.html(tidio_script, height=0)

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
# Add more content to enable scrolling
st.text("." * 1000)
