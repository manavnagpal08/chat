import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro with Watson")

st.title("💬 ScreenerPro with Watson Assistant")

# Full HTML wrapper for Watson script
components.html("""
<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <script>
      window.watsonAssistantChatOptions = {
        integrationID: "49156221-4969-48c2-8924-fd0b623c2f33", // your integration ID
        region: "au-syd", // your region
        serviceInstanceID: "bf63ba6f-d81c-4de9-9e39-645fd55f6cbb", // your instance ID
        onLoad: async (instance) => { await instance.render(); }
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
""", height=0, width=0)
