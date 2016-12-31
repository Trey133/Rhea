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
import psych#.PY     ### RHEA'S RESPONSES                 ###
import bot#.PY       ### RHEA'S FUNCTIONS                 ###
### FROM /USR/BIN/RHEA ###                                ###
#############################################################
### THESE FILES HOLD OUR FUNCTIONS AND RESPONSES FOR RHEA ###
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
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Rhea.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
while True:
    with open("Rheaconv.txt", "a") as myfile:
        myfile.write("\nRhea started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
    with open("Rhea.log", "a") as myfile:
        myfile.write("\nRhea started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
###############################################################
### LOAD FUNCTION 'LOCK()' FROM FILE 'BOT.PY'
    bot.lock()
###############################################################
    print("Login:")
    username = raw_input("Username: ")
    if username == "13":
        print("Sounds Legit...")
    else:
	bot.rhea()
	with open("Rhea.log", "a") as myfile:
            myfile.write("\nRhea terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to Incorrect Username.\n")
        print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
### IF USERNAME IS INCORRECT, TERMINATE PROGRAM
        quit()
    bot.rhea()
### DO NOT PRINT PASSWORD TO STDOUT [DON'T DISPLAY IT ON THE SCREEN AS YOU TYPE]
    os.system("stty -echo")
    password = raw_input("Please Enter Password: ")
### TURN PRINT TO STDOUT BACK ON 
    os.system("stty echo")
    print("\n")
    if password == "13":
	bot.unlock()
        print("Access Granted")
        print("Please Wait While System Loads...")
### WAIT FOR (2) SECONDS BEFORE CONTINUING
        time.sleep(2)
        break
    else: 
	bot.rhea()
        print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
	with open("Rhea.log", "a") as myfile:
            myfile.write("\nRhea terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to incorrect password.\n")
### IF PASSWORD IS INCORRECT, TERMINATE PROGRAM
        quit()
### PROGRAM INTRODUCTION
bot.rhea()
os.system("toilet Rhea")
time.sleep(5)
os.system('clear')
bot.rhea()
name = raw_input("What is your name? ")
with open("Rhea.log", "a") as myfile:
    myfile.write("\nRhea started by:  " + name + "\n")
with open("Rheaconv.txt", "a") as myfile:
    myfile.write("\nRhea started by:  " + name + "\n")
print("Hello, " + name + ". my name is Rhea.")
time.sleep(2)
bot.rhea()
print("What would you like me to do?")
time.sleep(2)
os.system('clear')
bot.rhea()
print("type 'quit' to exit program")
print("type '?' for help")
### START OF MAIN PROGRAM
while True:
    statement = raw_input(">")
    os.system('clear')
    bot.rhea()
### ANALYZE USER INPUT AND RETURN REPONSE FROM PSYCH.PY
    print(bot.analyze(statement))
########################################################
### ?
########################################################
    if statement == "?":
        bot.rhea()
        print("Loading available commands, " + name)
	time.sleep(3)
### LOAD BASH SCRIPT CONTAINING LIST OF COMMANDS WITH DESCRIPTIONS
        os.system('sh /usr/bin/rhea/comphelp.sh')
########################################################
### RESTART
########################################################
    elif statement == "restart":
	bot.rhea()
        print('Restarting. Please wait, ' + name)
        time.sleep(2)
### RESTART RHEA WITHOUT HAVING TO EXIT AND RELOAD PROGRAM
        os.execv(sys.executable, ['python'] + sys.argv)
    elif statement == "commands":
        print(commands)
########################################################
### STOCKS
########################################################
    elif statement == "stocks":
### GET CURRENT STOCK PRICES [SEE BOT.PY { FUNCTION: "GET_QUOTE()" } FOR MECHANICS]
	print(" Google: ", bot.get_quote('Google'))
        print(" Sony: ", bot.get_quote('sony'))
        print(" Yahoo: ", bot.get_quote('yahoo'))
        print(" Apple: ", bot.get_quote('apple'))
        print(" Tesla: ", bot.get_quote('tesla'))
        print(" Microsoft: ", bot.get_quote('microsoft'))
        print(" DOW: ", bot.get_quote('dow jones'))
        print(" Amex: ", bot.get_quote('XAX'))
        print(" Sprint: ", bot.get_quote('sprint corp'))
        print(" Verizon: ", bot.get_quote('verizon'))
        print(" AT&T: ", bot.get_quote('AT&T'))
        print(" SpaceX", bot.get_quote('spacex'))
########################################################
### MIRROR
########################################################
    elif statement == "mirror":
	bot.rhea()
	print("Let's clone a site, " + name)
	time.sleep(2)
	os.system('/usr/bin/httrack')
########################################################
### ALTLIB
########################################################
    elif statement == "altlib":
	bot.rhea()
	os.system('less /usr/bin/rhea/altlib.txt')
	os.system("read -p 'Enter Title (INCLUDE PATH EX: /path/to/file.pdf): ' title ; less /media/Program13/241*/HD/EBooks/$title")
########################################################
### 
########################################################

########################################################
### MERICA
########################################################
    elif statement == "merica":
### PRINT AMERICAN FLAG IN TERMINAL
	bot.aflag()
########################################################
### WEATHER
########################################################
    elif statement == "weather":
	bot.atom()
        print("Getting weather forcast, " + name + ". Please wait.")
	time.sleep(3)
### GET 3 DAY WEATHER FORCAST FOR ZIPCODE 42220
        os.system("curl wttr.in/42220")
        print("\n")
########################################################
### GETSITE
########################################################
    elif statement == "getsite":
	bot.rhea()
	site = raw_input("Enter URL " + name + ": ")
	response = requests.get(site)
	print(response.text)
########################################################
###   GETTXT   ###   MUST HAVE HTML2TEXT INSTALLED   ###
########################################################
    elif statement == "gettxt":
        bot.rhea()
	os.system("read -p 'Enter URL: ' url ; wget -qO- $url | html2text")
########################################################
### LIBRARY
########################################################
    elif statement == "library":
	bot.librarian()
        print("Loading Bookshelf...")
        time.sleep(3)
### LIST CONTENTS OF LIB13
	os.system("ls /usr/bin/rhea/lib13")
    elif statement == "commands":
### PRINT SMALL LIST OF COMMANDS [INCOMPLETE LIST] FROM PSYCH.PY{COMMANDS}
	print(psych.commands)
########################################################  
### REDPILL
########################################################
    elif statement == "redpill":
	bot.atom()
        print("Please wait while you're removed from the Matrix " + name + ".")
	time.sleep(3)
### DISPLAY 'MATRIX' TYPE ANIMATION IN TERMINAL
        os.system("cmatrix")
########################################################  
### SHUTDOWN
########################################################
    elif statement == "shutdown":
	bot.rhea()
	print("When would you like to shutdown, " + name + "?")
### SHUTDOWN COMPUTER SYSTEM AT SPECIFIED TIME [IN MINS]
	os.system('read -p "Enter Time Till Shutdown In Mins: " mins ; echo "SHUTTING DOWN IN $mins MINS...\n ^c TO CANCEL" ; shutdown -h +$mins')
########################################################  
### ..PWN
########################################################
    elif statement == "..pwn":
### PRINT SIMPLE ..PWN 'ANIMATION'
	bot.atom()
	print('.')
	time.sleep(1)
	bot.atom()
	print('..')
	time.sleep(1)
	bot.atom()
	os.system('toilet ..pwn')
	time.sleep(3)
	bot.atom()
### START DOTDOTPWN WITH SPECIFIED TARGET
        os.system("read -p 'Enter Target Host: ' target ; dotdotpwn -m http -h '$target' -M GET ")
########################################################  
### READPWN
########################################################
    elif statement == "readpwn":
	bot.atom()
### READ DOTDOTPWN REPORT
        os.system("read -p 'Enter File Name: ' file ; less /usr/bin/rhea/dotdotpwn/Reports/$file")
########################################################  
### ..PWNREPO
########################################################
    elif statement == "..pwnrepo":
	bot.atom()
	print("Getting Reports...")
	time.sleep(3)
### PRINT LIST OF DOTDOTPWN REPORTS
	os.system("ls '/usr/bin/rhea/dotdotpwn/Reports/' ; read output ")
########################################################  
### PROGRAM13
########################################################
    elif statement == "program13":
	bot.atom()
        print("Loading Program13...")
	time.sleep(3)
### LOAD HTTP://PROGRAM13.ME IN TERMINAL
        os.system("w3m http://program13.me")
########################################################  
### NEWDOC
########################################################
    elif statement == "newdoc":
	bot.rhea()
### CREATE A NEW DOCUMENT IN SPECIFIED DIRECTORY
	os.system('read -p "Enter Document Title: " doc ; read -p "Enter Save Location: " save ; nano $save/$doc')
########################################################  
### EDITDOC
########################################################
    elif statement == "editdoc":
	bot.rhea()
### EDIT SPECIFIED DOCUMENT
	os.system('read -p "Enter Document Title Including Location (ex: /path/to/doc.txt): " title ; nano $title')
########################################################  
### MUSIC
########################################################
    elif statement == " music":
	bot.rhea()
	print("Let's listen to some music, " + name + ".")
	time.sleep(3)
### START SPOTIFY FROM THE TERMINAL [OPENS GUI APPLICATION]
        os.system('spotify')
########################################################  
### PLAY
########################################################
    elif statement == "play":
	bot.controller()
	print("What game would you like to play, " + name + "?")
        print(" craft13\n compquiz")
### PICK WHICH OF THE 2 GAMES YOU WOULD LIKE TO PLAY
        statement = raw_input(">")
        if statement == "craft13":
          bot.controller()
          print("Loading Craft13...")
	  time.sleep(3)
### LOAD 13ELEMENTS
          os.system("python /usr/bin/rhea/13elements.py")
        if statement == "compquiz":
          bot.controller()
          print("Loading CompQuiz..." )
	  time.sleep(3)
### LOAD COMPQUIZ
          os.system("python /usr/bin/rhea/game2.py")
        elif statement != "craft13" or "compquiz":
           continue
########################################################  
### FUCKSHITUP
########################################################
    elif statement == "fuckshitup":
### DISPLAY FUCKSHITUP 'ANIMATION'
	bot.atom()
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
### OZZY
########################################################
    elif statement == "ozzy":
### TRIBUTE TO OZZY
	os.system('clear')
	bot.rnr()
	os.system('figlet "Rock & Roll"')
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
### MOON
########################################################
    elif statement == "moon":
	bot.bart()
        print("Let me find that for you " + name + ".")
	time.sleep(2)
### GET CURRENT PHASE OF THE MOON
        os.system("curl wttr.in/Moon")
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
### CALENDAR
########################################################
    elif statement == "calendar":
	bot.atom()
        print("Opening calendar")
### OPEN [GUI] CALENDAR
        os.system("zenity --calendar")
########################################################  
### CALC
########################################################
    elif statement == "calc":
	bot.atom()
        print("Opening calculator")
### OPEN [GUI] CALCULATOR
        os.system("gnome-calculator")
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
### CHAT
########################################################
    elif statement == "chat":
        bot.network()
        print("How would you like to chat, " + name + "?: ")
        print(" // irssi\n // neuron\n // hchat")
### PICK WHICH OF THE 2 GAMES YOU WOULD LIKE TO PLAY
        statement = raw_input(">")
        if statement == "irssi":
          bot.rhea()
          print("Loading Irssi...")
          time.sleep(3)
### LOAD 13ELEMENTS
          os.system("/usr/bin/irssi")
	  continue
        if statement == "neuron":
          bot.rhea()
          print("Loading Neuron Server..." )
          time.sleep(3)
### LOAD COMPQUIZ
          os.system("/usr/bin/rhea/server.py")
	  continue
	if statement == "hchat":
	  webbrowser.open("https://hack.chat/program13", new=0, autoraise=True)
	  continue
        elif statement != "irssi" or "neuron" or "hchat":
	   print("I'm sorry but I have not been programmed to do that.")
           continue
########################################################  
### GOOGLE
########################################################
    elif statement == "google":
	bot.atom()
        print("opening Google")
### OPEN HTTPS://GOOGLE.COM ON GOOGLE-CHROME
        os.system("google-chrome https://google.com")
########################################################  ### GOOGLEPAT
########################################################
    elif statement == "googlepat":
	bot.atom()
        print("opening google patent search")
### OPEN GOOGLE PATENT SEARCH IN GOOGLE-CHROME
        os.system("google-chrome https://patents.google.com/")
########################################################  
### DOWNLOAD
########################################################
    elif statement == "download":
	bot.atom()
        print("Please Enter URL")
### ENTER URL TO DOWNLOAD FILE FROM WEBSITE
        os.system("read -p 'Enter URL: ' id ; read -p 'Enter Output name: ' name ; read -p 'Enter Path To Output: ' dir ; service tor start ; proxychains wget -O '$name' -P '$dir' '$id' ")
########################################################  
### LOC
########################################################
    elif statement == "loc":
	bot.atom()
        print("Opening Lbrary of Congress")
### OPEN LIBRARY OF CONGRESS IN GOOGLE-CHROME
        os.system("google-chrome https://loc.gov")
########################################################  
### FIND
########################################################
    elif statement == "find":
        bot.atom()
        print("Who are you looking for, " + name + "?")
### SEARCH FOR INFORMATION ON TARGET WITH NAME AND STATE
        os.system('read -p "Enter First Name:" fname ; read -p "Enter Middle Name:" mname ; read -p "Enter Last Name:" lname ; read -p "Enter City:" city ; read -p "Enter State: " state ; w3m "https://pipl.com/search/?q=$fname+$mname+$lname&l=sloc=&in=5" && w3m "https://www.findmugshots.com/arrests/"$fname"_"$lname"_"$state && w3m "http://mugshots.com/search.html?q="$fname"+"$lname && w3m "http://10digits.us/n/"$fname"_"$lname"/location/"$city"_"$state ; read output ')
########################################################  
### HEADLINES
########################################################
    elif statement == "headlines":
	os.system('clear')
	bot.poc()
	print("Getting News Headlines...")
### GET CURRENT NEWS HEADLINES FROM GOOGLE NEWS
	response = requests.get('http://news.google.com')
	if (response.status_code == 200):
	    pagehtml = html.fromstring(response.text)
	    news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
	                          /a/span[@class="titletext"]/text()')
	print("\n".join(news))
########################################################  
### TECHNEWS
########################################################
    elif statement == "technews":
	os.system('clear')
	bot.poc()
        print("Getting Technology Headlines...")
### GET CURRENT TECHNOLOGY HEADLINES FROM GOOGLE NEWS
        response = requests.get('https://news.google.com/news/section?cf=all&pz=1&ned=us&topic=tc')
        if (response.status_code == 200):
            pagehtml = html.fromstring(response.text)
            news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
                                  /a/span[@class="titletext"]/text()')
        print("\n".join(news))
########################################################  
### DATASCRAPE
########################################################
    elif statement == "datascrape":
	bot.angryhomer()
	print("Let's scrape some data.")
### PERFORM DATA SCRAPE ON WEBSITE
	url = raw_input("Enter URL: ")
	page = requests.get(url)
	tree = html.fromstring(page.content)
	print(tree)
	print(page.content)
########################################################  
### IMGGET
########################################################
    elif statement == "imgget":
	bot.atom()
### GET ALL IMAGES FROM WEBPAGE [TO GET ALL IMAGES FROM ENTIE SITE, SEE 'ALLPICS']
        os.system('read -p "Enter URL: " url ; image-scraper --dump-urls --scrape-reverse $url')
################################################################################################
############################  GET CURRENT HACKING HEADLINES  ###################################
############################  ***DOES NOT CURRENTLY WORK***  ###################################
################################################################################################ 
### elif statement == "hacknews":                                                            ###
###	os.system('clear')                                                                   ###
###	bot.poc()                                                                            ###
###	print("Getting Hack News...")                                                        ###
###	response = requests.get("https://latesthackingnews.com/category/vulnerabilities/")   ###
########################   ADD HTML2TEXT   #####################################################
###	txt = response.text                                                                  ###
###	print(txt)                                                                           ###
################################################################################################
################################################################################################
################################################################################################
########################################################  
### SCINEWS
########################################################
    elif statement == "scinews":
	os.system('clear')
	bot.poc()
        print("Getting Science Headlines...")
### GET LATEST SCIENCE HEADLINES FROM GOOGLE NEWS
        response = request.get('https://news.google.com/news/section?cf=all&pz=1&ned=us&topic=snc&siidp=c85af5ebcc3b806c2d5ec06b06a2a9ab167c&ict=ln')
	if (response.status_code == 200):
	    pagehtml = html.fromstring(response.text)
	    news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
				  /a/span[@class="titletext"]/text()')
	print("\n".join(news))
########################################################  
### WEBINFO
########################################################
    elif statement == "webinfo":
	bot.atom()
        print("Enter URL to get web info")
### RUN VULNERABILITY SCAN ON TARGET WEBSITE
        os.system("read -p 'Enter Site Name: ' site ; whois $site ; dig $site ; % dig +short $site ; nslookup -type=any $site ; nikto -host $site -C all ; read output ")
########################################################  
### ALLPICS
########################################################
    elif statement == "allpics":
	os.system('clear')
	bot.tex()
### DOWNLOAD ALL IMAGES FROM WEBSITE
        os.system("read -p 'Enter URL:' site ; wget -r -p -l inf -np $site ")
########################################################  
### CFC
########################################################
    elif statement == "cfc":
	bot.atom()
        print("Creating New Case")
        os.system("gpg --decrypt-files /usr/bin/rhea/case.sh.gpg ; rm /usr/bin/rhea/case.sh.gpg ; sh /usr/bin/rhea/case.sh ; gpg -r Ender --encrypt-files /usr/bin/rhea/case.sh ; rm /usr/bin/rhea/case.sh")
########################################################  
### CFADD
########################################################
    elif statement == "cfadd":
	bot.atom()
### EDIT OR ADD INFORMATION TO A CASEFILE
        os.system("read -p 'Enter Case Number:' title ; gpg --decrypt-files /usr/bin/rhea/casefile/$title.gpg ; nano /usr/bin/rhea/casefile/$title ; gpg -e /usr/bin/rhea/casefile/$title ; rm /usr/bin/rhea/casefile/$title")
########################################################  
### CFREAD
########################################################
    elif statement == "cfread":
	bot.atom()
### READ AN EXISTING CASEFILE
        os.system("read -p 'Enter Case Number:' case ; gpg --decrypt-files /usr/bin/rhea/casefile/$case.gpg ; rm /usr/bin/rhea/$case.gpg ; less /usr/bin/rhea/casefile/$case ; gpg -e /usr/bin/rhea/casefile/$case ; rm /usr/bin/rhea/casefile/$case")
########################################################  
### CFLIST
########################################################
    elif statement == "cflist":
        bot.bshelf()
        print("Loading Casefile Bookshelf...")
        time.sleep(3)
### LIST CURRENT CASEFILES
        os.system("ls /usr/bin/rhea/casefile")
########################################################  
### DDG
########################################################
    elif statement == "ddg":
	bot.atom()
        print("Search Duck Duck Go")
### SEARCH DUCKDUCKGO.COM FROM TERMINAL
        os.system('read -p "Enter Search Term seperate terms with + :" search ; w3m "https://duckduckgo.com/?q=$search&t=h_&ia=web" ' )
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
### MANFILES
########################################################
    elif statement == "manfiles":
	bot.atom()
### LIST MANFILES
        os.system("less /media/Program13/13/truecrypt1/tuts/manfiles")
########################################################  
### C
########################################################
    elif statement == "c":
	bot.atom()
### RUN BASH COMMANDS FROM RHEA PROMPT
        os.system("read -p 'Enter Command: ' cmd ; $cmd ")
########################################################  
### HTTPTEST
########################################################
    elif statement == "httptest":
	bot.atom()
### START SLOWHTTPTEST
        os.system("/usr/bin/slowhttptest")
########################################################  
### SCAN
########################################################
    elif statement == "scan":
	bot.atom()
### START SIMPLE-SCAN [DOCUMENT SCANNER]
        os.system("/usr/bin/simple-scan")
########################################################  
### GRABBER
########################################################
    elif statement == "grabber":
	bot.atom()
        os.system("/usr/bin/grabber")
########################################################  
### SCREENSHOT
########################################################
    elif statement == "screenshot":
	bot.atom()
### TAKE SCREENSHOT OF CURRENT SCREEN
        os.system("/usr/bin/gnome-screenshot")
########################################################  
### KEYS
########################################################
    elif statement == "keys":
	bot.atom()
### START SEAHORSE [PASSWORDS AND KEYS MANAGER]
        os.system("/usr/bin/seahorse")
########################################################  
### RECORDME
########################################################
    elif statement == "recordme":
	bot.atom()
### RECORD DESKTOP WITH SOUND
        os.system("/usr/bin/recordmydesktop")
########################################################  
### QJACK
########################################################
    elif statement == "qjack":
	bot.atom()
### CREATE JACK AUDIO SERVER
        os.system("/usr/bin/qjackctl")
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
### ETERM
########################################################
    elif statement == "eterm":
	bot.atom()
### OPEN ANOTHER TERMINAL [ETERM IS A LOT SMALLER THAN GNOME TERMINAL. YOU MAY HAVE TROUBLE READING TEXT]
        os.system("/usr/bin/Eterm")
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
        os.system("read -p 'Enter Your Routers IP Address ex: 192.168.1.254 :' rip ; read -p 'Enter Your Local IP Address ex: 192.168.1.86 : ' lip ; arpspoof -i wlan0 -t $rip $lip & ettercap -Tqi wlan0 -M arp:remote /// & driftnet -i wlan0 ")
########################################################  
### KALI
########################################################
    elif statement == "kali":
	bot.atom()
### GO TO KALI LINUX TOOLS LISTING USING GOOGLE-CHROME
        os.system('google-chrome tools.kali.org/tools-listing')

########################################################  
### TAKENOTE
########################################################
    elif statement == "takenote":
	bot.atom()
### OPEN KEEPNOTE
        os.system('keepnote')
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
### IPSCAN
########################################################
    elif statement == "ipscan":
	bot.network()
        print("Scanning For IP Addresses")
	time.sleep(2)
### SCAN LOCAL NETWORK [VIA WIFI] FOR IP ADDRESSES
        os.system("arp-scan -l --interface=wlan0 --localnet")
########################################################  
### TIMER
########################################################
    elif statement == "timer":
	def dateprint():
	    os.system("date --rfc-3339='ns'")
	seconds = input("Number of seconds: ")
	startTime = time.time()
	finishTime = startTime + seconds
### START SIMPLE TIMER [TIME MARKED IN SECONDS]
	while time.time() < finishTime:
  	    time.sleep(.05)
            bot.buddha()
	    dateprint()
########################################################  
### CRAWL
########################################################
########################################################
###          *** DOESN'T CURRENTLY WORK ***          ### 
########################################################
###    elif statement == "crawl":
### 	bot.atom()
### 	class LinkParser(HTMLParser):
### 	    def handle_starting(self, tag, attrs):
### 		if tag == 'a':
### 		    for (key, value) in attrs:
### 			if key == 'href':
### 			    newUrl = parse.urljoin(self.baseUrl, value)
### 			    self.links = self.links + [newUrl]
### 	    def getLinks(self, url):
### 		self.links = []
### 		self.baseUrl = url
### 		response = urlopen(url)
### 		if response.getheader('Content-Type')=='text/html':
### 		    htmlBytes = response.read()
### 		    htmlString = htmlBytes.decode("utf-8")
### 		    self.feed(htmlString)
### 		    return htmlString, self.links
### 		else:
### 		    return "",[]
### 	    def spider(url, word, maxPages):
### 		pagesToVisit = [url]
### 		numberVisited = 0
### 		foundWord = False
### 		while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
### 		    numberVisited = numberVisited +1
### 		    url = pagesToVisit[0]
### 	            pagesToVisit = pagesToVisit[1:]
### 		    try:
### 			print(numberVisited, "Visiting:", url)
### 			parser = LinkParser()
### 			data, links = parser.getLinks(url)
### 			if data.find(word)>-1:
### 			    foundWord = True
### 			pagesToVisit = pagesToVisit + links
### 			print(" **Success!** ")
###		    except:
### 			print(" **Failed!** ")
### 		if foundWord:
### 		    print("The word", word, "was found at", url)
### 		else:
### 		    print("Word never found")
########################################################  
### STARWARS
########################################################
    elif statement == "starwars":
        os.system('clear')
	bot.atom()
        print("Lets Watch StarWars...")
	time.sleep(3)
### WATCH ASCII VERSION OF STARTWARS IN THE TERMINAL
        os.system("telnet towel.blinkenlights.nl")
########################################################  
### LEARN
########################################################
    elif statement == "learn":
	bot.librarian()
        print("Let's Learn Some Shit...")
	time.sleep(3)

### LEARN SOMETHING NEW
        os.system("ls /usr/bin | xargs whatis | grep -v nothing | less ")
########################################################  
### JOURNAL
########################################################
    elif statement == "journal":
	bot.bshelf()
        os.system("read -p 'Enter Title: ' title ; nano /usr/bin/rhea/journal/$title ; gpg -e /usr/bin/rhea/journal/$title ; rm /usr/bin/rhea/journal/$title ")
########################################################  
### VULNSCAN
########################################################
    elif statement == "vulnscan":
	bot.atom()
        print("Starting SkipFish")
	time.sleep(3)
        os.system('read -p "Enter URL: " url ; read -p "Enter File Title: " title ; mkdir /usr/bin/rhea/skipfish/$title ; skipfish -o /usr/bin/rhea/skipfish/$title -S /usr/share/skipfish/dictionaries/minimal.wl $url')
########################################################  
### TOR
########################################################
    elif statement == "tor":
	bot.atom()
        print("Loading Tor")
        os.system("read -p 'Enter Site URL: ' site ; service start tor ; proxychains firefox $site ; service tor stop ")
########################################################  
### 13BOOKS
########################################################
    elif statement == "13books":
	bot.bshelf()
        os.system('read -p "Enter Title: " title ; nano /usr/bin/rhea/13books/$title ; gpg -e /usr/bin/rhea/13books/$title ; rm /usr/bin/rhea/13books/$title')
########################################################  
### DDOS
########################################################
    elif statement == "ddos":
	bot.network()
        os.system('read -p "Target: " target ; hping3 -S -P -U --flood -V --rand-source $target ')
########################################################  
### READ13
########################################################
    elif statement == "read13":
	bot.bshelf()
        os.system('ls 13books ; read -p "Enter Title (without file ext  ex: .gpg): " title ; gpg --decrypt-files /usr/bin/rhea/13books/$title.gpg ; less /usr/bin/rhea/13books/$title ; gpg --encrypt-files /usr/bin/rhea/13books/$title ; rm /usr/bin/rhea/13books/$title')
########################################################  
### AP13
########################################################
    elif statement == "ap13":
	bot.bshelf()
        os.system('ls 13books ; read -p "Enter Title (without file ext  ex: .gpg): " title ; gpg --decrypt-files /usr/bin/rhea/13books/$title.gpg ; nano /usr/bin/rhea/13books/$title ; gpg --encrypt-files /usr/bin/rhea/13books/$title ; rm /usr/bin/rhea/13books/$title')
########################################################  
### 13BS
########################################################
    elif statement == "13bs":
	bot.bshelf()
        os.system('ls /usr/bin/rhea/13books')
########################################################  
### RANDJOURN
########################################################
    elif statement == "randjourn":
	bot.bshelf()
        os.system('read -p "Enter Title: " title ; nano /usr/bin/rhea/journal/random/$title ; gpg -e /usr/bin/rhea/journal/random/$title ; rm /usr/bin/rhea/journal/random/$title')
########################################################  
### JOURNALBS
########################################################
    elif statement == "journalbs":
	bot.bshelf()
        os.system('ls /usr/bin/rhea/journal')
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
### READRAND
########################################################
    elif statement == "readrand":
	bot.bshelf()
        os.system('ls /usr/bin/rhea/journal/random/ ; read -p "Enter Title: " title ; gpg --decrypt-files "/usr/bin/rhea/journal/random/$title"')
########################################################  
### READJOURN
########################################################
    elif statement == "readjourn":
	bot.bshelf()
        os.system('read -p "Enter Title: " title ; gpg --decrypt-files /usr/bin/rhea/journal/$title.gpg ; less /usr/bin/rhea/journal/$title ; gpg --encrypt-files $title ; rm "/usr/bin/rhea/journal/$title"')
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
### DEF
########################################################
    elif statement == "def":
	bot.atom()
        os.system("read -p 'Enter Word: ' word ; curl dict://dict.org/d:$word ; read output")
########################################################  
### CATANDMOUSE
########################################################
    elif statement == "catandmouse":
	bot.atom()
        print("Loading Cat And Mouse" )
        os.system("/usr/games/oneko")
########################################################  
### RANDPASS
########################################################
    elif statement == "randpass":
	bot.atom()
        print("Generating Random Passwords...")
	time.sleep(3)
        os.system("strings /dev/urandom | head -n 13 | tr -d '\n'; echo" )
########################################################  
### XSM
########################################################
    elif statement == "xsm":
	bot.atom()
        print("Opening Terminal")
        os.system("/usr/bin/xsm")
########################################################  
### MAGNIFY
########################################################
    elif statement == "magnify":
	bot.atom()
	os.system("/usr/bin/xmag")
########################################################  
### XHYDRA
########################################################
    elif statement == "xhydra":
	bot.atom()
        os.system("/usr/bin/xhydra")
########################################################  
### MAIL
########################################################
    elif statement == "mail":
	bot.atom()
        os.system("/usr/bin/mail")
########################################################  
### WATCHTHIS
########################################################
    elif statement == "watchthis":
	bot.atom()
        os.system("/usr/bin/xeyes")
########################################################  
### CHECKMAIL
########################################################
    elif statement == "checkmail":
	bot.atom()
        os.system("/usr/bin/xdgmail")
########################################################  
### DRAW
########################################################
    elif statement == "draw":
	bot.atom()
        os.system("/usr/bin/lodraw")
########################################################  
### DATABASE
########################################################
    elif statement == "database":
	bot.atom()
        os.system("/usr/bin/lobase")
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
### BATTERY
########################################################
    elif statement == "battery":
	bot.atom()
	print("Getting Current Battery Level...")
	time.sleep(2)
	os.system("/usr/bin/acpi")
########################################################  
### WEB
########################################################
    elif statement == "web":
	bot.atom()
        os.system("w3m google.com")
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
### MTRANSCODE
########################################################
    elif statement == "mtranscode":
	bot.atom()
        os.system("/usr/bin/arista-gtk")
########################################################  
### DISKUSAGE
########################################################
    elif statement == "diskusage":
	bot.atom()
        os.system("/usr/bin/baobab")
########################################################  
### DISKUSAGE
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
### GETMANUAL
########################################################
    elif statement == "getmanual":
	bot.atom()
        os.system("/usr/bin/catman")
        os.system("read -p 'Enter Program To Find Manual' prog ; man $prog")
########################################################  
### CODEBLOCKS
########################################################
    elif statement == "codeblocks":
	bot.atom()
        os.system("/usr/bin/codeblocks")
########################################################  
### DIAL_TONE
########################################################
    elif statement == "dial_tone":
	bot.atom()
        os.system("/usr/bin/dial_tone")
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
### GOOGLECON
########################################################
    elif statement == "googlecon":
	bot.atom()
        os.system("/usr/bin/google")
########################################################  
### MUG
########################################################
    elif statement == "mug":
	bot.atom()
        print("Enter Targets Name")
        os.system('read -p "First Name: " fname ; read -p "Last Name: " lname ; read -p "Enter State: " state ; w3m "http://www.findmugshots.com/arrests/$fname"_"$lname"_"$state" && w3m http://mugshots.com/search.html?q=$fname+$lname ; read output ')
########################################################  
### CONTACTS
########################################################
    elif statement == "contacts":
	bot.atom()
        print("Loading Contact List")
        os.system("mv /usr/bin/rhea/Contacts.txt /usr/bin/rhea/Contacts ; sort < /usr/bin/rhea/Contacts > /usr/bin/rhea/Contacts.txt ; rm /usr/bin/rhea/Contacts ; less /usr/bin/rhea/Contacts.txt")
########################################################  
### ADDCON
########################################################
    elif statement == "addcon":
	bot.atom()
        os.system("read -p 'Enter Name: ' name ; read -p 'Enter Phone Number: ' num ; echo '$name --- $num' >> /usr/bin/rhea/Contacts.txt")
########################################################  
### PSYOP
########################################################
    elif statement == "psyop":
	bot.atom()
        os.system('read -p "Enter Psyop Title: " title ; read -p "Enter Date: " date ; read -p "Enter Target Name: " target ; read -p "Enter Notes: " notes ; echo "Title $title" > /usr/bin/rhea/psyop/$title ; echo "Date: $date" >> /usr/bin/rhea/psyop/$title ; echo "Name: $target" >> /usr/bin/rhea/psyop/$title ; echo "Notes: $notes" >> /usr/bin/rhea/psyop/$title ; gpg --encrypt-files /usr/bin/rhea/psyop/$title ; rm /usr/bin/rhea/psyop/$title')
########################################################  
### EDITPSYOP
########################################################
    elif statement == "editpsyop":
	bot.atom()
        os.system("read -p 'Enter Title: ' title ; gpg --decrypt-files /usr/bin/rhea/psyop/$title.gpg ; nano /usr/bin/rhea/psyop/$title ; gpg -e /usr/bin/rhea/psyop/$title ; rm /usr/bin/rhea/psyop/$title")
########################################################  
### READPSYOP
########################################################
    elif statement == "readpsyop":
	bot.atom()
        os.system("read -p 'Enter Title: ' title ; gpg --decrypt-files /usr/bin/rhea/psyop/$title.gpg ; rm /usr/bin/rhea/psyop/$title.gpg ; less /usr/bin/rhea/psyop/$title ; gpg --encrypt-files /usr/bin/rhea/psyop/$title ; rm /usr/bin/rhea/psyop/$title")
########################################################  
### POPHOOD
########################################################
    elif statement == "pophood":
###############################################################
### LOAD FUNCTION 'LOCK()' FROM FILE 'BOT.PY'
        bot.lock()
###############################################################
        print("Login:")
        username = raw_input("Username: ")
        if username == "13":
            print("Sounds Legit...")
        else: 
            bot.rhea()
            print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
### IF USERNAME IS INCORRECT, TERMINATE PROGRAM
            quit()
        bot.rhea()
### DO NOT PRINT PASSWORD TO STDOUT [DON'T DISPLAY IT ON THE SCREEN AS YOU TYPE]
        os.system("stty -echo")
        password = raw_input("Please Enter Password: ")
### TURN PRINT TO STDOUT BACK ON 
        os.system("stty echo")
        print("\n")
        if password == "[Getthefuckout13###]":
            bot.unlock()
            print("Access Granted")
            print("Please Wait While System Loads...")
### WAIT FOR (2) SECONDS BEFORE CONTINUING
            time.sleep(2)
	    bot.atom()
            os.system("less /usr/bin/rhea/13.py")
	else:
	    break
########################################################  
### MAINTENANCE
########################################################
    elif statement == "maintenance":
###############################################################
### LOAD FUNCTION 'LOCK()' FROM FILE 'BOT.PY'
        bot.lock()
###############################################################
        print("Login:")
        username = raw_input("Username: ")
        if username == "13":
            print("Sounds Legit...")
        else: 
	    bot.rhea()
	    print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
### IF USERNAME IS INCORRECT, TERMINATE PROGRAM
	    quit()
	bot.rhea()
### DO NOT PRINT PASSWORD TO STDOUT [DON'T DISPLAY IT ON THE SCREEN AS YOU TYPE]
	os.system("stty -echo")
	password = raw_input("Please Enter Password: ")
### TURN PRINT TO STDOUT BACK ON 
	os.system("stty echo")
	print("\n")
	if password == "[Getthefuckout13###]":
	    bot.unlock()
	    print("Access Granted")
	    print("Please Wait While System Loads...")
### WAIT FOR (2) SECONDS BEFORE CONTINUING
	    time.sleep(2)
	    bot.rhea()
	    print('Please Restart Rhea When Maintenance Is Complete.')
	    time.sleep(3)
	    os.system("nano /usr/bin/rhea/13.py")
	    bot.rhea()
	    print("Please restart Rhea for changes to take effect...")
	else:
	    break
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
        os.system("read -p 'Enter Target IP Address: ' ip ; lynx -dump 'http://www.ip-adress.com/ip_tracer/$ip' | grep address | egrep 'city|state|country' | awk '{print $3,$4,$5,$6,$7,$8,$9}' | sed 's\ip address flag \\'|sed 's\My\\' ; read output")
########################################################  
### WOLF
########################################################
    elif statement == "wolf":
	bot.atom()
        print("Let's Search Wolfram-Alpha")
        os.system("read -p 'Enter Search Terms (if more than one word, seperater with +): ' search ; google-chrome 'https://www.worlframalpha.com/input/?i=$search' ")
########################################################  
### FINDPRIME
########################################################
    elif statement == "findprime":
	bot.atom()
        print("Enter Range To Search")
        lower = int(input("Enter Lower Range: "))
        upper = int(input("Enter Upper Range: "))
        prime =[]
        print("Searching For Prime Numbers")
        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        break
                else:
                    prime.append(num)
        print(prime)
########################################################  
### FBD
########################################################
    elif statement == "fbd":
	bot.atom()
        os.system('read -p "Enter Name (Seperate with + ): " name ; service tor start ; proxychains firefox "https://www.facebook.com/public/?query="$name"" ; service tor stop')
########################################################  
### SOCIALSEARCH
########################################################
    elif statement == "socialsearch":
	bot.atom()
        os.system('read -p "Enter Name (Seperate With +): " name ; service tor start ; proxychains firefox "https://www.social-searcher.com/social-buzz/?q5="$name"" ; service tor stop')
########################################################  
### NOTE
########################################################
    elif statement == "note":
	bot.atom()
        os.system('read -p "Enter  Title: " title ; read -p "Enter Note: " note ; echo $note > /usr/bin/rhea/notepad/$title')
########################################################  
### APNOTE
########################################################
    elif statement == "apnote":
	bot.atom()
        os.system('ls /usr/bin/rhea/notepad ; read -p "Enter Title: " title ; read -p "Enter New Notes: " notes ; echo $notes >> /usr/bin/rhea/notepad/$title')
########################################################  
### READNOTE
########################################################
    elif statement == "readnote":
	bot.atom()
        os.system('ls notepad ; read -p "Enter Title: " title ; less /usr/bin/rhea/notepad/$title')
########################################################  
### NEEDCARD
########################################################
    elif statement == "needcard":
	bot.atom()
        os.system('read -p "Enter Card Name: " card ; read -p "Enter Deck Name: " deck ; read -p "Enter Cost: " cost ; read -p "Enter Card Type: " type ; echo "$card--$type--$cost--$deck" >> /usr/bin/rhea/lib13/needmtg.txt')
########################################################  
### SEARCHMTG
########################################################
    elif statement == "searchmtg":
	bot.atom()
        os.system('less /usr/bin/rhea/lib13/smtg.txt ; read -p "Enter Search Term: " search ; less -p $search /usr/bin/rhea/lib13/MagicCompRules_21031101.pdf')
########################################################  
### DESIGNER
########################################################
    elif statement == "designer":
	bot.atom()
        os.system("/usr/bin/designer")
########################################################  
### MALTEGO
########################################################
    elif statement == "maltego":
	bot.atom()
        os.system("/usr/bin/casefile")
########################################################  
### CALIBRE
########################################################
    elif statement == "calibre":
	bot.atom()
        os.system("/usr/bin/calibre")
########################################################  
### AUTOPSY
########################################################
    elif statement == "autopsy":
	bot.atom()
        os.system("/usr/bin/autopsy")
########################################################  
### CREEPY
########################################################
    elif statement == "creepy":
	bot.atom()
        os.system("/usr/bin/creepy")
########################################################  
### CUCKOO
########################################################
    elif statement == "cuckoo":
	bot.atom()
        os.system("/usr/bin/cuckoo")
########################################################  
### CYMOTHOA
########################################################
    elif statement == "cymothoa":
	bot.atom()
        os.system("/usr/bin/cymothoa")
########################################################  
### DFF
########################################################
    elif statement == "dff":
	bot.atom()
        os.system("man dff ; /usr/bin/dff")
########################################################  
### DFFGUI
########################################################
    elif statement == "dffgui":
	bot.atom()
        os.system("/usr/bin/dff-gui")
########################################################  
### DROPBOX
########################################################
    elif statement == "dropbox":
        bot.atom()
        os.system("man dropbox")
        os.system("read -p 'Enter Commands: ' com ; /usr/bin/dropbox $com")
########################################################  
### DUMPCAP
########################################################
    elif statement == "dumpcap":
        bot.atom()
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
### FIMAP
########################################################
    elif statement == "fimap":
        bot.atom()
        os.system("/usr/bin/fimap -h")
        os.system("read -p 'Enter Commands: ' com ; /usr/bin/fimap $com")
########################################################  
### GOTOSITE
########################################################
    elif statement == "gotosite":
        bot.atom()
	os.system("read -p 'Enter URL: ' url ; google-chrome $url")
########################################################  
### BROWSEW3M
########################################################
    elif statement == "browsew3m":
        bot.network()
	print("Enter URL")
	os.system("read -p 'Enter URL: ' url ; w3m $url ")
########################################################  
### DISCORD
########################################################
    elif statement == "discord":
        bot.atom()
        print("Opening Discord")
        os.system('google-chrome "https://discordapp.com/channels/230421669808701441/23042166980870144')
########################################################  
### 10D
########################################################
    elif statement == "10d":
        bot.atom()
	print("Enter Name: ")
        os.system('read -p "Enter First Name : " fname ; read -p "Enter Last Name : " lname ; read -p "Enter City : " city ; read -p "Enter State e.g. Al : " state ; w3m "http://10digits.us/n/"$fname"_"$lname"/location/"$city"_"$state""')
########################################################  
### ALLMTG
########################################################
    elif statement == "allmtg":
        bot.atom()
        print("Loading All Magic Rules")
        os.system('less /usr/bin/rhea/lib13/MagicCompRules_21031101.pdf')
########################################################  
### MTGPRICE
########################################################
    elif statement == "mtgprice":
        bot.atom()
        os.system('read -p "Enter Card Name (seperate with %20 instead of space): " cname ; w3m "http://www.mtgprice.com/search?search="$cname""')
########################################################  
### NMAP
########################################################
    elif statement == "nmap":
        bot.network()
        print("Starting nMap")
        os.system('read -p "Enter Host : " host ; nmap -v -A "$host" ')
########################################################  
### TIME
########################################################
    elif statement == "time":
	bot.clock()
        os.system("date --rfc-3339=ns")
########################################################  
### MTGADD
########################################################
    elif statement == "mtgadd":
        bot.atom()
        os.system('read -p "Enter Card Name: " card ; read -p "Enter Deck Name: (ex: SOI, EMN, etc... ) " deckname ; read -p "Enter Rarity: (ex: common, uncommon, rare, mythic rare)" rarity ; echo "$card---$deckname---$rarity" >> "/media/Program13/13/truecrypt1/lib13/magiccollection.txt" ')
        print("Card Has Been Added")
########################################################  
### ALLMTGC
########################################################
    elif statement == "allmtgc":
        bot.atom()
        print("Loading Cards...")
	time.sleep(3)
        os.system('less "/usr/bin/rhea/lib13/allmtg.txt"')
########################################################  
### ALICE
########################################################
    elif statement == "alice":
	os.system('clear')
	bot.alice()
########################################################  
### SOCIALIZE
########################################################
    elif statement == "socialize":
	bot.atoml()
        os.system("/usr/bin/setoolkit")
########################################################  
### HARVEST
########################################################
    elif statement == "harvest":
	bot.atom()
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
	bot.atom()
	print('Loading Recon-ng...')
	time.sleep(3)
	os.system("/usr/bin/recon-ng")
########################################################  
### RECIPE
########################################################
    elif statement == "recipe":
        os.system('clear')
	bot.atom()
        print("What Would You Like To Search For?")
        os.system('read -p "Enter Recipe (Seperate Words With %20): " recipe ; google-chrome "http://allrecipes.com/search/results/?wt="$recipe"&sort=re"')
###############################################
###          LEARN SOME NEW SHIT            ###
###       (Some Files Need Editing)         ###
###############################################
########################################################  
###    CREDITCARDFRAUD
########################################################
    elif statement == "creditcardfraud":
	bot.rhea()
	print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
	time.sleep(1)
	print("Loading...")
	time.sleep(3)
	os.system('less /usr/bin/rhea/lib13/ccf')
########################################################  
###    PICKMASTERLOCK
########################################################
    elif statement == "pickmasterlock":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
	os.system('less /usr/bin/rhea/lib13/pml')
########################################################  
###    SMOKEBOMB
########################################################
    elif statement == "smokebomb":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/smoke')
########################################################  
###    LOCKPICKING
########################################################
    elif statement == "lockpicking":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/apl')
########################################################  
###    BEIGEBOX
########################################################
    elif statement == "beigebox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/beige')
########################################################  
###    JAMRADAR
########################################################
    elif statement == "jamradar":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/jamr')
########################################################  
###    HOTWIRE
########################################################
    elif statement == "hotwire":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/hwire')
########################################################  
###    UNLISTEDPHONE
########################################################
    elif statement == "unlistedphone":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/uphone')
########################################################  
###    CHEMICALEQUIV
########################################################
    elif statement == "chemicalequiv":
###############################################################
### LOAD FUNCTION 'LOCK()' FROM FILE 'BOT.PY'
        bot.lock()
###############################################################
        print("Login:")
        username = raw_input("Username: ")
        if username == "13":
            print("Sounds Legit...")
        else: 
            bot.rhea()
            print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
### IF USERNAME IS INCORRECT, TERMINATE PROGRAM
            quit()
        bot.rhea()
### DO NOT PRINT PASSWORD TO STDOUT [DON'T DISPLAY IT ON THE SCREEN AS YOU TYPE]
        os.system("stty -echo")
        password = raw_input("Please Enter Password: ")
### TURN PRINT TO STDOUT BACK ON 
        os.system("stty echo")
        print("\n")
        if password == "[Getthefuckout13###]":
            bot.unlock()
            print("Access Granted")
            print("Please Wait While System Loads...")
### WAIT FOR (2) SECONDS BEFORE CONTINUING
            time.sleep(2)
            bot.rhea()
            print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
            time.sleep(1)
            print("Loading...")
            time.sleep(3)
            os.system('less /usr/bin/rhea/lib13/chemeq')
	else:
	    break
########################################################  
###    PHONETAP
########################################################
    elif statement == "phonetap":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/tapphone')
########################################################  
###    PHONESYSTEM
########################################################
    elif statement == "phonesystem":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/phonesys')
########################################################  
###    AQUABOX
########################################################
    elif statement == "aquabox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/aqua')
########################################################  
###    BLACKBOX
########################################################
    elif statement == "blackbox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/black')
########################################################  
###    BLOTTOBOX
########################################################
    elif statement == "blottobox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/blotto')
########################################################  
###    BROWNBOX
########################################################
    elif statement == "brownbox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/brown')
########################################################  
###    CLEARBOX
########################################################
    elif statement == "clearbox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/clear')
########################################################  
###    CARFTMOD
########################################################
    elif statement == "carftmod":
###############################################################
### LOAD FUNCTION 'LOCK()' FROM FILE 'BOT.PY'
        bot.lock()
###############################################################
        print("Login:")
        username = raw_input("Username: ")
        if username == "13":
            print("Sounds Legit...")
        else: 
            bot.rhea()
            print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
### IF USERNAME IS INCORRECT, TERMINATE PROGRAM
            quit()
        bot.rhea()
### DO NOT PRINT PASSWORD TO STDOUT [DON'T DISPLAY IT ON THE SCREEN AS YOU TYPE]
        os.system("stty -echo")
        password = raw_input("Please Enter Password: ")
### TURN PRINT TO STDOUT BACK ON 
        os.system("stty echo")
        print("\n")
        if password == "[Getthefuckout13###]":
            bot.unlock()
            print("Access Granted")
            print("Please Wait While System Loads...")
### WAIT FOR (2) SECONDS BEFORE CONTINUING
            time.sleep(2)
            bot.rhea()
            print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
            time.sleep(1)
            print("Loading...")
            time.sleep(3)
            os.system('less /usr/bin/rhea/lib13/carft')
	else:
	    break
########################################################  
###    MACE
########################################################
    elif statement == "mace":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/mace')
########################################################  
###    BLUEBOX
########################################################
    elif statement == "bluebox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/blue')
########################################################  
###    RECOGNIZECC
########################################################
    elif statement == "recognizecc":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/reccreditcard')
########################################################  
###    NEWID
########################################################
    elif statement == "newid":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/newid')
########################################################  
###    PHONENUBERS
########################################################
    elif statement == "phonenumbers":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/phonenum')
########################################################  
###    REDBOX
########################################################
    elif statement == "redbox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/red')
########################################################  
###    SILVERBOX
########################################################
    elif statement == "silverbox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/silver')
########################################################  
###    WHITEBOX
########################################################
    elif statement == "whitebox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/white')
########################################################  
###    GOLDBOX
########################################################
    elif statement == "goldbox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/gold')
########################################################  
###    LUNCHBOX
########################################################
    elif statement == "lunchbox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/lunch')
########################################################  
###    OLIVEBOX
########################################################
    elif statement == "olivebox":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/olive')
########################################################  
###    TELNET
########################################################
    elif statement == "telnet":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/telnet')
########################################################  
###    INFINITYTRANS
########################################################
    elif statement == "infinitytrans":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/infinity')
########################################################  
###    MYRIGHTS
########################################################
    elif statement == "myrights":
        bot.rhea()
        print("Neither I, nor my developer shall be held responsible for your\n use of imformation attained within this program")
        time.sleep(1)
        print("Loading...")
        time.sleep(3)
        os.system('less /usr/bin/rhea/lib13/rights')
###############################################
###############################################
########################################################
###
########################################################
    elif statement == "hackchat":
	bot.rhea()
	print('Loading HackChat')
	time.sleep(2)
	bot.hchat()
###############################################
########################################################  
### QUIT
########################################################
    elif statement == "quit":
        with open("Rheaconv.txt", "a") as myfile:
            myfile.write("\nRhea terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
	os.system('clear')
        with open("Rhea.log", "a") as myfile:
            myfile.write("\nRhea terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
	bot.buck()
	print('Whatever...')
	os.system('cp /usr/bin/rhea/13.py /media/Program13/13/truecrypt1/.backup/13.py.backup')
        os.system('cp /usr/bin/rhea/bot.py /media/Program13/13/truecrypt1/.backup/bot.py.backup')
        os.system('cp /usr/bin/rhea/psych.py /media/Program13/13/truecrypt1/.backup/psych.py.backup')
        os.system('cp Rheaconv.txt /media/Program13/13/truecrypt1/.backup/Rheaconv.txt.backup')
        os.system('cp Rhea.log /media/Program13/13/truecrypt1/.backup/Rhea.log.backup')
        quit()

        if __name__ == "__main__":
             bot.main()
