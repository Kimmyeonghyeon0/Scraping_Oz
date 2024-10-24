import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 입력해주세요 : ")

url = base_url + keyword
print(url)
req = requests.get(url)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap") #30개

for i in results:
    if not i.select_one(".link_ad"):
        title = i.select_one(".title_link").text
        link = i.select_one(".title_link")['href']
        writer = i.select_one(".name").text
        dsc = i.select_one(".dsc_link").text

        print(f"제목 : {title}")
        print(f"작성자 : {writer}")
        print(f"링크 : {link}")
        print(f"요약 : {dsc}")
        print()
