
import random
#list 반복문을 만들어 내는 새로운 방법]
a = [i for i in range(10)]
print(a)

random.seed(1)

a = [random.randrange(100) for _ in range(10)]
print(a)
print(sum(a), max(a), min(a))

b = [i for i in a]
print(b)

b = [i*2 for i in a]
print(b)

b = [i for i in reversed(a)]
print(b)

#for i in a:
#    if i%2 == 1:
#        i

c = [i for i in a if i%2 == 1]
print(c)

a1 = [random.randrange(100) for _ in range(random.randrange(5, 15))]
a2 = [random.randrange(100) for _ in range(random.randrange(5, 15))]
a3 = [random.randrange(100) for _ in range(random.randrange(5, 15))]
all = [a1, a2, a3]
print(*all, sep='\n')

# all에 들어 있는 숫자의 갯수를 세어보시오
print(sum([len(i) for i in all]))
print(max([max(i) for i in all]))

# 10000보다 작은 양수에 포함된 8의 개수를 세어 보시오 
s = 'AABBCCAA'
print(s.count('A'))

print(sum([str(i).count('8') for i in range(10000)]))
print(str([i for i in range(10000)]).count('8'))
print(str(list(range(10000))).count('8'))