import requests
import re
urlS = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
urlF = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'


reStr = r'href=[\'"]?([^\'" >]+)'
req = requests.get(urlS)
reqText = req.text
reRez = re.findall(reStr, reqText)
rez = 'No'
for url in reRez:
#    print(url)
    req = requests.get(url)
    reqText = req.text
    reRez = re.findall(reStr, reqText)
    if urlF in reRez:
        rez = 'Yes'
print (rez)