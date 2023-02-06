from pyChatGPT import ChatGPT
import streamlit as vAR_st

def ChatGPT_Response():
    vAR_api = ChatGPT("") #Session token here
    col1,col2,col3,col4,col5 = vAR_st.columns([3,7,1,7,4])
    with col2:
        vAR_st.subheader("Enter Input")
    with col4:    
        vAR_input = vAR_st.text_area('')
    vAR_response = vAR_api.send_message(vAR_input)
    vAR_st.write(vAR_response)
