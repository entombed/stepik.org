listTmp = []
with open ('dataset_24465_4.txt') as r:
    for line in r:
        line = line.strip()
        listTmp.append(line)
listTmp.reverse()
with open ('w.txt', 'w') as w:
    w.write('\n'.join(listTmp))
