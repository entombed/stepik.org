import requests
listTmp = []
apiUrl = ''
with open('dataset_24476_3.txt', 'r') as file:
    for line in file:
        listTmp.append(line.strip())

print(listTmp)
for tmpInt in listTmp:
    url = 'http://numbersapi.com/' + tmpInt + '/math?json=true'
    print(url)
    req = requests.get(url)
    data = req.json()
    print(data)
    print(data['found'])