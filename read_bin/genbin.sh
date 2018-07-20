
#cat new1.txt | awk -F" " '{print NF}'
cat new1.txt | sed -e 's/ / ,0x/g' > out2
