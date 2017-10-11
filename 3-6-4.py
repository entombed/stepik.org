'''
https://stepik.org/lesson/24476/step/4?unit=6781
Name stepik
Client Id 7a84c7ef15081a79a0d6
Client Secret 3b44243f2f32942735dad45a507cf5c6
'''
import requests
import json
client_id = '7a84c7ef15081a79a0d6'
client_secret = '3b44243f2f32942735dad45a507cf5c6'
list_id = []
list_rez = []
with open('dataset_24476_4.txt', 'r') as file:
    for line in file:
        list_id.append(line.strip())

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token" : token}

for item in list_id:
    r = requests.get("https://api.artsy.net/api/artists/"+item, headers=headers)
    j = json.loads(r.text)
    list_rez.append(j['birthday'] + ' ' + j['sortable_name'])
#print(list_rez)
list_rez.sort()
with open('api.txt', 'w', encoding='UTF-8') as file:
    for item in list_rez:
        print(item[5:])
        file.write(item[5:])
