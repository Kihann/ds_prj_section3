import re

p = re.compile('ca.e') # 정규식.컴파일('원하는 형태')
# . = 하나의 문자, ca?e (cafe, case ...)
# ^ = 문자열의 시작, ^de (desk, destiny ...)
# $ = 문자열의 끝, se$ (case, base ...)

def print_match(m):
    if m:
        print('m.group() :', m.group()) # 일치하는 문자열 반환
        print('m.string :', m.string) # 일치하는 문자열이 있는 문자를 반환
        print('m.start() :', m.start()) # 일치하는 문자열이 시작되는 인덱스 반환
        print('m.end() :', m.end()) # 일치하는 문자열이 끝나는 인덱스 반환
        print('m.span() :', m.span()) # 일치하는 문자열의 시작과 끝 인덱스를 반환
    
    else:
        print('매칭 실패')


#m = p.search('good careless cafe')
#m = p.findall('good careless cafe')
# .findall, 일치하는 문자열을 리스트로 반환
# .search, 주어진 문자열 중, 일치하는 것이 있는지 확인
# print_match(m)