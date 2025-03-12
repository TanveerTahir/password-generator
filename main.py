import streamlit as st
import random
import string


def generate_password(Length, use_digits, use_special):
    characters = string.ascii_letters # include letters (A-Z and a-z) by default

    if use_digits:
        characters += string.digits #  include numbers (0-9) if selected
        
    if use_special:
        characters += string.punctuation # Add special characters (!, @, #, etc.)

    return ''.join(random.choice(characters) for _ in range(Length))

st.title("Password Generator")

Length = st.slider("Select Length of password", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

# use_letters = st.checkbox("Use Letters")

if st.button("Generate Password"):
    password = generate_password(Length, use_digits, use_special)
    st.write(f"Generated password: `{password}`")