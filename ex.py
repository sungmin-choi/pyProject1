import requests
from bs4 import BeautifulSoup

page = 1
f = open('test.txt', 'a', -1, 'utf-8')
string = ""
for i in range(3):
    url = 'https://ridibooks.com/category/bestsellers/2200?page='
    get_url = url+str(page)
    get_page = requests.get(get_url)
    soup = BeautifulSoup(get_page.text, 'html.parser')
    title_links = soup.findAll('a', 'title_link')
    detaillink = 'https://ridibooks.com'

    for link in title_links:
        get_detailPage = requests.get(detaillink+link['href'])
        soup2 = BeautifulSoup(get_detailPage.text, 'html.parser')
        title = soup2.find('h3', 'info_title_wrap')
        description = soup2.find('p', 'introduce_paragraph')
        string = string+"제목!!!!:  "+title.text+": \n"

        string = string+description.text
        print(string)
    page += 1


f.write(string)
f.close()
