'''
https://stepik.org/lesson/24473/step/2?unit=6777
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
'''

import csv

tmpDict = {}
with open('Crimes.csv') as file:
    readerRow = csv.DictReader(file)
    for row in readerRow:
        if '/2015' in row['Date']:
            typeTmp = row['Primary Type']
            dateTmp = row['Date']
            if row['Primary Type'] not in tmpDict:
                tmpDict.update({typeTmp:0})
            else:
                count = tmpDict[typeTmp]
                count += 1
                tmpDict.update({typeTmp:count})
max = 0
for item in tmpDict:
    if tmpDict[item] > max:
        max = tmpDict[item]
        rez = item
print(rez)
