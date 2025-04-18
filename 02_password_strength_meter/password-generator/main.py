import re
import random
import string
import streamlit as st

# List of common weak passwords to blacklist
BLACKLISTED_PASSWORDS = ["password123", "123456", "qwerty", "letmein", "admin", "welcome", "12345"]

# Function to generate a random strong password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation  # Adds special characters if selected

    return "".join(random.choice(characters) for _ in range(length))

# Password Strength Check with Custom Weights
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check (weight 1)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check (weight 1)
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check (weight 1)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check (weight 1)
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Custom Strength Rating
    if password in BLACKLISTED_PASSWORDS:
        feedback.append("❌ This is a commonly used password. Choose something unique.")
        score = -1  # Penalize heavily for common passwords
    
    if score == -1:
        feedback.append("❌ Weak Password - Choose a stronger one.")
    elif score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return feedback

# Streamlit UI Setup
st.title("Password Strength Checker and Generator")

# Password Generator
st.header("Generate a Strong Password")
length = st.slider("Select password length:", min_value=8, max_value=32, value=12)
use_digits = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    generated_password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{generated_password}`")

# Password Strength Check
st.header("Check Password Strength")
password = st.text_input("Enter your password to check its strength:")

if password:
    feedback = check_password_strength(password)
    for message in feedback:
        st.write(message)
