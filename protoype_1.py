import streamlit as st

# Set the title of the app
st.title("My First Streamlit App")

# Add a description
st.write("Hello, welcome to my first Streamlit app!")

# Create a simple input field
user_input = st.text_input("Enter your name:")

# Display the input back to the user
if user_input:
    st.write(f"Hello, {user_input}!")
