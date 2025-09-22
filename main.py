import streamlit as st
import streamlit.components.v1 as components

# Set up your Streamlit app layout
st.title("My Streamlit App with Tidio Chatbot")
st.write("Welcome to my app. You can find support using the chatbot in the corner!")

# Your existing Streamlit code goes here
st.header("App Content")
st.write("This is where the main content of your application would be.")
st.write("For example, a data dashboard, a user form, or any other interactive elements.")

# Paste your Tidio JavaScript code into the html() function
# Replace 'your_unique_public_key.js' with the actual key from your Tidio account
tidio_script = """
    <!-- Start of Tidio Script -->
    <script src="//code.tidio.co/c19vp8j19zbvdpbrizjxmw1apt8buoie.js" async></script>
    <!-- End of Tidio Script -->
"""

# Embed the HTML component
components.html(tidio_script, height=600)

