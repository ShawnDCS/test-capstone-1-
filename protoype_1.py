import streamlit as st
import time

# Header
st.title("Top-Class Streamlit App")
st.markdown("Welcome to our interactive data visualization app!")

# Add a loading animation
with st.spinner("Loading..."):
    time.sleep(1)  # Simulate loading time

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "About"])

# Add a background image
st.markdown("<style>body { background-image: url('https://images.unsplash.com/photo-1611162616471-5c3a7f6b6a5c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max'); background-size: cover; }</style>", unsafe_allow_html=True)

# Home Page
if page == "Home":
    st.subheader("Home")
    st.write("This app showcases various data visualizations.")
    st.image("https://images.unsplash.com/photo-1611162616471-5c3a7f6b6a5c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max", use_column_width=True)

# About Page
elif page == "About":
    st.subheader("About")
    st.write("This app was created to demonstrate the capabilities of Streamlit.")
    st.image("https://images.unsplash.com/photo-1611162616471-5c3a7f6b6a5c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max", use_column_width=True)

# Footer
st.markdown("---")
st.markdown("© 2024 Your Name. All rights reserved.")
st.write("Made with ❤️ using Streamlit")
