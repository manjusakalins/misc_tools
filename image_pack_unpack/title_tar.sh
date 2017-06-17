#!/bin/bash
echo "" > patch_title

GREP_STR="_P"
P_TXT="patch_list.txt"
#$P_TXT="PatchList.txt"

for i in $(seq 1 150)
do
    echo P$i
    ls | grep "_P"$i")" | awk '{print $0;system("tar zxf \""$0"\"")}'
    read_next=0;
    
    
    cat $P_TXT | while read line
    do
        if [ $read_next -eq 1 ]
        then
            if [[ $line == *"[["* ]]
            then
                echo "########## skip "$line
            else
                echo "P$i:  $line"
                echo "P$i:  $line" >> patch_title
            fi
        fi
        
        if [[ $line == *"Title for Customer"* ]] || [[ $line == *"Description:"* ]]
        then
            echo $line;
            read_next=1;
        else
            read_next=0;
        fi;
        
    done;
    
    rm $P_TXT
done

echo ' find . -name "*BPLGUInfoCustomApp_MT6735_S00_MOLY_LR9_*" | sed -n "'"/45/ \!p"'" | awk "'"{system(\"rm \" \$1)}"'" '
#find . -name "*BPLGUInfoCustomApp_MT6735_S00_MOLY_LR9_*" | sed -n '/45/!p' | awk '{system("rm -rf \""$0"\"")}'
