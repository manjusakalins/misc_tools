#coding=utf-8
import os
import pickle
import codecs
import sys
import _io
import os
import pickle
import codecs
import sys
import re
import operator
import random
import csv
import json
import subprocess
from pprint import pprint

f = open('pll.c', 'r');
in_lines=f.readlines();
f.close();
pakey = ["pllc1_mempll_n_info_30_24_n4",	
"pllc1_mempll_n_info_23_0_n4",	
"mempll2_m4pdiv_1_0",
"mempll2_fbdiv_6_0",		
"mempll3_m4pdiv_1_0",
"mempll3_fbdiv_6_0",
"mempll4_m4pdiv_1_0",
"mempll4_fbdiv_6_0",]
print pakey

pll=[533,800,1066,912,1000,1110, 1172];
out_st={};
out_cur_idx="";
cur_pl_plist={};

def jlink_fix_define_to_case(lines):
    lines = sorted(lines);
    for line in lines:
        names = line.split()[1]
        values = line.split("(")[1]
        #print names, values
        print "\t\t\t%s = (%s;" % (names, values)

for line in in_lines:
    for pl in pll:
        cur_pl_key = "DDR%d" % pl;
        #print cur_pl_key
        if line.find(cur_pl_key) != -1:
            out_cur_idx = cur_pl_key;
            if out_st.has_key(out_cur_idx):
                cur_pl_plist = out_st[out_cur_idx];
            else:
                cur_pl_plist = out_st[out_cur_idx] = {};
            continue;
    for k in pakey:
        if line.find(k) != -1:
            if cur_pl_plist.has_key(k):
                continue;
            else:
                cur_pl_plist[k] = line.strip();

pprint(out_st)
for pl in pll:
    cur_pl_key = "DDR%d" % pl;
    if out_st.has_key(cur_pl_key):
        print "\t\tcase %d:" % pl;
        vs = out_st[cur_pl_key].values();
        #pprint(vs)
        jlink_fix_define_to_case(vs)
        print "\t\t\tbreak;"
    
