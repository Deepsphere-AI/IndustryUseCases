import streamlit as vAR_st
vAR_st.set_page_config(page_title="ChatGPT & GPT3 Apps", layout="wide")

from DSAI_Utility.DSAI_Utility import All_Initialization,CSS_Property
from DSAI_GPT.DSAI_chatgpt import WorkOrder_ChatGPT_Response
from DSAI_GPT.DSAI_gpt3 import GPT3Tasks

if __name__=='__main__':
    vAR_hide_footer = """<style>
            footer {visibility: hidden;}
            </style>
            """
    vAR_st.markdown(vAR_hide_footer, unsafe_allow_html=True)
    
    try:
        # Applying CSS properties for web page
        CSS_Property("DSAI_Utility/DSAI_style.css")
        # Initializing Basic Componentes of Web Page
        All_Initialization()


        col1,col2,col3,col4,col5 = vAR_st.columns([1.2,9,0.8,9,2])
        with col2:
            vAR_st.subheader('Select the Model & API')
        with col4:
            vAR_st.write('')
            vAR_st.write('')
            vAR_model_option = vAR_st.selectbox('',('Select a Model','GPT-3', 'ChatGPT'))

        
        col1,col2,col3,col4,col5 = vAR_st.columns([1.2,9,0.8,9,2])
        with col2:
            vAR_st.subheader("Select Application Function")
        with col4:    
            vAR_st.write('')
            vAR_st.write('')
            vAR_option = vAR_st.selectbox('',('Select an Application Function','Work Order Analysis','Generate Interview Questions', 'English to Other Languages','Keyword Extraction','Essay Outline','Text Summarization','Chat','Chat DMV','SQL Translate','Classification','Factual Answering','Spreadsheet Creator','SQL Request','Analogy Maker'))

        if vAR_model_option=='ChatGPT' and vAR_option=='Work Order Analysis':
            
            WorkOrder_ChatGPT_Response()
        elif vAR_model_option=='GPT-3':
            
            GPT3Tasks(vAR_option)
        
        elif vAR_model_option=='ChatGPT' and vAR_option!='Work Order Analysis' and vAR_option!='Select an Application Function':
            col1,col2,col3 = vAR_st.columns([2,17,4])
            with col4:
                vAR_st.write('')
                vAR_st.write('')
                vAR_st.write('')
                vAR_st.info("Development in-progress")
        elif vAR_model_option=='ChatGPT' and vAR_option!='Work Order Analysis':
            
            GPT3Tasks(vAR_option)
        else:
            pass


    except BaseException as exception:
        print('Error in main function - ', exception)
        exception = 'Something went wrong - '+str(exception)
        vAR_st.error(exception)
