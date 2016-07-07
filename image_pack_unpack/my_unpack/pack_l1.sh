mkbootfs root | minigzip > first.img;
mkbootimg --kernel okernel --ramdisk target_ramdisk.img -o target_boot.img
