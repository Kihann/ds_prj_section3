import requests
from bs4 import BeautifulSoup

URL = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(URL)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
rank1 = soup.find('li', attrs={'class':'rank01'})
#print(rank1.a.get_text())
# rank2 = rank1.find_next_sibling('li')
# rank3 = rank2.find_next_sibling('li')
# rank1_1 = rank2.find_previous_sibling('li')
# print(rank1.find_next_siblings('li'))
webtoon = soup.find('a', text = '독립일기')
print(webtoon)