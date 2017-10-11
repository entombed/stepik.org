'''
https://stepik.org/lesson/24471/step/7?unit=6780
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">﻿.
Сайты следует выводить в алфавитном порядке.
Пример HTML файла:
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
Пример ответа:
mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
'''

import re
import requests
inputStr = input()
setUrl = set()
listUrl = list()
fundStr = r'(<a.*href=[\'"])(\w+://)?(\w[a-zA0-9.-]+)'
req = requests.get(inputStr.strip())
reqText = req.text
reRez = re.findall(fundStr, reqText)
for item in reRez:
    setUrl.add(item[2])
listUrl = list(setUrl)
listUrl.sort()
for item in listUrl:
    print(item)