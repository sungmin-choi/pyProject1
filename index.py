import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

driver = webdriver.Chrome('/Users/USER/Documents/chromedriver')

driver.implicitly_wait(3)
driver.get('https://webvpn.tsinghua.edu.cn/login')
driver.find_element_by_name('username').send_keys('2015080075')
driver.find_element_by_name('password').send_keys('csm0306')
# 로그인 버튼을 눌러주자.
login_btn = driver.find_element_by_class_name('el-button-login')
login_btn.click()
time.sleep(1)


get_url = 'https://webvpn.tsinghua.edu.cn/http/77726476706e69737468656265737421e7e056d2262526446d0187ab9040227bb9247e388133/szdw/jsdw1/ayjscz.htm'

driver.get(get_url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

research_title = soup.findAll("div", {"class": "research-name"})
pro_names = soup.findAll(
    "div", {"class": "teach-list"})

for title in research_title:
    print(title.text, end=":")
    for pro_name in pro_names:
        names = pro_name.findAll("div", {"class": "item"})
        for name in names:
            print(name.text, end=",")
