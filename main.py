import streamlit as st

st.set_page_config(page_title="ScreenerPro Partner Portal")

st.title("🚀 ScreenerPro Partner Portal")
st.write("Showcase your skills, collaborate with teams, earn badges, and apply to jobs — all in one modern career hub.")

# Inject Tidio script + force styles at top-level page
st.markdown(
    """
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>

    <script>
    function moveTidio() {
        const iframe = document.querySelector("#tidio-chat-iframe");
        if (iframe) {
            iframe.style.position = "fixed";
            iframe.style.left = "20px";
            iframe.style.right = "auto";
            iframe.style.bottom = "20px";
            iframe.style.zIndex = "999999";
        } else {
            // Try again until it loads
            setTimeout(moveTidio, 500);
        }
    }
    document.addEventListener("tidioChat-ready", moveTidio);
    </script>
    """,
    unsafe_allow_html=True
)
