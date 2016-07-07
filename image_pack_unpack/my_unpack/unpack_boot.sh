#!/bin/bash
kernel_size=`od -A n -t d -j 8 -N 4 $1 | sed 's/ //g'`
echo $kernel_size

dd if=$1 of=okernel bs=1 skip=2048 count=$kernel_size

start_ramdisk=$((((($kernel_size+2048)>>11)+1)<<11))
echo $start_ramdisk

dd if=$1 of=oramdisk bs=1 skip=$start_ramdisk

dd if=oramdisk of=ooramdisk.img bs=1 skip=512
rm -rf root
mkdir root
cd root
gunzip -c ../ooramdisk.img | cpio -i

