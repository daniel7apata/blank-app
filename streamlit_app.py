import streamlit as st
import requests
from bs4 import BeautifulSoup

# Título de la aplicación
st.title("Web Scrapping")

base_url = st.text_input("Link")

if not base_url:
  st.write("Ingrese link")
else:
  def fetch_page(base_url):
      response = requests.get(base_url)
      if response.status_code == 200:
          return BeautifulSoup(response.content, 'html.parser')
      else:
          print(f"Failed to retrieve {url}")
          return None
  
  def extract_titles(soup):
      titles = ""
      if soup:
          product_titles = soup.find_all()
          for title in product_titles:
              titles += title.get_text(strip=True) + "      "
      return titles
  
  num_pages = 1
  
  all_titles = []
  
  for page in range(1, num_pages + 1):
      if page == 1:
          url = base_url
      else:
          url = f"{base_url}?page={page}"
      st.write(f"Fetching page {page}: {url}")
      soup = fetch_page(url)
      titles = extract_titles(soup)
      st.write(titles)
