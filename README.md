# PROJECT DOCUMENTATION
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/seyirex/phishing-website-detector/main/app.py) Webapp link
## Introduction
Phishing is a form of cybercrime in which a target is contacted via email, telephone, or text message by an attacker disguising as a reputable entity or person. The attacker then lures individuals to counterfeit websites to trick recipients into providing sensitive data. According to the FBI, phishing incidents nearly doubled in frequency, from 114,702 incidents in 2019, to 241,324 incidents in 2020.
As the internet becomes a major mode for economic transactions and communications, online trust and cybercrimes have increasingly become an important area of study. The purpose of this project is to help individuals identify phishing URLs in order to provide safer practices online using machine learning techniques. The deployment of the Streamlit application allows users to verify the authenticity of URLs themselves.

## Approach 
1. Data collection          
2. Data Preprocessing           
3. Feature Extraction         
4. Modeling
5. Deployment

## Data Collection 
Legitimate URLs are collected from the dataset provided by University of New Brunswick, From the collection, 5000 URLs are randomly picked. Phishing URLs are collected from opensource service called PhishTank. This service provides a set of phishing URLs in multiple formats like csv, json etc. that gets updated hourly. From the obtained phishing collection, 5000 URLs are randomly picked. model deployment seemed to have its own pitfalls. Simple websites such as www.google.com were classified as phishing. When taking a closer look at our dataset, it was evident that legitimate URL samples did not include short, simple URLs.

## Data preprocessing 
Data cleaning included dropping null values (URLs that did not distinguish if legitimate or phishing), dropping unnecessary columns, changing dtypes, and adding a protocol to URLs without one. 

## Feature Extraction 
The following category of features was extracted: Address Bar based Features, Domain based Features
HTML & Javascript based Feature. All together 17 features are extracted from the dataset.
- Address Bar based Features considered are:
•	Domian of URL	•	Redirection ‘//’ in URL
•	IP Address in URL	•	‘http/https’ in Domain name
•	‘@’ Symbol in URL	•	Using URL Shortening Service
•	Length of URL	•	Prefix or Suffix "-" in Domain
•	Depth of URL	
- Domain based Features considered are:
•	DNS Record	•	Age of Domain
•	Website Traffic	•	End Period of Domain
- HTML and JavaScript based Features considered are:
•	Iframe Redirection	•	Disabling Right Click
•	Status Bar Customization	•	Website Forwarding

## Model Training & Evaluation 
This is a supervised machine learning task. There are two major types of supervised machine learning problems, called classification and regression. This data set comes under classification problem, as the input URL is classified as phishing (1) or legitimate (0). The machine learning models (classification) considered to train the dataset in this notebook are:
•	Random Forest
•	XGBoost
•	Support Vector Machines
The models are evaluated, and the considered metric is accuracy. Below Figure shows the training and test dataset accuracy by the respective models:
 
## Model Deployment 
Finally, the model is deployed through a Streamlit application. The application is designed for any individual to enter a URL, press a button, and the model will predict if the URL is a phishing or legitimate URL.

## Conclusion
Phishing threats are continuously evolving to become more complex. As a result, more users across the globe are falling victim to these attacks. Phishing awareness and detection becomes an increasingly important area of study and users should be conscious of their online practices. Ultimately, this project was successful in crafting a model that performs well above the baseline when predicting whether a URL is legitimate or phishing. In order to ensure safe practices online, users should treat every email with skepticism and never click on a link without examining it first. With the addition of 'Fishing for Phishers' application, users can utilize this tool to take responsibility in verifying URLs.
