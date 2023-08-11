#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pickle
import streamlit as st
import pandas as pd

# Load the model
classifier = pickle.load(open('classifie1r.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title='Customer Segmentation Web App', layout='centered')
st.title('Customer Segmentation Web App')

# Customer segmentation function
def segment_customers(input_data):
    prediction = classifier.predict(pd.DataFrame(input_data, columns=['Income', 'Kidhome', 'Teenhome', 'Age', 'Partner', 'Education_Level']))
    
    if prediction == 0:
        result = 'Cluster 0: Least Income, Having Partner and Undergraduates'
    elif prediction == 1:
        result = 'Cluster 1: Highest Income, Having Partner, Postgraduates, Few Customers'
    elif prediction == 2:
        result = 'Cluster 2: Max Number of customers, Having Partner, High Income, Postgraduates'
    elif prediction == 3:
        result = 'Cluster 3: Few Customers and less income, graduates and postgraduates, no partner'
    else:
        result = 'Cluster not recognized'
    
    return result

def main():
    Income = st.text_input("Household Income")
    Kidhome = st.radio("Number Of Kids In Household", ('0', '1', '2'))
    Teenhome = st.radio("Number Of Teens In Household", ('0', '1', '2'))
    Age = st.slider("Age", 18, 85)
    Partner = st.radio("Living With Partner?", ('Yes', 'No'))
    Education_Level = st.radio("Education", ("Undergraduate", "Graduate", "Postgraduate"))
    
    input_data = [[Income, Kidhome, Teenhome, Age, Partner, Education_Level]]
    
    if st.button("Segment Customer"):
        result = segment_customers(input_data)
        st.info(result)

if __name__ == '__main__':
    main()


# In[ ]:




