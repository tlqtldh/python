import requests
import re
import os

def saveImage(url, title):
    title = re.sub(r'\?', '', title)
    filename = 'Webtoon/{}.{}'.format(title, 'jpg')
    #print(filename)
    recvd = requests.get(url)

    f = open(filename, 'wb')
    f.write(recvd.content)
    f.close()

url = 'http://comic.naver.com/webtoon/weekday.nhn'
recvd = requests.get(url)
weekdays = re.findall(r'<div class="col_inner">.+?</ul>', recvd.text, re.DOTALL)

items = []
for index, day in enumerate(weekdays):
   # li = re.findall(r'<li>.+?</li?', day, re.DOTALL)
   # print(len(li))
    item = re.findall(r'src="(.+?)".+? title="(.+?)"',day, re.DOTALL)
   # print(len(item))
   # print(*item, sep='\n')

for img, title in item:
    if not '.gif' in img:
        #print(img, title)
        items.append(('월화수목금토일'[index], img, title))

print(*items, sep='\n')
#item = [{img, title} for img, title in item if not '.gif' in img]
#print(len(item))

if not os.path.exists('Webtoon'):
    os.mkdir('Webtoon')

for day, url, title in items:
    saveImage(url, title)