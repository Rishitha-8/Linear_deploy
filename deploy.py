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


classifier=pickle.load(open(r'C:\Users\NiruSai\Stock-price-prediction-TeamB-main\classifier.pkl','rb'))

def welcome():
    return "Welcome All"


def predict_note_authentication(Volume, Open, High, Low):
    prediction=classifier.predict([[Volume, Open, High, Low]])
    print(prediction)
    return prediction


def main():
    st.title("stock prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit stock prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Volume = st.text_input("volume","Type Here")
    Open = st.text_input("open","Type Here")
    High = st.text_input("high","Type Here")
    Low = st.text_input("low","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Volume, Open, High, Low)
    st.success('The output is {}'.format(result))
    
if __name__=='__main__':
    main()