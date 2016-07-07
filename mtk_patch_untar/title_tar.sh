#!/bin/bash
echo "" > patch_title


for i in $(seq 1 40)
do
    echo P$i
    ls | grep ".P"$i")" | awk '{print $0;system("tar zxf \""$0"\"")}'
    read_next=0;
    
    
    cat PatchList.txt | while read line
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
    
    rm PatchList.txt
done
