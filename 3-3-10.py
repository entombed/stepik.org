'''
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
Sample Input:
\w denotes word character
No slashes here
Sample Output:
\w denotes word character
'''

import re
import sys
for line in sys.stdin:
    line = line.rstrip()
    p = r'\\'
    mobj = re.search(p, line)
    if bool(mobj):
        print(line)