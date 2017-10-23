import random

#기존 : 음수(성공), 양수/제로(성공)
#수정 : 음수(실패), 양수(성공), 제로(보류)
def validate(n):
    if n < 0:
        return False
    
    return True

a = random.randrange(-5, 5)
print('input :', a)

if validate(a):
    print('pass')
else:
    print('fail')

print('-'*50)

try:  #이하에서 에러가 발생할 때 처리 문
    b = [1, 5, 9]
    print(b[len(b)])
except IndexError:
    print('IndexError')
except:
    print('unknown error')
while True:
    try:
        c = input('number :')
        c = int(c)
        print('result :', c**2)
        break
    except ValueError:
        print('ValueError')

print('end of code.')