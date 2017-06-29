
# Enable WiFi
adb root
adb shell svc wifi enable

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
