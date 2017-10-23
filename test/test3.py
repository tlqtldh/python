#a = {}      # dict
#print(type(a), a)
#a = {1}     # set
#print(type(a), a)
#a = {1:2}     # dict
#print(type(a), a)
#
#b = {1, 3, 5, 1, 3, 5, 1, 3, 5}
#print(b)
#
#c = [1,3,5,1,3,5,1,3,5]
#print(c)
#
#c = list(set(c))
#print(c)

#Dictionary 초기화
#d = {'color': 'red', 'price': 100} # key와 Value로 구성된 collection
d = dict(color='red', price=100) # 일반적으로 선호
print(d)
print(d['color'],d['price'])

d['title'] = 'pen'   #insert
print(d) 
d['title'] = 'bread'  #update
print(d)

print(d.keys())
print(d.values())
print(d.items())

for i in d.keys():
    print (i, d[i]) 

for l in d.values():
    print(l)

#for d in d.items():
#    print(d, d[0], d[1])

#for k, v in d.items():
#    print(k,v)

#for i in enumerate(d.items()):
#    print (i)
#    print (i[0], i[1][0], i[1][1])

for i, item in enumerate(d.items()):
    print (i, item[0], item[1])

t1, t2, t3, = 1, 2, 3
t1, (t1, t2) = 1, (2,3)
print (t1, t2, t3)

for i, (k, v) in enumerate(d.items()):
    print(i, k, v)