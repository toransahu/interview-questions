#!/bin/sh

uptime -p
free -m | awk 'FNR == 2 {usage= $3*100/$2} END {print usage}'
grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'
