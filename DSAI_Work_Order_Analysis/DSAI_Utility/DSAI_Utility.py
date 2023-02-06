
import streamlit as st
from PIL import Image


def CSS_Property(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def All_Initialization():
    image = Image.open('Logo_final.png')
    st.image(image)
    st.markdown("<h1 style='text-align: center; color: #454545; font-size:30px;'>Learn to Develop ChatGPT Applications</h1><h2 style='text-align: center; color: blue; font-size:25px;'>ChatGPT Simplifies Work Order Analysis</h2>", unsafe_allow_html=True)
    st.markdown("""
    <hr style="width:100%;height:3px;background-color:gray;border-width:10">
    """, unsafe_allow_html=True)
    choice1 =  st.sidebar.selectbox(" ",('Home','About Us'))
    choice2 =  st.sidebar.selectbox(" ",('Libraries in Scope','OpenAI','pyChatGPT','Pandas','Streamlit'))
    choice3 =  st.sidebar.selectbox(" ",('Models Used','ChatGPT', 'GPT3', 'GPT3 - Ada','GPT3 - Babbage','GPT3 - Davinci'))
    menu = ["Google Cloud Services in Scope","Cloud Storage", "Cloud Run", "Cloud Function", "Secret Manager"]
    choice = st.sidebar.selectbox(" ",menu)
    st.sidebar.write('')
    st.sidebar.write('')
    href = """<form action="#">
    <input type="submit" value="Clear/Reset" />
</form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
    
    # vAR_clear_button = st.sidebar.button('Clear/Reset')
    # if vAR_clear_button:
    #     st.experimental_rerun()
