import streamlit as st

# Header
st.title("Top-Class Streamlit App")
st.markdown("Welcome to our interactive data visualization app!")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "About"])

# Home Page
if page == "Home":
    st.subheader("Home")
    st.write("This app showcases various data visualizations.")

# About Page
elif page == "About":
    st.subheader("About")
    st.write("This app was created to demonstrate the capabilities of Streamlit.")
    
# Footer
st.markdown("---")
st.markdown("© 2024 Your Name. All rights reserved.")
