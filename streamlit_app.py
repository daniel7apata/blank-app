import streamlit as st
import requests
from bs4 import BeautifulSoup

# Título de la aplicación
st.title("Web Scrapping")

url_objetivo = st.text_input("Link")
st.write("El link ingresado es: " + url_objetivo)
