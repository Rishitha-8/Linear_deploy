# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 08:21:20 2021

@author: NiruSai
"""
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import os
import inspect

pickle_in=open("classifier.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return "Welcome All"


def predict_stock(Volume, Open, High, Low):
    prediction=model.predict([[Volume, Open, High, Low]])
    print(prediction)
    return prediction


def main():
    st.title("STOCK PREDICTION USING LINEAR REGRESSION ")
    html_temp = """
    <div style="background-color:pink;padding:10px">
    <h2 style="color:black;text-align:center;">Stock Prediction Using Streamlit </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Volume = st.text_input("Volume")
    Open = st.text_input("Open")
    High = st.text_input("High")
    Low = st.text_input("Low")
    result=""
    if st.button("Predict"):
        result=predict_stock(Volume, Open, High, Low)
    st.success('The output is {}'.format(result))
    radio = st.radio(label="", options=["Yes", "No"])
    if radio == "Yes":
        st.write("import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import os
import inspect
pickle_in=open("classifier.pkl","rb")
model=pickle.load(pickle_in)
def welcome():
    return "Welcome All"
def predict_stock(Volume, Open, High, Low):
    prediction=model.predict([[Volume, Open, High, Low]])
    print(prediction)
    return prediction
def main():
    st.title("STOCK PREDICTION USING LINEAR REGRESSION ")
    html_temp = """
    <div style="background-color:pink;padding:10px">
    <h2 style="color:black;text-align:center;">Stock Prediction Using Streamlit </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Volume = st.text_input("Volume")
    Open = st.text_input("Open")
    High = st.text_input("High")
    Low = st.text_input("Low")
    result=""
    if st.button("Predict"):
        result=predict_stock(Volume, Open, High, Low)
    st.success('The output is {}'.format(result))")
     
    
if __name__=='__main__':
    main()

