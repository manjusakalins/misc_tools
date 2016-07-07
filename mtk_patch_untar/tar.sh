#!/bin/bash
for i in $(seq 1 100)
do
    echo P$i
    ls | grep ".P"$i")" | awk '{print $0;system("tar zxf \""$0"\"")}'
done
