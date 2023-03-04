import streamlit as st

import pickle

from transformers import BioGptTokenizer, BioGptForCausalLM
from transformers import pipeline

from helpers.hide_toolbar import hide_toolbars
from helpers.translator import read_text,detect_language,translate

def load_generator():
    model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
    tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
    return generator

generator = load_generator()

# res = generator("COVID-19 is", max_length=100, num_return_sequences=1, do_sample=True)

st.sidebar.write("""## Fill the form with medical information to complete""")
health_text_input,lang = read_text("Text",sidebar = True)

res = generator(health_text_input, max_length=1000, num_return_sequences=1, do_sample=True)
res = ' '.join(res[0]["generated_text"].split())
res = translate(res,source='en',target=lang)

st.title("RECO") 
st.write(res)