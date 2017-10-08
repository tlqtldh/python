import csv

# 기본적인 CSV 파일 파싱하기
def readCsv_1(filename):
    f = open(filename, 'r', encoding='utf-8')

    for line in f:
        print(line.strip())
        row = line.strip().split(',')# 쉼표 단위로 분리
        print(row)
    f.close()

# CSV Moudle 이용하여 간편하게 파싱
def readCsv_2(filename):
    f = open(filename, 'r', encoding='utf-8')
    rows = []
    for row in csv.reader(f): # csv module이 자동적으로 ""등을 제거
        #print(row)
        rows.append(row)
    f.close()
    return rows

# 파일에 csv 형식으로 쓰기
def writeCsv(filename, rows):
    f = open(filename, 'w', encoding='utf-8')
    #f = open(filename, 'w', encoding='utf-8', newline='') # 입력 데이터들 줄간 공백이 있을 때 없얘는 방법
    #for row in rows:
    #    #f.write(str(row)) #list 형태로 write
    #    f.write(','.join(row)) #,로 분리된 String 형태로 write
    #    f.write('\n') # 줄단위
    
    # 위와 같이 ,로 분리하여 string 형태로 저장하는것을 손쉽게 하기 위해 csv 모듈 사용로 분리해주기 위해 개행문자 삽입
    #writer = csv.writer(f) #  f를 csv에 위임
    writer = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=':') # dataㄹ들을 ""로 감싸고, :로 구분하고 싶을때 (default-> ,)
    #for row in rows:
    #    writer.writerow(row)
    writer.writerows(rows) # 위에 for문을 한줄로 표현
    f.close()

if __name__ == '__main__':
    
    #filename = 'C:/Users/Lia/git/python/data/kma.csv'
    #readCsv_1(filename)
    
    filename = 'C:/Users/Lia/git/python/data/us-500.csv'
    us500 = readCsv_2(filename)
    print(us500)
    
    writeCsv('C:/Users/Lia/git/python/data/write.txt', us500)