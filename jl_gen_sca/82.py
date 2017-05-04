#coding=utf-8
import os
import pickle
import codecs
import sys
import re
import operator
import random

#partition PRELOADER size 0000000000000000 0000000001400000 
#- partition_index: SYS0
#  partition_name: PRELOADER
#  file_name: preloader_zh960.bin
#  is_download: true
#  type: SV5_BL_BIN
#  linear_start_addr: 0x0
#  physical_start_addr: 0x0
#  partition_size: 0x1400000
#  region: EMMC_BOOT_1
#  storage: HW_STORAGE_EMMC
#  boundary_check: true
#  is_reserved: false
#  operation_type: BOOTLOADERS
#  reserve: 0x00

inf=open("input_pt");
pt_lines=inf.readlines();
inf.close();
print pt_lines

inf=open("MT6582_Android_scatter.txt")
sca_lines=inf.readlines();
inf.close();
print sca_lines;

out_str=""
sca_rd_idx=0;
pl_size=0;

def write_out_sca_line(cur_str):
    global out_str
    cur_str = cur_str.strip("\n")
    out_str = "%s\n%s" % (out_str, cur_str)


for cur_line in pt_lines:
    cur_list=cur_line.split();
    print cur_list
    pt_name = cur_list[1]
    st_addr = int(cur_list[3],16);
    size = int(cur_list[4],16);
    print pt_name
    if pt_name.find("PRELOADER") != -1:
        pl_size = size;
    #print hex(st_addr)
    pt_got=0;
    while sca_rd_idx < len(sca_lines):
        cur_sca_line = sca_lines[sca_rd_idx]
        sca_rd_idx = sca_rd_idx + 1;

        if cur_sca_line.find(pt_name) != -1:
            print cur_sca_line
            pt_got=1;
            write_out_sca_line(cur_sca_line);
            continue;
            
        if pt_got == 1 and cur_sca_line.find("linear_start_addr") != -1:
            cur_str = "  linear_start_addr: 0x%x" % st_addr;
            write_out_sca_line(cur_str);
            continue;
        if pt_got == 1 and cur_sca_line.find("physical_start_addr") != -1:
            if pt_name.find("PRELOADER") != -1:
                cur_str = cur_sca_line;
            else:
                cur_str = "  physical_start_addr: 0x%x" % (st_addr-pl_size);
            write_out_sca_line(cur_str);
            continue;
        if pt_got == 1 and cur_sca_line.find("partition_size") != -1:
            cur_str = "  partition_size: 0x%x" % size;
            write_out_sca_line(cur_str);
            pt_got = 0;
            break;
        write_out_sca_line(cur_sca_line);#write ori line

#write out last lines.
while sca_rd_idx < len(sca_lines):
    cur_sca_line = sca_lines[sca_rd_idx]
    sca_rd_idx = sca_rd_idx + 1;
    write_out_sca_line(cur_sca_line);#write ori line

print out_str
genf=open("outsca.txt", 'w+');
genf.write(out_str);
genf.close();
