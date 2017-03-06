#!/bin/bash
echo "" > patch_title


for i in $(seq 1 140)
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

echo ' find . -name "*BPLGUInfoCustomApp_MT6735_S00_MOLY_LR9_*" | sed -n "'"/45/ \!p"'" | awk "'"{system(\"rm \" \$1)}"'" '

echo "replace mk file verno"
#ls | sed -n '/)/ !p' | awk '{system( " sed -i '"'"'s/MOLY.LR9.W1444.MD.LWTG.MP.V110.5/MOLY.LR9.W1444.MD.LWTG.MP.V110.5.P45/g'"'"' "$1)}'

