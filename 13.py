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
###
########################################################
    elif statement == "kronos":
	os.system('python /usr/bin/rhea/kronos.py')
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
### OZZY
########################################################
    elif statement == "ozzy":
### TRIBUTE TO OZZY
	os.system('clear')
	bot.rnr()
	os.system('figlet "Rock & Roll"')
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
### DDG
########################################################
    elif statement == "ddg":
	bot.atom()
        print("Search Duck Duck Go")
### SEARCH DUCKDUCKGO.COM FROM TERMINAL
        os.system('read -p "Enter Search Term seperate terms with + :" search ; w3m "https://duckduckgo.com/?q=$search&t=h_&ia=web" ' )
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
### SCREENSHOT
########################################################
    elif statement == "screenshot":
	bot.atom()
### TAKE SCREENSHOT OF CURRENT SCREEN
        os.system("/usr/bin/gnome-screenshot")
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
### TAKENOTE
########################################################
    elif statement == "takenote":
	bot.atom()
### OPEN KEEPNOTE
        os.system('keepnote')
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
### 13BOOKS
########################################################
    elif statement == "13books":
	bot.bshelf()
        os.system('read -p "Enter Title: " title ; nano /usr/bin/rhea/13books/$title ; gpg -e /usr/bin/rhea/13books/$title ; rm /usr/bin/rhea/13books/$title')
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
### GOOGLECON
########################################################
    elif statement == "googlecon":
	bot.atom()
        os.system("/usr/bin/google")
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
### WOLF
########################################################
    elif statement == "wolf":
	bot.atom()
        print("Let's Search Wolfram-Alpha")
        os.system("read -p 'Enter Search Terms (if more than one word, seperater with +): ' search ; google-chrome 'https
://www.worlframalpha.com/input/?i=$search' ")
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
### DROPBOX
########################################################
    elif statement == "dropbox":
        bot.atom()
        os.system("man dropbox")
        os.system("read -p 'Enter Commands: ' com ; /usr/bin/dropbox $com")
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
### RECIPE
########################################################
    elif statement == "recipe":
        os.system('clear')
	bot.atom()
        print("What Would You Like To Search For?")
        os.system('read -p "Enter Recipe (Seperate Words With %20): " recipe ; google-chrome "http://allrecipes.com/search/results/?wt="$recipe"&sort=re"')
###############################################
###############################################
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
