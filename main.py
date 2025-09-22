import streamlit as st
st.components.v1.html(
    """
    <html>
      <body>
        <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
        <script>
        function onTidioChatApiReady() {
            tidioChatApi.adjustStyles('#tidio { left: 20px !important; right: auto !important; bottom: 20px !important; position: fixed !important; z-index: 999999 !important;}');
        }
        if (window.tidioChatApi) {
            window.tidioChatApi.on('ready', onTidioChatApiReady);
        } else {
            document.addEventListener('tidioChat-ready', onTidioChatApiReady);
        }
        </script>
      </body>
    </html>
    """,
    height=0,  # hide the iframe
    width=0,
)
