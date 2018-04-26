#coding=utf-8
import os
import pickle
import codecs
import sys
import re
import operator
import random


inf=open(sys.argv[1]);
pt_lines=inf.readlines();
inf.close();


#allow vtservice debugfs_ged:file { write open };
#we define g_sep['vtservice debugfs_ged:file'] = { 'operation1':1, 'operation2':1 } map
g_sep={}

def get_target_val(line, st_split, end_split):
    cmd = '''echo "%s" | awk -F '%s' '{print $2}'  | awk -F '%s' '{print $1}'  ''' % (line, st_split, end_split)
    ret = os.popen(cmd).readlines()[0].strip().split(",")[0];
    #print ret;
    return ret;

#avc: denied { read } for pid=122 comm="read_kmsg" name="DCIM" dev="fuse" ino=6 scontext=u:r:kernel:s0 tcontext=u:object_r:fuse:s0 tclass=dir permissive=0
for cline in pt_lines:
    print cline;
    if len(cline) < 10:
        continue;
    sc=get_target_val(cline, "scontext=u:r:", ":");
    tc=get_target_val(cline, "tcontext=u:object_r:", ":");
    if (len(tc) == 0):
        tc=get_target_val(cline, "tcontext=u:r:", ":");
    tclass=get_target_val(cline, "tclass=", " ");
    oper=get_target_val(cline, "{ ", " }");
    key='%s %s:%s' %(sc, tc, tclass);
    if g_sep.has_key(key):
        ori_list=g_sep[key];
        ori_list[oper]=1;
        g_sep[key]=ori_list;
    else:
        nlist={};
        nlist[oper]=1;
        g_sep[key]=nlist;
        

print g_sep
for key in g_sep.keys():
    #print key;
    opers=""
    val=g_sep[key];
    for oper in val.keys():
        opers="%s %s" % (opers, oper)
    print "allow " + key + "{ " + opers + " };"
    
