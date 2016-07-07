#coding=utf-8
import os
import pickle
import codecs
import sys
import xlrd
import xlwt
import re
import operator

import random
import cairo
import pycha.scatter
import pycha.bar
hwocvs=[];
vbats=[];
qs=[];
test_current = 420;
per_test_time_min = 5;
qmax=1680;


perq=per_test_time_min*test_current/60;

def process_xls(xlsf):
    sumq=0;
    wb = xlrd.open_workbook(xlsf);
    for sheet_idx in range(0, len(wb.sheet_names())):
        #print wb.sheet_names()[sheet_idx]
        if wb.sheet_names()[sheet_idx] == "ubootoutput":
            sheet = wb.sheet_by_index(sheet_idx);
            for jdx in range(0, len(sheet.col_values(0))):
                hwocvs.append(sheet.col_values(0)[jdx]);
                vbats.append(sheet.col_values(1)[jdx]);
                qs.append(float(sumq));
                sumq = sumq + perq;
                #print "\t{%f, %f}," % (sheet.col_values(0)[jdx], sheet.col_values(1)[jdx])

#======================================================
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

inputxls=sys.argv[1];
process_xls(inputxls)

print hwocvs
print vbats


book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("all")


for i in range(0, len(hwocvs)):
    sheet1.write(i, 0, hwocvs[i]);
    sheet1.write(i, 1, vbats[i]);
    sheet1.write(i, 2, qs[i]);

sheet1 = book.add_sheet("gen_for_header")
cur_percent=0;
out_hwcvs=[];
out_vbats=[];
out_qs=[];
out_perc=[];

print qs;
for i in range(0, len(qs)):
    if (qs[i]*100/qmax) >=  cur_percent:
        print i,(qs[i]*100/qmax)
        if i == 0:
            out_hwcvs.append(hwocvs[i]);
            out_vbats.append(vbats[i]);
            out_qs.append(qs[i]);
        else:
            cur_ratio = (cur_percent - qs[i-1]*100/qmax) / ((qs[i]-qs[i-1])*100/qmax);
            print cur_ratio;
            out_hwcvs.append(cur_ratio * (hwocvs[i]-hwocvs[i-1]) + hwocvs[i-1]);
            out_vbats.append(float(cur_ratio * (vbats[i]-vbats[i-1]) + vbats[i-1]));
            out_qs.append(cur_percent);
        out_perc.append(cur_percent);
        cur_percent =  cur_percent + 2;

print out_hwcvs;
print out_vbats
print out_qs;

for i in range(0, len(out_qs)):
    print "\t{%d, %d}," % (int(out_perc[i]), int(out_hwcvs[i]));
    
for i in range(0, len(out_qs)):
    print "\t{%d, %d}," % (int((out_hwcvs[i]-out_vbats[i])*1000/test_current), int(out_hwcvs[i]));
book.save("output.xls")

