import requests
dataNumbers = []
with open('dataset_24476_3.txt', 'r') as file:
    for line in file:
        dataNumbers.append(line.strip())

for tmpInt in dataNumbers:
    url = 'http://numbersapi.com/' + tmpInt + '/math?json=true'
    req = requests.get(url)
    data = req.json()
    if data['found']:
        print('Interesting')
    else:
        print('Boring')
