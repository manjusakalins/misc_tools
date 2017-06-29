
# Enable WiFi
adb root
adb shell svc wifi enable

PRE_CMD="adb shell"
#$PRE_CMD touch /data/misc/wifi/fwpath
$PRE_CMD "echo \"sta_mode\" > /data/misc/wifi/fwpath"

$PRE_CMD chown wifi.wifi /data/misc/wifi/fwpath

$PRE_CMD chmod 0777 /data/misc/wifi/*

$PRE_CMD insmod /system/lib/modules/sprdwl.ko

$PRE_CMD wcnd_cli wcn poweron

$PRE_CMD wcnd_cli wcn WIFI-OPEN

$PRE_CMD ifconfig wlan0 up

$PRE_CMD /system/bin/wpa_supplicant -Dnl80211 -iwlan0 -C/data/misc/wifi/sockets -c/data/misc/wifi/wpa_supplicant.conf -dd &
sleep 4
echo "start add"
$PRE_CMD wpa_cli -iwlan0 -p/data/misc/wifi/sockets add_network 0
echo "name"
$PRE_CMD wpa_cli -iwlan0 -p/data/misc/wifi/sockets set_network 0 ssid "TP-LINK_580E4E"

$PRE_CMD wpa_cli -iwlan0 -p/data/misc/wifi/sockets set_network 0 key_mgmt WPA-PSK
echo "key"
$PRE_CMD wpa_cli -iwlan0 -p/data/misc/wifi/sockets set_network 0 psk "jl123456"

$PRE_CMD wpa_cli -iwlan0 -p/data/misc/wifi/sockets set_network 0 priority 3

$PRE_CMD wpa_cli -iwlan0 -p/data/misc/wifi/sockets enable_network 0

$PRE_CMD wpa_cli -iwlan0 -p/data/misc/wifi/sockets status

#$PRE_CMD wcnd_cli wcn WIFI-CLOSE

#$PRE_CMD wcnd_cli wcn poweroff
