'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.
Пример:
s = "abababa"
t = "aba"
Вхождения строки t в строку s:
abababa
abababa
abababa
'''

s = "aaaaa"
t = "a"
#s, t = input(), input()
step = len(t)
start = 0
count = 0
while True:
    tmpStr = s[start:step]
    if t in tmpStr:
        count += 1
    start += 1
    step += 1
    if start == len(s):
        break
print(count)