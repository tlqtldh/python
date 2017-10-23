def not_used():
    def f_1(a, b, c):
        print(a, b, c)

    f_1(1,2,3)  # position argument(위치를 가지고 파악할 것인가?)
    f_1(a=1,b=2,c=3) # keyword argument(이름을 가지고 파악할 것이가?)
    f_1(b=2, c=3, a=1) # 위치가 중요하지 않고 이름이 중요해졌다. 반대로 속도는 position이 빠름
    f_1(1, b=2, c=3) # position 과 keyward를 섞어 쓸 수 도 있다.
    #f_1(a=1, 2, c=3) # pisition은 keyward 앞에만 올 수 있다.

def f_2(a=0,b=0,c=0): # 모든 언어들은 default parameter 기능이 지원
    print(a, b, c)

#def f_2(a=0,b=0,c=0): # print 함수의 정의를 보면 default parameter의 쓰임새를 알수 있음
#    print(a, b, c, sep='**')

f_2(1,2,3)
f_2() # parameter를 생략해도 default parameter를 사용 
f_2(1)
f_2(1,2)
f_2(a=1, b=2, c=3)
f_2(c=3) # 맨 마지막 parameter에만 값을 다르게 입력 가능

def f_3(*args): # 가변 인자 (데이터의 개수가 정해져 있지 않고 마음대로 조정 가능)
    print(args) # 3개를 던지지만 args는 한개로 받는다 그리고 출력을 tuple로
    print(*args) # unpack 3개를 각각 출력하려면
f_3()
f_3(1)
f_3(1,2)
f_3(1,2,3) # pack

#t1 = (1)
#t2 = (1,)
#print(type(t1), type(t2))

a = ['hello', 'python', 'welcome']
print(a)
print(*a)
print(*a, sep='\n')

def f_4(**kwargs): #keyword argument
    print(kwargs)

def f_5(**kwargs):
#    f_4(kwargs)
    f_4(d=kwargs)
    f_4(**kwargs)

#f_4(1,2,3) # error
f_4(a=1, b=2, c=3)
f_5(a=1, b=2, c=3)

#d = {'color':'red', 'price':100}
#d = dict(color='red', price=100) # dict 함수를 살펴 보면 keyword argument로 받는 것을 알 수 있음

