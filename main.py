import streamlit as st

st.set_page_config(page_title="ScreenerPro with Watson")

st.title("💬 ScreenerPro with Watson Assistant")

# Use markdown so Watson attaches globally (not inside iframe)
st.markdown("""
<script>
  window.watsonAssistantChatOptions = {
    integrationID: "49156221-4969-48c2-8924-fd0b623c2f33",
    region: "au-syd",
    serviceInstanceID: "bf63ba6f-d81c-4de9-9e39-645fd55f6cbb",
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
