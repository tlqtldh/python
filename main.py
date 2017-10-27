#import re
#import numpy as np 
#from matplotlib import pyplot as plt
import bmt_parser as bp 
import bmt_chart as bc 


cpu_result = []
cpu_result.append(bp.pop_paser('2620v4', 'Number of threads:', 'total time:', 20000))
cpu_result.append(bp.pop_paser('intel4110', 'Number of threads:', 'total time:', 20000))
cpu_result.append([[1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0], [892.4414908, 1663.69408, 3275.46264, 4629.8747, 5959.5818, 6268.808686, 8205.87652, 8716.254542, 9931.532652, 10920.39929, 11945.54772, 12980.9601, 14188, 15036, 16044, 17024, 17964, 18515, 19066, 19617, 20168, 20244 ]])
cpu_result.append(bp.pop_paser('intel4114', 'Number of threads:', 'total time:', 20000))
cpu_result.append([[1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0, 56.0, 58.0], [860, 1711, 3388, 4796, 6154, 7330, 8510, 9621, 10686, 11633, 12723, 13735, 14782, 15696, 16611, 17525, 18439, 19354, 20268, 21183, 22097, 23011, 23926, 24840, 25754, 26050, 26345, 26641, 26936, 26930]])
cpu_result.append(bp.pop_paser('intel5120', 'Number of threads:', 'total time:', 20000))

#
#cpu_result.append(bp.pop_paser('intel4108', 'Number of threads:', 'total time:', 20000))
#cpu_result.append(bp.pop_paser('intel4110', 'Number of threads:', 'total time:', 20000))
#cpu_result.append(bp.pop_paser('intel4114', 'Number of threads:', 'total time:', 20000))
#cpu_result.append(bp.pop_paser('intel5120', 'Number of threads:', 'total time:', 20000))
print(cpu_result)
cpu_title = ['2620v4', '4110', '2630v4', '4114', '2660v4', '5120']
cpu_style = ['--', '-', '--','-', '--', '-']
#cpu_title = ['2630v4','2660v4', '2620v4', 'intel4108', 'intel4110', 'intel4114','intel5120']
#cpu_style = ['--','--', '--', '-', '-', '-', '-', '-']

#for i in range(len(cpu_result[0])):
#    print(cpu_result[0][i], cpu_result[1][i])
#print(cpu_result)
#print(len(cpu_result))
#print(len(cpu_result[0][0]))

mem_result = []
mem_btw_result = []
mem_lat_result = []

mem_result.append(bp.mem_paser('intel4108', 'Triad: '))
mem_result.append(bp.mem_paser('intel4110', 'Triad: '))
mem_result.append(bp.mem_paser('intel4114', 'Triad: '))
mem_result.append(bp.mem_paser('intel5120', 'Triad: '))

for i in range(len(mem_result)):
    mem_btw_result.append(mem_result[i][0])
    mem_lat_result.append(mem_result[i][1:3])

mem_title = ['intel4108', 'intel4110', 'intel4114', 'intel5120']
mem_style = ['-', '-', '-', '-']

# return(r_read_bw, r_read_iops, r_write_bw, r_write_ipos, r_m_read_bw, r_m_read_iops, r_m_write_bw, r_m_write_iops)
#sto_result = bp.sto_paser('BDP-BMT-MGMT01')
#print(sto_result)
#block_size = [4, 8, 16, 32]

#bc.single_line_chart( cpu_result[0][0], cpu_result[0][1], 'intel4108', 'Thread', 'POPS' )
bc.multi_line_chart( cpu_result, cpu_title, cpu_style, 'Thread', 'POPS', 'SysBench CPU POPS' )
bc.multi_line_chart( mem_lat_result, mem_title, mem_style, 'Array Size(MB)', 'Latency(ns)', 'LMBench Memory Latency' )
#bc.line_chart( block_size, sto_result[1], 'Random Read', 'Block Size(KB)', 'Bandwdith(GB/S)' )
#bc.line_chart( block_size, sto_result[3], 'Random write', 'Block Size(KB)', 'Bandwdith(GB/S)' )

bc.bar_chart( 
)
#bc.line_chart( )
