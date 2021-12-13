import requests
from bs4 import BeautifulSoup

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
params ={'serviceKey' : 'erS8us854s8cPbsN88GRrXpLckdLlkH7ImC49YQu6lwrC6hElTlGBIoOVmPw5g+r6H43SBkVEni+QPOHPkFf3w==', 'pageNo' : '1', 'numOfRows' : '10', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

res = requests.get(url, params=params)
soup = BeautifulSoup(res.text, 'lxml')
items = soup.find('items')

for item in items:
        
    date = item.find('item', attrs={'class':'거래금액'})
    print(date.get_text())