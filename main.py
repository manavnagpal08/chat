import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration
st.set_page_config(layout="wide")

# The Tidio JavaScript code with your unique key
# Embed this script once, and let Tidio handle its own iframe positioning
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# Embed the Tidio script
# Allow Tidio to create its iframe within this component and manage its own position.
components.html(tidio_script, height=1, scrolling=False) # Set scrolling to False if only embedding script

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
st.text("." * 1000)
