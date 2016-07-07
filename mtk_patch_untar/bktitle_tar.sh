#!/bin/bash
echo "" > patch_title


for i in $(seq 1 22)
do
    echo P$i
    ls | grep ".P"$i")" | awk '{print $0;system("tar zxf \""$0"\"")}'
    read_next=0;
    
    
    cat PatchList.txt | while read line
    do
        if [ $read_next -eq 1 ]
        then
            echo "P$i:  $line"
            echo "P$i:  $line" >> patch_title
        fi
        
        if [[ $line == *"Title for Customer"* ]]
        then
            echo $line;
            read_next=1;
        else
            read_next=0;
        fi;
    done;
    
    rm PatchList.txt
done
