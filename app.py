import streamlit as st
import pickle
import time
import pandas as pd
import plotly.express as px
import pickle
from utils import *


start = time.time()
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

@st.cache(allow_output_mutation=True)# load model from file
def load_model():
	model = pickle.load(open("./Model/XGBoostClassifier.pickle.dat", "rb"))
	return model
loaded_model = load_model()# intalizing the model function

# Frontend
def main():
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Site Title
    st.markdown("<h1 style = 'color:Gold; Text-align: Center; font-size: 40px;'>Phishing Website Detection </h1>", unsafe_allow_html=True)
    st.markdown("<p>Phishing is one of the major problems faced by cyber-world and leads to financial losses for both industries and individuals.Detection of phishing attack with high accuracy has always been a challenging issue. One of the effective way of checkingif a website/url is legitimate, or a scam is by checking its url.This detector uses an ML model to check if the given url is legitimate.</p>",unsafe_allow_html=True)
    # Form for the Url input
    with st.form(key='my_form'):
        url = st.text_input(label='Enter URL of The Site')
        submit_button = st.form_submit_button(label='Check Url')
    
    with st.spinner('The AI model is checking the Url ⏳⏳⏳⏳'):
            time.sleep(5)
    #
    if submit_button:
        df = pd.DataFrame(featureExtraction(url), index=[0])
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
   
if __name__=='__main__':
    main()
    
       
       
       
