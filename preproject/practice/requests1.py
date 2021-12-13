import requests
res = requests.get('http://www.google.com')
res.raise_for_status() # 응답코드 상태, 200이면 정상

print(res.text)

with open('mygoogle.html', 'w', encoding='utf8') as f: 
    # mygoogle.html에 w(쓰기모드), utf-8 인코딩로 열기
    f.write(res.text)
    # res.text를 씀