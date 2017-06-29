
echo "usage: xx.sh internal_time usb_iserial"
echo $#
while true
do
	tmpname=$RANDOM
	if [ $# -ge 2 ]
	then
		echo aaaaaa
		adb -s $2 shell screencap /data/out_$tmpname.png
		adb -s $2 pull /data/out_$tmpname.png
	else
		adb shell screencap /data/out_$tmpname.png
		adb pull /data/out_$tmpname.png
	fi

	if [ -f out_$tmpname.png ]
	then
		eog out_$tmpname.png &
	fi


	if [ $# -ge 1 ]
	then
		sleep $1
	else
		sleep 4
	fi
	sudo rm out_$tmpname.png
done
