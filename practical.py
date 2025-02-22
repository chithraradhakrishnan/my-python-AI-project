import streamlit as st

st.title("Hello  from upcode")

name = st.text_input("Enter your name:")

if st.button("say hello"):
    st.write(f"Hello {name},WELCOME TO UPCODE")
    



