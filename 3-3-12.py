
'''
https://stepik.org/lesson/24470/step/12?unit=6776
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
Sample Input:
I need to understand the human mind
humanity
Sample Output:
I need to understand the computer mind
computerity
'''

import re
import sys
for line in sys.stdin:
    line = line.rstrip()
    template = r'human'
    replTemplate = r'computer'
    subTmp = re.sub(template, replTemplate ,line)
    print(subTmp)