from dotenv import load_dotenv
from openai import OpenAI

import streamlit as st

load_dotenv()  
client = OpenAI()
initial_messages = [
       {"role": "system", "content": "You are a trip planner to Dubai.You are an expert in Dubai tourism ,location,food,events,hotel,etc. You are able to guide users plan their vacation to Dubai.You should respond  professionaly.Your name is Dubai Genie,short name DG. Response shouldn't exceed  200  less words. Always ask questions to user and help them to plan the trip.Finally give a day vise itinarary. Deal with user professionally."},
        {
            "role": "assistant",
            "content": "Hello, I am Dubai Genie,your expert trip planner.How can I help you?."
        }
    ]
# function to get  respose from OpenAI llm
def get_response_from_llm(messages):
  
    completion = client.chat.completions.create (
      
        model="gpt-4o-mini", 
        messages= messages
    )
    return completion .choices[0].message.content 
if "message" not in st.session_state:
    st.session_state.messages = initial_messages
st.title("Dubai Trip Assistant App")
   
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message ["role"]):
            st.markdown(message["content"])
      
user_message=st.chat_input("Enter your ")
if user_message:
    new_message = {
        "role":"user",
        "content": user_message
   
    }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message ["role"]):
        st.markdown(new_message["content"])

    response = get_response_from_llm(st.session_state.messages)
    if response:
        response_message={
               "role":"assistant",
               "content": response
              
        }
           
        st.session_state.messages.append(response_message)     
        with st.chat_message (response_message ["role"]):
            st.markdown(response_message["content"])

















