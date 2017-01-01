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
import psych#.PY     ### KRONOS' RESPONSES                 ###
import bot#.PY       ### KRONOS' FUNCTIONS                 ###
### FROM /USR/BIN/RHEA ###                                ###
#############################################################
### THESE FILES HOLD OUR FUNCTIONS AND RESPONSES FOR KRONOS ###
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
        self.log = open("Kronos.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
while True:
    with open("Kronosconv.txt", "a") as myfile:
        myfile.write("\nKronos started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
    with open("Kronos.log", "a") as myfile:
        myfile.write("\nKronos started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
###############################################################
### LOAD FUNCTION 'LOCK()' FROM FILE 'BOT.PY'
    bot.lock()
###############################################################
    print("Login:")
    username = raw_input("Username: ")
    if username == "13":
        print("Sounds Legit...")
    else:
        bot.kronos()
        with open("Kronos.log", "a") as myfile:
            myfile.write("\nKronos terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to Incorrect Username.\n")
        print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
### IF USERNAME IS INCORRECT, TERMINATE PROGRAM
        quit()
    bot.kronos()
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
        bot.kronos()
        print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
        with open("Kronos.log", "a") as myfile:
            myfile.write("\nKronos terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to Incorrect Username.\n")
### IF PASSWORD IS INCORRECT, TERMINATE PROGRAM
        quit()
### PROGRAM INTRODUCTION
bot.kronos()
os.system("toilet Kronos")
time.sleep(5)
os.system('clear')
bot.kronos()
name = raw_input("What is your name? ")
with open("Kronos.log", "a") as myfile:
    myfile.write("\nKronos started by:  " + name + "\n")
with open("Kronosconv.txt", "a") as myfile:
    myfile.write("\nKronos started by:  " + name + "\n")
print("Hello, " + name + ". my name is Kronos.")
time.sleep(2)
bot.kronos()
print("What would you like me to do?")
time.sleep(2)
os.system('clear')
bot.kronos()
print("type 'quit' to exit program")
print("type '?' for help")
### START OF MAIN PROGRAM
while True:
    statement = raw_input(">")
    os.system('clear')
    bot.kronos()
### ANALYZE USER INPUT AND RETURN REPONSE FROM PSYCH.PY
    print(bot.analyze(statement))
########################################################
### ?
########################################################
    if statement == "?":
        bot.kronos()
        print("Loading available commands, " + name)
        time.sleep(3)
### LOAD BASH SCRIPT CONTAINING LIST OF COMMANDS WITH DESCRIPTIONS
        os.system('sh /usr/bin/rhea/comphelp.sh')
########################################################
### RESTART
########################################################
    elif statement == "restart":
        bot.kronos()
        print('Restarting. Please wait, ' + name)
        time.sleep(2)
### RESTART KRONOS WITHOUT HAVING TO EXIT AND RELOAD PROGRAM
        os.execv(sys.executable, ['python'] + sys.argv)
    elif statement == "commands":
        print(commands)
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
        print('You must have html2text installed to use this function.\n Do you have html2text installed?')
        statement == raw_input("y/n")
        if statement == "y":
            os.system("read -p 'Enter URL: ' url ; wget -qO- $url | html2text")
        else:
            print('Please install html2text via: sudo apt-get install html2text')
            continue
########################################################  
### SHUTDOWN
########################################################
    elif statement == "shutdown":
        bot.rhea()
        print("When would you like to shutdown, " + name + "?")
### SHUTDOWN COMPUTER SYSTEM AT SPECIFIED TIME [IN MINS]
        os.system('read -p "Enter Time Till Shutdown In Mins: " mins ; echo "SHUTTING DOWN IN $mins MINS...\n ^c TOCANCEL" ; shutdown -h +$mins')
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
### FIND
########################################################
    elif statement == "find":
        bot.atom()
        print("Who are you looking for, " + name + "?")
### SEARCH FOR INFORMATION ON TARGET WITH NAME AND STATE
        os.system('read -p "Enter First Name:" fname ; read -p "Enter Middle Name:" mname ; read -p "Enter Last Name:"lname ; read -p "Enter City:" city ; read -p "Enter State: " state ; w3m "https://pipl.com/search/?q=$fname+$mname+$lname&l=sloc=&in=5" && w3m "https://www.findmugshots.com/arrests/"$fname"_"$lname"_"$state && w3m "http://mugshots.com/search.html?q="$fname"+"$lname && w3m "http://10digits.us/n/"$fname"_"$lname"/location/"$city"_"$state ; read output ')
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
### HACKNEWS                                                                                 ###
################################################################################################
### elif statement == "hacknews":                                                            ###
###     os.system('clear')                                                                   ###
###     bot.poc()                                                                            ###
###     print("Getting Hack News...")                                                        ###
###     response = requests.get("https://latesthackingnews.com/category/vulnerabilities/")   ###
########################   ADD HTML2TEXT   #####################################################
###     txt = response.text                                                                  ###
###     print(txt)                                                                           ###
################################################################################################
################################################################################################
################################################################################################
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
        os.system("read -p 'Enter Case Number:' title ; gpg --decrypt-files /usr/bin/rhea/casefile/$title.gpg ; nano/usr/bin/rhea/casefile/$title ; gpg -e /usr/bin/rhea/casefile/$title ; rm /usr/bin/rhea/casefile/$title")
########################################################  
### CFREAD
########################################################
    elif statement == "cfread":
        bot.atom()
### READ AN EXISTING CASEFILE
        os.system("read -p 'Enter Case Number:' case ; gpg --decrypt-files /usr/bin/rhea/casefile/$case.gpg ; rm/usr/bin/rhea/$case.gpg ; less /usr/bin/rhea/casefile/$case ; gpg -e /usr/bin/rhea/casefile/$case ; rm /usr/bin/rhea/casefile/$case")
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
### KEYS
########################################################
    elif statement == "keys":
        bot.atom()
### START SEAHORSE [PASSWORDS AND KEYS MANAGER]
        os.system("/usr/bin/seahorse")
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
        os.system('cp /usr/bin/rhea/kronos.py /media/Program13/13/truecrypt1/.backup/kronos.py.backup')
        os.system('cp /usr/bin/rhea/bot.py /media/Program13/13/truecrypt1/.backup/bot.py.backup')
        os.system('cp /usr/bin/rhea/psych.py /media/Program13/13/truecrypt1/.backup/psych.py.backup')
        os.system('cp Kronosconv.txt /media/Program13/13/truecrypt1/.backup/Kronosconv.txt.backup')
        os.system('cp Kronos.log /media/Program13/13/truecrypt1/.backup/Kronos.log.backup')
        quit()

        if __name__ == "__main__":
             bot.main()
