#####################
#####################
##                ###
##   KALI LINUX   ###
##                ###
#####################
#####################
while True:
    import os
    import re
    import sys
    import users
    import time
    import bot
    import psych
    import webbrowser
    import urllib
    import urllib2
    import requests
    import random
    import numpy as np
    import math
    import subprocess
    from lxml import html
    bot.dp()
    name = users.name
    print("What kind of scum bags are we taking out today " + name + "?")
    time.sleep(2)
    os.system('clear')
    bot.dp()
    print("type 'quit' to exit program")
    print("type '?' for help")
### START OF MAIN PROGRAM FOR Kali LINUX 
    while True:
        statement = raw_input("[" + name + "]: ")
        os.system('clear')
        bot.dp()
### ANALYZE USER INPUT AND RETURN REPONSE FROM PSYCH.PY
        print(bot.analyze(statement))
########################################################
### ?
#######################################################
        if statement == "?":
            bot.dp()
            print("Loading available commands, " + name)
            time.sleep(3)
#### LOAD BASH SCRIPT CONTAINING LIST OF COMMANDS WITH DESCRIPTIONS
            os.system('sh /media/root/13/truecrypt1/rhea/D34D9001comphelp.sh')
########################################################
### RESTART
########################################################
        elif statement == "restart":
            bot.dp()
            print('Restarting. Gimme a fuckin minute, ' + name)
            time.sleep(2)
### RESTART D34D9001 WITHOUT HAVING TO EXIT AND RELOAD PROGRAM
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
            bot.cp()
            print("Fuck this mac address. Let's get a new one, " + name + ".")
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
        elif statement == "audit":
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
            bot.dp()
            os.system('usr/bin/dradis')
########################################################
### EVILGRADE
########################################################
        elif statement == "evilgrade":
            bot.dp()
            os.system('usr/bin/evilgrade')
########################################################
### FIERCE
########################################################
        elif statement == "fierce":
            bot.dp()
            os.system('usr/bin/fierce')
########################################################
### FIMAP
########################################################
        elif statement == "fimap":
            bot.dp()
            os.system('usr/bin/fimap')
########################################################
### FRAGROUTER
########################################################
        elif statement == "fragrouter":
            bot.dp()
            os.system('usr/bin/fragrouter')
########################################################
### GERIX WIFI CRACKER
########################################################
        elif statement == "gerix":
            bot.dp()
            os.system('usr/bin/gerix')
########################################################
### HEARTBLEED
########################################################
        elif statement == "heartbleed":
            bot.dp()
            os.system('usr/bin/heartbleed')
########################################################
### GETHOSTIP
########################################################
        elif statement == "gethostip":
            bot.dp()
            os.system('usr/bin/gethostip')
########################################################
### GHOST PHISHER
########################################################
        elif statement == "ghost":
            bot.dp()
            os.system('usr/bin/ghost-phisher')
########################################################
### HAMSTER
########################################################
        elif statement == "hamster":
            bot.dp()
            os.system('usr/bin/hamster')
########################################################
### ZARP
########################################################
        elif statement == "zarp":
            bot.dp()
	    os.system('/usr/bin/zarp')
########################################################
### ZENMAP
########################################################
        elif statement == "zenmap":
            bot.dp()
	    os.system('/usr/bin/zenmap')
########################################################
### ZAPROXY
########################################################
        elif statement == "zaproxy":
            bot.dp()
	    os.system('/usr/bin/zaproxy')
########################################################
### SHUTDOWN
########################################################
        elif statement == "shutdown":
            bot.dp()
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
            bot.dp()
### START DOTDOTPWN WITH SPECIFIED TARGET
            os.system("read -p 'Enter Target Host: ' target ; dotdotpwn -m http -h $target -M GET ")
########################################################
### READPWN
########################################################
        elif statement == "readpwn":
            bot.dp()
### READ DOTDOTPWN REPORT
            os.system("read -p 'Enter File Name: ' file ; less /usr/bin/rhea/dotdotpwn/Reports/$file")
########################################################
### ..PWNREPO
########################################################
        elif statement == "..pwnrepo":
            bot.dp()
            print("Getting Reports...")
            time.sleep(3)
### PRINT LIST OF DOTDOTPWN REPORTS
            os.system("ls '/usr/bin/rhea/dotdotpwn/Reports/' ; read output ")
########################################################
### FUCKSHITUP
########################################################
        elif statement == "fuckshitup":
### DISPLAY FUCKSHITUP 'ANIMATION'
            bot.dp()
            os.system("toilet Lets")
            time.sleep(1)
            bot.dp()
            os.system("figlet Fuck")
            time.sleep(1)
            bot.dp()
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
            bot.dp()
            print("Bluepot now loading")
### LOAD BLUEPOT [BLUETOOTH HONEY POT CREATOR]
            os.system('cd /pentest/bluetooth/bluepot && ./run.sh "$@"')
########################################################
### MERCURY
########################################################
        elif statement == "mercury":
            bot.dp()
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
            bot.dp()
            print("Loading GPG Key Generator...")
### GENERATE A NEW GPG KEY
            os.system("gpg --gen-key")
########################################################
### VIPER
########################################################
        elif statement == "viper":
            bot.dp()
            print("Loading Viper")
### RUN VIPER.PY
            os.system("viper.py")
########################################################
### WEBINFO
########################################################
        elif statement == "webinfo":
            bot.dp()
            print("Enter URL to get web info")
### RUN VULNERABILITY SCAN ON TARGET WEBSITE
            os.system("read -p 'Enter Site Name: ' site ; whois $site ; dig $site ; % dig +short $site ; nslookup -type=any $site ; nikto -host $site -C all ; read output ")
########################################################
### METAGOO
########################################################
        elif statement == "metagoo":
            bot.dp()
### START METAGOOFIL
            os.system("read -p 'Enter Domain to search: ' dom ; read -p 'Enter Filetype To Download (pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx): ' down ; read -p 'Where Do You Want To Save Downloaded Files?: ' dfile ; read -p 'Enter Where Do You Want To Save Output File?: ' ofile ; /usr/bin/metagoofil -d $dom -t $down -o $dfile -f $ofile ")
########################################################
### W3AF
########################################################
        elif statement == "w3af":
            bot.dp()
            print("Loading W3AF")
### RUN W3AF IN TERMINAL
            os.system("/usr/bin/w3af_console")
########################################################
### W3GUI
########################################################
        elif statement == "w3gui":
            bot.dp()
            print("Loading W3AF")
### OPEN W3AF [GUI] APPLICATION
            os.system("/usr/bin/w3af_gui")
########################################################
### HTTPTEST
########################################################
        elif statement == "httptest":
            bot.dp()
### START SLOWHTTPTEST
            os.system("/usr/bin/slowhttptest")
########################################################
### GRABBER
########################################################
        elif statement == "grabber":
            bot.dp()
            os.system("/usr/bin/grabber")
########################################################
### KEYS
########################################################
        elif statement == "keys":
            bot.dp()
### START SEAHORSE [PASSWORDS AND KEYS MANAGER]
            os.system("/usr/bin/seahorse")
########################################################
### ETTERCAP
########################################################
        elif statement == "ettercap":
            os.system('clear')
            bot.dp()
            print('Starting Ettercap...')
            time.sleep(3)
### START ETTERCAP [CONFIGURED FOR WLAN0]
            os.system("/usr/bin/ettercap -i wlan0 -T")
########################################################
### PYRIT
########################################################
        elif statement == "pyrit":
            bot.dp()
            print("Recognized options:\n  -b               : Filters AccessPoint by BSSID\n  -e               : Filters AccessPoint by ESSID\n  -h               : Print help for a certain command\n  -i               : Filename for input ('-' is stdin)\n  -o               : Filename for output ('-' is stdout)\n  -r               : Packet capture source in pcap-format\n  -u               : URL of the storage-system to use\n  --all-handshakes : Use all handshakes instead of the best one\n \n Recognized commands:\n  analyze                 : Analyze a packet-capture file\n  attack_batch            : Attack a handshake with PMKs/passwords from the db\n  attack_cowpatty         : Attack a handshake with PMKs from a cowpatty-file\n  attack_db               : Attack a handshake with PMKs from the db\n  attack_passthrough      : Attack a handshake with passwords from a file\n  batch                   : Batchprocess the database\n  benchmark               : Determine performance of available cores\n  benchmark_long          : Longer and more accurate version of benchmark (~10 minutes)\n  check_db                : Check the database for errors\n  create_essid            : Create a new ESSID\n  delete_essid            : Delete a ESSID from the database\n  eval                    : Count the available passwords and matching results\n  export_cowpatty         : Export results to a new cowpatty file\n  export_hashdb           : Export results to an airolib database\n  export_passwords        : Export passwords to a file\n  help                    : Print general help\n  import_passwords        : Import passwords from a file-like source\n  import_unique_passwords : Import unique passwords from a file-like source\n  list_cores              : List available cores\n  list_essids             : List all ESSIDs but don't count matching results\n  passthrough             : Compute PMKs and write results to a file\n  relay                   : Relay a storage-url via RPC\n  selftest                : Test hardware to ensure it computes correct results\n  serve                   : Serve local hardware to other Pyrit clients\n  strip                   : Strip packet-capture files to the relevant packets\n  stripLive               : Capture relevant packets from a live capture-source\n  verify                  : Verify 10% of the results by recomputation")
### START PYRIT
            os.system("read -p 'Enter Options: ' option ; read -p 'Enter Commands: ' com ; /usr/bin/pyrit $option $com")
########################################################
### HIDEME
########################################################
        elif statement == "hideme":
            bot.dp()
            print("Well let's just run to the shadows why don't we? Ya fuckin pussy...")
            os.system("service tor start ")
########################################################
### DRIFT
########################################################
        elif statement == "drift":
            bot.dp()
            print("Let's see what these fags are lookin at...")
### START DRIFTNET [ALREADY CONFIGURED FOR USE WITH WLAN0
### { IF USING ETHERNET, CHANGE ALL INSTANCES OF WLAN0 TO
### ETH0 OR ETH1 DEPENDING ON YOUR SYSTEM CONFIGURATION}]
            os.system("read -p 'Enter Your Routers IP Address ex: 192.168.1.254 :' rip ; read -p 'Enter Your Local IPAddress ex: 192.168.1.86 : ' lip ; arpspoof -i wlan0 -t $rip $lip & ettercap -Tqi wlan0 -M arp:remote /// & driftnet -i wlan0 ")
########################################################
### P0F
########################################################
        elif statement == "p0f":
            bot.dp()
### START PASSIVE OS FINGERPRINTING UTILITY
            os.system('p0f -i wlan0 -p -o /tmp/p0f.log')
########################################################
### REAVERSCAN
########################################################
        elif statement == "wash":
            bot.dp()
### START WIFI PROTECTED SETUP SCAN TOOL
            os.system('read -p "Enter Channel: " chan ; wash -i mon0 -c $chan -C')
########################################################
### REAVER
########################################################
        elif statement == "reaver":
            bot.dp()
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
            bot.dp()
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
            bot.dp()
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
            bot.dp()
            os.system('read -p "Enter Host: " host ; dig $host')
########################################################
### DMITRY
########################################################
        elif statement == "dmitry":
            bot.dp()
            os.system('read -p "Enter Host: " host ; dmitry $host')
########################################################
### XHYDRA
########################################################
        elif statement == "xhydra":
            bot.dp()
            os.system("/usr/bin/xhydra")
########################################################
### AFL
########################################################
        elif statement == "afl":
            bot.dp()
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
            bot.dp()
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
            bot.dp()
            os.system("/usr/bin/blueman-browse")
########################################################
### BLUEPHONEBOOK
########################################################
        elif statement == "bluephonebook":
            bot.dp()
            print('bluesnarfer: you must set bd_addr\n bluesnarfer, version 0.1 -\n usage: bluesnarfer [options] [ATCMD] -b bt_addr\n ATCMD     : valid AT+CMD (GSM EXTENSION)\n TYPE      : valid phonebook type ..\n example   : "DC" (dialed call list)\n            "SM" (SIM phonebook)\n            "RC" (recevied call list)\n            "XX" much more\n -b bdaddr : bluetooth device address\n -C chan   : bluetooth rfcomm channel\n -c ATCMD  : custom action\n -r N-M    : read phonebook entry N to M \n -w N-M    : delete phonebook entry N to M\n -f name   : search "name" in phonebook address\n -s TYPE   : select phonebook memory storage\n -l        : list aviable phonebook memory storage\n -i        : device info')
            os.system("/usr/bin/bluesnarfer ")
            os.system("/usr/bin/bluesnarfer ")
########################################################
### BOMBARDMENT
########################################################
        elif statement == "bombardment":
            bot.dp()
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
            bot.dp()
            os.system("man /usr/bin/bully")
            os.system("/usr/bin/bully ")
########################################################
### BURPSUITE
########################################################
        elif statement == "burpsuite":
            bot.dp()
            os.system("/usr/bin/burpsuite")
########################################################
### DIG
########################################################
        elif statement == "dig":
            bot.dp()
            os.system("man /usr/bin/dig")
            os.system("/usr/bin/dig ")
########################################################
### DUMPZILLA
########################################################
        elif statement == "dumpzilla":
            bot.dp()
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
            bot.dp()
            os.system("read -p 'Enter Target IP Address: ' ip ; lynx -dump 'http://www.ip-adress.com/ip_tracer/$ip' | grepaddress | egrep 'city|state|country' | awk '{print $3,$4,$5,$6,$7,$8,$9}' | sed 's\ip address flag \\'|sed 's\My\\' ; read output")
########################################################
### MALTEGO
########################################################
        elif statement == "maltego":
            bot.dp()
            os.system("/usr/bin/casefile")
########################################################
### CALIBRE
########################################################
        elif statement == "calibre":
            bot.dp()
            os.system("/usr/bin/calibre")
########################################################
### AUTOPSY
########################################################
        elif statement == "autopsy":
            bot.dp()
            os.system("/usr/bin/autopsy")
########################################################
### CREEPY
########################################################
        elif statement == "creepy":
            bot.dp()
            os.system("/usr/bin/creepy")
########################################################
### CUCKOO
########################################################
        elif statement == "cuckoo":
            bot.dp()
            os.system("/usr/bin/cuckoo")
########################################################
### CYMOTHOA
########################################################
        elif statement == "cymothoa":
            bot.dp()
            os.system("/usr/bin/cymothoa")
########################################################
### DFF
########################################################
        elif statement == "dff":
            bot.dp()
            os.system("man dff ; /usr/bin/dff")
########################################################
### DFFGUI
########################################################
        elif statement == "dffgui":
            bot.dp()
            os.system("/usr/bin/dff-gui")
########################################################
### DUMPCAP
########################################################
        elif statement == "dumpcap":
            bot.dp()
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
            bot.dp()
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
            bot.dp()
            print('Loading Recon-ng...')
            time.sleep(3)
            os.system("/usr/bin/recon-ng")
########################################################
### CISC0-0CS
########################################################
        elif statement == "ocs":
            bot.dp()
            os.system('usr/bin/cisco-ocs')
########################################################
### CRYPTCAT
########################################################
        elif statement == "cryptcat":
            bot.dp()
            os.system('usr/bin/cryptcat')
########################################################
### DUND
########################################################
        elif statement == "dund":
            bot.dp()
            os.system('/usr/bin/dund -h')
            os.system("read -p 'Enter Options: ' opts ; dund $opts")
########################################################
### GOLISMERO
########################################################
        elif statement == "golismero":
            bot.dp()
            os.system('golismero -h')
            os.system("read -p 'Enter Options: ' opts ; usr/bin/golismero $opts")
########################################################
### GOOFILE
########################################################
        elif statement == "goofile":
            bot.dp()
            os.system("read -p 'Enter Domain: ' domain ; read -p 'Enter Filetype: ' type ; /usr/bin/goofile.py -d $domain -f $type pdf")
########################################################
### ATK6
########################################################
        elif statement == "atk6":
            bot.dp()
            os.system("python /media/root/13/truecrypt1/rhea/atkpool.py")
########################################################
### DNC2TCPC
########################################################
        elif statement == "dns2tcpc":
            bot.dp()
            os.system('/usr/bin/dns2tcpc')
########################################################
### DNS2TCPD
########################################################
        elif statement == "dns2tcpd":
            bot.dp()
            os.system('/usr/bin/dns2tcpd')
########################################################
### DUMP RSA PUBLIC KEY
########################################################
        elif statement == "dumprsapk":
            bot.dp()
            os.system('/usr/bin/dumpRSAPublicKey')
########################################################
### ETTER PROGRAMS
########################################################
        elif statement == "etter":
            bot.dp()
	    print"""
ettercap  ettercap-pkexec  etterfilter  etterlog
"""
            os.system("read -p 'Enter Program (Exclude *etter* ex: ettercap --> cap): ' prog ; /usr/bin/etter$prog")
########################################################
### FAKE PROGRAMS
########################################################
        elif statement == "fakeit":
            bot.dp()
	    print""" faked-sysv // faked-tcp // fakeroot // fakeroot-sysv // fakeroot-tcp """
            os.system("read -p 'Enter Program Name (Exclude 'fake' ex: faked-sysv --> d-sysv): ' prog ; /usr/bin/fake$prog")
########################################################
### FANTAIP
########################################################
        elif statement == "fanta":
            bot.dp()
            os.system('usr/bin/fantaip')
########################################################
### FIKED
########################################################
        elif statement == "fiked":
            bot.dp()
	    print("Let's Fike It Up!!!")
            os.system('usr/bin/fiked')
########################################################
### FPING
########################################################
        elif statement == "fping":
            bot.dp()
	    prog = raw_input("Which Program Would You Like To Use?:\n 1: fping\n 2: fping6\n : ")
	    if prog == "1":
		bot.dp()
	        print"""
Usage: fping [options] [targets...]
   -a         show targets that are alive
   -A         show targets by address
   -b n       amount of ping data to send, in bytes (default 56)
   -B f       set exponential backoff factor to f
   -c n       count of pings to send to each target (default 1)
   -C n       same as -c, report results in verbose format
   -D         print timestamp before each output line
   -e         show elapsed time on return packets
   -f file    read list of targets from a file ( - means stdin) (only if no -g specified)
   -g         generate target list (only if no -f specified)
                (specify the start and end IP in the target list, or supply a IP netmask)
                (ex. fping -g 192.168.1.0 192.168.1.255 or fping -g 192.168.1.0/24)
   -H n       Set the IP TTL value (Time To Live hops)
   -i n       interval between sending ping packets (in millisec) (default 25)
   -I if      bind to a particular interface
   -l         loop sending pings forever
   -m         ping multiple interfaces on target host
   -n         show targets by name (-d is equivalent)
   -O n       set the type of service (tos) flag on the ICMP packets
   -p n       interval between ping packets to one target (in millisec)
                (in looping and counting modes, default 1000)
   -q         quiet (don't show per-target/per-ping results)
   -Q n       same as -q, but show summary every n seconds
   -r n       number of retries (default 3)
   -R         random packet data (to foil link data compression)
   -s         print final stats
   -S addr    set source address
   -t n       individual target initial timeout (in millisec) (default 500)
   -T n       ignored (for compatibility with fping 2.4)
   -u         show targets that are unreachable
   -v         show version
   targets    list of targets to check (if no -f specified)
"""
 	        os.system("read -p 'Enter Options: ' opts ; /usr/bin/fping $opts")
	    elif prog == "2":
		bot.dp()
		print"""
Usage: fping6 [options] [targets...]
   -a         show targets that are alive
   -A         show targets by address
   -b n       amount of ping data to send, in bytes (default 56)
   -B f       set exponential backoff factor to f
   -c n       count of pings to send to each target (default 1)
   -C n       same as -c, report results in verbose format
   -D         print timestamp before each output line
   -e         show elapsed time on return packets
   -f file    read list of targets from a file ( - means stdin) (only if no -g specified)
   -g         generate target list (only if no -f specified)
                (specify the start and end IP in the target list, or supply a IP netmask)
                (ex. fping6 -g 192.168.1.0 192.168.1.255 or fping6 -g 192.168.1.0/24)
   -H n       Set the IP TTL value (Time To Live hops)
   -i n       interval between sending ping packets (in millisec) (default 25)
   -I if      bind to a particular interface
   -l         loop sending pings forever
   -m         ping multiple interfaces on target host
   -n         show targets by name (-d is equivalent)
   -O n       set the type of service (tos) flag on the ICMP packets
   -p n       interval between ping packets to one target (in millisec)
                (in looping and counting modes, default 1000)
   -q         quiet (don't show per-target/per-ping results)
   -Q n       same as -q, but show summary every n seconds
   -r n       number of retries (default 3)
   -R         random packet data (to foil link data compression)
   -s         print final stats
   -S addr    set source address
   -t n       individual target initial timeout (in millisec) (default 500)
   -T n       ignored (for compatibility with fping 2.4)
   -u         show targets that are unreachable
   -v         show version
   targets    list of targets to check (if no -f specified)
"""
                os.system("read -p 'Enter Options: ' opts ; usr/bin/fping6 $opts")
	    elif prog != "1" or "2":
	        print("Error: [ \"" + prog + "\" ] Invalid Response.\n You Must Select Either (1) or (2)...")
########################################################
### GEOIP
########################################################
        elif statement == "geoip":
            bot.dp()
            os.system('usr/bin/geoip')
########################################################
### HACKRF
########################################################
        elif statement == "hackrf":
            bot.dp()
	    print("hackrf_cpldjtag // hackrf_info // hackrf_max2837 // hackrf_rffc5071 // hackrf_si5351c // hackrf_spiflash // hackrf_transfer")
            os.system("read -p 'Enter Program Name (Exclude \'hackrf_\'  ex: hackrf_cpldjtag --> cpldjtag): ' prog ; usr/bin/hackrf_$prog")
########################################################
### HALFLIFE
########################################################
        elif statement == "halflife":
            bot.dp()
	    print"""   Usage: ./halflife target port
   ./halflife 192.168.1.101 27010"""
            os.system("read -p 'Enter Target IP: ' ip ; read -p 'Enter Target Port: ' port ; usr/bin/halflife $ip $port")
########################################################
### IKESCAN
########################################################
        elif statement == "ikescan":
            bot.dp()
	    print"""
Usage: ike-scan [options] [hosts...]

Target hosts must be specified on the command line unless the --file option is
given, in which case the targets are read from the specified file instead.

The target hosts can be specified as IP addresses or hostnames.  You can also
specify IPnetwork/bits (e.g. 192.168.1.0/24) to specify all hosts in the given
network (network and broadcast addresses included), and IPstart-IPend
(e.g. 192.168.1.3-192.168.1.27) to specify all hosts in the inclusive range.

These different options for specifying target hosts may be used both on the
command line, and also in the file specified with the --file option.

In the options below a letter or word in angle brackets like <f> denotes a
value or string that should be supplied. The corresponding text should
indicate the meaning of this value or string. When supplying the value or
string, do not include the angle brackets. Text in square brackets like [<f>]
mean that the enclosed text is optional. This is used for options which take
an optional argument.

Options:

--help or -h		Display this usage message and exit.

--file=<fn> or -f <fn>	Read hostnames or addresses from the specified file
			instead of from the command line. One name or IP
			address per line.  Use "-" for standard input.

--sport=<p> or -s <p>	Set UDP source port to <p>, default=500, 0=random.
			Some IKE implementations require the client to use
			UDP source port 500 and will not talk to other ports.
			Note that superuser privileges are normally required
			to use non-zero source ports below 1024.  Also only
			one process on a system may bind to a given source port
			at any one time. Use of the --nat-t option changes
			the default source port to 4500

--dport=<p> or -d <p>	Set UDP destination port to <p>, default=500.
			UDP port 500 is the assigned port number for ISAKMP
			and this is the port used by most if not all IKE
			implementations. Use of the --nat-t option changes
			the default destination port to 4500

--retry=<n> or -r <n>	Set total number of attempts per host to <n>,
			default=3.

--timeout=<n> or -t <n>	Set initial per host timeout to <n> ms, default=500.
			This timeout is for the first packet sent to each host.
			subsequent timeouts are multiplied by the backoff
			factor which is set with --backoff.

--bandwidth=<n> or -B <n> Set desired outbound bandwidth to <n>, default=56000
			The value is in bits per second by default.  If you
			append "K" to the value, then the units are kilobits
			per second; and if you append "M" to the value,
			the units are megabits per second.
			The "K" and "M" suffixes represent the decimal, not
			binary, multiples.  So 64K is 64000, not 65536.

--interval=<n> or -i <n> Set minimum packet interval to <n> ms.
			The packet interval will be no smaller than this number.
			The interval specified is in milliseconds by default.
			if "u" is appended to the value, then the interval
			is in microseconds, and if "s" is appended, the
			interval is in seconds.
			If you want to use up to a given bandwidth, then it is
			easier to use the --bandwidth option instead.
			You cannot specify both --interval and --bandwidth
			because they are just different ways to change the
			same underlying variable.

--backoff=<b> or -b <b>	Set timeout backoff factor to <b>, default=1.50.
			The per-host timeout is multiplied by this factor
			after each timeout.  So, if the number of retries
			is 3, the initial per-host timeout is 500ms and the
			backoff factor is 1.5, then the first timeout will be
			500ms, the second 750ms and the third 1125ms.

--verbose or -v		Display verbose progress messages.
			Use more than once for greater effect:
			1 - Show when each pass is completed and when
			    packets with invalid cookies are received.
			2 - Show each packet sent and received and when
			    hosts are removed from the list.
			3 - Display the host, Vendor ID and backoff lists
			    before scanning starts.

--quiet or -q		Don't decode the returned packet.
			This prints less protocol information so the
			output lines are shorter.

--multiline or -M	Split the payload decode across multiple lines.
			With this option, the decode for each payload is
			printed on a separate line starting with a TAB.
			This option makes the output easier to read, especially
			when there are many payloads.

--lifetime=<s> or -l <s> Set IKE lifetime to <s> seconds, default=28800.
			RFC 2407 specifies 28800 as the default, but some
			implementations may require different values.
			If you specify this as a a decimal integer, e.g.
			86400, then the attribute will use a 4-byte value.
			If you specify it as a hex number, e.g. 0xFF, then
			the attribute will use the appropriate size value
			(one byte for this example).
			If you specify the string "none" then no lifetime
			attribute will be added at all.
			You can use this option more than once in conjunction
			with the --trans options to produce multiple transform
			payloads with different lifetimes.  Each --trans option
			will use the previously specified lifetime value.

--lifesize=<s> or -z <s> Set IKE lifesize to <s> Kilobytes, default=0.
			If you specify this as a a decimal integer, e.g.
			86400, then the attribute will use a 4-byte value.
			If you specify it as a hex number, e.g. 0xFF, then
			the attribute will use the appropriate size value
			(one byte for this example).
			You can use this option more than once in conjunction
			with the --trans options to produce multiple transform
			payloads with different lifesizes.  Each --trans option
			will use the previously specified lifesize value.

--auth=<n> or -m <n>	Set auth. method to <n>, default=1 (PSK).
			RFC defined values are 1 to 5.  See RFC 2409 Appendix A.
			Checkpoint hybrid mode is 64221.
			GSS (Windows "Kerberos") is 65001.
			XAUTH uses 65001 to 65010.
			This is not applicable to IKEv2.

--version or -V		Display program version and exit.

--vendor=<v> or -e <v>	Set vendor id string to hex value <v>.
			You can use this option more than once to send
			multiple vendor ID payloads.

--trans=<t> or -a <t>	Use custom transform <t> instead of default set.
			You can use this option more than once to send
			an arbitrary number of custom transforms.
			There are two ways to specify the transform:
			The new way, where you specify the attribute/value
			pairs, and the old way where you specify the values
			for a fixed list of attributes.
			For the new method, the transform <t> is specified as
			(attr=value, attr=value, ...)
			Where "attr" is the attribute number, and "value" is
			the value to assign to that attribute.  You can specify
			an arbitary number of attribute/value pairs.
			See RFC 2409 Appendix A for details of the attributes
			and values.
			Note that brackets are special to some shells, so you
			may need to quote them, e.g.
			--trans="(1=1,2=2,3=3,4=4)". For example,
			--trans=(1=1,2=2,3=1,4=2) specifies
			Enc=3DES-CBC, Hash=SHA1, Auth=shared key, DH Group=2;
			and --trans=(1=7,14=128,2=1,3=3,4=5) specifies
			Enc=AES/128, Hash=MD5, Auth=RSA sig, DH Group=5.
			For the old method, the transform <t> is specified as
			enc[/len],hash,auth,group.
			Where enc is the encryption algorithm,
			len is the key length for variable length ciphers,
			hash is the hash algorithm, and group is the DH Group.
			For example, --trans=5,2,1,2 specifies
			Enc=3DES-CBC, Hash=SHA1, Auth=shared key, DH Group=2;
			and --trans=7/256,1,1,5 specifies
			Enc=AES-256, Hash=MD5, Auth=shared key, DH Group=5.
			This option is not yet supported for IKEv2.

--showbackoff[=<n>] or -o[<n>]	Display the backoff fingerprint table.
			Display the backoff table to fingerprint the IKE
			implementation on the remote hosts.
			The optional argument specifies time to wait in seconds
			after receiving the last packet, default=60.
			If you are using the short form of the option (-o)
			then the value must immediately follow the option
			letter with no spaces, e.g. -o25 not -o 25.

--fuzz=<n> or -u <n>	Set pattern matching fuzz to <n> ms, default=500.
			This sets the maximum acceptable difference between
			the observed backoff times and the reference times in
			the backoff patterns file.  Larger values allow for
			higher variance but also increase the risk of
			false positive identifications.
			Any per-pattern-entry fuzz specifications in the
			patterns file will override the value set here.

--patterns=<f> or -p <f> Use IKE backoff patterns file <f>,
			default=/usr/share/ike-scan/ike-backoff-patterns.
			This specifies the name of the file containing
			IKE backoff patterns.  This file is only used when
			--showbackoff is specified.

--vidpatterns=<f> or -I <f> Use Vendor ID patterns file <f>,
			default=/usr/share/ike-scan/ike-vendor-ids.
			This specifies the name of the file containing
			Vendor ID patterns.  These patterns are used for
			Vendor ID fingerprinting.

--aggressive or -A	Use IKE Aggressive Mode (The default is Main Mode)
			If you specify --aggressive, then you may also
			specify --dhgroup, --id and --idtype.  If you use
			custom transforms with aggressive mode with the --trans
			option, note that all transforms should have the same
			DH Group and this should match the group specified
			with --dhgroup or the default if --dhgroup is not used.

--id=<id> or -n <id>	Use <id> as the identification value.
			This option is only applicable to Aggressive Mode.
			<id> can be specified as a string, e.g. --id=test or as
			a hex value with a leading "0x", e.g. --id=0xdeadbeef.

--idtype=<n> or -y <n>	Use identification type <n>.  Default 3 (ID_USER_FQDN).
			This option is only applicable to Aggressive Mode.
			See RFC 2407 4.6.2 for details of Identification types.

--dhgroup=<n> or -g <n>	Use Diffie Hellman Group <n>.  Default 2.
			This option is only applicable to Aggressive Mode and
			IKEv2.  For both of these, it is used to determine the
			size of the key exchange payload.
			If you use Aggressive Mode with custom transforms, then
			you will normally need to use the --dhgroup option
			unless you are using the default DH group.
			Acceptable values are 1,2,5,14,15,16,17,18 (MODP only).

--gssid=<n> or -G <n>	Use GSS ID <n> where <n> is a hex string.
			This uses transform attribute type 16384 as specified
			in draft-ietf-ipsec-isakmp-gss-auth-07.txt, although
			Windows-2000 has been observed to use 32001 as well.
			For Windows 2000, you'll need to use --auth=65001 to
			specify Kerberos (GSS) authentication.

--random or -R		Randomise the host list.
			This option randomises the order of the hosts in the
			host list, so the IKE probes are sent to the hosts in
			a random order.  It uses the Knuth shuffle algorithm.

--tcp[=<n>] or -T[<n>]	Use TCP transport instead of UDP.
			This allows you to test a host running IKE over TCP.
			You won't normally need this option because the vast
			majority of IPsec systems only support IKE over UDP.
			The optional value <n> specifies the type of IKE over
			TCP.  There are currently two possible values:
			1 = RAW IKE over TCP as used by Checkpoint (default);
			2 = Encapsulated IKE over TCP as used by Cisco.
			If you are using the short form of the option (-T)
			then the value must immediately follow the option
			letter with no spaces, e.g. -T2 not -T 2.
			You can only specify a single target host if you use
			this option.

--tcptimeout=<n> or -O <n> Set TCP connect timeout to <n> seconds (default=10).
			This is only applicable to TCP transport mode.

--pskcrack[=<f>] or -P[<f>] Crack aggressive mode pre-shared keys.
			This option outputs the aggressive mode pre-shared key
			(PSK) parameters for offline cracking using the
			"psk-crack" program that is supplied with ike-scan.
			You can optionally specify a filename, <f>, to write
			the PSK parameters to.  If you do not specify a filename
			then the PSK parameters are written to standard output.
			If you are using the short form of the option (-P)
			then the value must immediately follow the option
			letter with no spaces, e.g. -Pfile not -P file.
			You can only specify a single target host if you use
			this option.
			This option is only applicable to IKE aggressive mode.

--nodns or -N		Do not use DNS to resolve names.
			If you use this option, then all hosts must be
			specified as IP addresses.

--noncelen=<n> or -c <n> Set the nonce length to <n> bytes. Default=20
			This option controls the length of the nonce payload
			that is sent in an aggressive mode or IKEv2 request.
			Normally there is no need to use this option unless you
			want to reduce the nonce size to speed up pre-shared
			key cracking, or if you want to see how a particular
			server handles different length nonce payloads.
			RFC 2409 states that the length of nonce payload
			must be between 8 and 256 bytes, but ike-scan does
			not enforce this.
			Specifying a large nonce length will increase the
			size of the packet sent by ike-scan. A very large nonce
			length may cause fragmentation, or exceed the maximum
			IP packet size.
			This option is only applicable to IKE aggressive mode.

--headerlen=<n> or -L <n> Set the length in the ISAKMP header to <n> bytes.
			You can use this option to manually specify the value
			to be used for the ISAKMP header length.
			By default, ike-scan will fill in the correct value.
			Use this option to manually specify an incorrect
			length.
			<n> can be specified as "+n" which sets the length
			to n bytes more than it should be, "-n" which sets
			it to n bytes less, or "n" which sets it to exactly
			bytes.
			Changing the header length to an incorrect value can
			sometimes disrupt VPN servers.

--mbz=<n> or -Z <n>	Use the value <n> for reserved (MBZ) fields, default=0.
			Specifying this option makes the outgoing packet
			non-RFC compliant, and should only be used if you want
			to see how a VPN server will respond to invalid packets.
			The value of <n> should be in the range 0-255.

--headerver=<n> or -E <n> Specify the ISAKMP header version.
			The default is 0x10 (16) which corresponds to v1.0.
			Specifying a non-default value will make the outgoing
			packet non-RFC compliant, and should only be used if
			you want to see how the VPN server reacts to strange
			versions.
			The value should be in the range 0-255.

--certreq=<c> or -C <c> Add the CertificateRequest payload <c>.
			<c> should be specified as a hex value.
			The first byte of the hex value will be interpreted as
			the certificate type; the remaining bytes as the
			certificate authority as described in RFC 2408 3.10.
			The certificate types are listed in RFC 2408 sec 3.9.
			RFC 2048 states "The Certificate Request payload MUST
			be accepted at any point during the exchange"

--doi=<d> or -D <d>	Set the SA DOI to <d>, default 1 (IPsec).
			You will not normally want to change this unless you
			want to see how the VPN server responds to a
			non-standard DOI.

--situation=<s> or -S <s> Set the SA Situation to <d>, default 1.
			The meaning of the situation depends on the DOI, and
			is detailed in the appropriate DOI document.  For the
			IPsec DOI, the default Situation of 1 represents
			SIT_IDENTITY_ONLY.
			You will not normally want to change this unless you
			want to see how the VPN server responds to a
			non-standard situation.

--protocol=<p> or -j <p> Set the Proposal protocol ID to <p>, default 1.
			The meaning of the proposal protocol ID depends on
			the DOI, and is detailed in the appropriate DOI
			document.  For the IPsec DOI, the default proposal
			protocol id of 1 represents PROTO_ISAKMP.
			You will not normally want to change this unless you
			want to see how the VPN server responds to a
			non-standard protocol ID.

--transid=<t> or -k <t> Set the Transform ID to <t>, default 1.
			The meaning of the transform ID depends on the
			DOI, and is detailed in the appropriate DOI
			document.  For the IPsec DOI, the default
			transform id of 1 represents KEY_IKE.
			You will not normally want to change this unless you
			want to see how the VPN server responds to a
			non-standard transform ID.

--spisize=<n>		Set the proposal SPI size to <n>.  Default=0
			If this is non-zero, then a random SPI of the
			specified size will be added to the proposal payload.
			The default of zero means no SPI.

--hdrflags=<n>		Set the ISAKMP header flags to <n>.  Default=0
			The flags are detailed in RFC 2408 section 3.1

--hdrmsgid=<n>		Set the ISAKMP header message ID to <n>.  Default=0
			This should be zero for IKE Phase-1.

--cookie=<n>		Set the ISAKMP initiator cookie to <n>
			The cookie value should be specified in hex.
			By default, the cookies are automatically generated
			and have unique values.  If you specify this option,
			then you can only specify a single target, because
			ike-scan requires unique cookie values to match up
			the response packets.

--exchange=<n>		Set the exchange type to <n>
			This option allows you to change the exchange type in
			the ISAKMP header to an arbitrary value.
			Note that ike-scan only supports Main and Aggressive
			modes (values 2 and 4 respectively).  Specifying
			other values will change the exchange type value in
			the ISAKMP header, but will not adjust the other
			payloads.
			The exchange types are defined in RFC 2408 sec 3.1.

--nextpayload=<n>	Set the next payload in the ISAKMP header to <n>
			Normally, the next payload is automatically set to the
			correct value.

--randomseed=<n>	Use <n> to seed the pseudo random number generator.
			This option seeds the PRNG with the specified number,
			which can be useful if you want to ensure that the
			packet data is exactly repeatable when it includes
			payloads with random data such as key exchange or nonce.
			By default, the PRNG is seeded with an unpredictable
			value.

--timestamp		Display timestamps for received packets.
			This option causes a timestamp to be displayed for
			each received packet.

--sourceip=<s>		Set source IP address for outgoing packets to <s>.
			This option causes the outgoing IKE packets to have
			the specified source IP address.
			The address can either be an IP address in dotted
			quad format, or the string "random" which will use
			a different random source address for each packet that
			is sent.
			If this option is used, no packets will be received
			This option requires raw socket support, and you
			will need superuser privileges to use this option,
			even if you specify a high source port.
			This option does not work on all operating systems.

--shownum		Display the host number for received packets.
			This displays the ordinal host number of the
			responding host before the IP address. It can be useful
			when sending many packets to the same target IP, to
			see if any probes are being ignored.

--nat-t			Use RFC 3947 NAT-Traversal encapsulation.
			This option adds the non-ESP marker to the beginning
			of outgoing packets and strips it from received
			packets, as described in RFC 3947. It also changes the
			default source port to 4500 and the default destination
			port to 4500, which are the ports for NAT-T IKE.
			These port numbers can be changed with the --sport and
			--dport options, providing they are used after the
			--nat-t option.

--rcookie=<n>		Set the ISAKMP responder cookie to <n>.
			This sets the responder cookie to the specified hex
			value.  By default, the responder cookie is set to zero.

--ikev2 or -2		Use IKE version 2
			This causes the outgoing packets to use IKEv2 format
			as defined in RFC 4306 instead of the default IKEv1
			format. Any packets returned are automatically decoded
			as IKE or IKEv2 depending on their payloads irrespective
			of this option.
			The --ikev2 option is currently experimental. It has not
			been extensively tested, and it only supports sending
			the default proposal.

Report bugs or send suggestions to ike-scan@nta-monitor.com
See the ike-scan homepage at http://www.nta-monitor.com/tools/ike-scan/
"""
            os.system("read -p 'Enter Options: ' opts ; read -p 'Enter Host(s): ' hosts ; usr/bin/ike-scan $opts $hosts")
########################################################
###
########################################################
#    elif statement == "":
#        bot.dp()
#        os.system('usr/bin/')
########################################################
###
########################################################
#    elif statement == "":
#        bot.dp()
#        os.system('usr/bin/')
########################################################
###
########################################################
#    elif statement == "":
#        bot.dp()
#        os.system('usr/bin/')
########################################################
###
########################################################
#    elif statement == "":
#        bot.dp()
#        os.system('usr/bin/')
#########################################################
###
########################################################
#    elif statement == "":
#        bot.dp()
#        os.system('usr/bin/')
########################################################
###
########################################################
#    elif statement == "":
#        bot.dp()
#        os.system('usr/bin/')
########################################################
###
########################################################
#    elif statement == "":
#        bot.dp()
#        os.system('usr/bin/')
########################################################
### QUIT
########################################################
        elif statement == "quit":
            with open("D34D9001conv.txt", "a") as myfile:
                myfile.write("\nD34D9001 terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
            os.system('clear')
            with open("D34D9001.log", "a") as myfile:
                myfile.write("\nD34D9001 terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
            bot.dp()
            print('ERROR: FILE BACKUP HAS BEEN SKIPPED!!!\n PLEASE RUN D34DP001 FROM CYBORG LINUX TO AUTO-BACKUP FILES.')
            quit()

            if __name__ == "__main__":
                bot.main()
