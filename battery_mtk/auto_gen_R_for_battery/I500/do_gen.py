#coding=utf-8
import os
import pickle
import codecs
import sys
import xlrd
import re
import operator

array_soc_vbat_provider=[];

#read all details in excel into excel_all_hw
def read_target_array(detailf):
    wb = xlrd.open_workbook(detailf);
    #print wb.sheet_names();
    #start parse per hw type
    for sheet_idx in range(0, len(wb.sheet_names())):
        #print wb.sheet_names()[sheet_idx]
        if wb.sheet_names()[sheet_idx] == "vbat-soc":
            sheet = wb.sheet_by_index(sheet_idx);
            #print sheet
            for jdx in range(0, len(sheet.col_values(0))):
                print "\t{%f, %f}," % (sheet.col_values(0)[jdx], sheet.col_values(1)[jdx])
            #for jdx in range(0, len(sheet.col_values(0))):
            #    print "\t{%f, %d}," % (sheet.col_values(1)[jdx]/15.80, int(sheet.col_values(0)[jdx]*1000))
            cur=0;
            for jdx in range(0, len(sheet.col_values(0))):
                if int(sheet.col_values(1)[jdx]/15.80) == cur:
                    print "\t{%d, %d}," % (sheet.col_values(1)[jdx]/15.80, int(sheet.col_values(0)[jdx]*1000)+60)
                    #print "\t{%d, %d}," % (98, int(sheet.col_values(0)[jdx]*1000)+60)
                    cur+=2;





read_target_array("input_from_provider.xls")

