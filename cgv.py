import requests
from bs4 import BeautifulSoup

def get_movie_chart():
    header_user = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
    req = requests.get(url, headers=header_user)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    movie_chart = soup.select(".sect-movie-chart")


    for i in movie_chart:
        rank = i.select_one(".rank").text.strip() if i.select_one(".rank") else "N/A"
        title = i.select_one(".title").text.strip() if i.select_one(".title") else "N/A"
        percent = i.select_one(".percent").text.strip() if i.select_one(".percent") else "N/A"
        opening = i.select_one(".txt-info").text.strip() if i.select_one(".txt-info") else "N/A"


        print(f'순위 : {rank}')
        print(f'영화 제목 : {title}')
        print(f'예매율 : {percent}')
        print(f'개봉일자 : {opening}')
        print()

        if __name__ == "__main__":
            get_movie_chart()