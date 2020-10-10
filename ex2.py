import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/bestsellers/2200?page=1'
get_page = requests.get(url)
soup = BeautifulSoup(get_page.text, 'html.parser')
