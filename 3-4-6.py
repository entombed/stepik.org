import requests
import re
urlS = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
urlF = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'

def getUrl(url):
    req = requests.get(url)
    reqText  = req.text
    reStr = r'https://stepic.org/.*\d.html'
    reRez = re.findall(reStr, reqText)
    return reRez[0]
count = 0
while True:
    urlS = getUrl(urlS)
    if (urlS == urlF and count > 3) or count > 3:
        rezText = 'No'
        break
    if urlS == urlF and count == 2:
        rezText = 'Yes'
        break
    count += 1

print(rezText)
