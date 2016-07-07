adb remount;
adb push new_pwr /system/bin/vtservice
adb push autoreboot.sh /data/auto_test_monkey.sh

adb shell ps | grep vtservice  | awk '{system("adb shell kill "$2)}'

adb shell ps | grep " sh"


