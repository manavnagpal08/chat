import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration at the very top of your script
st.set_page_config(layout="wide")

# The Tidio JavaScript code with your unique key
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# Embed the Tidio script using components.html with a very small height.
# The key here is to allow Tidio to create its floating UI *outside* this minimal iframe.
# If Tidio is designed to inject elements into the *parent* document, this will work.
# If Tidio strictly renders within its own iframe, we need another approach (see next point).
components.html(tidio_script, height=1, scrolling=False) # Ensure minimal footprint for the script embedder

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
st.text("." * 1000)
