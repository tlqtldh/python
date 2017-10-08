import p8_Control_CSV
import sqlite3

def createDB(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    query = 'CREATE TABLE kma (prov text, city text, mode text, date text, desc text, tmin int, tmax int)'
    cur.execute(query)

    conn.commit()
    conn.close()

def insertDB(filename, row):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    base = 'INSERT INTO kma VALUES ("{}","{}","{}","{}","{}","{}","{}")'
    query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    cur.execute(query)

    conn.commit()
    conn.close()

def insertAllDB(filename, rows):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    base = 'INSERT INTO kma VALUES ("{}","{}","{}","{}","{}","{}","{}")'
    for row in rows:
        query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        cur.execute(query)

    conn.commit()
    conn.close()

def fetchDB(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    query = 'SELECT * from kma'
    rows = [] 
    for row in cur.execute(query):
        rows.append(row)
    #conn.commit() # 읽기는 commit을 호출하지 않음
    conn.close()
    return rows

def searchDB(filename, search):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    query = 'SELECT * from kma WHERE city = "{}"'.format(search)
    rows = [] 
    for row in cur.execute(query):
        rows.append(row)
    conn.close()
    return rows

#rows = p8_Control_CSV.readCsv_2('C:/Users/Lia/git/python/data/kma.csv')
#print(*rows, sep='\n')
#
filename = 'C:/Users/Lia/git/python/data/kma.sqlite'
#createDB(filename)

#for row in rows:
#    insertDB(filename, row)

#insertAllDB(filename, rows)
#rows = fetchDB(filename)
#print(*rows, sep='\n')

rows = searchDB(filename, '부산')
print(*rows, sep='\n')