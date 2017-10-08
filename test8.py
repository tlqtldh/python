import csv

def readCsv_1(filename):
    f = open(filename, 'r', encoding='utf-8')

    for line in f:
       # print(line.strip())
        row = line.strip().split(',')# 쉼표 단위로 분리
        print(row)
    f.close()

def readCsv_2(filename):
    f = open(filename, 'r', encoding='utf-8')
    rows = []
    for row in csv.reader(f):
        print(row)
    f.close()

def readCsv(filename):
    f = open(filename, 'w', encoding='utf-8')
    for row in rows:
        f.write(str(row))

    f.close()
#filename = 'D:/git/python/data/kma.csv'
#readCsv_1(filename)

#filename = 'D:/git/python/data/us-500.csv'
#readCsv_2(filename)

filename = 'D:/git/python/data/us-500.csv'
kma = readCsv_2(filename)

writeCsv('D:/git/python/data/write.csv', kma)