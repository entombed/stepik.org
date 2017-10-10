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