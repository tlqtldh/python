
#def read_1(filename):
#    f = open(filename, 'r')
#    lines = f.readlines()
#    print(lines)
#    for line in lines:
##        print(line, end='')
#        print(line.strip()) # Strip : 문자열 양 끝에 있는 공백들 제거 
#    f.close()
#
#filename = './data/poem.txt'
#read_1(filename)

#def read_2(filename):
#    f = open(filename, 'r')
#
#    while True:
#        line = f.readline()
#       # if len(line) == 0:
#        if not line:   # 파이썬에서 자주 쓰이는 형태
#            break 
#        print(line.strip())
#    f.close()
#
#filename = './data/poem.txt'
#read_2(filename)

#def read_3(filename):
#    f = open(filename, 'r')
#    for line in f:
#        print(line.strip())
#    f.close()
#
#filename = './data/poem.txt'
#read_3(filename)

#def read_4(filename):
#    with open(filename, 'r') as f:
#        for line in f:
#            print(line.strip())
#    return line

#def read_5(filename):
#    lines = []
#    with open(filename, 'r') as f:
#        for line in f:
#            lines.append(line.strip())
#    return lines

def read_6(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return ''.join(lines) 

filename = './data/poem.txt'
lines = read_6(filename)
print (lines)

#temp = '\t\t\n\n  kim seung sik \n\n\t\t'
#print('[{}]'.format(temp))
#temp = temp.strip()
#print (temp)

a = 'AA,BB,CC'
b = a.split(',')
print (b)
c = ''.join(b)
print (c)
