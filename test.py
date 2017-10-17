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
            print(w[1])
            workload_list[j].insert(0, workload_list[j-1][0])
    
    print(workload_list)

sto_paser('BDP-BMT-MGMT01')

