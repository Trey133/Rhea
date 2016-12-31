#!/usr/bin/python

def menu():
print (‘Welcome to the menu’)
choice = (raw_input(‘Would you like to encrypt or decrypt? Enter E for encrypt or D for decrypt: ‘)).upper()
if choice == ‘E’:
encrypt()
elif choice == ‘D’:
decrypt()
else:
print ‘That is not a valid answer’
menu()

def encrypt():
plaintext=raw_input(“Please enter the message you wish to encode: “)
#This allows the user to enter the message they wish to encrypt.
keyword=raw_input(“Please enter your keyword, preferably shorter than the plaintext: “)
#This allows the user to enter a keyword.
encoded=””
#This creates a string for the user to input the encrypted message to.
while len(keyword)len(plaintext):
#This sees if the string length of the keyword is now longer than the string length of the plaintext.
newkey=keyword[:len(plaintext)]
#This cuts the string length of the keyword
for c in range(len(plaintext)):
char=ord(plaintext[c])
temp=ord(keyword[c])
newchar=char+temp
if newchar>ord(“Z”):
newchar-=25
newnewchar=chr(newchar)
encoded+=newnewchar
print(encoded)

def decrypt():
plaintext=raw_input(“Please enter the message you wish to decode: “)
#This allows the user to enter the message they wish to encrypt.
keyword=raw_input(“Please enter your keyword, preferably shorter than the plaintext: “)
#This allows the user to enter a keyword.
encoded=””
#This creates a string for the user to input the encrypted message to.
while len(keyword)len(plaintext):
#This sees if the string length of the keyword is now longer than the string length of the plaintext.
newkey=keyword[:len(plaintext)]
#This cuts the string length of the keyword
for c in range(len(plaintext)):
char=ord(plaintext[c])
temp=ord(keyword[c])
newchar=char-temp
if newchar<ord("a"):
newchar+=25
newnewchar=chr(newchar)
encoded+=newnewchar
print(encoded)

menu()
