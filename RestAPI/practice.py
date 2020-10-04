import requests
import json

# user = {
#     "id": "gildong",
#     "password": "192837",
#     "age": 30,
#     "hobby": ["football", "programming"]
# }
#
# # dump 는 파일로 쓰는 것, dumps 는 json 문자열로 변환
# json_data = json.dumps(user, indent=4)
# print(json_data)

# load 도 파일을 읽는 것, loads 는 json 문자열을 dictionary 로
# print()
# data = json.loads(json_data)
# print(type(data))

base_url: str = "https://jsonplaceholder.typicode.com"

response = requests.get(base_url + "/users")
# print(response.text)
data = response.json()

# data = json.loads(response.text)  # .json()하고 똑같다!
# print(data)

names = list()
for user in data:
    names.append(user['name'])

print(names)









