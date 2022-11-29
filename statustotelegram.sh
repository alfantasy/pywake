#!/bin/bash
info_cpu="*CPU*
----------------------
$(cat /proc/loadavg | awk '{print $2" of 100 percents; running processes: "$4}')
"
info_ram="*RAM*
----------------------
Free: $(free -m | grep Mem | awk '{print $4 * 0.001 "MB of " $2 * 0.001 "MB total." $4 * 100 / $2 "% free"}')
"
info_hdd="*HDD*
----------------------
$(df /dev/sda1 -h | grep /dev/sda1 | awk '{print "Free: "$4". Used: "$5"%"}')
"
text=$(printf "$info_cpu$info_ram$info_hdd")
printf '%s\n' "$text" > statustotelegram.txt