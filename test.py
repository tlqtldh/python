path = 'D:/git/python/results/'
hostname = 'intelssd'

item_list = []
with open( path + "sto_" + hostname + ".out", 'r') as content_file:
    source = content_file.readlines()
    content_file.close()
    for line in source:
        item_list.append(line.split(";"))
    content_file.close()

s_read_bw = []
s_write_bw = []
r_read_bw = []
r_write_bw = []
r_rwread_bw = []
r_rwwrite_bw = []

s_read_iops = []
s_write_iops = []
r_read_iops = []
r_write_iops = []
r_rwread_iops = []
r_rwwrite_iops = []

for i in range(len(item_list)):
    if 'read' in item_list[i][2]:
        s_read_bw.append(item_list[i][6])
        s_read_iops.append(item_list[i][7])
    elif 'write' in item_list[i][2]:
        s_write_bw.append(item_list[i][47])
        s_write_iops.append(item_list[i][48])
    elif 'k100' in item_list[i][2]:
        r_read_bw.append(item_list[i][6])
        r_read_iops.append(item_list[i][7])
    elif 'k0' in item_list[i][2]:
        r_write_bw.append(item_list[i][47])
        r_write_iops.append(item_list[i][48])
    elif 'k7' in item_list[i][2]:
        r_rwread_bw.append(item_list[i][6])
        r_rwread_iops.append(item_list[i][7])
        r_rwwrite_bw.append(item_list[i][47])
        r_rwwrite_iops.append(item_list[i][48])
    
print(s_read_bw, s_write_bw, r_read_bw, r_write_bw, r_rwread_bw, r_rwwrite_bw,'iops', s_read_iops, s_write_iops, r_read_iops, r_write_iops, r_rwread_iops, r_rwwrite_iops)