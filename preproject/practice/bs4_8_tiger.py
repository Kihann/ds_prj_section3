import requests
from bs4 import BeautifulSoup

URL = 'https://comic.naver.com/webtoon/list?titleId=650305'
res = requests.get(URL)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# cartoons = soup.find_all('td', attrs={'class':'title'})
# title = cartoons[1].get_text()
# link = cartoons[1].a['href']
# print(title.strip())
# print('https://comic.naver.com' + link)

# for cartoon in cartoons:
#     title = cartoon.get_text()
#     link = 'https://comic.naver.com' + cartoon.a['href']
#     print(title.strip(), link)

total_rates=0
stars = soup.find_all('div', attrs={'class':'rating_type'})
for star in stars:
    rate = star.find('strong').get_text()
    total_rates +=float(rate)
print('점수 합 :', total_rates)
print('평균 점수 :', total_rates/len(stars))
