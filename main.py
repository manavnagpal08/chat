import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro Partner Portal")

st.title("🚀 ScreenerPro Partner Portal")
st.write("Showcase your skills, collaborate with teams, earn badges, and apply to jobs — all in one modern career hub.")

components.html(
    """
    <style>
    /* Extra insurance: force chat iframe styles */
    #tidio-chat-iframe {
        position: fixed !important;
        left: 20px !important;
        right: auto !important;
        bottom: 20px !important;
        z-index: 999999 !important;  /* keep above everything */
    }
    #tidio {
        position: fixed !important;
        left: 20px !important;
        right: auto !important;
        bottom: 20px !important;
        z-index: 999999 !important;
    }
    </style>

    <!-- Load Tidio -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>

    <script>
    function onTidioChatApiReady() {
        // Adjust styles via JS API
        tidioChatApi.adjustStyles('#tidio-chat-iframe { position: fixed !important; left: 20px !important; right: auto !important; bottom: 20px !important; z-index: 999999 !important; }');
        tidioChatApi.adjustStyles('#tidio { position: fixed !important; left: 20px !important; right: auto !important; bottom: 20px !important; z-index: 999999 !important; }');

        // Mobile adjustment (overrides desktop)
        tidioChatApi.adjustStyles(
          '@media only screen and (max-width: 980px) { #tidio-chat-iframe, #tidio { position: fixed !important; left: 10px !important; right: auto !important; bottom: 10px !important; z-index: 999999 !important; } }'
        );
    }

    // Ensure script runs at right time
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
