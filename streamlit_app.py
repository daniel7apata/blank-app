import requests
from bs4 import BeautifulSoup

# Título de la aplicación
st.title("Web Scrapping")

url_objetivo = st.text_input("Link")
