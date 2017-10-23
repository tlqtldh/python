# code와 data를 합쳐 놓은것 class

class Info:
    def __init__(self, age):
        print('c-tor') 
        self.age = age

    def show(self):
        print('show', self.age)
    
    @property    
    def myAge(self):
        return self.age

i1 = Info(10)
i2 = Info(20)

print(i1)

Info.show(i1) # unbound method 클래스 이름을 쓴다음에 호출에서 해당 변수를 전달
i1.show()
i2.show() # bound method 변수를 앞쪽으로 옮겨놓는 방법

print('age:' , i1.age)
#print('my age : ', i1.myAge())
print('my age : ', i1.myAge) # 모양은 함수 이지만 쓰는것은 변수 처럼 위에서 property로 정의했기 때문에
# il.myAge = 30 # il.myAge는 변경 할 수 없는 Read only 

#re.findall # re 는 변수가 아님
#''.format # ''는 변수


