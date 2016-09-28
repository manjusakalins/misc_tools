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
time_soc_dataset=[];
time_count_name=[];
time_count_valset=[];

inputlog=sys.argv[1];

#for mtk
#using d5
cmd = '''cat %s | grep AvgVbat | awk -F '.' '{print $1}' | awk -F '[' '{print $2}' | tee pylog_time ''' % inputlog
list_time = os.popen(cmd).readlines()
cmd = '''cat %s | grep AvgVbat | awk -F 'AvgVbat=' '{print $2}' | awk -F '(' '{print $2}' | awk -F ')' '{print $1}'  | tee pylog_soc ''' % inputlog
list_soc=os.popen(cmd).readlines()

#using d2
#cmd = '''cat %s | grep oam_result_inf | awk -F '.' '{print $1}' | awk -F '[' '{print $2}' | tee pylog_time ''' % inputlog
#list_time = os.popen(cmd).readlines()
#cmd = '''cat %s | grep oam_result_inf | awk -F ',' '{print $2}' ''' % inputlog
#list_soc=os.popen(cmd).readlines()

print len(list_soc)
print len(list_time)
# for sprd
#cmd = '''cat %s | grep ,cap: | awk -F '.' '{print $1}' | awk -F '[' '{print $2}' | tee pylog_time ''' % inputlog
#list_time = os.popen(cmd).readlines()

#cmd = '''cat %s | grep ,cap: | awk -F ',cap:' '{print $2}' | awk -F ',' '{print $1}' | tee pylog_soc ''' % inputlog
#using d2
#cmd = '''cat %s | grep oam_result_inf | awk -F ',' '{print $2}' ''' % inputlog
#list_soc=os.popen(cmd).readlines()

for i in range(0, len(list_time)):
    list_time[i]=list_time[i].rstrip('\\n').strip();
for i in range(0, len(list_soc)):
    list_soc[i]=list_soc[i].rstrip('\\n').strip();

#excel sheet1
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("time-soc")
for i in range(0, len(list_time)):
    sheet1.write(i, 0, list_time[i]);
for i in range(0, len(list_soc)):
    sheet1.write(i, 1, list_soc[i]);


#excel sheet2
sheet2=book.add_sheet("soc_counts")
mset={};
for i in range(0, len(list_soc)):
    mset[list_soc[i]] = 0;
for i in range(0, len(list_soc)):
    if isinstance(mset[list_soc[i]], int):
        mset[list_soc[i]] = mset[list_soc[i]] + 1;

sort_item=mset.items();
sort_item.sort();
#for key,value in sort_item:
#    print "%s = %d" % (key, value)
idx=0;
for key,value in sort_item:
    sheet2.write(idx, 0, key);
    sheet2.write(idx, 1, value);
    idx=idx+1;

book.save("gen_xls.xls")

#======================================================
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

base_time = int(list_time[0]);
print "base time: " + str(base_time)
#for line png
for i in range(0, len(list_soc)):
    cur_soc=list_soc[i];
    cur_time=list_time[i];

    if cur_soc.isdigit():
        cur_soc=int(cur_soc);
        if cur_soc < 3200:
            cur_soc = 3200
        if cur_soc > 4400:
            cur_soc = 4250;
    else:
        cur_soc=3200

    if cur_time.isdigit():
        tmpval=((int(cur_time)-base_time)/10,cur_soc-3200)
        time_soc_dataset.append(tmpval);
print time_soc_dataset


##start to gen ocv table?
same_r = 105;
same_i = 700;
total_time = time_soc_dataset[len(time_soc_dataset)-1][0]
cap_diff = 90;
ocv_max=4082
ocv_min=3530

per_unit = total_time/cap_diff+2;
cnt=0;
for vals in time_soc_dataset:
    if vals[0] > cnt*per_unit:
        print "%d, %d  %d" % (cnt+10, vals[1]+3200 + same_r*same_i/1000, vals[1]+3200)
        cnt=cnt+1;

cnt=0;
for vals in time_soc_dataset:
    if vals[0] > cnt*per_unit:
        if cnt%2==0:
            print "{%d, %d}," % (cnt+10, vals[1]+3200 + same_r*same_i/1000)
        cnt=cnt+1;
##################################################
'''
	{0   , 4179},         
	{2   , 4155},         
	{4   , 4136},         
	{6   , 4118},         
	{8   , 4098},         
	{10  , 4082},         
	{12  , 4065},         
	{14  , 4048},         
	{16  , 4029},         
	{18  , 4014},         
	{20  , 4000},         
	{22  , 3986},         
	{24  , 3973},         
	{26  , 3959},         
	{28  , 3946},         
	{30  , 3936},         
	{32  , 3924},         
	{34  , 3914},         
	{36  , 3901},         
	{38  , 3889},         
	{40  , 3867},         
	{42  , 3850},         
	{44  , 3837},         
	{46  , 3827},         
	{48  , 3819},         
	{50  , 3812},         
	{52  , 3806},         
	{54  , 3800},         
	{56  , 3796},         
	{58  , 3791},         
	{60  , 3788},         
	{62  , 3781},         
	{64  , 3778},         
	{66  , 3777},         
	{68  , 3774},         
	{70  , 3771},         
	{72  , 3769},         
	{74  , 3762},         
	{76  , 3755},         
	{78  , 3746},         
	{80  , 3739},         
	{82  , 3730},         
	{84  , 3718},         
	{86  , 3704},         
	{88  , 3688},         
	{90  , 3681},         
	{92  , 3677},         
	{94  , 3670},         
	{96  , 3644},         
	{98  , 3562},         
	{100 , 3408},         
	{100 , 3349}, 
'''

#for bar
bar_sort_item={};
for key,value in sort_item:
    if RepresentsInt(key):
        bar_sort_item[int(key)]=value;
#print bar_sort_item;

out_item=[]
for k,v in zip(bar_sort_item.iterkeys(),bar_sort_item.itervalues()):
    if int(k) <= 100:
        out_item.append((str(k),v))
#print out_item;
#==============================================
# gen png
def scatterplotChart(output):
    global time_soc_dataset
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1920, 1080)
    #surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 6920, 4080)

    top = 2
    dataSet = (
        ('points 1', [(i, random.random() * float(top)) for i in range(top)]),
        )
    #print dataSet
    dataSet=(('points 1',time_soc_dataset),);
    #print dataSet
    options = {
        'background': {
            'color': '#eeeeff',
            'lineColor': '#444444',
        },
        'colorScheme': {
            'name': 'rainbow',
            'args': {
                'initialColor': 'blue',
            },
        },
        'legend': {
            'hide': True,
        },
        'title': u'Scatter plot',
    }
    chart = pycha.scatter.ScatterplotChart(surface, options)

    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png(output)



def barChart(output, chartFactory):
    lines=tuple(out_item);
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1920, 1080)

    dataSet = (
        ('lines', [(i, l[1]) for i, l in enumerate(lines)]),
        )
    print dataSet
    print lines
    namesdd=[dict(v=i, label=l[0]) for i, l in enumerate(lines)]
    print namesdd
    #for i, l in enumerate(lines):
    #dataSet= (('lines', sort_item),);
    #print dataSet
    #print sort_item
    options = {
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(lines)],
                'label': 'Files',
                'rotate': 25,
            },
            'y': {
                'tickCount': 4,
                'rotate': 25,
                'label': 'Lines'
            }
        },
        'background': {
            'chartColor': '#ffeeff',
            'baseColor': '#ffffff',
            'lineColor': '#444444'
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'red',
            },
        },
        'legend': {
            'hide': True,
        },
        'padding': {
            'left': 0,
            'bottom': 0,
        },
        'title': 'Sample Chart'
    }
    chart = chartFactory(surface, options)

    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png(output)

scatterplotChart('discharge_curve.png');
#barChart('discharge_bar.png', pycha.bar.VerticalBarChart)

