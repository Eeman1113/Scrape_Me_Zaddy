from bs4 import BeautifulSoup
import requests
import streamlit as st


def scrape_me(url,tag,class_,name):
    url=url
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    code_element = soup.find(tag, class_=class_)
    code = code_element.text.strip()
    
    f = open(f"./subbmition/{name}.txt", "w")
    f.write(code)
    f.close()
    st.write(code)

st.markdown("<h1 style='text-align: center; '>Scrape Me Up Zaddy 擦</h1>", unsafe_allow_html=True)

with st.form("my_form"):
    Url = st.text_input("Enter URL")
    Tag = st.text_input("Enter Tag")
    Class_ = st.text_input("Enter Class")
    Name = st.text_input("Enter Name")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        scrape_me(Url,Tag,Class_,Name)