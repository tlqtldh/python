import re
import numpy as np 
from matplotlib import pyplot as plt

path = 'D:/git/python/results/'

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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
    
    print(workload_list)
   
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
    
    print(r_read_bw, r_read_iops, r_write_bw, r_write_ipos, r_m_read_bw, r_m_read_iops, r_m_write_bw, r_m_write_iops)

sto_paser('BDP-BMT-MGMT01')

