adb shell cat /sys/class/mmc_host/mmc0/mmc0:0001/type
adb shell cat /sys/class/mmc_host/mmc0/mmc0:0001/name
adb shell cat /sys/class/mmc_host/mmc0/mmc0:0001/date
CID=$(adb shell cat /sys/class/mmc_host/mmc0/mmc0:0001/cid)
echo $CID
REV=$(adb shell cat /sys/class/mmc_host/mmc0/mmc0:0001/prv)
echo $REV

if [[ $CID == *"8801034e43617264202"* ]] #8801034e436172642021b21d4e60c297:1548
then
    echo "jbl"
    if [[ $REV == *"0x21"* ]]
    then
        echo "not update firmware"
    else
    	echo "updated already"
    fi
else
    echo "NOT F9 16G EMMC"
fi
