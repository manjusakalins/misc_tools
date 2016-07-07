#!/bin/bash

#Modify this with your IP range
MY_IP_RANGE="192\.168\.1"

#You usually wouldn't have to modify this
PORT_BASE=5555

#List the devices on the screen for your viewing pleasure
adb devices
echo

#Find USB devices only (no emulators, genymotion or connected devices
declare -a deviceArray=(`adb devices -l | grep -v emulator | grep -v vbox | grep -v "${MY_IP_RANGE}" | grep " device " | awk '{print $1}'`)  

echo "found ${#deviceArray[@]} device(s)"
echo

for index in ${!deviceArray[*]}
do
    echo "finding IP address for device ${deviceArray[index]}"
    IP_ADDRESS=$(adb -s ${deviceArray[index]} shell ifconfig wlan0 | grep "255.255")
    if [[ $IP_ADDRESS == *"inet addr"* ]]
    then
        IP_ADDRESS=$(echo $IP_ADDRESS | awk '{print $2}' | awk -F":" '{print $2}')
    elif [[ $IP_ADDRESS == *"ip"* ]]
    then
        IP_ADDRESS=$(echo $IP_ADDRESS | awk '{print $3}')
    else
        echo "not regconize ip string"
        echo $IP_ADDRESS
    fi

    echo "IP address found : $IP_ADDRESS "
    echo ${#IP_ADDRESS}

    echo "Connecting..."
    adb -s ${deviceArray[index]} tcpip $(($PORT_BASE + $index))
    adb -s ${deviceArray[index]} connect "$IP_ADDRESS:$(($PORT_BASE + $index))"

    echo
    echo
done

adb devices -l
#exit
