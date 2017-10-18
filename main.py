#import re
#import numpy as np 
#from matplotlib import pyplot as plt
import bmt_parser as bp 
import bmt_chart as bc 


cpu_result = bp.pop_paser('BDP-BMT-MGMT01', 'Number of threads:', 'total time:', 20000)
#for i in range(len(cpu_result[0])):
#    print(cpu_result[0][i], cpu_result[1][i])
print(cpu_result)

mem_result = bp.mem_paser('BDP-BMT-MGMT01', 'Triad: ')
print(mem_result)

# return(r_read_bw, r_read_iops, r_write_bw, r_write_ipos, r_m_read_bw, r_m_read_iops, r_m_write_bw, r_m_write_iops)
sto_result = bp.sto_paser('BDP-BMT-MGMT01')
#print(sto_result)
block_size = [4, 8, 16, 32]

#bc.line_chart( cpu_result[0], cpu_result[1], 'CPU BMT', 'Thread', 'POPS' )
#bc.line_chart( mem_result[1], mem_result[2], 'Memory BMT', 'Array Size(MB)', 'Latency(ns)' )
bc.line_chart( block_size, sto_result[1], 'Random Read', 'Block Size(KB)', 'Bandwdith(GB/S)' )
bc.line_chart( block_size, sto_result[3], 'Random write', 'Block Size(KB)', 'Bandwdith(GB/S)' )

#bc.line_chart( )
