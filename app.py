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


pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)



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
    Volume = st.text_input("Volume")
    Open = st.text_input("Open")
    High = st.text_input("High")
    Low = st.text_input("Low")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Volume, Open, High, Low)
    st.success('The output is {}'.format(result))
    
if __name__=='__main__':
    main()