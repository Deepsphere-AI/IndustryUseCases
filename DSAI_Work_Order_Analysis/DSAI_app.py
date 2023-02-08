import streamlit as vAR_st
vAR_st.set_page_config(page_title="ChatGPT & GPT3 Apps", layout="wide")

from DSAI_Utility.DSAI_Utility import All_Initialization,CSS_Property
from DSAI_GPT.DSAI_chatgpt import ChatGPT_Response
from DSAI_GPT.DSAI_gpt3 import GPT3Tasks

if __name__=='__main__':
    
    try:
        # Applying CSS properties for web page
        CSS_Property("DSAI_Utility/DSAI_style.css")
        # Initializing Basic Componentes of Web Page
        All_Initialization()


        col1,col2,col3,col4,col5 = vAR_st.columns([2.5,7.5,1.4,9,2])
        with col2:
            vAR_st.write('')
            vAR_st.write('')
            vAR_st.write('')
            vAR_st.write('')
            vAR_st.subheader('Select the Model & API')
        with col4:
            vAR_st.write('')
            vAR_st.write('')
            vAR_option = vAR_st.selectbox('',('Select a Model','GPT-3', 'ChatGPT'))

        if vAR_option=='ChatGPT':
            
            ChatGPT_Response()
        elif vAR_option=='GPT-3':
            
            GPT3Tasks()
        else:
            pass


    except BaseException as exception:
        print('Error in main function - ', exception)
        exception = 'Something went wrong - '+str(exception)
        vAR_st.error(exception)