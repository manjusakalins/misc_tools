#!/bin/bash
while true
do
TT=$(adb shell uptime | awk '{print $3}')
echo $TT
    if [ "$TT" -ge 1 ]; then
        echo $TT"new reboot"
        adb reboot
    fi

sleep 5
done
