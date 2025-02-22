import streamlit as st

st.title("Chat windows")

with st.chat_message("assistant"):

 st.markdown("Hello, I am AI Assistant")

with st.chat_message("human"):
 st.markdown("i am planning vacation to dubai")
 
message=st.chat_input("Enter your ")

if message:
    with st.chat_message('human'):
         st.markdown(message)
 

