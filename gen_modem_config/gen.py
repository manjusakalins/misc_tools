#coding=utf-8
import os
import pickle
import codecs
import sys
import re
import operator
import random

outstr=""
inf=open(sys.argv[1]);
inlines = inf.readlines();
inf.close();
print inlines;
for cline in inlines:
    #print cline.split();
    clist=cline.split();
    if len(clist) >= 2:
        outstr="%s\n%s = %s" %(outstr, clist[0], clist[1])
        
print outstr
of=open("out","w+")
of.write(outstr);
of.close();
