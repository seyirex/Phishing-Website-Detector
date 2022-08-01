import streamlit as st
import pickle
import time
import pandas as pd
import plotly.express as px
import pickle
from utils import *


def main():
    # page info setup
    menu_items = {
        'Get help':'https://www.linkedin.com/in/oluwaseyi-gbadamosi-41015216b/' ,
        'Report a bug': 'https://www.linkedin.com/in/oluwaseyi-gbadamosi-41015216b/',
        'About': '''
        ## My Custom App

        Some markdown to show in the About dialog.
        '''
    }
    st.set_page_config(page_title="Phishing Website Detector", page_icon="./images/favicon.png", layout='centered',menu_items=menu_items)
    st.set_option('deprecation.showfileUploaderEncoding', False)
    # Frontend
    start = time.time()
    loaded_model= load_model()
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Site Title
    st.markdown("<h1 style = 'color:Gold; Text-align: Center; font-size: 30px;'>Phishing Website Detection </h1>", unsafe_allow_html=True)
    # creating tabs for navigation
    
    st.markdown("<p>Phishing is one of the major problems faced by cyber-world and leads to financial losses for both industries and individuals.Detection of phishing attack with high accuracy has always been a challenging issue. One of the effective way of checkingif a website/url is legitimate, or a scam is by checking its url.This detector uses an ML model to check if the given url is legitimate.</p>",unsafe_allow_html=True)
    # Form for the Url input
    with st.form(key='my_form'):
        url = st.text_input(label='Enter URL of The Site')
        submit_button = st.form_submit_button(label='Check Url')

    if submit_button:
        df = pd.DataFrame(featureExtraction(url), index=[0])
        
        with st.spinner('The AI model is checking the Url ⏳⏳⏳⏳'):
            time.sleep(2)
        prediction = loaded_model.predict_proba(df)
        prediction_label = loaded_model.predict(df)
        st.text("")
        st.text("Dataframe showing the features extracted")
        st.dataframe(df)
        st.text("")
    
        if(prediction_label[0] == 0):
            st.success("This is legitimate URL, you are safe to proceed")
        else:
            st.warning("This is phishing URL, you are NOT safe to proceed")
        
        end5 = time.time()
        st.subheader("Time Taken for Prediction")
        st.write(f"This check costed you {round(end5-start,2)} seconds of your precious time.")
            
        fig = px.pie(prediction, values=prediction[0][:], names=[
                    "Legitimate URL", "Phishing URL"]
                    , title='Phishing Website Detection percentage for both label') 
                    
        st.plotly_chart(fig)
    
    with st.expander("Video resources"):
        st.write("Video resources are used to explain how to prevent being a victim of phishing attacks.")
        col1, col2= st.columns(2)
        with col1:
            st.header("Resources 1")
            st.video("https://www.youtube.com/watch?v=zflsg6TRuos")

        with col2:
            st.header("Resources 2")
            st.video("https://youtu.be/LrFarFrzbD4")


if __name__ == '__main__':
    main()