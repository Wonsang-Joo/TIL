import requests, pprint

name = 'ruby'

url = f'https://api.nationalize.io/?name={name}'
#https://api.nationalinz.io
#?
#name=michael 은 추가 데이터

#.text -> 데이터를 꺼낸다
#.jason() -> 메서드(기능)을 실행시킨다.
response = requests.get(url).json()
#pprint.pprint(response)
name = response['name']
country_id = response['country'][0]['country_id']
probability = round(response['country'][0]['probability'] * 100, 2)

print(f'{name}님의 국적은  {probability}% 확률로 {country_id}입니다.')