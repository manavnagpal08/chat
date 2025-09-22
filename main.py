import streamlit as st

st.set_page_config(page_title="ScreenerPro Partner Portal")

st.title("🚀 ScreenerPro Partner Portal")
st.write(
    "Showcase your skills, collaborate with teams, earn badges, "
    "and apply to jobs — all in one modern career hub."
)

# ✅ Inject Tidio into the TOP page, not just Streamlit iframe
st.markdown(
    """
    <script>
    (function() {
        var s = document.createElement("script");
        s.src = "//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js";
        s.async = true;
        s.onload = function() {
            function moveTidio() {
                var iframe = window.top.document.querySelector("#tidio-chat-iframe");
                if (iframe) {
                    iframe.style.position = "fixed";
                    iframe.style.left = "20px";
                    iframe.style.right = "auto";
                    iframe.style.bottom = "20px";
                    iframe.style.zIndex = "999999";
                } else {
                    setTimeout(moveTidio, 500);
                }
            }
            if (window.tidioChatApi) {
                window.tidioChatApi.on("ready", moveTidio);
            } else {
                window.top.document.addEventListener("tidioChat-ready", moveTidio);
            }
        };
        window.top.document.body.appendChild(s);
    })();
    </script>
    """,
    unsafe_allow_html=True
)
