#def write():
#    f = open('./data/write.txt', 'w', encoding='utf-8')
#    f.write('hello\n')
#    f.write('python' + '\n')
#    f.write('welcome')
#    f.write('\n')
#    f.close()

#write()

import requests
import re

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)

location = re.findall(r'<location wl_ver="3">.+?</location>', recvd.text, re.DOTALL)
for loc in location:
    pro = re.findall(r'<province>(.+?)</province>', loc)
    city = re.findall(r'<city>(.+?)</city>', loc)
    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    for datum in data:
        mode = re.findall(r'<mode>(.+?)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', datum)
        wf = re.findall(r'<wf>(.+?)</wf>', datum)
        tmn = re.findall(r'<tmn>(.+?)</tmn>', datum)
        tmx = re.findall(r'<tmx>(.+?)</tmx>', datum)
        reli = re.findall(r'<reliablility>(.+?)</reliability>', datum)
        items = re.findall(r'<mode>(.+?)</mode>.+<tmEf>(.+?)</tmEf>.+<wf>(.+?)</wf>.+<tmn>(.+?)</tmn>.+<tmx>(.+?)</tmx>', datum, re.DOTALL)
        row = '{},{},{},{},{},{},{}'.format(pro[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0])
        print(row)
