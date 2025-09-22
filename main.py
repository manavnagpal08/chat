import streamlit as st
import streamlit.components.v1 as components

# Set the page config
st.set_page_config(layout="wide")

# Tidio script
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# Create a toggle button in sidebar
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

if st.sidebar.button("Toggle Chat"):
    st.session_state.chat_open = not st.session_state.chat_open

# If/Else condition for size
if st.session_state.chat_open:
    height = 600
    width = 700
else:
    height = 5
    width = 5  # very small when "closed"

# Embed Tidio widget with conditional size
components.html(tidio_script, height=height, width=width, scrolling=False)

# Example app content
st.title("My Streamlit App")
st.write("Scroll down to see Tidio widget behavior.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
st.text("." * 1000)
