import streamlit as st
import pyshorteners as pyst

st.markdown("<h1 style='text-align: center;'>URL Shortener</h1>", unsafe_allow_html=True)
form = st.form("name")
url =  form.text_input("URL Here")
s_btn = form.form_submit_button("Short")
shortener = pyst.Shortener()

try:
    if s_btn:
        shorted_url = shortener.tinyurl.short(url)
        st.markdown("<h3>Shorted URL</h3>", unsafe_allow_html=True)
        st.markdown(f"<h6 style='text-align: center;'>{shorted_url}</h6>", unsafe_allow_html=True)

except:
    st.warning('Please enter a valid URL', icon="⚠️")