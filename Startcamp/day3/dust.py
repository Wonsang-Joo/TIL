#공공데이터 api 활용 실습(대기오염정보)
#1. 필요한 라이브러리 import 하기

import requests

url = http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty
servicekey = DSj8PIqyFSz3DJmlXI55wj%2FdTxVr6m2axFJT9Hn%2BytVW3JiIXaM%2BNJeqWJwjAtethhWxRXm8V2qe0wa8xCTi6A%3D%3D

response = requests.get(url).json()
sidoname = '광주'
pm10Value = '미세먼지 농도'
print(f'{sidoname} {pm10Value}')