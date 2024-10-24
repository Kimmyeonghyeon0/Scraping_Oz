#순위 1위부터 100위까지 노래 정보 가져오기
#순위, 노래제목, 가수, 앨범정보
#chatgpt 사용해서 결과를 flask, jinja를 이용해서 화면에 결과 보여주기

import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    header_user = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    url = "https://www.melon.com/chart/index.htm"
    req = requests.get(url, headers=header_user)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    lst50 = soup.select(".lst50")
    lst100 = soup.select(".lst100")
    lst_top_100 = lst50 + lst100

    lst_top_100 = soup.find_all(class_=[lst50, lst100])

    for i in lst_top_100:
        rank = i.select_one(".rank")
        song_title = i.select_one(".ellipsis.rank01 a")
        singer = i.select_one(".ellipsis.rank02 a")
        album = i.select_one(".ellipsis.rank03 a")

        print(f'순위 : {rank}')
        print(f'순위 : {song_title}')
        print(f'순위 : {singer}')
        print(f'순위 : {album}')
        print()