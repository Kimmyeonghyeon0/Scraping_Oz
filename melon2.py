from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.8)

#이벤트페이지에서 메인페이지로
driver.find_element(By.CSS_SELECTOR, "a.link-logo").click()
time.sleep(0.8)



#멜론차트 
driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)


for i in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

#51위부터 100위까지보기위한 버튼
driver.find_element(By.XPATH, '//button[@onclick="hasMore2();"]').click()
time.sleep(0.3)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
chart_list = soup.select(".list_item")


for index, music in enumerate(chart_list, start=1):
    rank_tag = music.select_one(".ranking_num")
    if rank_tag:
        rank = rank_tag.text.strip()
        title = music.select_one(".title.ellipsis").text.strip()
        artist = music.select_one(".name.ellipsis").text.strip()
            

        print(f"[순위] : {rank}")
        print(f"[노래 제목] : {title}")
        print(f"[가수 이름] : {artist}")
        print()

#아래 순서대로 스크래핑한 자료를 출력해주세요
#순위 :
#노래 제목 :
#가수 이름 :

driver.quit()