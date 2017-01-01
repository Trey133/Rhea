#!/bin/sh

arp-scan -l --interface=wlan0 --localnet > testsh.txt; nmap -v -A 192.168.1.1-254 >> testsh.txt; 
