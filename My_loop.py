str = 'kimjiyou'
for i in str:
    print(i)

print('='*30)
list = [1,2,3,4,'a', 'b', 'c']
for i in list:
    print(i)

print('='*30)
dict = {'a':123, 'b':456, 'c':789}
for i in dict:
    print(i)

print('='*30)
for i in range(10):
    print(i)

print('='*30)
for i in range(2, 10, 2):
    print(i)
    
print('='*30)
scope = [1,2,3,4,5]
for i in scope:
    print(i)
    if i < 3:
        continue
    else:
        break

print('='*30)
x = 0
while x < 10:
    x = x + 1
    if x < 3:
        print(x)
        continue
    if x > 7:
        break

print('='*30)
x = 1
total = 0
while True:
    total = total + x
    if total > 10000:
        print(x)
        print(total)
        break
    x = x + 1