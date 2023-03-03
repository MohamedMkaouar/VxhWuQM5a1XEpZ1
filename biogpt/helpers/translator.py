from deep_translator import GoogleTranslator
from deep_translator import exceptions as excp
from langdetect import detect

import streamlit as st

def translate(text,source='auto', target= "en"):
    try:
        text = GoogleTranslator(source=source, target=target).translate(text)
    except (excp.NotValidPayload, excp.NotValidLength) as e:
        text = ""
    return text

def detect_language(text):
    try:
        lang = detect(text)
    except:
        lang = "en"
    return lang

def read_text(free_text_name,sidebar = True,target = "en"):
    if sidebar == True:
        text = st.sidebar.text_area(free_text_name,"")
    else:
        text = st.text_area(free_text_name,"")
    
    return translate(text,'auto',target),detect_language(text)


