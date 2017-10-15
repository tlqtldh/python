import re
import numpy as np 
from matplotlib import pyplot as plt

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

def mem_paser(filename, find_str1, find_str2, prime_num):
     ## open the steam bmt result file
    with open( 'D:/git/python/data/mem_bwt.txt', 'r') as content_file:
        source = content_file.read()
        content_file.close()
    ## finding Triad using Regular expression operations
    string = "Triad: \s+\d+.\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)
    btw_data = 0
    btw_num = 0
    for items in text:
        set_btw = items.split(':')
        btw_data += float(set_btw[1].strip())
        btw_num += 1
    mem_btw = btw_num / btw_num
    
    with open( 'D:/git/python/data/mem-lat.txt', 'r') as content_file:
        source = content_file.read()
        content_file.close()
    
    string = "\d+[.]\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)
    
    mb = text[::2]
    tim = text[1::2]
    p = []
    x = []
    data_size = []
    mem_lat = []
    for i in range(4):
        for j in range(37):
            p.append([mb[j], tim[j]])
        x.append(p)
    
    for i in range(37):
        data_size.append(float(x[0][i][0]))
        mem_lat.append(float(x[0][i][1]))

    return mem_btw, data_size, mem_lat

def line_chart(x_value, y_value, title, x_label, y_label):
    line_color = ['b', 'r', 'g', 'y']
    #plt.subplot(2,1,1)
    
    plt.plot(x_value, y_value, line_color[0], label=title)
    plt.xlabel( x_label, fontsize=10)
    plt.ylabel( y_label, fontsize=10)
    plt.title('CPU BMT', fontsize=20)
    print(x_value)
    plt.xticks(x_value, rotation=75)
    plt.legend()
    plt.grid()
    plt.text(0, 0, 'Figure. CPU BMT', ha='center')
    plt.savefig('bmt1.png')
    plt.show()

def bar_chart(x, y, title):
    pass

def gen_report():
    pass



#print(mb)
#print('='*30)
#print(tim)

cpu_result = pop_paser('result.txt', 'Number of threads:', 'total time:', 20000)
print(cpu_result)

#line_chart( data_size, mem_lat, 'CPU BMT', 'Array Size(MB)', 'Latency(ns)' )
