import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tidio Fixed", layout="wide")

st.title("🚀 ScreenerPro Partner Portal")
st.write("Scroll the page — the Tidio bubble should stay fixed at the corner.")

# ---------------- Tidio Script ----------------
tidio_script = """
<script>
(function() {
    // Inject Tidio script into top document (not Streamlit iframe)
    var s = document.createElement("script");
    s.src = "//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js";
    s.async = true;
    s.onload = function() {
        function fixTidio() {
            var iframe = window.top.document.querySelector("#tidio-chat-iframe");
            if (iframe) {
                iframe.style.position = "fixed";
                iframe.style.bottom = "20px";
                iframe.style.right = "20px";
                iframe.style.left = "auto";
                iframe.style.zIndex = "999999";
            } else {
                setTimeout(fixTidio, 500);
            }
        }
        if (window.tidioChatApi) {
            window.tidioChatApi.on("ready", fixTidio);
        } else {
            window.top.document.addEventListener("tidioChat-ready", fixTidio);
        }
    };
    window.top.document.body.appendChild(s);
})();
</script>
"""

# Inject with no height/width
components.html(tidio_script, height=0, width=0, scrolling=False)
