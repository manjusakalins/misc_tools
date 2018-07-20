#!/usr/bin/env python
#coding=utf-8
import os,sys
from optparse import OptionParser 

'''
使用 main.py -c [system/custom] -d [systemdir/customdir] -C filesystem_config.txt -S file_contexts.bin -o outputfile -l size [-t time] [-s systemdir] 
	option:
		-c : (class)  system/custom
		-d : (directory) systemdir/customdir
		-o : (outputfile) system.img/custom.img
		-l : (long size) image partition size
		-S : (file_contexts.bin)
		-C : (filesystem_config.txt)
		-t : (可选) ota中时间戳,比-s优先
		-s : (可选) systemdir 从build.prop获取timestamp
'''

def ZeroPadSimg(image_file, pad_size):
  blocks = pad_size // BLOCK_SIZE
  print("Padding %d blocks (%d bytes)" % (blocks, pad_size))
  simg = sparse_img.SparseImage(image_file, mode="r+b", build_map=False)
  simg.AppendFillChunk(0, blocks)

if __name__ == '__main__':
    parser = OptionParser(usage="%prog [options]")
    parser.add_option("-c","--class",action="store",type="string",dest="pclass",help="")
    parser.add_option("-d","--directory",action="store",type="string",dest="pdirec",help="")
    parser.add_option("-o","--output",action="store",type="string",dest="poutput",help="")
    parser.add_option("-S","--filecontexts",action="store",type="string",dest="pfilecontext",help="")
    parser.add_option("-l","--size",action="store",type="int",dest="psize",help="")
    parser.add_option("-t","--time",action="store",type="string",dest="ptime",help="")
    parser.add_option("-s","--systemdir",action="store",type="string",dest="psystemdir",help="")
    parser.add_option("-C","--filesystem",action="store",type="string",dest="pfilesystem",help="")
    (options,args)=parser.parse_args()
    if options.pclass:
        if cmp(options.pclass,"system") ==0 or cmp(options.pclass,"custom")==0:
            print "class:",options.pclass
        else:
            print "class only can be system or custom,use -c [system|custom]"
            sys.exit(0)
        
    if not options.pdirec:
        print "have no output file,use -d dirctory"
        sys.exit(0)
    if not options.poutput:
        print "have no output file,use -o outputfile"
        sys.exit(0)
    if not options.pfilecontext:
        print "hava no file_contexts,use -S file_contexts.bin"
        sys.exit(0)
    if not options.psize:
        print "hava no partiton size,use -l size"
        sys.exit(0)
    if options.ptime:
        print "time:",options.ptime
    if options.psystemdir:
        print "systemdir:",options.psystemdir
    os.system("rm -rf verity.img verity_fec.img verity_metadata.img")
    realsize="0"
    if cmp(options.pclass,"system") ==0:
        cmd="python ./bin/system_verity_size.py " + str(options.psize)
        realsize=os.popen(cmd).read().strip() 
    if not options.ptime:
        if options.psystemdir:
            length=len(options.psystemdir)
            if options.psystemdir[length-1] != '/':
                options.psystemdir=options.psystemdir+"/"
            print "propfile=",options.psystemdir+"build.prop"
            propfile=open(options.psystemdir+"build.prop","r")
            for eachLine in propfile:
                if "ro.build.date.utc=" in eachLine:
                    options.ptime=eachLine[18:-1]
                    break
    length=len(options.pdirec)
    print "c=",options.pdirec[length-1]
    if options.pdirec[length-1] == '/':
                options.pdirec=options.pdirec[0:length-1]
    curdir=os.path.abspath('.')
    
    if options.ptime:
        length=len(options.pdirec)
        index=options.pdirec.rfind("/")
        systemoutpath=options.pdirec.strip()
        systempath=options.pdirec.strip()
        if index > 0:
            print "systemoutpath=",systemoutpath
            systemoutpath=options.pdirec[0:index].strip()
            systempath=options.pdirec[index+1:].strip()
            os.chdir(systemoutpath)
        cmd="zip -qry "+options.pclass+".zip " + systempath
        print "cmd=",cmd
        print "curdir=",curdir
        curdir2=os.path.abspath('.')
        print "curdir2=",curdir2
        #os.system(cmd)
        if cmp(options.pclass,"system") ==0:
            os.chdir(curdir)
            #cmd="zipinfo -1 "+systemoutpath+"/system.zip | awk 'BEGIN {FS=\""+systempath+"/\"}/^"+systempath+"\//{print \"system/\" $2}' | ./bin/fs_config -C -D " +systempath+ " -S " + options.pfilecontext +">"+curdir+"/filesystem_config.txt"
            #os.system(cmd)
            #print cmd
            cmd="./bin/make_ext4fs -s -T "+options.ptime+" -S "+options.pfilecontext+" -C "+options.pfilesystem+" -B system.map -L system -l "+realsize+" -a system "+options.poutput+" "+options.pdirec+" "+options.pdirec
            print cmd
            os.system(cmd)
            cmd="./bin/build_verity_tree -A aee087a5be3b982978c923f566a94613496b417f2af592639bc80d141e34dfe7 "+options.poutput+" ./verity.img"
            print cmd
            hashstr=os.popen(cmd).read().strip()
            hashstrs=hashstr.split()
            cmd="python ./bin/build_verity_metadata.py "+realsize+" ./verity_metadata.img "+hashstrs[0]+" " +hashstrs[1]+ " /dev/block/platform/mtk-msdc.0/11230000.msdc0/by-name/system ./bin/verity_signer ./bin/key/verity.pk8"
            print cmd
            os.system(cmd)
            cmd="cat ./verity_metadata.img >> ./verity.img"
            print cmd
            os.system(cmd)
            cmd="./bin/fec -e "+options.poutput+" ./verity.img ./verity_fec.img"
            print cmd
            os.system(cmd)
            cmd="cat ./verity_fec.img >> ./verity.img"
            print cmd
            os.system(cmd)
            cmd="./bin/append2simg "+options.poutput+" ./verity.img"
            print cmd
            os.system(cmd)
            #cmd="./bin/simg2img "+options.poutput+" ./unsparse_system.img"
            #print "cmd",cmd
            #os.system(cmd)
            #cmd="./bin/e2fsck -f -n ./unsparse_system.img"
            #print "cmd",cmd
            #os.system(cmd)
        elif cmp(options.pclass,"custom") ==0:
            length=len(options.pdirec)
            index=options.pdirec.rfind("/")
            customoutpath=options.pdirec[0:index]
            custompath=options.pdirec[index+1:]
            os.chdir(customoutpath)
            cmd="zip -qry "+options.pclass+".zip " + custompath
            print cmd
            os.system(cmd)
            cmd="zipinfo -1 " + options.pclass+".zip | awk 'BEGIN {FS=\""+custompath+"/\"}/^"+custompath+"\//{print \"custom/\" $2}' | ./bin/fs_config -C -D " +systempath+ " -S "  + options.pfilecontext +">"+curdir+"/custom_filesystem_config.txt"
            os.system(cmd)
            print cmd
            os.chdir(curdir)
            cmd="./bin/make_ext4fs -s -T "+options.ptime+" -S "+options.pfilecontext+" -C custom_filesystem_config.txt -B custom.map -L custom -l "+str(options.psize)+" -a custom "+options.poutput+" "+options.pdirec
            print cmd
            os.system(cmd)
    else:
        if cmp(options.pclass,"system") ==0:
            cmd="./bin/make_ext4fs -s -T -1 -S "+options.pfilecontext+" -L system -l "+realsize+" -a system "+options.poutput+" "+options.pdirec+" "+options.pdirec
            #cmd="./bin/mkuserimg.sh -s "+options.pdirec+" "+options.poutput+" ext4 system "+realsize+" -D "+options.pdirec+" -L system "+options.pfilecontext
            print cmd
            os.system(cmd)
            cmd="./bin/build_verity_tree -A aee087a5be3b982978c923f566a94613496b417f2af592639bc80d141e34dfe7 "+options.poutput+" ./verity.img"
            print cmd
            hashstr=os.popen(cmd).read().strip()
            hashstrs=hashstr.split()
            cmd="python ./bin/build_verity_metadata.py "+realsize+" ./verity_metadata.img "+hashstrs[0]+" " +hashstrs[1]+ " /dev/block/platform/mtk-msdc.0/11230000.msdc0/by-name/system ./bin/verity_signer ./bin/key/verity.pk8"
            print cmd
            os.system(cmd)
            cmd="cat ./verity_metadata.img >> ./verity.img"
            print cmd
            os.system(cmd)
            cmd="./bin/fec -e "+options.poutput+" ./verity.img ./verity_fec.img"
            print cmd
            os.system(cmd)
            cmd="cat ./verity_fec.img >> ./verity.img"
            print cmd
            os.system(cmd)
            cmd="./bin/append2simg "+options.poutput+" ./verity.img"
            print cmd
            os.system(cmd)
        elif cmp(options.pclass,"custom") ==0:
            #cmd="./bin/make_ext4fs -s -T -1 -S "+options.pfilecontext+" -L custom -l "+str(options.psize)+" -a custom "+options.poutput+" "+options.pdirec
            cmd="./bin/make_ext4fs -s -T -1 -S "+options.pfilecontext+" -l "+str(options.psize)+" -a custom "+options.poutput +" "+options.pdirec #未接lable
            print cmd
            os.system(cmd)
        #print "cmd=",cmd
        #os.system(cmd)
        
        #cmd="make_ext4fs -s -T "+ options.ptime + " -S "+options.pfilecontext + " -C /tmp/targetfiles-9n4mjU/META/filesystem_config.txt -B "+options.pclass+".map -L " +options.pclass+ " -l "+realsize+" -a "+options.pclass+"  " +options.poutput+ " " +options.pdirec
    
