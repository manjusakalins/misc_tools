mkbootfs root | minigzip > first.img;mkimage first.img ROOTFS > target_ramdisk.img;
mkbootimg --kernel okernel --ramdisk target_ramdisk.img -o target_boot.img
