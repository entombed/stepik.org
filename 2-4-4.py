'''
https://stepik.org/lesson/24465/step/4?unit=6772
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
Пример входного файла:
ab
c
dde
ff
Пример выходного файла:
ff
dde
c
ab
'''
listTmp = []
with open('dataset_24465_4.txt') as r:
    for line in r:
        line = line.strip()
        listTmp.append(line)
listTmp.reverse()
with open('w.txt', 'w') as w:
    w.write('\n'.join(listTmp))
