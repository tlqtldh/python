#import re
#import numpy as np 
#from matplotlib import pyplot as plt
import bmt_parsing as bp 
import bmt_report as br 


cpu_result = bp.pop_paser('BDP-BMT-MGMT01', 'Number of threads:', 'total time:', 20000)
for i in range(len(cpu_result[0])):
    print(cpu_result[0][i], cpu_result[1][i])
print(cpu_result)

mem_result = bp.mem_paser('BDP-BMT-MGMT01', 'Triad: ')
print(mem_result)
#
br.line_chart( cpu_result[0], cpu_result[1], 'CPU BMT', 'Thread', 'POPS' )
#line_chart( mem_result[1], mem_result[2], 'Memory BMT', 'Array Size(MB)', 'Latency(ns)' )

#if __name__ == '__main__':