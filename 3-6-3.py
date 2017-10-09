import requests
dataNumbers = []
with open('dataset_24476_3.txt', 'r') as file:
    for line in file:
        dataNumbers.append(line.strip())

print(dataNumbers)
for tmpInt in dataNumbers:
    url = 'http://numbersapi.com/' + tmpInt + '/math?json=true'
    print(url)
    req = requests.get(url)
    data = req.json()
    print(data)
    print(data['found'])
