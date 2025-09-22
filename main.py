import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

tidio_script = """
<html>
  <head>
    <style>
      body, html { margin:0; padding:0; }
      #tidio-container {
        width: 5px;
        height: 5px;
        transition: all 0.3s ease-in-out;
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

# Streamlit inject
components.html(tidio_script, height=700, width=700, scrolling=False)
