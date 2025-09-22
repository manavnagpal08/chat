import streamlit as st
from component_html import tidio_chatbot_component

# Call the custom component at the start of your script
tidio_chatbot_component()

# Your normal Streamlit app content goes here
st.title("My Streamlit App")
st.write("Scroll down to see that the Tidio widget stays in place.")
st.header("Some App Content")
st.write("This is some content to make the page long enough to scroll.")
st.text("." * 1000)
