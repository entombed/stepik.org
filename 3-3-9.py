'''
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
zabcz
zzxzz
'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    p = r'z\w{3}z'
    mobj = re.search(p, line)
    if bool(mobj):
        print(line)