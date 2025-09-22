import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tidio Test", layout="wide")

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

# ---------------- Tidio Embed ----------------
tidio_script = """
<html>
  <head>
    <style>
      body, html { margin:0; padding:0; background:transparent; }
      #tidio-container {
        width: 5px;
        height: 5px;
        position: fixed;
        bottom: 20px;
        right: 20px;
        transition: all 0.3s ease-in-out;
        z-index: 999999;
      }
    </style>
  </head>
  <body>
    <div id="tidio-container"></div>
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <script>
      function onTidioChatApiReady() {
        const container = document.getElementById("tidio-container");
        tidioChatApi.on("open", () => {
          container.style.width = "700px";
          container.style.height = "600px";
        });
        tidioChatApi.on("close", () => {
          container.style.width = "5px";
          container.style.height = "5px";
        });
      }
      if (window.tidioChatApi) {
        window.tidioChatApi.on("ready", onTidioChatApiReady);
      } else {
        document.addEventListener("tidioChat-ready", onTidioChatApiReady);
      }
    </script>
  </body>
</html>
"""

components.html(tidio_script, height=700, width=700, scrolling=False)
