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
                print "\t{%f, %d}," % (sheet.col_values(0)[jdx], sheet.col_values(1)[jdx])





read_target_array("input_from_provider.xls")

