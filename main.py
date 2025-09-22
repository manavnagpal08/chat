import streamlit as st
import streamlit.components.v1 as components
import time

# Set the page configuration at the very top of your script
st.set_page_config(layout="wide")

# The Tidio JavaScript code with your unique key
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# The JavaScript to move the Tidio widget to the main body
move_script = """
<script>
    function moveTidioFrame() {
        const tidioFrame = document.querySelector('iframe[src*="tidio"]');
        if (tidioFrame && tidioFrame.parentNode) {
            // Remove the iframe from its current parent (the Streamlit iframe)
            tidioFrame.parentNode.removeChild(tidioFrame);
            // Move it to the main page's body
            window.parent.document.body.appendChild(tidioFrame);
        }
    }

    // Wait a moment for the Tidio script to load and create the iframe
    setTimeout(moveTidioFrame, 2000);
</script>
"""

# Embed the Tidio script first. It needs a moment to create its iframe.
components.html(tidio_script, height=1)

# Embed the moving script to execute the relocation
components.html(move_script, height=1)

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
st.text("." * 1000)
