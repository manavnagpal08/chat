import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tidio Fixed", layout="wide")

# ---------------- Page Content ----------------
st.title("🚀 ScreenerPro Partner Portal")
st.write(
    "Welcome to the ScreenerPro Partner Portal! "
    "Showcase your skills, collaborate with teams, earn badges, "
    "and apply to jobs — all in one modern career hub."
)

st.header("📌 Features")
st.markdown(
    """
    - 🏆 Earn career badges  
    - 👥 Collaborate with industry teams  
    - 💼 Apply to exclusive job postings  
    - 📊 Track your progress in real time  
    """
)

st.header("📖 About Us")
st.write(
    "ScreenerPro is designed to bridge the gap between talented professionals "
    "and hiring companies. Join thousands of users already building their careers."
)

st.header("📬 Contact")
st.write("Have questions? Chat with us using the Tidio bubble below 👇")

# ---------------- Tidio Script ----------------
tidio_script = """
<!-- Start of Tidio Script -->
<script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>

<script>
function onTidioChatApiReady() {
  // Force fixed bubble at bottom-right, always visible
  tidioChatApi.adjustStyles('#tidio-chat-iframe { position: fixed !important; bottom: 20px !important; right: 20px !important; left: auto !important; z-index: 999999 !important; }');
  tidioChatApi.adjustStyles('#tidio { position: fixed !important; bottom: 20px !important; right: 20px !important; left: auto !important; z-index: 999999 !important; }');
}

if (window.tidioChatApi) {
  window.tidioChatApi.on("ready", onTidioChatApiReady);
} else {
  document.addEventListener("tidioChat-ready", onTidioChatApiReady);
}
</script>
<!-- End of Tidio Script -->
"""

# Inject script without taking space
components.html(tidio_script, height=7000, width=0, scrolling=False)
