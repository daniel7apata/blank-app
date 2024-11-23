import streamlit as st
import requests
from bs4 import BeautifulSoup

# Título de la aplicación
st.title("Web Scrapping")

url_objetivo = st.text_input("Link")

if not url_objetivo:
  st.write("Ingrese link")
else:
  st.write("El link ingresado es: " + url_objetivo)
  respuesta = requests.get(url_objetivo)
  
  if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser') #response.content
  
    elements = soup.find_all()
  
    for i in elements:
      result = i.get_text(strip=True)
      st.write(result)
  else:
      st.write(f'Error al acceder a la página: {respuesta.status_code}')
