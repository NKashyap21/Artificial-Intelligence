import streamlit as st
import ollama

def response_generator(messages):
    response = ollama.chat(model="llama2",
                           messages=messages,
                           )
    return response["message"]["content"]

# async def get_response(messages):
#     await response_generator(messages=messages)
    

st.title("llama2 ChatBot")

#Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
#Render all the messages when the app reruns
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#React to User Input
if prompt := st.chat_input("Say Something"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({
            "role":"user",
            "content":prompt,
        })
#Assistant's response
    with st.chat_message("assistant"):
        response = response_generator(messages=st.session_state.messages)
        st.session_state.messages.append({
            "role":"assistant",
            "content":response
        })
        st.write(response)
        
    
    
    