def makeDouble(n):
    return n*2

f1 = makeDouble
print(f1(3))
print(makeDouble(3))

f2 = lambda n: n*2
print(f2(3))
print((lambda n: n*2)(3)) # 다른 언어에서는 inline , block 등으로 존재

def add(a, b):
    return a+b

def sub(a, b):
    return a-b
def proxy(f, a1, a2):
    return f(a1,a2)

print(proxy(add, 3, 5))
print(proxy(sub, 3, 5))
print(proxy(lambda a,b: a+b, 3, 5))# 외부에 add 함수를 정의해서 쓰는것보다 lambda로 바로 쓰면 편리

