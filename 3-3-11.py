'''
https://stepik.org/lesson/24470/step/11?unit=6776
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa
Sample Output:
blabla is a tandem repetition
123123 is good too
'''
import re
import sys
for line in sys.stdin:
    line = line.rstrip()
    template = r'\b(\w+)\B\1\b'
    foundTmp = re.match(template, line)
    if bool(foundTmp):
        print(line)