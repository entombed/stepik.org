'''
https://stepik.org/lesson/24466/step/5?unit=6773
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.

Sample Input 1:
2016 4 20
14

Sample Output 1:
2016 5 4
'''
import datetime
inStr = input()
inDays = int(input())
dateList = inStr.split()
dateTmp = datetime.date(int(dateList[0]), int(dateList[1]), int(dateList[2]))
delta = datetime.timedelta(days=inDays)
dateTmp = dateTmp + delta
print(dateTmp.year, dateTmp.month, dateTmp.day)