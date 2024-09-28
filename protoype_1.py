import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Header
st.title("Top-Class Streamlit App")
st.markdown("Welcome to our interactive data visualization app!")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "Data Visualization", "About"])

# Home Page
if page == "Home":
    st.subheader("Home")
    st.write("This app showcases various data visualizations.")

# Data Visualization Page
elif page == "Data Visualization":
    st.subheader("Data Visualization")
    # Sample data
    data = pd.DataFrame({
        'x': np.linspace(0, 10, 100),
        'y': np.sin(np.linspace(0, 10, 100))
    })
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'])
    st.pyplot(fig)

# About Page
elif page == "About":
    st.subheader("About")
    st.write("This app was created to demonstrate the capabilities of Streamlit.")
    
# Footer
st.markdown("---")
st.markdown("© 2024 Your Name. All rights reserved.")
