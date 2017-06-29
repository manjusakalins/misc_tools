
# Enable WiFi
adb root
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
$PRE_CMD svc wifi enable
adb shell
# Get to wpa_cli prompt
wpa_cli -p /data/misc/wifi/sockets/ -i wlan0

# Add new WiFi network
add_network
set_network 0 auth_alg OPEN
set_network 0 key_mgmt WPA-PSK
set_network 0 ssid "TP-LINK_580E4E"
set_network 0 proto RSN
set_network 0 mode 0
set_network 0 psk "jl123456"

# Connect to it
select_network 0
enable_network 0
reassociate

# Check the status
status

#$PRE_CMD wcnd_cli wcn WIFI-CLOSE

#$PRE_CMD wcnd_cli wcn poweroff
