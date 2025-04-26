import streamlit as st
import re
import string
import secrets

def check_strength(pwd):
    score = sum([
        len(pwd) >= 8,
        bool(re.search(r"[A-Z]", pwd)),
        bool(re.search(r"[a-z]", pwd)),
        bool(re.search(r"[0-9]", pwd)),
        bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd)),
    ])
    strength = ["Weak", "Moderate", "Strong"][min(score // 2, 2)]
    color = ["#FF5555", "#FFD700", "#00FF7F"][min(score // 2, 2)]
    return score, strength, color

def generate_pwd(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    st.title("🔒 Password Tool")
    tab1, tab2 = st.tabs(["Check Password", "Generate Password"])
    
    with tab1:
        pwd = st.text_input("Enter Password", type="password")
        if pwd:
            score, strength, color = check_strength(pwd)
            st.progress(score / 5)
            st.markdown(f"**Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
    
    with tab2:
        length = st.slider("Length", 8, 32, 12)
        if st.button("Generate Password"):
            st.code(generate_pwd(length))

if __name__ == "__main__":
    main()
