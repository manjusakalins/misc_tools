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




#print sca_lines;

out_str=""
out_pt_idx=2; #we make pl,gpt fix to 0,1
sca_info=[];
sca_info_map={}
pt_info=[]
pt_info_map={}


def write_out_sca_line(cur_str):
    global out_str
    cur_str = cur_str.strip("\n")
    out_str = "%s\n%s" % (out_str, cur_str)

def common_write_sca_line_number(lines,st,end):
    for idx in range(st,end):
        write_out_sca_line(lines[idx]);

def __common_get_last_val(cstr, splitor):
    if cstr.find(splitor) != -1:
        return cstr[cstr.find(splitor)+1:]
    else:
        return "not_found"

def common_get_val(cur_str):
        return __common_get_last_val(cur_str,"=");

def common_replace_pt_st(cur_pt_info, lines, cur_sca_info):
    global out_pt_idx;
    outstr=""
    if cur_pt_info[0] == 'flashinfo':
        cur_pt_info[1] = 0xFFFF0084
        cur_pt_info[2] = 0x1000000
    for idx in range(cur_sca_info[1], cur_sca_info[2]):
        cur_line=lines[idx];
        cur_str=cur_line;
        if cur_line.find("partition_size") != -1:
            cur_str = "  partition_size: 0x%x\n" % cur_pt_info[2];
        if cur_line.find("linear_start_addr") != -1:
            cur_str = "  linear_start_addr: 0x%x\n" % cur_pt_info[1];
        if cur_line.find("physical_start_addr") != -1:
            cur_str = "  physical_start_addr: 0x%x\n" % cur_pt_info[1];
        if cur_line.find("partition_index") != -1:
            cur_str = "- partition_index: SYS%d\n" % out_pt_idx;
            out_pt_idx = out_pt_idx +1;
        outstr="%s%s" %(outstr,cur_str)
    return outstr;
def common_new_pt_st(cur_pt_info):
    global out_pt_idx;

    ptstr='''- partition_index: SYS%d
  partition_name: %s
  file_name: NONE
  is_download: false
  type: EXT4_IMG
  linear_start_addr: 0x%x
  physical_start_addr: 0x%x
  partition_size: 0x%x
  region: EMMC_USER
  storage: HW_STORAGE_EMMC
  boundary_check: true
  is_reserved: false
  operation_type: PROTECTED
  reserve: 0x00\n''' % (out_pt_idx, cur_pt_info[0], cur_pt_info[1], cur_pt_info[1], cur_pt_info[2]);
    out_pt_idx = out_pt_idx + 1;
    return ptstr;
 

def sca_preprocess_for_info(lines):
    pt_start=0;
    pt_end=0;
    cur_pt_name=""
    for i in range(0,len(lines)):
        cur_sca_line = lines[i];
        if len(cur_sca_line) < 10:
            continue;
        if cur_sca_line.find("partition_index:") != -1:
            if len(cur_pt_name) > 1:
                #print cur_pt_name, pt_start, (i)
                cur_pt_st=[cur_pt_name, pt_start, i]
                sca_info_map[cur_pt_name]=cur_pt_st
                sca_info.append(cur_pt_st);
            pt_start = i;
            continue;
        if cur_sca_line.find("partition_name") != -1:
            cur_pt_name=__common_get_last_val(cur_sca_line, ": ").strip();
            #print cur_pt_name
    cur_pt_st=[cur_pt_name, pt_start, len(lines)]
    sca_info_map[cur_pt_name]=cur_pt_st
    sca_info.append(cur_pt_st);
    print sca_info



def pt_pre_process():
    inf=open("80_1");
    pt_lines=inf.readlines();
    inf.close();
    #print pt_lines
    for cur_line in pt_lines:
        if len(cur_line) < 10:
            continue;
        cur_list=cur_line.split(",");
        pt_name = common_get_val(cur_list[0]).strip()
        st_addr = int(common_get_val(cur_list[2]).strip(), 16)*512;
        size = int(common_get_val(cur_list[3]).strip(), 16)*512;

        #print pt_name, hex(st_addr), hex(size)
        cur_pt_st = [pt_name, st_addr, size];
        pt_info_map[pt_name]=cur_pt_st
        pt_info.append(cur_pt_st);

def print_pt_from_sca_info(sca_ori_lines):
    global out_str;
    #write out preheader: preloader gpt.
    common_write_sca_line_number(sca_ori_lines, 0, sca_info[2][1]);
    for cur_pt_st in pt_info:
        print cur_pt_st
        if sca_info_map.has_key(cur_pt_st[0]):
            cur_sca_pt_st=sca_info_map[cur_pt_st[0]];
            cur_pt_str=common_replace_pt_st(cur_pt_st, sca_ori_lines, cur_sca_pt_st)
            out_str = "%s\n%s" % (out_str, cur_pt_str)
        else:
            cur_pt_str=common_new_pt_st(cur_pt_st);
            out_str = "%s\n%s" % (out_str, cur_pt_str)
    
    ##for sgpt:
    if sca_info_map.has_key('sgpt'):
        new_pt=['sgpt', 0xFFFF0004, 0x80000]
        cur_sca_pt_st=sca_info_map[new_pt[0]];
        cur_pt_str=common_replace_pt_st(new_pt, sca_ori_lines, cur_sca_pt_st)
        out_str = "%s\n%s" % (out_str, cur_pt_str)

        


inf=open("MT6580_Android_scatter.txt");
sca_lines=inf.readlines();
inf.close();
############### 1 get sca info ###########
sca_preprocess_for_info(sca_lines);
print "!!!!!!!!!!!!!!! sca done"
############### 2 get pt info ###########
pt_pre_process();
print pt_info
print "!!!!!!!!!!!!!!! target pt done"
print_pt_from_sca_info(sca_lines);




#print out_str
genf=open("outsca.txt", 'w+');
genf.write(out_str);
genf.close();
