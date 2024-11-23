import streamlit as st
import requests
from bs4 import BeautifulSoup

# Título de la aplicación
st.title("Web Scrapping")

url_objetivo = st.text_input("Link")

if not url_objetivo:
  st.write("Ingrese link")
else:
  def fetch_page(url_objetivo):
      response = requests.get(url)
      if response.status_code == 200:
          return BeautifulSoup(response.content, 'html.parser')
      else:
          print(f"Failed to retrieve {url}")
          return None
  
  def extract_titles(soup):
      titles = []
      if soup:
          product_titles = soup.find_all()
          for title in product_titles:
              titles.append(title.get_text(strip=True))
      return titles
  
  num_pages = 2
  
  all_titles = []
  
  for page in range(1, num_pages + 1):
      if page == 1:
          url = base_url
      else:
          url = f"{base_url}?page={page}"
      st.write(f"Fetching page {page}: {url}")
      soup = fetch_page(url)
      titles = extract_titles(soup)
      all_titles.extend(titles)
  
  for idx, title in enumerate(all_titles, start=1):
      st.write(f"{idx}. {title}")
