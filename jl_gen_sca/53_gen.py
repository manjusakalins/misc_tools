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

inf=open("jty_gpt");
pt_lines=inf.readlines();
inf.close();
#print pt_lines

inf=open("KMT6753_EMMC_y960_mt6753_66_n_ForSW.sca")
sca_lines=inf.readlines();
inf.close();
#print sca_lines;

out_str=""
sca_rd_idx=0;
pl_size=0;

head_53='''

############################################################################################################
#
#  General Setting 
#    
############################################################################################################
- general: MTK_PLATFORM_CFG
  info: 
    - config_version: V1.1.2
      platform: MT6753
      project: y960_mt6753_66_n
      storage: EMMC
      boot_channel: MSDC_0
      block_size: 0x20000
############################################################################################################
#
#  Layout Setting
#
############################################################################################################
- partition_index: SYS0
  partition_name: preloader
  file_name: preloader_y960_mt6753_66_n.bin
  is_download: false
  type: SV5_BL_BIN
  linear_start_addr: 0x0
  physical_start_addr: 0x0
  partition_size: 0x40000
  region: EMMC_BOOT_1
  storage: HW_STORAGE_EMMC
  boundary_check: true
  is_reserved: false
  operation_type: BOOTLOADERS
  reserve: 0x00

- partition_index: SYS1
  partition_name: pgpt
  file_name: NONE
  is_download: false
  type: NORMAL_ROM
  linear_start_addr: 0x0
  physical_start_addr: 0x0
  partition_size: 0x80000
  region: EMMC_USER
  storage: HW_STORAGE_EMMC
  boundary_check: true
  is_reserved: false
  operation_type: INVISIBLE
  reserve: 0x00
'''
def write_out_sca_line(cur_str):
    global out_str
    cur_str = cur_str.strip("\n")
    out_str = "%s\n%s" % (out_str, cur_str)

def common_get_val(cur_str):
    if cur_str.find("=") != -1:
        return cur_str[cur_str.find("=")+1:]
cur_idx=2;
write_out_sca_line(head_53)
for cur_line in pt_lines:
    if len(cur_line) < 10:
        continue;
    cur_list=cur_line.split(",");
    print cur_list
    pt_name = common_get_val(cur_list[0]).strip()
    st_addr = int(common_get_val(cur_list[2]).strip(), 16)*512;
    size = int(common_get_val(cur_list[3]).strip(), 16)*512;

    print pt_name, hex(st_addr), hex(size)
    cur_pt_str = '''\n\n- partition_index: SYS%d
  partition_name: %s
  file_name: %s
  is_download: true
  type: NORMAL_ROM
  linear_start_addr: 0x%x
  physical_start_addr: 0x%x
  partition_size: 0x%x
  region: EMMC_USER
  storage: HW_STORAGE_EMMC
  boundary_check: true
  is_reserved: false
  operation_type: UPDATE
  reserve: 0x00\n\n''' % (cur_idx, pt_name, pt_name, st_addr, st_addr, size)
    print cur_pt_str;
    write_out_sca_line(cur_pt_str)
    cur_idx = cur_idx + 1;
    


#print out_str
genf=open("outsca.txt", 'w+');
genf.write(out_str);
genf.close();
