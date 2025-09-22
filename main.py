import streamlit as st
import streamlit.components.v1 as components
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

st.set_page_config(page_title="ScreenerPro with Watson")
# ✅ Inject Tidio Chat properly (no iframe height/width restriction)
components.html(
    """
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <style>
      iframe[title="Tidio Chat"] {
        left: 20px !important;
        right: auto !important;
        bottom: 20px !important;
        position: fixed !important;
        z-index: 999999 !important;
      }
    </style>
    """,
    height=600,   # <- no visible box
    width=700,    # <- no visible box
)
st.title(" ScreenerPro with Watson Assistant")
st.markdown(
    """
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    """,
    unsafe_allow_html=True
)
st.title(" ScreenerPro with Watson Assistant")
st.title(" ScreenerPro with Watson Assistant")
st.title(" ScreenerPro with Watson Assistant")
st.title(" ScreenerPro with Watson Assistant")
components.html("""
<!DOCTYPE html>
<html>
  <head></head>
  <body style="margin:0; padding:0;">
    <div id="watson-chat" style="width:100%; height:600px;"></div>

    <script>
      window.watsonAssistantChatOptions = {
        integrationID: "49156221-4969-48c2-8924-fd0b623c2f33",
        region: "au-syd",
        serviceInstanceID: "bf63ba6f-d81c-4de9-9e39-645fd55f6cbb",
        onLoad: async (instance) => { 
          await instance.render(); 
        }
      };
      setTimeout(function(){
        const t=document.createElement('script');
        t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + 
               (window.watsonAssistantChatOptions.clientVersion || 'latest') + 
               "/WatsonAssistantChatEntry.js";
        document.head.appendChild(t);
      });
    </script>
  </body>
</html>
""", height=650, width=900)
