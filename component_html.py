import os
import streamlit.components.v1 as components

# The directory where your HTML file will be stored
_RELEASE = True
if not _RELEASE:
    _component_func = components.declare_component(
        "tidio_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("tidio_component", path=build_dir)

def tidio_chatbot_component():
    """Creates the HTML wrapper for the Tidio chatbot."""
    tidio_html = """
        <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    """
    _component_func(tidio_script=tidio_html, default=None)
