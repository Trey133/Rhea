#!/bin/sh
sudo arp-scan -l --interface=wlan0 --localnet > cyborgspy.txt; nmap -v -A 192.168.1.1-254 >> cyborgspy.txt; passive_discovery6 -D wlan0 >> cyborgspy.txt