import streamlit as st

st.set_page_config(page_title="ScreenerPro with Watson")

st.title("💬 ScreenerPro with Watson Assistant")

# Inject Watson Web Chat
st.markdown("""
<script>
  window.watsonAssistantChatOptions = {
    integrationID: "49156221-4969-48c2-8924-fd0b623c2f33", // The ID of this integration.
    region: "au-syd", // The region your integration is hosted in.
    serviceInstanceID: "bf63ba6f-d81c-4de9-9e39-645fd55f6cbb", // The ID of your service instance.
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
""", unsafe_allow_html=True)
