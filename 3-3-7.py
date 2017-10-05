'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

Sample Input:
catcat
cat and cat
catac
cat
ccaatt

Sample Output:
catcat
cat and cat
'''
import sys

for line in sys.stdin:
    line = line.rstrip()
    if line.count('cat') >= 2:
        print(line)