import streamlit as st
import pyshorteners as pyst

st.markdown("<h1 style='text-align: center;'>URL Shortener</h1>", unsafe_allow_html=True)
form = st.form("name")
url =  form.text_input("URL Here")
s_btn = form.form_submit_button("Short")

shortener = pyst.Shortener()
if s_btn:
    shorted_url = shortener.tinyurl.short(url)
    print(shorted_url)