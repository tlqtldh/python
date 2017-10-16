import re
import numpy as np 
from matplotlib import pyplot as plt

path = 'D:/git/python/results/'


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

    for items in text:
        if 'group' in items:
            item_list.append(items[:-8])
        #elif 'read' in items or 'write' in items:
        #    pattern = items[:-1]
        #    print(pattern)
        elif 'bw' in items:
            bw = items.split('=')
            item_list.append(int(bw[1].strip()))
        elif 'iops' in items:
            iops = items.split('=')
            item_list.append(int(iops[1].strip()))
    print(item_list)

sto_paser('BDP-BMT-MGMT01')