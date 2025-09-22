import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro with Watson")

st.title("💬 ScreenerPro with Watson Assistant (Embedded)")

# Embed the Watson chat UI directly
components.html("""
<!DOCTYPE html>
<html>
  <head></head>
  <body style="margin:0; padding:0;">
    <iframe 
      src="https://web-chat.global.assistant.watson.appdomain.cloud/preview.html?integrationID=49156221-4969-48c2-8924-fd0b623c2f33&region=au-syd&serviceInstanceID=bf63ba6f-d81c-4de9-9e39-645fd55f6cbb"
      style="width:100%; height:600px; border:none;">
    </iframe>
  </body>
</html>
""", height=650, width=800)
