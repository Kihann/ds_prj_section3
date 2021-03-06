import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
res = requests.get(URL, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all('li', attrs={'class':re.compile('^search-product')})
#print(items[0].find('div', attrs={'class':'name'}).get_text())

for item in items:
    # 광고 상품 제거
    ad = item.find('span', attrs={'class':'ad-badge-text'})
    if ad:
        print('<광고 제거>')
        continue

    name = item.find('div', attrs={'class':'name'}).get_text()
    #애플 제외
    if 'Apple' in name:
        print('<애플 제외>')
        continue
   
    price = item.find('strong', attrs={'class':'price-value'}).get_text()
    
    rate = item.find('em', attrs={'class':'rating'})
    if rate:
        rate = rate.get_text()
        #print('리뷰 평점', rate)
    else:
        print('평점 없음')
        continue

    rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
        #print('리뷰 수', rate_cnt)
    else:
        print('평점 수 없음')
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
         print(name, price, rate, rate_cnt)