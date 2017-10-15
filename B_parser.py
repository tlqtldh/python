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

    thread_list = []
    time_list = []

    for items in text:
        if find_str1 in items:
            set_thread = items.split(':')
            thread_num = set_thread[1].strip()
        elif int(thread_num) <= start_thread:
            set_time = items.split(':')
            time_num = set_time[1].strip()
            time_sum += float(time_num)
        else:
            thread_list.append(int(thread_num))
            time_list.append(time_sum)
            start_thread = int(thread_num)
            time_sum = float(time_num) 
    
    return (thread_list, time_list)    

def mem_paser(filename1, filename2, find_str):
    ## open the steam bmt result file
    with open( path + filename1, 'r') as content_file:
        source = content_file.read()
        content_file.close()
    string = find_str + "\s+\d+.\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)
    btw_data = 0
    btw_num = 0
    for items in text:
        set_btw = items.split(':')
        btw_data += float(set_btw[1].strip())
        btw_num += 1
    btw_result = btw_data / btw_num

    ## open the steam bmt result file
    with open( path + filename2, 'r') as content_file:
        source = content_file.read()
        content_file.close()
    string = "\d+[.]\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)
    
    source_data = text[::2]
    source_time = text[1::2]
    source_combine = []
    source_array = []
    size_list = []
    lat_list = []

    for i in range(4):
        for j in range(37):
            source_combine.append([source_data[j], source_time[j]])
        source_array.append(source_combine)

    for i in range(37):
        size_list.append(float(source_array[0][i][0]))
        lat_list.append(float(source_array[0][i][1]))

    return (btw_result, size_list, lat_list)

def disk_paser(filename1, filename2, find_str):
    pass

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



cpu_result = pop_paser('result.txt', 'Number of threads:', 'total time:', 20000)
for i in range(len(cpu_result[0])):
    print(cpu_result[0][i], cpu_result[1][i])
print(cpu_result)

mem_result = mem_paser('mem_bwt.txt', 'mem-lat.txt', 'Triad: ')
print(mem_result)

line_chart( cpu_result[0], cpu_result[1], 'CPU BMT', 'Thread', 'POPS' )
line_chart( mem_result[1], mem_result[2], 'Memory BMT', 'Array Size(MB)', 'Latency(ns)' )