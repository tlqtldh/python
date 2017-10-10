import re

prime_num = 20000
result_file = 'C:/Users/Lia/git/python/data/result.txt'
find_string1 = 'Number of threads:'
find_string2 = 'total time:'
start_thread = 1
time_sum = 0

## open the pop bmt result file
with open( result_file, 'r') as content_file:
    source = content_file.read()
    content_file.close()

## finding threads and total time using Regular expression operations
string = find_string1 + "\s+\d+|"+ find_string2 + "\s+\d+.\d+"
re_search = re.compile(string)
text = re_search.findall(source, re.MULTILINE)

result = {}

for items in text:
    if find_string1 in items:
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
    
print(result) 

## divide list by even(value) and odd(thread)
#thread = text[0::2]
#time = text[1::2]
#thread_num = []
#time_num = []

## fill list with thread numbers only and merge the same numbers in the list
#for re_filter in thread:
#        thread_num.append(int(re.findall('\d+|\d.\d+', re_filter)[0]))
#print(set(thread_num)

#thread_num = list(set(thread_num))
#thread_num.sort()
#print(thread_num)
#
### fill list with times only and merge numbers in 5 slices
#for re_filter2 in time:
#        time_num.append(float(re.findall('\d+.\d+',re_filter2)[0]))
#prime_op = [prime_num/(sum(time_num[i:i+5])/5) for i in range(0, len(time_num), 5)]
#print(prime_op)