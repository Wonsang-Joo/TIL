#가장 최근에 메세지를 보낸 사용자에게
# '안녕하세요' 메세지 보내기.


#1.요청에 필요한 라이브러리를 import
import requests, pprint

#2. api 요청 url + token 확인
token = '1599905271:AAEJbJVLwnRCNBwKUz0tuTe6JkrVao8QjHQ'
api_url = f' https://api.telegram.org/bot{token}'
#3. 메세지 보낸 사용자의 ID값 찾기 
# 요청 & 응답

chat_id_url = f'{api_url}/getupdates'
response = requests.get(chat_id_url).json()
# pprint.pprint(response)
chat_id = response['result'][0]['message']['chat']['id']
# print(chat_id)

#4. cath id 에게 메시지 보내기
text = input('메세지를 입력하세요: ')
message_url = f'{api_url}/sendmessage?chat_id={chat_id}&text={text}'

requests.get(message_url)
