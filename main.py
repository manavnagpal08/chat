import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro with Tidio")

st.title("🚀 ScreenerPro Partner Portal")
st.write("Showcase your skills, collaborate with teams, earn badges, and apply to jobs — all in one modern career hub.")

components.html(
    """
    <!-- Tidio base script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    
    <!-- Force bottom-left position -->
    <script>
    function onTidioChatApiReady() {
        // Desktop
        tidioChatApi.adjustStyles('#tidio { left: 20px !important; right: auto !important; bottom: 20px !important; }');
        
        // Mobile
        tidioChatApi.adjustStyles(
          '@media only screen and (max-width: 980px) { #tidio { left: 20px !important; right: auto !important; bottom: 20px !important; } }'
        );
    }
    if (window.tidioChatApi) {
        window.tidioChatApi.on("ready", onTidioChatApiReady);
    } else {
        document.addEventListener("tidioChat-ready", onTidioChatApiReady);
    }
    </script>
    """,
    height=0,
    width=0,
)
