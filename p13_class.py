# code와 data를 합쳐 놓은것 class

class Info:
    def __init__(self):
        print('c-tor') 
    def show(self):
        print('show', self)

i1 = Info()
print(i1)

Info.show(i1)
i1.show()
