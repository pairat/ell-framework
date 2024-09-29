import streamlit as st

# Title of the app
st.title("Welcome to My Streamlit App")

# Write a simple text
st.write("This is a basic example of a Streamlit app.")

# Example interactive widget
user_input = st.text_input("Enter some text:")

# Display the input from the user
if user_input:
    st.write(f"You entered: {user_input}")

# Example of a button
if st.button("Click me"):
    st.write("Button clicked!")
