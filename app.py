import streamlit as st

# Page config
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀",
    layout="centered"
)

# Title
st.title("🚀 Welcome to My Streamlit Application")

# Subtitle
st.subheader("Hosted using Streamlit Cloud")

# Text
st.write("""
This is a simple Streamlit app.
You can customize it with forms, charts, images, and more.
""")

# Input box
name = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    if name:
        st.success(f"Hello {name}! 👋 Welcome to Streamlit.")
    else:
        st.warning("Please enter your name.")

# Slider
age = st.slider("Select your age:", 1, 100, 18)
st.write(f"Your age is: **{age}**")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")