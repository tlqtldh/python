#import re
#import numpy as np 
#from matplotlib import pyplot as plt
import bmt_parser as bp 
import bmt_chart as bc 



cpu_result = [([1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0], [892.4414908, 1663.69408, 3275.46264, 4629.8747, 5959.5818, 6268.808686, 8205.87652, 8716.254542, 9931.532652, 10920.39929, 11945.54772, 12980.9601, 14188, 15036, 16044, 17024, 17964, 18515, 19066, 19617, 20168, 20244 ])]
cpu_title = ['2630v4','intel4108', 'intel5120']
cpu_result.append(bp.pop_paser('intel4108', 'Number of threads:', 'total time:', 20000))
cpu_result.append(bp.pop_paser('intel5120', 'Number of threads:', 'total time:', 20000))
#for i in range(len(cpu_result[0])):
#    print(cpu_result[0][i], cpu_result[1][i])
print(cpu_result)
print(len(cpu_result))
print(len(cpu_result[0][0]))

#mem_result = bp.mem_paser('intel4108', 'Triad: ')
#print(mem_result)

# return(r_read_bw, r_read_iops, r_write_bw, r_write_ipos, r_m_read_bw, r_m_read_iops, r_m_write_bw, r_m_write_iops)
#sto_result = bp.sto_paser('BDP-BMT-MGMT01')
#print(sto_result)
#block_size = [4, 8, 16, 32]

#bc.single_line_chart( cpu_result[0][0], cpu_result[0][1], 'intel4108', 'Thread', 'POPS' )
bc.multi_line_chart( cpu_result, cpu_title, 'Thread', 'POPS' )
#bc.line_chart( mem_result[1], mem_result[2], 'Memory BMT', 'Array Size(MB)', 'Latency(ns)' )
#bc.line_chart( block_size, sto_result[1], 'Random Read', 'Block Size(KB)', 'Bandwdith(GB/S)' )
#bc.line_chart( block_size, sto_result[3], 'Random write', 'Block Size(KB)', 'Bandwdith(GB/S)' )

#bc.line_chart( )
