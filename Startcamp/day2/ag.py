import requests

# api 요청 url 확인 + 필요한 데이터 건내주기
name = 'chaim'
url = f'https://api.agify.io?name={name}'

# url로 요청 보내기
response = requests.get(url).json()

name = response['name']
age = response['age']
print(f'{name}님의 예상 나이는 {age}살 입니다.')
