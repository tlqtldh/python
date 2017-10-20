import re

path = 'D:/git/python/results/'

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def average(values):
    if len(values) == 0:
        return None
    return sum(values, 0.0) / len(values)

def pop_paser(hostname, find_str1, find_str2, prime_num):
    
    ## open the pop bmt result file
    with open( path + "pops_" + hostname + ".out", 'r') as content_file:
        source = content_file.read()
        content_file.close()

    ## finding threads and total time using Regular expression operations
    string = find_str1 + "\s+\d+|"+ find_str2 + "\s+\d+.\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)

    thread_sum = []
    thread_list = []
    time_list = []
    time_avg = []

    for items in text:
        if find_str1 in items:
            set_thread = items.split(':')
            thread_num = set_thread[1].strip()
            thread_list.append(int(thread_num))
        elif find_str2 in items:
            set_time = items.split(':')
            time_num = set_time[1].strip()
            time_list.append(float(time_num))

    for i in range(0,len(thread_list),5):
        thread_sum.append(sum(thread_list[i:i+4])/4)

    for i in range(0,len(time_list),5):
        time_avg.append(20000/average(time_list[i:i+4]))
      
    return (thread_sum, time_avg)  

cpu_result = pop_paser('intel4108', 'Number of threads:', 'total time:', 20000)
print(cpu_result)