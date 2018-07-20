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

f = open('./out2', 'r');
in_lines=f.readlines();
f.close();
wf = open("outbin22", "wb")
print len(in_lines);

for iline in in_lines:
    #print iline
    inums = iline.split(",")
    inums=inums[0:len(inums)]
    for nu in inums:
        print int(nu,16)
        wf.write(chr(int(nu,16)));
wf.close();
