import json

j1 = '{"ip": "8.8.8.8"}'
d1 = json.loads(j1)

print(d1)
print(type(d1))
print(d1['ip'])

j2 = '''{  
   "Accept-Language": "en-US,en;q=0.8",
   "Host": "headers.jsontest.com",
   "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}'''

#문제 J2를 해석해서 value만 출력

d2 = json.loads(j2)
print(d2)
print(d2['Host'])

for k, v in d2.items():
    print(k,v)

for k in d2:  # key만 넘어옴
    print(k,d2[k])

# load : string -> object
# dump : object -> string

j3 = json.dumps(d2)
print (j3)
print (type(j3))


import requests

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
recvd = requests.get(url)
print(recvd.text)
text = ''
text = bytes(recvd.text, 'iso-8859-1').decode('utf-8') 
print(text)

#깨져 나오는 경우는 utf-8로 디코딩 해준다.


# 코드와 도시 이름만 출력

items = json.loads(text)
print(items)
print(type(items))

for item in items:
    print (item['code'], item['value'])
