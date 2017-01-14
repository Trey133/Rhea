#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import re
import sys
import users
import time
#############################################################
### IMPORT ###                                            ###
import psych#.PY     ### D34D9001's RESPONSES             ###
import bot#.PY       ### D34D9001's FUNCTIONS             ###
### FROM /USR/BIN/RHEA ###                                ###
#############################################################
### THESE FILES HOLD OUR FUNCTIONS AND RESPONSES FOR D34D9001 ###
#############################################################
#############################################################
###   import image_scraper ### [THIS IS NEEDED FOR (1) COMMAND.]
#############################################################
### THIS PROGRAM WILL NOT FUNCTION PROPERLY IF NOT RUN AS 'ROOT'
os.system('sudo')
### LOGIN SCREEN
os.system('clear')
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("D34D9001.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
while True:
    osys = raw_input("ARE YOU USING KALI LINUX? y/n: ")
    if osys == "n":
	os.system('python /usr/bin/rhea/dc.py')
        os.system('python /media/root/13/truecrypt1/rhea/dc.py')
    elif osys == "y":
	bot.dragon()
	time.sleep(1)
    import config
    with open("D34D9001conv.txt", "a") as myfile:
        myfile.write("\nD34D9001 started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
    with open("D34D9001.log", "a") as myfile:
        myfile.write("\nD34D9001 started at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "\n")
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
        with open("D34D9001.log", "a") as myfile:
            myfile.write("\nD34D9001 terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to Incorrect Username.\n")
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
        if osys == "n":
            os.system("gpg -e -r Ender /usr/bin/rhea/config.py --output '/usr/bin/rhea/config.py.gpg' ")
    	    os.system('rm config.py')
            os.system('rm config.pyc')
	elif osys == "y":
	    bot.dragon()
	    time.sleep(2)
        os.system('clear')
        print("Access Granted")
        print("Please Wait While System Loads...")
### WAIT FOR (2) SECONDS BEFORE CONTINUING
        time.sleep(2)
        break
    else:
        bot.dp()
        print("INTRUDER ALERT!!!" , "SYSTEM LOCKED")
        with open("D34D9001.log", "a") as myfile:
            myfile.write("\nD34D9001 terminated at:  " + time.strftime("%H:%M:%S") + "  " + time.strftime("%d/%m/%Y") + "Due to Incorrect Username.\n")
        if osys == "n":
### IF PASSWORD IS INCORRECT, TERMINATE PROGRAM
            os.system("gpg -e -u Ender /usr/bin/rhea/config.py --output '/usr/bin/rhea/config.py.gpg' ")
            os.system('rm config.py')
            os.system('rm config.pyc')
	elif osys == "y":
	    bot.dragon()
	    time.sleep(2)
	os.system('clear')
        quit()
### PROGRAM INTRODUCTION
bot.dp()
os.system("toilet ' D34D9001'")
time.sleep(5)
os.system('clear')
bot.dp()
name = raw_input("What is your name? ")
with open("D34D9001.log", "a") as myfile:
    myfile.write("\nD34D9001 started by:  " + name + "\n")
with open("/media/Program13/13/truecrypt1/rhea/users.py" , "w") as myfile:
    myfile.write("#!/usr/bin/python\nname = " + "\"" + name + "\"")
with open("/usr/bin/rhea/users.py" , "w") as myfile:
    myfile.write("name = " + "\"" + name + "\"")
with open("D34D9001conv.txt", "a") as myfile:
    myfile.write("\nD34D9001 started by:  " + name + "\n")
print("What's up " + name + "? My name is D34D9001.")
time.sleep(2)
bot.dp()
opsys = raw_input("Which Operating System Are You Using?: cyborg // kali // ubuntu1604 \n[DP@CL]: ")
####################
####################
####################
### CYBORG LINUX ###
####################
####################
####################
if opsys == "cyborg":
    os.system("python /media/Program13/13/truecrypt1/rhea/D34D9001_Cyborg.py")
##############
##############
##############
###  KALI  ###
##############
##############
##############
elif opsys == "kali":
    os.system('python /media/root/13/truecrypt1/rhea/D31D9001_kali.py')
####################
####################
####################
### UBUNTU 16.04 ###
####################
####################
####################
elif opsys == "ubuntu1604":
    os.system('python /media/Program13/13/truecrypt1/rhea/D34D9001_Ubuntu.py')
else:
    print("ERROR: Operating System '" + opsys + "' Not Supported")
