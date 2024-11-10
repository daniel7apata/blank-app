import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)




import requests
from bs4 import BeautifulSoup

base_url = 'https://www.scrapethissite.com/pages/simple/'

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Failed to retrieve {url}")
        return None

def extract_titles(soup):
    titles = []
    if soup:
        product_titles = soup.find_all('span', class_='country-area')
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
    print(f"Fetching page {page}: {url}")
    soup = fetch_page(url)
    titles = extract_titles(soup)
    all_titles.extend(titles)

mayor_poblacion = 0

for cantidad in titles:
  print(cantidad)

mayor_poblacion = max(titles)


st.write(
    f"El país con mayor población tiene: {mayor_poblacion} habitantes"
)
