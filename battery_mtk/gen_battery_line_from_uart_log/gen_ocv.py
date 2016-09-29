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

#FIXME: MODIFY MAX Q
max_q = 3100
g_print_h=0;


time_soc_dataset=[];
time_count_name=[];
time_count_valset=[];

input_f=sys.argv[1];
input_dir=input_f[:input_f.rfind('/')]
print input_dir
f=open(input_f, 'r');
lines=f.readlines();

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_target_val(line, split):
    cmd = '''echo "%s" | awk -F '%s' '{print $2}'  ''' % (line, split)
    ret = os.popen(cmd).readlines()[0].strip().split(",")[0];
    #print ret;
    return ret;

########## jlink_show_done_record 2437 ##########: ocv: 4211, cur: 9042, t: 512, size: 30 bvbat: 4137, vbat:(4096,4034)(4096 4043)
record_start=0;
top_rec=[];
cur_rec={};
sum_q=0;
stop_sumq=0;
real_rec_num=0;
for cur_line in lines:
    if cur_line.find('jlink_show_done_record') != -1:
        print cur_line
        record_start=1;
        cur_rec["ocv"] = int(get_target_val(cur_line, "ocv:"));
        cur_rec["cur"] = int(get_target_val(cur_line, "cur:"));
        cur_rec["time"] = int(get_target_val(cur_line, "t:"));
        cur_rec["size"] = int(get_target_val(cur_line, "size:"));
        cur_rec["bvbat"] = int(get_target_val(cur_line, "bvbat:"));
        cur_rec["dis_q"] = cur_rec["time"]*cur_rec["cur"]/3600;
        if cur_rec["time"] > 13:
            sum_q = sum_q + cur_rec["dis_q"];
            real_rec_num = real_rec_num + 1;

        continue;
    if record_start == 1:
        cur_vbat = cur_line.split(",");
        cur_rec["vbats"]=cur_vbat;
        record_start = 2;
        continue;
    if record_start == 2:
        cur_mvbat = cur_line.split(",");
        cur_rec["mvbat"]=cur_mvbat;

        record_start = 3;
        if stop_sumq != 1:
            for vidx in range(len(cur_mvbat)):
                if RepresentsInt(cur_mvbat[vidx]):
                    if int(cur_mvbat[vidx]) < 3450:
                        print ":stop"
                        stop_sumq=1;
                        sum_q = sum_q - cur_rec["dis_q"]*(len(cur_mvbat)-vidx)/len(cur_mvbat);
                        break;
                    

    if record_start == 3:
        print cur_rec
        top_rec.append(cur_rec);
        cur_rec={};
        record_start = -1;

print sum_q
print len(top_rec)
print real_rec_num;
real_max_q = sum_q/10;
#print top_rec
sum_q = top_rec[0]["cur"] * top_rec[0]["time"] / 36000;

if g_print_h == 0:
    out_ocv = "battery_profile_t2_num = <77>;\nbattery_profile_t2 = <0 %d\n" % top_rec[0]["ocv"]
    out_r = "r_profile_t2_num = <77 >;\nr_profile_t2 = <0 %d\n" % top_rec[0]["ocv"]
else:
    out_ocv="//start define\nBATTERY_PROFILE_STRUC lk_py_battery_ocv_%dmah[] =\n{\n{0, %d},\n" % (max_q,top_rec[0]["ocv"]);
    out_r="R_PROFILE_STRUC lk_py_r_%dmah[] =\n{\n{0, %d},\n" % (max_q,top_rec[0]["ocv"]);


for idx in range(1,77):   
    if idx < len(top_rec) :
        #print top_rec[idx-1]["size"] - 1

        r = (top_rec[idx]["ocv"] - int(top_rec[idx-1]["vbats"][top_rec[idx-1]["size"] - 1]))*10000/top_rec[idx-1]["cur"]
        dq = top_rec[idx]["cur"] * top_rec[idx]["time"] / 36000
        #print top_rec[idx]["ocv"],int(top_rec[idx-1]["vbats"][top_rec[idx-1]["size"] - 1]), sum_q, r, (sum_q*1000/max_q + 5)/10
    
        #print (sum_q*1000/max_q + 5)/10, (float(sum_q)*100/float(max_q)), top_rec[idx]["ocv"], top_rec[idx]["dis_q"]

        if g_print_h == 0:
            out_ocv="%s%d %d\n" % (out_ocv, (sum_q*1000/real_max_q + 5)/10, top_rec[idx]["ocv"])
        else:
            out_ocv="%s{%d, %d},\n" % (out_ocv, (sum_q*1000/real_max_q + 5)/10, top_rec[idx]["ocv"])

        if g_print_h == 0:
            out_r="%s%d %d\n" % (out_r, r, top_rec[idx]["ocv"])
        else:
            out_r="%s{%d, %d},\n" % (out_r, r, top_rec[idx]["ocv"])
        sum_q = sum_q + dq;
    else:
        if g_print_h == 0:
            out_ocv="%s100 3212\n" % out_ocv;
        else:
            out_ocv="%s{100, 3212},\n" % out_ocv;

        if g_print_h == 0:
            out_r="%s180 3212\n" % out_r;
        else:
            out_r="%s{180, 3212},\n" % out_r;


if g_print_h == 0:
    out_ocv = "%s>;\n" % out_ocv
    out_r = "%s>;\n" % out_r
else:
    out_ocv="%s};\n" % out_ocv;
    out_r="%s};\n" % out_r;

#print out_ocv
#print out_r

if g_print_h == 0:
    out_file=input_dir + "/lk_ocv.dtsi"
else:
    out_file=input_dir + "/lk_ocv_out"
genf=open(out_file, 'w+');
genf.write(out_ocv);
genf.write(out_r);
genf.close();

