import datetime
import requests # 요청을 보내고 응답을 받아오는 역할
from bs4 import BeautifulSoup #데이터를 구조화 (예쁘게!)


url = 'https://finance.naver.com/marketindex/' #데이터를 추출할 url확인


response = requests.get(url).text

soup = beautifulsoup(response, 'html.parser')
# print(type(soup))

#원하는 데이터 추출하기
text = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(text)