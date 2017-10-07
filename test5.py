import random

def makeRandoms():
    a = []
    for _ in range(10):
        a.append(random.randrange(100))
    return a

random.seed(1)
a = makeRandoms()
print (a)
print (a[0], a[-2], a[-1])
print (a[0:5])

# 뒷쪽 절반을 출력
print (a[len(a)//2:len(a)])

print(a[:5])
print (a[5:])
print (a[len(a)//2:])

# 짝수 / 홀수 번째 요소만 출력
print(a[::2]) # 시작:종료:증가 
print(a[1::2])

# 꺼꾸로 출력 / 꺼꾸로 짝수/홀수번째만 출력
print(a[::-1])
print(a[len(a)-1:0:-1])
print(a[len(a)-1:-1:-1])
print(a[-1:-1:-1])
print(a[3:3])
print(a[::-2])
print(a[-2::-2])