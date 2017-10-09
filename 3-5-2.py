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
