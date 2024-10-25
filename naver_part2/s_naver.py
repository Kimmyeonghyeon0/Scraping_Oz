from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 입력해주세요 : ")
url = base_url + keyword

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

for i in range(5):
    driver.excute_scrpt("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

result = soup.select(".view_wrap")

for i in result:
    title = i.select_one(".title_link").text
    link = i.select_one(".title_link")['href']
    writer = i.select_one(".name").text
    dsc = i.select_one(".dsc_link").text

    print(f"제목 : {title}")
    print(f"작성자 : {writer}")
    print(f"요약 : {dsc}")
    print(f"링크 : {link}")
    print()

