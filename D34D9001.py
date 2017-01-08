#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import time
import webbrowser
import re
import urllib
import urllib2
import sys
import random
import numpy as np
import math
import subprocess
import future
import requests
#############################################################
### IMPORT ###                                            ###
import psych#.PY     ### ZUES' RESPONSES                  ###
import bot#.PY       ### ZUES' FUNCTIONS                  ###
### FROM /USR/BIN/RHEA ###                                ###
#############################################################
### THESE FILES HOLD OUR FUNCTIONS AND RESPONSES FOR ZUES ###
#############################################################
#############################################################
###   import image_scraper ### [THIS IS NEEDED FOR (1) COMMAND.]
#############################################################
from lxml import html
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
### THIS PROGRAM WILL NOT FUNCTION PROPERLY IF NOT RUN AS 'ROOT'
os.system('sudo')
### LOGIN SCREEN
os.system('clear')
os.system('python /usr/bin/rhea/dc.py')
import config
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Deadpool.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
while True:
    with open("Deadpoolconv.txt", "a") as myfile:
        myfile.write("\nZues started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
    with open("Deadpool.log", "a") as myfile:
        myfile.write("\nZues started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
###############################################################
### LOAD FUNCTION 'LOCK()' FROM FILE 'BOT.PY'
    bot.lock()
###############################################################
    print("Login:")
    username = raw_input("Username: ")
    if username == config.username:
        print("Sounds Legit...")
    else:
        bot.dp()
        with open("Deadpool.log", "a") as myfile:
            myfile.write("\nZues terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to Incorrect Username.\n")
        print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
### IF USERNAME IS INCORRECT, TERMINATE PROGRAM
        quit()
    bot.dp()
### DO NOT PRINT PASSWORD TO STDOUT [DON'T DISPLAY IT ON THE SCREEN AS YOU TYPE]
    os.system("stty -echo")
    password = raw_input("Please Enter Password: ")
### TURN PRINT TO STDOUT BACK ON 
    os.system("stty echo")
    print("\n")
    if password == config.password:
        bot.unlock()
        os.system("gpg -e -r Ender /usr/bin/rhea/config.py --output '/usr/bin/rhea/config.py.gpg' ")
	os.system('rm config.py')
        os.system('rm config.pyc')
	os.system('clear')
        print("Access Granted")
        print("Please Wait While System Loads...")
### WAIT FOR (2) SECONDS BEFORE CONTINUING
        time.sleep(2)
        break
    else:
        bot.dp()
        print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
        with open("Deadpool.log", "a") as myfile:
            myfile.write("\nDeadpool terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to Incorrect Username.\n")
### IF PASSWORD IS INCORRECT, TERMINATE PROGRAM
        os.system("gpg -e -u Ender /usr/bin/rhea/config.py --output '/usr/bin/rhea/config.py.gpg' ")
        os.system('rm config.py')
        os.system('rm config.pyc')
	os.system('clear')
        quit()
### PROGRAM INTRODUCTION
bot.dp()
os.system("toilet D34D9001")
time.sleep(5)
os.system('clear')
bot.dp()
name = raw_input("What is your name? ")
with open("Deadpool.log", "a") as myfile:
    myfile.write("\nDeadpool started by:  " + name + "\n")
with open("Deadpoolconv.txt", "a") as myfile:
    myfile.write("\nDeadpool started by:  " + name + "\n")
print("Hello, " + name + ". my name is D34D900l.")
time.sleep(2)
bot.dp()
print("What scum bags are we takin' out today?")
time.sleep(2)
os.system('clear')
bot.dp()
print("type 'quit' to exit program")
print("type '?' for help")
### START OF MAIN PROGRAM
while True:
    statement = raw_input(">")
    os.system('clear')
    bot.dp()
### ANALYZE USER INPUT AND RETURN REPONSE FROM PSYCH.PY
    print(bot.analyze(statement))
########################################################
### ?
########################################################
    if statement == "?":
        bot.dp()
        print("Loading available commands, " + name)
        time.sleep(3)
### LOAD BASH SCRIPT CONTAINING LIST OF COMMANDS WITH DESCRIPTIONS
        os.system('sh /usr/bin/rhea/zuescomphelp.sh')
########################################################
### RESTART
########################################################
    elif statement == "restart":
        bot.dp()
        print('Restarting. Please wait, ' + name)
        time.sleep(2)
### RESTART DEADPOOL WITHOUT HAVING TO EXIT AND RELOAD PROGRAM
        os.execv(sys.executable, ['python'] + sys.argv)
########################################################
### SCRIPT
########################################################
    elif statement == "script":
	bot.dp()
	os.system("read -p 'Enter Ouput File Name: ' name ; script $name")
########################################################
### C
########################################################
    elif statement == "c":
	bot.dp()
	os.system("read -p 'Enter Bash Command: ' cmd ; $cmd")
########################################################
### MACCHANGE
########################################################
    elif statement == "macchange":
        bot.dp()
        print("Let's change the mac address real quick, " + name + ".")
        time.sleep(2)
        os.system('/usr/bin/macchanger')
########################################################
### AIROLIB
########################################################
    elif statement == "airolib":
	bot.dp()
	os.system('usr/bin/airolib-ng')
########################################################
### AIRDECLOAK
########################################################
    elif statement == "airdecloak":
        bot.dp()
        os.system('usr/bin/airdecloak-ng')
########################################################
### AIRDECAP
########################################################
    elif statement == "airdecap":
        bot.dp()
        os.system('usr/bin/airdecap-ng')
########################################################
### AIRCRACK
########################################################
    elif statement == "aircrack":
        bot.dp()
        os.system('usr/bin/aircrack-ng')
########################################################
### ANDROID BRUTEFORCE ENCRYPTION
########################################################
    elif statement == "abe":
        bot.dp()
        os.system('usr/bin/android-bruteforce-encryption')
########################################################
### ARP FINGERPRINT 
########################################################
    elif statement == "arpfinger":
        bot.dp()
        os.system('usr/bin/arp-fingerprint')
########################################################
### AUTOPSY
########################################################
    elif statement == "autopsy":
        bot.dp()
        os.system('usr/bin/autopsy')
########################################################
### BACKDOOR FACTORY
########################################################
    elif statement == "backdoor":
        bot.dp()
        os.system('usr/bin/backdoor-factory')
########################################################
### BACKFUZZ
########################################################
    elif statement == "backfuzz":
        bot.dp()
        os.system('usr/bin/backfuzz')
########################################################
### BEEF
########################################################
    elif statement == "beef":
        bot.dp()
        os.system('usr/bin/beef')
########################################################
### BKHIVE
########################################################
    elif statement == "bkhive":
        bot.dp()
        os.system('usr/bin/bkhive')
########################################################
### BLUEMAHO
########################################################
    elif statement == "bluemaho":
        bot.dp()
        os.system('usr/bin/bluemaho')
########################################################
### BRAA
########################################################
    elif statement == "braa":
        bot.dp()
        os.system('usr/bin/braa')
########################################################
### CADAVER
########################################################
    elif statement == "cadaver":
        bot.dp()
        os.system('usr/bin/cadaver')
########################################################
### CEWL
########################################################
    elif statement == "cewl":
        bot.dp()
        os.system('usr/bin/cewl')
########################################################
### CISCO AUDIT
########################################################
    elif statement == "ciscoaudit":
        bot.dp()
        os.system('usr/bin/cisco-auditing-tool')
########################################################
### CISCO GLOBAL EXPLOITER
########################################################
    elif statement == "cge":
        bot.dp()
        os.system('usr/bin/cisco-global-exploiter')
########################################################
### CISCO TORCH
########################################################
    elif statement == "torch":
        bot.dp()
        os.system('usr/bin/cisco-torch')
########################################################
### CONCH SSHv2 CLIENT
########################################################
    elif statement == "conch":
        bot.dp()
        os.system('usr/bin/conch')
########################################################
### COOKIE-CADGER
########################################################
    elif statement == "ccadger":
        bot.dp()
        os.system('usr/bin/cookie-cadger')
########################################################
### COPY ROUTER CONFIG
########################################################
    elif statement == "croutconf":
        bot.dp()
        os.system('usr/bin/copy-router-config')
########################################################
### DISCO
########################################################
    elif statement == "disco":
        bot.dp()
        os.system('usr/bin/disco')
########################################################
### DNSRECON
########################################################
    elif statement == "dnsrec":
        bot.dp()
        os.system('usr/bin/dnsrecon')
########################################################
### DRADIS
########################################################
    elif statement == "dradis":
        bot.zues()
        os.system('usr/bin/dradis')
########################################################
### EVILGRADE
########################################################
    elif statement == "evilgrade":
        bot.zues()
        os.system('usr/bin/evilgrade')
########################################################
### FIERCE
########################################################
    elif statement == "fierce":
        bot.zues()
        os.system('usr/bin/fierce')
########################################################
### FIMAP
########################################################
    elif statement == "fimap":
        bot.zues()
        os.system('usr/bin/fimap')
########################################################
### FRAGROUTER
########################################################
    elif statement == "fragrouter":
        bot.zues()
        os.system('usr/bin/fragrouter')
########################################################
### GERIX WIFI CRACKER
########################################################
    elif statement == "gerix":
        bot.zues()
        os.system('usr/bin/gerix')
########################################################
### HEARTBLEED
########################################################
    elif statement == "heartbleed":
        bot.zues()
        os.system('usr/bin/heartbleed')
########################################################
### GETHOSTIP
########################################################
    elif statement == "gethostip":
        bot.zues()
        os.system('usr/bin/gethostip')
########################################################
### GHOST PHISHER
########################################################
    elif statement == "ghost":
        bot.zues()
        os.system('usr/bin/ghost-phisher')
########################################################
### HAMSTER
########################################################
    elif statement == "hamster":
        bot.zues()
        os.system('usr/bin/hamster')
########################################################
### ZARP
########################################################
    elif statement == "zarp":
        bot.zues()
	os.system('/usr/bin/zarp')
########################################################
### ZENMAP
########################################################
    elif statement == "zenmap":
        bot.zues()
	os.system('/usr/bin/zenmap')
########################################################
### ZAPROXY
########################################################
    elif statement == "zaproxy":
        bot.zues()
	os.system('/usr/bin/zaproxy')
########################################################  
### SHUTDOWN
########################################################
    elif statement == "shutdown":
        bot.zues()
        print("When would you like to shutdown, " + name + "?")
### SHUTDOWN COMPUTER SYSTEM AT SPECIFIED TIME [IN MINS]
        os.system('read -p "Enter Time Till Shutdown In Mins: " mins ; echo "SHUTTING DOWN IN $mins MINS...\n ^c TOCANCEL" ; shutdown -h +$mins')
########################################################  
### ..PWN
########################################################
    elif statement == "..pwn":
### PRINT SIMPLE ..PWN 'ANIMATION'
	bot.load()
        os.system('toilet ..pwn')
        time.sleep(3)
        bot.zues()
### START DOTDOTPWN WITH SPECIFIED TARGET
        os.system("read -p 'Enter Target Host: ' target ; dotdotpwn -m http -h $target -M GET ")
########################################################  
### READPWN
########################################################
    elif statement == "readpwn":
        bot.zues()
### READ DOTDOTPWN REPORT
        os.system("read -p 'Enter File Name: ' file ; less /usr/bin/rhea/dotdotpwn/Reports/$file")
########################################################  
### ..PWNREPO
########################################################
    elif statement == "..pwnrepo":
        bot.zues()
        print("Getting Reports...")
        time.sleep(3)
### PRINT LIST OF DOTDOTPWN REPORTS
        os.system("ls '/usr/bin/rhea/dotdotpwn/Reports/' ; read output ")
########################################################  
### FUCKSHITUP
########################################################
    elif statement == "fuckshitup":
### DISPLAY FUCKSHITUP 'ANIMATION'
        bot.zues()
        os.system("toilet Lets")
        time.sleep(1)
        bot.atom()
        os.system("figlet Fuck")
        time.sleep(1)
        bot.dragon()
        os.system('toilet Shit')
        time.sleep(1)
        bot.satan()
        os.system('figlet Up!!!')
        time.sleep(2)
### LOAD FUCKSHITUP-SCANNER
        os.system('cd /pentest/scanners/fuckshitup-master && sudo php fsu.php "$@"')
########################################################  
### BLUEPOT
########################################################
    elif statement == "bluepot":
        bot.atom()
        print("Bluepot now loading")
### LOAD BLUEPOT [BLUETOOTH HONEY POT CREATOR]
        os.system('cd /pentest/bluetooth/bluepot && ./run.sh "$@"')
########################################################  
### MERCURY
########################################################
    elif statement == "mercury":
        bot.atom()
        print("Starting Mercury")
### START MERCURY REVERSE ENGINEERING CLIENT
        os.system('cd /pentest/reverse-engineering/mercury/client && sudo ./mercury.py "$@"')
########################################################  
### TSHARK
########################################################
    elif statement == "tshark":
        bot.network()
        print("Let's see whats going on in the network, " + name + ".")
        time.sleep(2)
        bot.network()
        print("Starting tshark...")
        time.sleep(3)
### RUN 'WIRESHARK' IN TERMINAL
        os.system("tshark -i wlan0")
########################################################  
### GPG
########################################################
    elif statement == "gpg":
        bot.atom()
        print("Loading key generator")
### GENERATE A NEW GPG KEY
        os.system("gpg --gen-key")
########################################################  
### VIPER
########################################################
    elif statement == "viper":
        bot.atom()
        print("Loading Viper")
### RUN VIPER.PY
        os.system("viper.py")
########################################################  
### WEBINFO
########################################################
    elif statement == "webinfo":
        bot.atom()
        print("Enter URL to get web info")
### RUN VULNERABILITY SCAN ON TARGET WEBSITE
        os.system("read -p 'Enter Site Name: ' site ; whois $site ; dig $site ; % dig +short $site ; nslookup -type=any $site ; nikto -host $site -C all ; read output ")
########################################################  
### METAGOO
########################################################
    elif statement == "metagoo":
        bot.atom()
### START METAGOOFIL
        os.system("read -p 'Enter Domain to search: ' dom ; read -p 'Enter Filetype To Download (pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx): ' down ; read -p 'Where Do You Want To Save Downloaded Files?: ' dfile ; read -p 'Enter Where Do You Want To Save Output File?: ' ofile ; /usr/bin/metagoofil -d $dom -t $down -o $dfile -f $ofile ")
########################################################  
### W3AF
########################################################
    elif statement == "w3af":
        bot.atom()
        print("Loading W3AF")
### RUN W3AF IN TERMINAL
        os.system("/usr/bin/w3af_console")
########################################################  
### W3GUI
########################################################
    elif statement == "w3gui":
        bot.atom()
        print("Loading W3AF")
### OPEN W3AF [GUI] APPLICATION
        os.system("/usr/bin/w3af_gui")
########################################################
########################################################  
### HTTPTEST
########################################################
    elif statement == "httptest":
        bot.atom()
### START SLOWHTTPTEST
        os.system("/usr/bin/slowhttptest")
########################################################  
### GRABBER
########################################################
    elif statement == "grabber":
        bot.atom()
        os.system("/usr/bin/grabber")
########################################################  
### KEYS
########################################################
    elif statement == "keys":
        bot.atom()
### START SEAHORSE [PASSWORDS AND KEYS MANAGER]
        os.system("/usr/bin/seahorse")
########################################################  
### ETTERCAP
########################################################
    elif statement == "ettercap":
        os.system('clear')
        bot.atom()
        print('Starting Ettercap...')
        time.sleep(3)
### START ETTERCAP [CONFIGURED FOR WLAN0]
        os.system("/usr/bin/ettercap -i wlan0 -T")
########################################################  
### PYRIT
########################################################
    elif statement == "pyrit":
        bot.atom()
        print("Recognized options:\n  -b               : Filters AccessPoint by BSSID\n  -e               : Filters AccessPoint by ESSID\n  -h               : Print help for a certain command\n  -i               : Filename for input ('-' is stdin)\n  -o               : Filename for output ('-' is stdout)\n  -r               : Packet capture source in pcap-format\n  -u               : URL of the storage-system to use\n  --all-handshakes : Use all handshakes instead of the best one\n \n Recognized commands:\n  analyze                 : Analyze a packet-capture file\n  attack_batch            : Attack a handshake with PMKs/passwords from the db\n  attack_cowpatty         : Attack a handshake with PMKs from a cowpatty-file\n  attack_db               : Attack a handshake with PMKs from the db\n  attack_passthrough      : Attack a handshake with passwords from a file\n  batch                   : Batchprocess the database\n  benchmark               : Determine performance of available cores\n  benchmark_long          : Longer and more accurate version of benchmark (~10 minutes)\n  check_db                : Check the database for errors\n  create_essid            : Create a new ESSID\n  delete_essid            : Delete a ESSID from the database\n  eval                    : Count the available passwords and matching results\n  export_cowpatty         : Export results to a new cowpatty file\n  export_hashdb           : Export results to an airolib database\n  export_passwords        : Export passwords to a file\n  help                    : Print general help\n  import_passwords        : Import passwords from a file-like source\n  import_unique_passwords : Import unique passwords from a file-like source\n  list_cores              : List available cores\n  list_essids             : List all ESSIDs but don't count matching results\n  passthrough             : Compute PMKs and write results to a file\n  relay                   : Relay a storage-url via RPC\n  selftest                : Test hardware to ensure it computes correct results\n  serve                   : Serve local hardware to other Pyrit clients\n  strip                   : Strip packet-capture files to the relevant packets\n  stripLive               : Capture relevant packets from a live capture-source\n  verify                  : Verify 10% of the results by recomputation")
### START PYRIT 
        os.system("read -p 'Enter Options: ' option ; read -p 'Enter Commands: ' com ; /usr/bin/pyrit $option $com")
########################################################  
### HIDEME
########################################################
    elif statement == "hideme":
        bot.atom()
        print("I Am Hiding You")
        os.system("service tor start ")
########################################################  
### DRIFT
########################################################
    elif statement == "drift":
        bot.atom()
        print("Let's Drift")
### START DRIFTNET [ALREADY CONFIGURED FOR USE WITH WLAN0
### { IF USING ETHERNET, CHANGE ALL INSTANCES OF WLAN0 TO 
### ETH0 OR ETH1 DEPENDING ON YOUR SYSTEM CONFIGURATION}]
        os.system("read -p 'Enter Your Routers IP Address ex: 192.168.1.254 :' rip ; read -p 'Enter Your Local IPAddress ex: 192.168.1.86 : ' lip ; arpspoof -i wlan0 -t $rip $lip & ettercap -Tqi wlan0 -M arp:remote /// & driftnet -i wlan0 ")
########################################################  
### KALI
########################################################
    elif statement == "kali":
        bot.atom()
### GO TO KALI LINUX TOOLS LISTING USING GOOGLE-CHROME
        os.system('google-chrome tools.kali.org/tools-listing')
########################################################  
### P0F
########################################################
    elif statement == "p0f":
        bot.atom()
### START PASSIVE OS FINGERPRINTING UTILITY
        os.system('p0f -i wlan0 -p -o /tmp/p0f.log')
########################################################  
### REAVERSCAN
########################################################
    elif statement == "wash":
        bot.atom()
### START WIFI PROTECTED SETUP SCAN TOOL
        os.system('read -p "Enter Channel: " chan ; wash -i mon0 -c $chan -C')
########################################################  
### REAVER
########################################################
    elif statement == "reaver":
        bot.atom()
### START WIFI PROTRECTED SETUP ATTACK TOOL
        os.system('read -p "Enter BSSID: " bssid ; reaver -i mon0 -b $bssid -v')
########################################################  
### WIPASS
########################################################
    elif statement == "wipass":
        bot.network()
        print("Getting Wifi Password")
        time.sleep(3)
### DISPLAY CURRENT WIFI NETWORK NAME AND PASSWORD
        os.system('awk -F= "/^(psk|id)/{print $2}" /etc/NetworkManager/system-connections/"$(iwgetid -r)" ')
########################################################  
### ARPSCAN
########################################################
    elif statement == "arpscan":
        bot.network()
        print("Scanning For IP Addresses")
        time.sleep(2)
### SCAN LOCAL NETWORK [VIA WIFI] FOR IP ADDRESSES
        os.system("arp-scan -l --interface=wlan0 --localnet")
########################################################  
### VULNSCAN
########################################################
    elif statement == "vulnscan":
        bot.atom()
        print("Starting SkipFish")
        time.sleep(3)
        os.system('read -p "Enter URL: " url ; read -p "Enter File Title: " title ; mkdir /usr/bin/rhea/skipfish/$title; skipfish -o /usr/bin/rhea/skipfish/$title -S /usr/share/skipfish/dictionaries/minimal.wl $url')
########################################################  
### DDOS
########################################################
    elif statement == "ddos":
        bot.network()
        os.system('read -p "Target: " target ; hping3 -S -P -U --flood -V --rand-source $target ')
########################################################  
### AUTOMATER
########################################################
    elif statement == "automater":
        os.system('clear')
        bot.atom()
        os.system('read -p "Enter Host: " host ; automater -t $host')
########################################################  
### AUTODETECT
########################################################
    elif statement == "autodetect":
        bot.network()
        print"Loading Autodetect"
        time.sleep(3)
        os.system('autodetect-network')
########################################################  
### ARPING
########################################################
    elif statement == "arping":
        bot.network()
        print("Loading Arping...")
        time.sleep(3)
        os.system('read -p "Enter Channel: " chan ; read -p "Enter IP: " ip ; arping -I wlan0 -c $chan $ip')
########################################################  
### DISFIRE
########################################################
    elif statement == "disfire":
        bot.network()
        print("Although I Think This Is A Terrible Fucking Idea I Am Disabling Your Firewall")
        time.sleep(3)
        os.system("ufw disable ; iptables -F ")
########################################################  
### REFIRE
########################################################
    elif statement == "refire":
        bot.network()
        print("It's About Fucking Time Ass Hole...")
        print("[*'Incomprehensible Mumbled Swears'*]")
        time.sleep(3)
        os.system("ufw enable ; iptables-restore < iptablesdefault_conf")
########################################################  
### NETWATCH
########################################################
    elif statement == "netwatch":
        bot.network()
        print("Let's watch the net.")
        time.sleep(2)
        os.system('detect-new-ip6 wlan0')
########################################################  
### DIG
########################################################
    elif statement == "dig":
        bot.atom()
        os.system('read -p "Enter Host: " host ; dig $host')
########################################################  
### DMITRY
########################################################
    elif statement == "dmitry":
        bot.atom()
        os.system('read -p "Enter Host: " host ; dmitry $host')
########################################################  
### XHYDRA
########################################################
    elif statement == "xhydra":
        bot.atom()
        os.system("/usr/bin/xhydra")
########################################################  
### AFL
########################################################
    elif statement == "afl":
        bot.atom()
        print("Please Connect Android Device Before Running This Command...")
        time.sleep(2)
        while True:
            print("Is your Android device connected? y/n: ")
            statement = raw_input(">").split()
            if len(statement) == 0:
                break
            if len(statement) > 0:
                verb = statement[0].lower()
            if statement == "y":
                time.sleep(3)
                os.system("/usr/bin/aflogical")
                os.system("usr/bin/abd devices")
            if statement == "n":
                bot.doh()
                print("You will need to connect your Android device before running this command...")
                break
            else:
                bot.doh()
                print("I didn't understand your response. Exiting AFLogical ")
                time.sleep(3)
                break
########################################################  
### ANDROSDK
########################################################
    elif statement == "androsdk":
        bot.atom()
        os.system("/usr/bin/android-sdk")
########################################################  
### SYSPRINT
########################################################
    elif statement == "sysprint":
        bot.network()
        os.system('read -p "Enter IP Address Or Host Name: " ip ; /usr/bin/arp-fingerprint -o "-N -I wlan0" $ip')
########################################################  
### BLUEBROWSE
########################################################
    elif statement == "bluebrowse":
        bot.atom()
        os.system("/usr/bin/blueman-browse")
######################################################## 
### BLUEPHONEBOOK
########################################################
    elif statement == "bluephonebook":
        bot.atom()
        print('bluesnarfer: you must set bd_addr\n bluesnarfer, version 0.1 -\n usage: bluesnarfer [options] [ATCMD] -b bt_addr\n ATCMD     : valid AT+CMD (GSM EXTENSION)\n TYPE      : valid phonebook type ..\n example   : "DC" (dialed call list)\n            "SM" (SIM phonebook)\n            "RC" (recevied call list)\n            "XX" much more\n -b bdaddr : bluetooth device address\n -C chan   : bluetooth rfcomm channel\n -c ATCMD  : custom action\n -r N-M    : read phonebook entry N to M \n -w N-M    : delete phonebook entry N to M\n -f name   : search "name" in phonebook address\n -s TYPE   : select phonebook memory storage\n -l        : list aviable phonebook memory storage\n -i        : device info')
        os.system("/usr/bin/bluesnarfer ")
        os.system("/usr/bin/bluesnarfer ")
########################################################  
### BOMBARDMENT
########################################################
    elif statement == "bombardment":
        bot.atom()
        os.system("man bombardment")
        os.system("/usr/bin/bombardment")
########################################################  
### WIFIBUDDY
########################################################
    elif statement == "wifibuddy":
        bot.network()
        os.system("man /usr/bin/easside-ng")
        os.system("/usr/bin/easside-ng")
        os.system("man /usr/bin/buddy-ng")
        os.system("/usr/bin/buddy-ng")
########################################################  
### BULLY
########################################################
    elif statement == "bully":
        bot.atom()
        os.system("man /usr/bin/bully")
        os.system("/usr/bin/bully ")
########################################################  
### BURPSUITE
########################################################
    elif statement == "burpsuite":
        bot.atom()
        os.system("/usr/bin/burpsuite")
########################################################  
### DIG
########################################################
    elif statement == "dig":
        bot.atom()
        os.system("man /usr/bin/dig")
        os.system("/usr/bin/dig ")
########################################################  
### DUMPZILLA
########################################################
    elif statement == "dumpzilla":
        bot.atom()
        os.system("/usr/bin/dumpzilla")
        os.system("/usr/bin/dumpzilla ")
########################################################  
### WHOIS
########################################################
    elif statement == "whois":
        bot.network()
        os.system('clear')
        os.system("read -p 'Enter Host: ' host ; whois $host")
########################################################  
### GEOIP
########################################################
    elif statement == "geoip":
        bot.atom()
        os.system("read -p 'Enter Target IP Address: ' ip ; lynx -dump 'http://www.ip-adress.com/ip_tracer/$ip' | grepaddress | egrep 'city|state|country' | awk '{print $3,$4,$5,$6,$7,$8,$9}' | sed 's\ip address flag \\'|sed 's\My\\' ; read output")
########################################################  
### MALTEGO
########################################################
    elif statement == "maltego":
        bot.kronos()
        os.system("/usr/bin/casefile")
########################################################  
### CALIBRE
########################################################
    elif statement == "calibre":
        bot.kronos()
        os.system("/usr/bin/calibre")
########################################################  
### AUTOPSY
########################################################
    elif statement == "autopsy":
        bot.kronos()
        os.system("/usr/bin/autopsy")
########################################################  
### CREEPY
########################################################
    elif statement == "creepy":
        bot.kronos()
        os.system("/usr/bin/creepy")
########################################################  
### CUCKOO
########################################################
    elif statement == "cuckoo":
        bot.kronos()
        os.system("/usr/bin/cuckoo")
########################################################  
### CYMOTHOA
########################################################
    elif statement == "cymothoa":
        bot.kronos()
        os.system("/usr/bin/cymothoa")
########################################################  
### DFF
########################################################
    elif statement == "dff":
        bot.kronos()
        os.system("man dff ; /usr/bin/dff")
########################################################  
### DFFGUI
########################################################
    elif statement == "dffgui":
        bot.kronos()
        os.system("/usr/bin/dff-gui")
########################################################  
### DUMPCAP
########################################################
    elif statement == "dumpcap":
        bot.kronos()
        os.system("/usr/bin/dumpcap -i wlan0")
########################################################  
### FERN
########################################################
    elif statement == "fern":
        bot.network()
        print("Loading Fern Wifi Cracker...")
        time.sleep(3)
        os.system("/usr/bin/fern-wifi-cracker")
########################################################  
### NMAP
########################################################
    elif statement == "nmap":
        bot.network()
        print("Starting nMap")
        os.system('read -p "Enter Host : " host ; nmap -v -A "$host" ')
########################################################  
### HARVEST
########################################################
    elif statement == "harvest":
        bot.kronos()
        print("-d: Domain to search or company name")
        print("-b: Data source (google,bing,bingapi,pgp,linkedin,google-profiles,people123,jigsaw,all)")
        print("-s: Start in result number X (default 0)")
        print("-v: Verify host name via dns resolution and search for virtual hosts")
        print("-f: Save the results into an HTML and XML file")
        print("-n: Perform a DNS reverse query on all ranges discovered")
        print("-c: Perform a DNS brute force for the domain name")
        print("-t: Perform a DNS TLD expansion discovery")
        print("-e: Use this DNS server")
        print("-l: Limit the number of results to work with(bing goes from 50 to 50 results,")
        print("-h: use SHODAN database to query discovered hosts")
        print(" google 100 to 100, and pgp doesn't use this option)")
        print("Examples:./theharvester.py -d microsoft.com -l 500 -b google")
        print(" ./theharvester.py -d microsoft.com -b pgp")
        print(" ./theharvester.py -d microsoft -l 200 -b linkedin")
        os.system('read -p "Enter Options: " options ; /usr/bin/theharvester $options')
########################################################  
### RECON
########################################################
    elif statement == "recon":
        os.system('clear')
        bot.kronos()
        print('Loading Recon-ng...')
        time.sleep(3)
        os.system("/usr/bin/recon-ng")
###############################################
###############################################
###############################################
########################################################  
### QUIT
########################################################
    elif statement == "quit":
        with open("Kronosconv.txt", "a") as myfile:
            myfile.write("\nKronos terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
        os.system('clear')
        with open("Kronos.log", "a") as myfile:
            myfile.write("\nKronos terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
        bot.dp()
        print('Fuck off...')
        os.system('cp /usr/bin/rhea/kronos.py /media/Program13/13/truecrypt1/.backup/kronos.py.backup')
        os.system('cp /usr/bin/rhea/bot.py /media/Program13/13/truecrypt1/.backup/bot.py.backup')
        os.system('cp /usr/bin/rhea/psych.py /media/Program13/13/truecrypt1/.backup/psych.py.backup')
        os.system('cp Kronosconv.txt /media/Program13/13/truecrypt1/.backup/Kronosconv.txt.backup')
        os.system('cp Kronos.log /media/Program13/13/truecrypt1/.backup/Kronos.log.backup')
        quit()

        if __name__ == "__main__":
             bot.main()
