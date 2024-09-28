import streamlit as st
import time

# Header
st.title("Stroke Prediction Website")
st.markdown("Welcome to our stroke prediction website !")

# Add a loading animation
with st.spinner("Loading..."):
    time.sleep(1)  # Simulate loading time

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "About"])

# Add a background image
# Set background color to dark red
st.markdown(
    "<style>body { background-color: #8B0000; }</style>", 
    unsafe_allow_html=True
)

# Home Page
if page == "Home":
    st.subheader("Home")
    st.write("Please enter your details in order for use to predict the chances of you having a stroke hahaha.")
    
# About Page
elif page == "About":
    st.subheader("About")
    st.write("This app was created to show the capabilities of me hahaha .")
   

# Footer
st.markdown("---")
st.markdown("© 2024 Your Name. All rights reserved.")
st.write("Made with ❤️ using Streamlit")
