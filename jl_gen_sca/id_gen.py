#coding=utf-8
import os
import pickle
import codecs
import sys
import re
import operator
import random



inf=open("id_card_to_birth");
sca_lines=inf.readlines();
inf.close();

for cline in sca_lines:
#    print cline.strip()
    if len(cline) > 15:
        print cline[6:10]+"-"+cline[10:12]+"-"+cline[12:14]
    else:
        print "null"

inf=open("ph");
sca_lines=inf.readlines();
inf.close();
for cline in sca_lines:
    cl =  cline.split();
    print cl[1]
