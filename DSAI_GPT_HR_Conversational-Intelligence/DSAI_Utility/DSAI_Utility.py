
import streamlit as st
from PIL import Image


def CSS_Property(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def All_Initialization():
    image = Image.open('DSAI_Utility/Logo_final.png')
    st.image(image)
    st.markdown("<h1 style='text-align: center; color: #454545; font-size:25px;'>ChatGPT Keeps Human Resources Stay in Compliance</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black; font-size:15px;width:100%;'>ChatGPT Empowers Business with Conversational Intelligence: ChatGPT Identifies, Scores, and Classifies Hate,Insult, Threats, Obscene, and Profanity in a Live Conversation.</h2>",unsafe_allow_html=True)
    st.markdown("""
    <hr style="width:100%;height:3px;background-color:gray;border-width:10">
    """, unsafe_allow_html=True)
    choice1 =  st.sidebar.selectbox(" ",('Home','About Us'))
    choice2 =  st.sidebar.selectbox(" ",('Libraries in Scope','OpenAI','Pandas','Streamlit','OS'))
    choice3 =  st.sidebar.selectbox(" ",('Models Used','ChatGPT(GPT-3.5-turbo)', 'GPT3 - Ada','GPT3 - Babbage','GPT3 - Davinci','GPT3 - Curie'))
    menu = ["Google Cloud Services in Scope","Cloud Storage", "Cloud Run", "Cloud Function", "Secret Manager"]
    choice = st.sidebar.selectbox(" ",menu)
    st.sidebar.write('')
    st.sidebar.write('')
    href = """<form action="#">
    <input type="submit" value="Clear/Reset" />
</form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
    st.sidebar.write('')
    st.sidebar.write('')
    st.sidebar.text('Build & Deployed on')
    st.sidebar.write('')
    st.sidebar.image('DSAI_Utility/Google-Cloud-Platform-GCP-logo.png')
    
    # vAR_clear_button = st.sidebar.button('Clear/Reset')
    # if vAR_clear_button:
    #     st.experimental_rerun()
