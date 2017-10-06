'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:
attraction
buzzzz
Sample Output:
atraction
buz
'''
import re
import sys
for line in sys.stdin:
    line = line.rstrip()
    template = r'((\w)\2{1,})'
    replTemplate = r'\2'
    #subTmp = re.findall(template, line)
    subTmp = re.sub(template, replTemplate, line)
    print(subTmp)