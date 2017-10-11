import re

path = 'D:/git/python/data/'

def pop_paser(filename, find_str1, find_str2, prime_num):
    
    start_thread = 1
    time_sum = 0    
    
    ## open the pop bmt result file
    with open( path + filename, 'r') as content_file:
        source = content_file.read()
        content_file.close()

    ## finding threads and total time using Regular expression operations
    string = find_str1 + "\s+\d+|"+ find_str2 + "\s+\d+.\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)

    result = {}

    for items in text:
        if find_str1 in items:
            set_thread = items.split(':')
            thread_num = set_thread[1].strip()
        elif int(thread_num) <= start_thread:
            set_time = items.split(':')
            time_num = set_time[1].strip()
            time_sum += float(time_num)
        else:
            result[thread_num] = time_sum
            start_thread = int(thread_num)
            time_sum = float(time_num) 
    return result    


#cpu_result = pop_paser('result.txt', 'Number of threads:', 'total time:', 20000)
#print(cpu_result)

 ## open the pop bmt result file
with open( 'C:/Users/Lia/git/python/data/mem_bwt.txt', 'r') as content_file:
    source = content_file.read()
    content_file.close()

## finding threads and total time using Regular expression operations
string = "Triad: \s+\d+.\d+"
re_search = re.compile(string)
text = re_search.findall(source, re.MULTILINE)
btw_num = 0
j = 0
for items in text:
    set_btw = items.split(':')
    btw_num += float(set_btw[1].strip())
    j += 1

print(btw_num/j)

with open( 'C:/Users/Lia/git/python/data/mem-lat.txt', 'r') as content_file:
    source = content_file.read()
    content_file.close()

string = "\d+[.]\d+"
re_search = re.compile(string)
text = re_search.findall(source, re.MULTILINE)

mb = text[::2]
tim = text[1::2]
p = []
x = []
for i in range(4):
    for j in range(37):
        p.append([mb[j], tim[j]])
    x.append(p)

for i in range(37):
    print(x[0][i][1])

#print(mb)
#print('='*30)
#print(tim)
