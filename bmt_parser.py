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

def mem_paser(hostname, find_str):
    ## open the steam bmt result file
    with open( path + "membtw_" + hostname + ".out", 'r') as content_file:
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
    with open( path + "memlat_" + hostname + ".out", 'r') as content_file:
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

def sto_paser(hostname):
    
    ## open the storage bmt result file
    with open( path + "sto_" + hostname + ".out", 'r') as content_file:
        source = content_file.read()
        content_file.close()

    ## finding threads and total time using Regular expression operations
    string = ".*[:].*group|write[:]|read.*[:].|bw=\d+|iops=\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)

    item_list = []
    workload_list = []
    r_read_bw = []
    r_read_iops = []
    r_write_bw = []
    r_write_ipos = []
    r_m_read_bw = []
    r_m_read_iops = []
    r_m_write_bw = []
    r_m_write_iops = []

    for items in text:
        if 'group' in items:
            item_list.append(items[:-8])
        elif 'read' in items or 'write' in items:
            item_list.append(items[:-1])
        elif 'bw' in items:
            bw = items.split('=')
            item_list.append(int(bw[1].strip()))
        elif 'iops' in items:
            iops = items.split('=')
            item_list.append(int(iops[1].strip()))
            workload_list.append(item_list)
            item_list = []
        
    for j, w in enumerate(workload_list):
        if isNumber(w[1]):
            workload_list[j].insert(0, workload_list[j-1][0])
   
    for x in workload_list:
        if 'k100' in x[0]:
            r_read_bw.append(x[-2])
            r_read_iops.append(x[-1])
        elif 'k0' in x[0]:
            r_write_bw.append(x[-2])
            r_write_ipos.append(x[-1])
        elif 'k70' in x[0] and 'read' in x[1]:
            r_m_read_bw.append(x[-2])
            r_m_read_iops.append(x[-1])
        elif 'k70' in x[0] and 'write' in x[1]:
            r_m_write_bw.append(x[-2])
            r_m_write_iops.append(x[-1])
    
    return(r_read_bw, r_read_iops, r_write_bw, r_write_ipos, r_m_read_bw, r_m_read_iops, r_m_write_bw, r_m_write_iops)


def sto_paser_(hostname):
     with open( path + "sto_" + hostname + ".out", 'r') as content_file:
        source = content_file.read()
        content_file.close(
        )
    
    item_list = []
    ## finding threads and total time using Regular expression operations
    text = source.split(";")
    item_list.append(text)
    string = ".*[:].*group|write[:]|read.*[:].|bw=\d+|iops=\d+"
    re_search = re.compile(string)
    text = re_search.findall(source, re.MULTILINE)   

if __name__ == '__main__':    
    pass
