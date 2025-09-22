import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration at the very top of your script
st.set_page_config(layout="wide")

# Your Tidio JavaScript code with your unique key
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# Embed the Tidio script using a small, but non-zero height.
# This prevents it from appearing at the top and ensures proper rendering.
components.html(tidio_script, height=1)

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")

# Add enough content to enable scrolling
for i in range(50):
    st.write(f"Line {i+1}")
