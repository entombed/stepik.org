'''
https://stepik.org/lesson/24476/step/3?unit=6781
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true
Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true
Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''
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
