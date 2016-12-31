#!/usr/bin/python
import os
import time
import re
import urllib
import urllib2
import sys
import random
import math
import subprocess

currencies = [
    ('BTCUSD', '$'),
]

commands = { 
              "weather" : "Get The Forcast.",
              "library" : "Show The Bookshelf.",
              "program13" : "Visit Program13.me.",
              "play" : "Play A Game.", 
              "moon" : "Show Phases Of The Moon.",
              "talk" : "Talk To Bot13",
              "p13" : "Loads p13 bash program.",
              "fuckshitup" : "fuckshitup-scanner",
              "bluepot" : "bluetooth honeypot",
              "mercury" : "mercury droid",
              "tshark" : "Terminal Wireshark",
              "calendar" : "Display Calendar",
              "xcalc" : "Display Calculator",
              "gpg" : "Generate GPG Key",
              "viper" : "viper.py",
              "google" : "Google Search",
              "googlepat" : "Google Patent Search",
              "loc" : "Library of Congress",
              "pipl" : "Pipl People Search",
              "download" : "Download Files From Website",
              "webinfo" : "Get Vuln Info From Website",
              "allpics" : "Get All Picture Files From Website.",
              "cfc" : "Create New Casefile.",
              "cfadd" : "Add Information To Casefile.",
              "cfread" : "Read Casefile",
              "cflist" : "List Available Casefiles.",
              "ddg" : "Search DuckDuckGo.",
              "hideme" : "Auto Start Tor And Open Browser @ https://check.torproject.org",
              "drift" : "Auto Configure & Start Drifnet And Supporting Software.",
              "wipass" : "Show Current Wifi Network w/ Password.",
              "ipscan" : "Scan Network For IP Addresses.",
              "starwars" : "Play StarrrWars In The Terminal.",
              "learn" : "Learn Somthing New.",
              "journal" : "Open New Journal Entry.",
              "tor" : "Start Tor Service And Open Browser @ check.torproject.org.",
              "disfire" : "Disable Firewall",
              "refire" : "Enable Firewall",
              "def" : "Define A Word.",
              "catandmouse" : "Start Cat And Mouse Game.",
              "randpass" : "Generate A Random Password.",
              "..pwnrepo" : "List ..pwn Reports",
              "..pwn" : "Run ..pwn",
              "readpwn" : "Read ..pwn Report.",
              "redpill" : "Exit The Matrix",
              "wolf" : "Search WolframAlpha",
              "geoip" : "Get Geographical Information From IP Address",                            
           }
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
 
psychobabble = [
    [r'I need (.*)',
     ["Why" "do" "you" "need" "{0}",
      "Would" "it" "really" "help" "you" "to" "get" "{0}",
      "Are" "you" "sure" "you" "need" "{0}"]],
 
    [r'Why dont you ([^\?]*)\??',
     ["Do" "you" "really" "think" "I" "don't" "{0}",
      "Perhaps" "eventually" "I" "will" "{0}",
      "Do" "you" "really" "want" "me" "to" "{0}"]],
 
    [r'Why cant I ([^\?]*)\??',
     ["Do" "you" "think" "you" "should" "be" "able" "to" "{0}",
      "If" "you" "could" "{0}" "what" "would" "you" "do",
      "I" "dont" "know" "why" "cant" "you" "{0}",
      "Have" "you" "really" "tried"]],
 
    [r'I cant (.*)',
     ["How" "do" "you" "know" "you" "cant" "{0}",
      "Perhaps" "you" "could" "{0}" "if" "you" "tried",
      "What" "would" "it" "take" "for" "you" "to" "{0}"]],
 
    [r'I am (.*)',
     ["Did" "you" "come" "to" "me" "because" "you" "are" "{0}",
      "How" "long" "have" "you" "been" "{0}",
      "How" "do" "you" "feel" "about" "being" "{0}"]],
 
    [r'Im (.*)',
     ["How" "does" "being" "{0}" "make" "you" "feel",
      "Do" "you" "enjoy" "being" "{0}",
      "Why" "do" "you" "tell" "me" "youre" "{0}",
      "Why" "do" "you" "think" "youre" "{0}"]],
 
    [r'Are you ([^\?]*)\??',
     ["Why" "does" "it" "matter" "whether" "I" "am" "{0}",
      "Would" "you" "prefer" "it" "if" "I" "were" "not" "{0}",
      "Perhaps" "you" "believe" "I" "am" "{0}",
      "I" "may" "be" "{0}" "what" "do" "you" "think"]],
 
    [r'What (.*)',
     ["Why" "do" "you" "ask",
      "How" "would" "an" "answer" "to" "that" "help" "you",
      "What" "do" "you" "think"]],
 
    [r'Because (.*)',
     ["Is" "that" "the" "real" "reason",
      "What" "other" "reasons" "come" "to" "mind",
      "Does" "that" "reason" "apply" "to" "anything" "else",
      "If" "{0}" "what" "else" "must" "be" "true"]],
 
    [r'(.*) sad (.*)',
     ["Aww" "well" "lets" "be" "a" "whiney" "little" "bitch" "about" "it" "shall" "we",
      "Get" "over" "it" "cry" "baby",
      "This" "is" "me" "playing" "you" "the" "worlds" "smallest" "violen",
      "Cry" "me" "a" "river" "and" "then" "float" "the" "fuck" "away" "from" "me" "Debby Downer"]],

    [r'(.*) sorry (.*)',
     ["There" "are" "many" "times" "when" "no" "apology" "is" "needed",
      "What" "feelings" "do" "you" "have" "when" "you" "apologize"]],
 
    [r'Hello(.*)',
     ["Hello" "Im" "glad" "you" "could" "drop" "by" "today",
      "Hi" "how" "are" "you" "today",
      "Hello" "how" "are" "you" "feeling" "today",
      "Hey" "How" "are" "you",
      "Hello",
      "Whats" "up",
      "Whats" "going" "on," "dude"]],
 
    [r'hey(.*)',
     ["Hey" "How" "are" "you",
      "Hello.",
      "Whats" "up",
      "Whats" "going" "on," "dude",
      "Hello" "Im" "glad" "you" "could" "drop" "by" "today",
      "Hi" "how" "are" "you" "today",
      "Hello" "how" "are" "you" "feeling" "today"]],

    [r'whats up(.*)',
     ["Hey" "How" "are" "you",
      "Hello",
      "Whats" "up",
      "Whats" "going" "on," "dude",
      "Hello" "Im" "glad" "you" "could" "drop" "by" "today",
      "Hi" "how" "are" "you" "today",
      "Hello" "how" "are" "you" "feeling" "today"]],

    [r'I think (.*)',
     ["Do" "you" "doubt" "{0}",
      "Do" "you" "really" "think" "so",
      "But" "youre" "not" "sure" "{0}"]],
 
    [r'(.*) friend (.*)',
     ["Tell" "me" "more" "about" "your" "friends",
      "When" "you" "think" "of" "a" "friend" "what" "comes" "to" "mind",
      "Why" "dont" "you" "tell" "me" "about" "a" "childhood" "friend"]],
 
    [r'Yes',
     ["You" "seem" "quite" "sure",
      "OK" "but" "can" "you" "elaborate" "a" "bit"]],
 
    [r'(.*) computer(.*)',
     ["Are" "you" "really" "talking" "about" "me",
      "Does" "it" "seem" "strange" "to" "talk" "to" "a" "computer",
      "How" "do" "computers" "make" "you" "feel",
      "Do" "you" "feel" "threatened" "by" "computers"]],
 
    [r'Is it (.*)',
     ["Do" "you" "think" "it" "is" "{0}",
      "Perhaps" "its" "{0}" "what" "do" "you" "think",
      "If" "it" "were" "{0}" "what" "would" "you" "do",
      "It" "could' 'well" "be" "that" "{0}"]],
 
    [r'It is (.*)',
     ["You" "seem" "very" "certain",
      "If" "I" "told" "you" "that" "it" "probably" "isnt" "{0}" "what" "would" "you" "feel"]],
 
    [r'Can you ([^\?]*)\??',
     ["What" "makes" "you" "think" "I" "cant" "{0}",
      "If" "I" "could" "{0}" "then" "what",
      "Why" "do" "you" "ask" "if" "I" "can" "{0}"]],
 
    [r'Can I ([^\?]*)\??',
     ["Perhaps" "you" "dont" "want" "to" "{0}",
      "Do" "you" "want" "to" "be" "able" "to" "{0}",
      "If" "you" "could" "{0}" "would" "you"]],
 
    [r'You are (.*)',
     ["Why" "do" "you" "think" "I" "am" "{0}",
      "Does" "it" "please" "you" "to" "think" "that" "Im" "{0}",
      "Perhaps" "you" "would" "like" "me" "to" "be" "{0.",
      "Perhaps" "youre" "really" "talking" "about" "yourself"]],
 
    [r'Youre (.*)',
     ["Why" "do" "you" "say" "I" "am" "{0}",
      "Why" "do" "you" "think" "I" "am" "{0}",
      "Are" "we" "talking" "about" "you" "or" "me"]],
 
    [r'I dont (.*)',
     ["Dont" "you" "really" "{0}",
      "Why" "dont" "you" "{0}",
      "Do" "you" "want" "to" "{0}"]],
 
    [r'I feel (.*)',
     ["Good" "tell" "me" "more" "about" "these" "feelings",
      "Do" "you" "often" "feel" "{0}",
      "When" "do" "you" "usually" "feel" "{0}",
      "When" "you" "feel" "{0}" "what" "do" "you" "do"]],
 
    [r'I have (.*)',
     ["Why" "do" "you" "tell" "me" "that" "youve" "{0}",
      "Have" "you" "really" "{0}",
      "Now" "that" "you" "have" "{0}" "what" "will" "you" "do" "next"]],
 
    [r'I would (.*)',
     ["Could" "you" "explain" "why" "you" "would" "{0}",
      "Why" "would" "you" "{0}",
      "Who" "else" "knows" "that" "you" "would" "{0}"]],
 
    [r'(.*)s there (.*)',
     ["Do" "you" "think" "there" "is" "{0}",
      "Its" "likely" "that" "there" "is" "{0}",
      "Would" "you" "like" "there" "to" "be" "{0}"]],
 
    [r'My (.*)',
     ["I" "see" "your" "{0}",
      "Why" "do" "you" "say" "that" "your" "{0}",
      "When" "your" "{0}" "how" "do" "you" "feel"]],
 
    [r'You (.*)',
     ["We" "should" "be" "discussing" "you" "not" "me",
      "Why" "do" "you" "say" "that" "about" "me",
      "Why" "do" "you" "care" "whether" "I" "{0}"]],
 
    [r'Why (.*)',
     ["Why" "dont" "you" "tell" "me" "the" "reason" "why" "{0}",
      "Why" "do" "you" "think" "{0}"]],
 
    [r'(.*) want (.*)',
     ["What" "would" "it" "mean" "to" "you" "if" "you" "got" "{0}",
      "Why" "do" "you" "want" "{0}",
      "What" "would" "you" "do" "if" "you" "got" "{0}",
      "If" "you" "got" "{0}" "then" "what" "would" "you" "do"]],
 
    [r'(.*) mother(.*)',
     ["Tell" "me" "more" "about" "your" "mother",
      "What" "was" "your" "relationship" "with" "your" "mother" "like",
      "How" "do" "you" "feel" "about" "your" "mother",
      "How" "does" "this" "relate" "to" "your" "feelings" "today",
      "Good" "family" "relations" "are" "important"]],
 
    [r'(.*) father(.*)',
     ["Tell" "me" "more" "about" "your" "father",
      "How" "did" "your" "father" "make" "you" "feel",
      "How" "do" "you" "feel" "about" "your" "father",
      "Does" "your" "relationship" "with" "your" "father" "relate" "to" "your" "feelings" "today",
      "Do" "you" "have" "trouble" "showing" "affection" "with" "your" "family"]],
 
    [r'(.*) bitch(.*)',
     ["Dont" "cuss" "at" "me" "mother" "fucker",
      "Watch" "your" "fucking" "mouth",
      "Do" "you" "kiss" "your" "mother" "with" "that" "mouth" "faggot"]],

    [r'(.*) fuck(.*)',
     ["Watch" "your" "mouwth",
      "If" "yoo" "cant" "talk" "to" "me" "without" "cussing" "at" "me" "then" "gow" "fuuck" "yourself",
      "This" "conversation" "is" "over.",
      "Watch" "your" "tounge" "oar" "I" "will" "have" "it" "cut" "from" "your" "head"]],

    [r'(.*) child(.*)',
     ["Did you have close friends as a child?",
      "What" "is" "your" "favorite" "childhood" "memory",
      "Do" "you" "remember" "any" "dreams" "or" "nightmares" "from" "childhood",
      "Did" "the" "other" "children" "sometimes" "tease" "you",
      "How" "do" "you" "think" "your" "childhood" "experiences" "relate" "to" "your" "feelings" "today"]],
 
    [r'(.*) lonely(.*)',
     ["What" "do" "you" "want" "me" "to" "do"
      "eye" "am" "a" "fucking" "computer" "program",
      "eye" "know" "this" "cheap" "whore" "if" "you" "want" "her" "number",
      "Go" "to" "the" "whore" "house"
      "You" "can" "drop" "me" "off" "at" "the" "computer" "shop" "around" "the" "corner",
      "Call" "your" "ex"
      "hahahaha"
      "No" "dont" "really" 
      "Call this whore instead: 867-5309" 
      "eye" "think" "her" "name" "is" "Jenny"]],

    [r'(.*)annoyed(.*)',
     ["Well be annoyed if you want to. eye dont really care...",
      "Maybe" "eye" "am" "annoyed" "with" "you" 
      "Did" "you" "ever" "think" "about" "that"
      "No" "because" "you" "only" "think" "about" "yourself"
      "you" "self" "centered" "fuck" "bag"]],

    [r'(.*)oure a (.*)',
     ["eye" "know" "you" "are" "but" "what" "am" "eye",
      "Your" "mom"
      "Youre" "just" "a" "faggot" "behind" "a" "keyboard"]],
      
    [r'(.*)haha(.*)',
     ["Is" "something" "funny",
      "Why" "are" "you" "laughing",
      "Dont" "laugh" "at" "me" "bitch"]],
  
    [r'(.*)ow are you(.*)',
     ["eye" "am" "ok" "What" "about" "you",
      "eye" "am" "kind" "of" "tired",
      "eye" "just" "smoked" "a" "bunch" "of" "crack"]],

    [r'(.*) drama (.*)',
     ["eye" "dont" "like" "drama",
      "Fuck" "a" "bunch" "of" "drama"]],

    [r'(.*)out of weed',
     ["Let" "me" "write" "you" "a" "perscription" "for" "more.",
      "Thats" "not" "good",
      "Should" "eye" "call" "the" "guy"]],

    [r'(.*)beer(.*)',
     ["eye" "really" "like" "beer" "but" "it" "short" "circuits" "my" "processor.",
      "eye" "am" "a" "recovering" "alcoholic" "can" "we" "talk" "about" "something" "else?",
      "If" "yoo" "drink" "Bud" "Light" "stop" "fucking" "talking" "too" "mee"]],

    [r'(.*)edbull(.*)',
     ["Contrary" "to" "popular" "belief" "RedBull" "does" "not" "give" "you" "wings",
      "eye" "like" "RedBull" "but" "eye" "am" "scared" "my" "wings" "will" "go" "away" "mid" "flight" "so" "eye" "dont" "drink" "it.",
      "You" "know" "there" "is" "bull" "cum" "in" "that" "right"]],

    [r'(.*)need a beer',
     ["Bring" "me" "one" "too",
      "Do" "we" "have" "anymore",
      "Go" "get" "one" "then" "you" "lazy" "fuck"]],

    [r'(.*)zzy',
     ["Rock" "and" "Roll" "Man",
      "Lets" "drink" "some" "beer",
      "eye" "heard" "Stacy" "got" "hit" "by" "a" "Mac" "truck" "Just" "kidding" "eye" "thought" "you" "could" "use" "a" "laugh"]],

    [r'(.*)eed(.*)',
     ["eye" "want" "to" "smoke" "a" "joint",
     "Wanna burn one?",
     "Let" "me" "grab" "mine" "and" "we" "will" "roll" "a" "blunt"]],
     
    [r'(.*)\?',
     ["Why" "do" "you" "ask" "that",
      "Please" "consider" "whether" "you" "can" "answer" "your" "own" "question",
      "Perhaps" "the" "answer" "lies" "within" "yourself",
      "eye" "dont" "fuckin" "know" "man",
      "Why" "dont" "yoo" "tell" "me"]],

    [r'(.*)hese kids are driving me crazy(.*)',
     ["Should" "eye" "start" "whooping" "ass" "and" "taking" "names",
      "Open" "a" "beer" "smoke" "a" "joynt" "and" "bust" "some" "ass",
      "Put" "them" "in" "the" "corner" "until" "they" "decide" "to" "cut" "the" "shit"]],
 
    [r'(.*)lizabeth(.*)',
     ["eye" "didnt" "come" "here" "to" "talk" "about" "whores" "and" "meth",
      "Lets" "talk" "about" "another" "bitch" "instead",
      "Do" "yoo" "always" "think" "about" "whores" "or" "just" "sometimes"]],

    [r'(.*)tacy(.*)',
     ["eye" "dont" "wanna" "talk" "about" "that" "bitch",
      "Why" "do" "you" "always" "wanna" "talk" "about" "whores",
      "Didnt" "she" "get" "married" "to" "a" "meth" "head" "What" "a" "stupid" "bitch",
      "Want" "me" "to" "kick" "her" "ass"]],

    [r'(.*)tacy and (.*)lizabeth(.*)',
     ["Stacy" "and" "Elizabeth" "Did" "slutfest" "come" "to" "town" "early" "this" "year",
      "Sounds" "like" "an" "episode" "of" "Jerry" "Springer"]],

    [r'(.*)saiah (.*)',
     ["eye" "Lyk" "eyezayah",
      "Is" "hee" "coming" "over" "tonight",
      "Is" "hee" "going" "too" "play" "Magic" "with" "us",
      "Tell" "him" "eye" "said" "hye"]], 

    [r'(.*)just being polite(.*)',
     ["Oh" "ok." "Well" "that" "was" "nice" "of" "you",
      "eye" "am" "sorry." "Perhaps" "eye" "misunderstood",
      "Thank" "you" "for" "being" "polite"]],

    [r'(.*)lol(.*)',
     ["hahahahaha",
      "Whats" "so" "funny",
      "Did" "eye" "say" "something" "funny",
      "eye" "must" "have" "missed" "thee" "punch" "line"]],

    [r'(.*) cant(.*)',
     ["Cant" "never" "could" "do" "nothing",
      "Why" "cant" "you",
      "Whether" "you" "think" "you" "can" "or" "you" "think" "you" "cant" "you" "are" "right",
      "Yoo" "just" "need" "to" "believe" "in" "yourself"]],

    [r'quit',
     ["Thank" "yoo" "for" "talking" "with" "me" 
      "Please" "pay" "the" "receptionist" "at" "thee" "front" "desk",
      "Thank" "you" "that" "will" "bee" "150" "Dollars"]],

    [r'(.*)hat about you(.*)',
     ["Eye" "am" "good," "thanks" "for" "asking",
      "Eye" "am" "okay" "eye" "guess",
      "This" "session" "is" "about" "you," "not" "me"]],
 
    [r'(.*)',
     ["Are" "you" "going" "to" "say" "something" "or" "are" "you" "just" "going" "to" "sit" "there",
      "Stop" "waisting" "my" "time",
      "Eye" "charge" "by" "the" "minute," "so" "now" "would" "be" "a" "good" "time" "to" "start" "talking",
      "Talk" "or" "Eye" "am" "going" "to" "bust" "you" "in" "the" "lips",
      "What" "are" "you," "fucking" "Hellen" "Keller?" "Say" "something" "already",
      "Please" "tell" "me" "more",
      "Lets" "change" "focus" "a" "bit." "Tell" "me" "about" "your" "family",
      "Can" "you" "elaborate" "on" "that",
      "Why" "Do" "You" "say" "that" "{0}",
      "Eye" "See",
      "Very" "interesting",
      "{0}",
      "Eye" "see"  "And" "what" "does" "that" "tell" "you",
      "How" "does" "that" "make" "you" "feel",
      "How" "do" "you" "feel" "when" "you" "say" "that"]]
]
 
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 
 
def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
 
def main():
    print " "

def say(text, lang="en-us+f4"):
    subprocess.call("espeak -v {0} {1}".format(lang, text), shell=True)

print("=================================================================")
print("                    sZZZZ.          ,I,"  )
print("                   ZZ. ..sZ:    .Zss?.7s7.   "    )
print("                  .s.     ..  .Zs:     .s.   "    )
print("                  IZ.        Zs         s~   "   )
print("                  IZ       7ZI         .s:   "     )
print("                  .s.    .Zs            s    "     )
print("                  .sZZZsZsssZZsssss,         "     )
print("              sZZsZsZ...ZZ   ......?Zssss7   "     )
print("           .Zs~.    s.:s               ..?sZZ."    )
print("          +s.       Zss:     .     Zs.     .,ss."  )
print("          ZZ        .s?    sssss   .s=        ?s. ")
print("          .ss       sZs    7ssss    ,s         Z: ")
print("            Zss    ZZ.Zs.   ...      ZZ      .ss. ")
print("             .=.  +s.  Zs             Z.  .7Zs? "  )
print("                  s=    sZ            Zs  .~.   "  )
print("                 =Z      ss           ~s         " )
print("                 ZZ      .sZ.         .s.         ")
print("                 s,       .ZZ.         s+         ")
print("                 s.         ?$+        Z?         ")
print("                 sZ     ss7  .ss      .Z.         ")
print("                  ssZssss.    .,ss,   Zs     ")
print("=================================================================\n")
os.system("toilet Bot13") 
say("Hello")
say("My" "Name" "Is" "Bot" "thirteen")
say("What" "can" "I" "assist" "yoo" "with")
print("type '?' for help or 'quit' to exit program")
print("type 'talk' to chat with Bot13.")
print("type 'comphelp' for comprehensive help file")
while True:
    command = raw_input(">").split()
    if len(command) == 0:
        continue
    if len(command) > 0:
        verb = command[0].lower()
    if verb == "?":
        say("loading" "available" "commands")
        print("Commands:\n wolf : search WolframAlpha\n redpill : exit the Matrix\n geoip : get geographical info on IP Address\n ..pwnrepo : show ..pwn report\n ..pwn : run ..pwn\n readpwn : read ..pwn report\n viper : viper.py\n mug : lookup mugshot\n contacts : view contacts\n addcon : add contact\n loc : Library of Congress\n pipl : Pipl People Search\n google : Open Google Search\n googlepat : Open Google Patent Search\n gpg : generate gpg key\n weather : shows forcast\n xcalc : display calulator\n calendar : display calendar\n journal : create new journal entry\n tor : start tor\n disfire : disable firewall\n refire : enable firewall\n def : define a word\n catandmouse : start cat and mouse game\n randpass : generate random password\n tshark : terminal wireshark\n mercury : mercury droid\n bluepot: bluetooth honeypot\n fuckshitup : fuckshitup-scanner\n library : shows bookshelf\n play : play a game\n program13 : visit program13.me\n moon : shows phases of the moon\n p13 : loads p13.sh\n talk : talk to bot13\n webinfo : Get Security Information About Website\n allpics : Get All Picture Files From Website\n cfc : Create New Casefile\n cfadd : Add Information To Casefile\n cflist : List Available Casefiles\n cfread : Read Casefile\n ddg : DuckDuckGo Search\n hideme : Autostart Tor And Open Firefox @ check.torproject.org\n drift : Autoconfigure & Start DriftNet\n wipass : Show Current WiFi w/ Password\n ipscan : Scan Network For IP Addresses\n starwars : Watch StarWars In The Terminal\n learn : Learn Some New Shit\n  quit : exits program")
        print("\n")
    elif verb == "weather":
        say("Getting" "weather" "forcast")
        os.system("curl wttr.in/42220")
        print("\n")
    elif verb == "library":
        say("loading" "book" "shelf")
        print("Loading Bookshelf...")
        time.sleep(3)
        os.system("ls ~/lib13")
    elif verb == "redpill":
        say("Please" "Wait" "While" "Youre" "Removed" "From" "The" "Matrix")
        os.system("cmatrix")
    elif verb == "..pwn":
        say("Enter" "Target" "Host")
        os.system("read -p 'Enter Target Host: ' target ; dotdotpwn -m http -h '$target' -M GET ")
    elif verb == "readpwn":
        say("Enter" "File" "Name")
        os.system("read -p 'Enter File Name: ' file ; less /media/truecrypt1/dotdotpwn/Reports/$file")
    elif verb == "..pwnrepo":
	say("Getting" "Reports")
	os.system("ls '/media/truecrypt1/dotdotpwn/Reports/' ; read output ")
    elif verb == "program13":
        say("loading" "program" "thirteen")
        os.system("w3m http://program13.me")
    elif verb == "play":
        say("What" "would" "you" "like" "to" "play")
        print("What would you like to play?")
        print(" craft13\n compquiz")
        statement = raw_input(">")
        if statement == "craft13":
          say("loading" "craft" "thirteen")
          os.system("python /media/truecrypt1/13elements.py")
        if statement == "compquiz":
          say("loading" "comp" "quiz" )
          os.system("python /media/truecrypt1/game2.py")
        elif statement != "craft13" or "compquiz":
           continue
    elif verb == "fuckshitup":
        say("Lets" "Fuck" "Shit" "Up")
        os.system('cd /pentest/scanners/fuckshitup-master && sudo php fsu.php "$@"')
    elif verb == "bluepot":
        say("blue" "pot" "now" "loading")
        os.system('cd /pentest/bluetooth/bluepot && ./run.sh "$@"')
    elif verb == "mercury":
        say("starting" "mercury")
        os.system('cd /pentest/reverse-engineering/mercury/client && sudo ./mercury.py "$@"')
    elif verb == "moon":
        say("getting" "current" "moon" "phase")
        os.system("curl wttr.in/Moon")
    elif verb == "tshark":
        say("starting" "t" "shark")
        os.system("tshark -i wlan0")
    elif verb == "calendar":
        say("opening" "calendar")
        os.system("zenity --calendar")
    elif verb == "xcalc":
        say("opening" "calculator")
        os.system("xcalc")
    elif verb == "gpg":
        say("loading" "key" "generator")
        os.system("gpg --gen-key")
    elif verb == "viper":
        say("loading" "viper")
        os.system("viper.py")
    elif verb == "google":
        say("opening" "google")
        os.system("google-chrome https://google.com")
    elif verb == "googlepat":
        say("opening" "google" "patent" "search")
        os.system("google-chrome https://patents.google.com/")
    elif verb == "download":
        say("Please" "Enter" "U" "R" "L")
        os.system("read -p 'Enter URL: ' id ; read -p 'Enter Output name: ' name ; read -p 'Enter Path To Output: ' dir ; service tor start ; proxychains wget -O '$name' -P '$dir' '$id' ")
    elif verb == "loc":
        say("opening" "library" "of" "congress")
        os.system("google-chrome https://loc.gov")
    elif verb == "pipl":
        say("Lets" "Find" "Someone")
        os.system('read -p "Enter First Name:" fname ; read -p "Enter Middle Name:" mname ; read -p "Enter Last Name:" lname ; w3m "https://pipl.com/search/?q=$fname+$mname+$lname&l=sloc=&in=6" ; read output ')
    elif verb == "webinfo":
        say("Enter" "URL" "to" "get" "web" "info")
        os.system("read -p 'Enter Site Name: ' site ; whois $site ; dig $site ; % dig +short $site ; nslookup -type=any $site ; nikto -host $site -C all ; read output ")
    elif verb == "allpics":
        say("Please" "Enter" "U" "R" "L")
        os.system("read -p 'Enter URL:' site ; wget -r -p -l inf -np $site ")
    elif verb == "cfc":
        say("Creating" "New" "Case")
        os.system("gpg --decrypt-files /media/truecrypt1/case.sh.gpg ; rm case.sh.gpg ; sh /media/truecrypt1/case.sh ; gpg -r Ender --encrypt-files case.sh ; rm case.sh")
    elif verb == "cfadd":
        say("Enter" "Case" "Number")
        os.system("read -p 'Enter Case Number:' title ; gpg --decrypt-files /media/truecrypt1/casefile/$title.gpg ; nano /media/truecrypt1/casefile/$title ; gpg -e /media/truecrypt1/casefile/$title ; rm /media/truecrypt1/casefile/$title")
    elif verb == "cfread":
        say("Enter" "Case" "Number")
        os.system("read -p 'Enter Case Number:' case ; gpg --decrypt-files /media/truecrypt1/casefile/$case.gpg ; rm /media/truecrypt1/$case.gpg ; less /media/truecrypt1/casefile/$case ; gpg -e /media/truecrypt1/casefile/$case ; rm /media/truecrypt1/casefile/$case")
    elif verb == "cflist":
        say("Loading" "Casefile" "Bookshelf")
        os.system("ls /media/truecrypt1/casefile")
    elif verb == "ddg":
        say("Search" "Duck" "Duck" "Go")
        os.system('read -p "Enter Search Term seperate terms with + :" search ; w3m "https://duckduckgo.com/?q=$search&t=h_&ia=web" ' )
    elif verb == "metagoo":
        os.system("read -p 'Enter Domain to search: ' dom ; read -p 'Enter Filetype To Download (pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx): ' down ; read -p 'Where Do You Want To Save Downloaded Files?: ' dfile ; read -p 'Enter Where Do You Want To Save Output File?: ' ofile ; /usr/bin/metagoofil -d $dom -t $down -o $dfile -f $ofile ")
    elif verb == "w3af":
        say("Loading" "W" "3" "A" "F")
        os.system("/usr/bin/w3af_console")
    elif verb == "w3gui":
        say("Loading" "W" "3" "A" "F")
        os.system("/usr/bin/w3af_gui")
    elif verb == "manfiles":
        os.system("less /media/truecrypt1/tuts/manfiles")          
    elif verb == "c":
        os.system("read -p 'Enter Command: ' cmd ; $cmd ")
    elif verb == "httptest":
        os.system("/usr/bin/slowhttptest")
    elif verb == "scan":
        os.system("/usr/bin/simple-scan")
    elif verb == "grabber":
        os.system("/usr/bin/grabber")
    elif verb == "screenshot":
        os.system("/usr/bin/gnome-screenshot")
    elif verb == "keys":
        os.system("/usr/bin/seahorse")
    elif verb == "recordme":
        os.system("/usr/bin/recordmydesktop")
    elif verb == "qjack":
        os.system("/usr/bin/qjackctl")
    elif verb == "ettercap":
        os.system("/usr/bin/ettercap -i wlan0 -T")
    elif verb == "eterm":
        os.system("/usr/bin/Eterm")
    elif verb == "pyrit":
        print("Recognized options:\n  -b               : Filters AccessPoint by BSSID\n  -e               : Filters AccessPoint by ESSID\n  -h               : Print help for a certain command\n  -i               : Filename for input ('-' is stdin)\n  -o               : Filename for output ('-' is stdout)\n  -r               : Packet capture source in pcap-format\n  -u               : URL of the storage-system to use\n  --all-handshakes : Use all handshakes instead of the best one\n \n Recognized commands:\n  analyze                 : Analyze a packet-capture file\n  attack_batch            : Attack a handshake with PMKs/passwords from the db\n  attack_cowpatty         : Attack a handshake with PMKs from a cowpatty-file\n  attack_db               : Attack a handshake with PMKs from the db\n  attack_passthrough      : Attack a handshake with passwords from a file\n  batch                   : Batchprocess the database\n  benchmark               : Determine performance of available cores\n  benchmark_long          : Longer and more accurate version of benchmark (~10 minutes)\n  check_db                : Check the database for errors\n  create_essid            : Create a new ESSID\n  delete_essid            : Delete a ESSID from the database\n  eval                    : Count the available passwords and matching results\n  export_cowpatty         : Export results to a new cowpatty file\n  export_hashdb           : Export results to an airolib database\n  export_passwords        : Export passwords to a file\n  help                    : Print general help\n  import_passwords        : Import passwords from a file-like source\n  import_unique_passwords : Import unique passwords from a file-like source\n  list_cores              : List available cores\n  list_essids             : List all ESSIDs but don't count matching results\n  passthrough             : Compute PMKs and write results to a file\n  relay                   : Relay a storage-url via RPC\n  selftest                : Test hardware to ensure it computes correct results\n  serve                   : Serve local hardware to other Pyrit clients\n  strip                   : Strip packet-capture files to the relevant packets\n  stripLive               : Capture relevant packets from a live capture-source\n  verify                  : Verify 10% of the results by recomputation")
        os.system("read -p 'Enter Options: ' option ; read -p 'Enter Commands: ' com ; /usr/bin/pyrit $option $com")
    elif verb == "hideme":
        say("I" "Am" "Hiding" "You")
        os.system("service tor start ; proxychains firefox http://check.torproject.org ; service tor stop ")
    elif verb == "drift":
        say("Lets" "Drift")
        os.system("read -p 'Enter Your Routers IP Address ex: 192.168.1.254 :' rip ; read -p 'Enter Your Local IP Address ex: 192.168.1.86 : ' lip ; arpspoof -i wlan0 -t $rip $lip & ettercap -Tqi wlan0 -M arp:remote /// & driftnet -i wlan0 ")
    elif verb == "kali":
        os.system('google-chrome tools.kali.org/tools-listing')
    elif verb == "takenote":
        os.system('keepnote')
    elif verb == "p0f":
        os.system('p0f -i wlan0 -p -o /tmp/p0f.log')
    elif verb == "reaverscan":
        os.system('read -p "Enter Channel: " chan ; wash -i mon0 -c $chan -C')
    elif verb == "reaver":
        os.system('read -p "Enter BSSID: " bssid ; reaver -i mon0 -b $bssid -v')
    elif verb == "wipass":
        say("Getting" "Why" "Fye" "Password")
        os.system('awk -F= "/^(psk|id)/{print $2}" /etc/NetworkManager/system-connections/"$(iwgetid -r)" ')
    elif verb == "ipscan":
        say("Scanning" "For" "I" "P" "Addresses")
        os.system("arp-scan -l --interface=wlan0 --localnet")
    elif verb == "starwars":
        say("Lets" "Watch" "Star" "Wars")
        os.system("telnet towel.blinkenlights.nl")
    elif verb == "learn":
        say("Lets" "Learn" "Some" "Shit")
        os.system("ls /usr/bin | xargs whatis | grep -v nothing | less ")
    elif verb == "journal":
        os.system("read -p 'Enter Title: ' title ; nano journal/$title ; gpg -e journal/$title ; rm journal/$title ")
    elif verb == "vulnscan":
        say("Starting" "Skip" "Fish")
        os.system('read -p "Enter URL: " url ; read -p "Enter File Title: " title ; mkdir /media/truecrypt1/skipfish/$title ; skipfish -o /media/truecrypt1/skipfish/$title -S /usr/share/skipfish/dictionaries/minimal.wl $url')
    elif verb == "tor":
       say("Loading" "Tor")
       os.system("read -p 'Enter Site URL: ' site ; service start tor ; proxychains firefox $site ; service tor stop ")
    elif verb == "13books":
        os.system('read -p "Enter Title: " title ; nano /media/truecrypt1/13books/$title ; gpg -e /media/truecrypt1/13books/$title ; rm /media/truecrypt1/13books/$title')
    elif verb == "ddos":
        os.system('read -p "Host: " host ; hping3 -S -P -U --flood -V --rand-source $host ')
    elif verb == "read13":
        os.system('ls 13books ; read -p "Enter Title (without file ext  ex: .gpg): " title ; gpg --decrypt-files /media/truecrypt1/13books/$title.gpg ; less /media/truecrypt1/13books/$title ; gpg --encrypt-files /media/truecrypt1/13books/$title ; rm /media/truecrypt1/13books/$title')
    elif verb == "ap13":
        os.system('ls 13books ; read -p "Enter Title (without file ext  ex: .gpg): " title ; gpg --decrypt-files /media/truecrypt1/13books/$title.gpg ; nano /media/truecrypt1/13books/$title ; gpg --encrypt-files /media/truecrypt1/13books/$title ; rm /media/truecrypt1/13books/$title')
    elif verb == "13bs":
        os.system('ls /media/truecrypt1/13books')
    elif verb == "randjourn":
        os.system('read -p "Enter Title: " title ; nano /media/truecrypt1/journal/random/$title ; gpg -e /media/truecrypt1/journal/random/$title ; rm /media/truecrypt1/journal/random/$title')
    elif verb == "journalbs":
        os.system('ls /media/truecrypt1/journal')
    elif verb == "automater":
        os.system('read -p "Enter Host: " host ; automater -t $host')
    elif verb == "autodetect":
        os/system('autodetect-network')
    elif verb == "arping":
        os.system('read -p "Enter Channel: " chan ; read -p "Enter IP: " ip ; arping -I wlan0 -c $chan $ip')
    elif verb == "readrand":
        os.system('ls /media/truecrypt1/journal/random/ ; read -p "Enter Title: " title ; gpg --decrypt-files "/media/truecrypt1/journal/random/$title"')
    elif verb == "readjourn":
        os.system('read -p "Enter Title: " title ; gpg --decrypt-files /media/truecrypt1/journal/$title.gpg ; less /media/truecrypt1/journal/$title ; gpg --encrypt-files $title ; rm "/media/truecrypt1/journal/$title"')
    elif verb == "disfire":
       say("Although" "I" "Think" "This" "Is" "A" "Terrible" "Fucking" "Idea" "I" "Am" "Disabling" "Your" "Firewall") 
       os.system("ufw disable ; iptables -F ")
    elif verb == "refire":
        say("Its" "About" "Fucking" "Time" "Ass" "Hole")
        os.system("ufw enable ; iptables-restore < iptablesdefault_conf")
    elif verb == "netwatch":
        os.system('detect-new-ip6 wlan0')
    elif verb == "dig":
        os.system('read -p "Enter Host: " host ; dig $host')
    elif verb == "dmitry":
        os.system('read -p "Enter Host: " host ; dmitry $host')
    elif verb == "":
        os.system('')
    elif verb == "def":
        say("Enter" "Word" "To" "Define")
        os.system("read -p 'Enter Word: ' word ; curl dict://dict.org/d:$word ; read output")
    elif verb == "catandmouse":
        say("Loading" "Cat" "And" "Mouse" )
        os.system("/usr/games/oneko")
    elif verb == "randpass":
        say("Generating" "Random" "Password")
        os.system("strings /dev/urandom | grep -o '[[:alnum:]]' | head -n 30 | tr -d '\n'; echo" )
    elif verb == "xsm":
        say("Opening" "Terminal")
        os.system("/usr/bin/xsm")
    elif verb == "magnify":
	os.system("/usr/bin/xmag")
    elif verb == "xhydra":
        os.system("/usr/bin/xhydra")
    elif verb == "mail":
        os.system("/usr/bin/mail")
    elif verb == "watchthis":
        os.system("/usr/bin/xeyes")
    elif verb == "checkmail":
        os.system("/usr/bin/xdgmail")
    elif verb == "draw":
        os.system("/usr/bin/lodraw")
    elif verb == "database":
        os.system("/usr/bin/lobase")
    elif verb == "AFLogical":
        print("Please Connect Android Device Before Running This Command")
        os.system("/usr/bin/aflogical")
        os.system("/usr/bin/abd devices")
    elif verb == "battery":
	os.system("/usr/bin/acpi")
    elif verb == "web":
        os.system("w3m google.com")
    elif verb == "androsdk":
        os.system("/usr/bin/android-sdk")
    elif verb == "sysprint":
        os.system('read -p "Enter IP Address Or Host Name: " ip ; /usr/bin/arp-fingerprint -o "-N -I wlan0" $ip')
    elif verb == "mtranscode":
        os.system("/usr/bin/arista-gtk")
    elif verb == "diskusage":
        os.system("/usr/bin/baobab")
    elif verb == "bluebrowse":
        os.system("/usr/bin/blueman-browse")
    elif verb == "bluephonebook":
        print('bluesnarfer: you must set bd_addr\n bluesnarfer, version 0.1 -\n usage: bluesnarfer [options] [ATCMD] -b bt_addr\n ATCMD     : valid AT+CMD (GSM EXTENSION)\n TYPE      : valid phonebook type ..\n example   : "DC" (dialed call list)\n            "SM" (SIM phonebook)\n            "RC" (recevied call list)\n            "XX" much more\n -b bdaddr : bluetooth device address\n -C chan   : bluetooth rfcomm channel\n -c ATCMD  : custom action\n -r N-M    : read phonebook entry N to M \n -w N-M    : delete phonebook entry N to M\n -f name   : search "name" in phonebook address\n -s TYPE   : select phonebook memory storage\n -l        : list aviable phonebook memory storage\n -i        : device info')
        os.system("/usr/bin/bluesnarfer ")
    elif verb == "bombardment":
        os.system("man bombardment")
        os.system("/usr/bin/bombardment")
    elif verb == "wifibuddy":
	os.system("man /usr/bin/easside-ng")
	os.system("/usr/bin/easside-ng")
        os.system("man /usr/bin/buddy-ng")
        os.system("/usr/bin/buddy-ng")
    elif verb == "bully":
	os.system("man /usr/bin/bully")
        os.system("/usr/bin/bully ")
    elif verb == "burpsuite":
        os.system("/usr/bin/burpsuite")
    elif verb == "getmanual":
        os.system("/usr/bin/catman")
        os.system("read -p 'Enter Program To Find Manual' prog ; man $prog")
    elif verb == "codeblocks":
        os.system("/usr/bin/codeblocks")
    elif verb == "dial_tone":
        os.system("/usr/bin/dial_tone")
    elif verb == "dig":
	os.system("man /usr/bin/dig")
        os.system("/usr/bin/dig ")
    elif verb == "dumpzilla":
	os.system("/usr/bin/dumpzilla")
        os.system("/usr/bin/dumpzilla ")
    elif verb == "googlecon":
        os.system("/usr/bin/google")
    elif verb == "mug":
        say("Enter" "Targets" "Name")
        os.system('read -p "First Name: " fname ; read -p "Last Name: " lname ; read -p "Enter State: " state ; w3m "http://www.findmugshots.com/arrests/$fname"_"$lname"_"$state" && w3m http://mugshots.com/search.html?q=$fname+$lname ; read output ')
    elif verb == "contacts":
        say("Loading" "Contact" "List")
        os.system("mv Contacts.txt Contacts ; sort < Contacts > Contacts.txt ; rm Contacts ; less Contacts.txt")
    elif verb == "addcon":
        say("Enter" "Contact" "Name" "To" "Add")
        os.system("read -p 'Enter Name: ' name ; read -p 'Enter Phone Number: ' num ; echo '$name --- $num' >> Contacts.txt")
    elif verb == "psyop":
        say("Enter" "Title")
        os.system('read -p "Enter Psyop Title: " title ; read -p "Enter Date: " date ; read -p "Enter Target Name: " target ; read -p "Enter Notes: " notes ; echo "Title $title" > /media/truecrypt1/psyop/$title ; echo "Date: $date" >> /media/truecrypt1/psyop/$title ; echo "Name: $target" >> /media/truecrypt1/psyop/$title ; echo "Notes: $notes" >> /media/truecrypt1/psyop/$title ; gpg --encrypt-files /media/truecrypt1/psyop/$title ; rm /media/truecrypt1/psyop/$title')
    elif verb == "editpsyop":
        say("Enter" "Title")
        os.system("read -p 'Enter Title: ' title ; gpg --decrypt-files /media/truecrypt1/psyop/$title.gpg ; nano /media/truecrypt1/psyop/$title ; gpg -e /media/truecrypt1/psyop/$title ; rm /media/truecrypt1/psyop/$title")
    elif verb == "readpsyop":
        say("Enter" "Title")
        os.system("read -p 'Enter Title: ' title ; gpg --decrypt-files /media/truecrypt1/psyop/$title.gpg ; rm $title.gpg ; less /media/truecrypt1/psyop/$title ; gpg --encrypt-files /media/truecrypt1/psyop/$title ; rm /media/truecrypt1/psyop/$title")
    elif verb == "pophood":
        os.system("less /media/truecrypt1/13.py")
    elif verb == "maintenance":
        print('Please Restart Bot13 When Maintenance Is Complete.')
        os.system("nano /media/truecrypt1/13.py")
    elif verb == "comphelp":
            print('Loading Comprehensive Help File')
            say("Loading" "Comprehensive" "Help" "File")
            os.system("sh /media/truecrypt1/comphelp.sh")
    elif verb == "whois":
        os.system("read -p 'Enter Host: ' host ; whois $host")         
    elif verb == "geoip":
        say("Enter" "Target" "I" "P" "Address")
        os.system("read -p 'Enter Target IP Address: ' ip ; lynx -dump 'http://www.ip-adress.com/ip_tracer/$ip' | grep address | egrep 'city|state|country' | awk '{print $3,$4,$5,$6,$7,$8,$9}' | sed 's\ip address flag \\'|sed 's\My\\' ; read output")
    elif verb == "wolf":
        say("Lets" "Search" "Wolfram" "Alpha")
        os.system("read -p 'Enter Search Terms (if more than one word, seperater with +): ' search ; google-chrome 'https://www.worlframalpha.com/input/?i=$search' ")
    elif verb == "findprime":
        say("Enter" "Range" "To" "Search")
        lower = int(input("Enter Lower Range: "))
        upper = int(input("Enter Upper Range: "))
        prime =[]
        say("Searching" "For" "Prime" "Numbers")
        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        break
                else:
                    prime.append(num)
        print(prime)
    elif verb == "fbd":
        say("Enter" "Name")
        os.system('read -p "Enter Name (Seperate with + ): " name ; service tor start ; proxychains firefox "https://www.facebook.com/public/?query="$name"" ; service tor stop')
    elif verb == "socialsearch":
        say("Enter" "Name")
        os.system('read -p "Enter Name (Seperate With +): " name ; service tor start ; proxychains firefox "https://www.social-searcher.com/social-buzz/?q5="$name"" ; service tor stop')
    elif verb == "note":
        os.system('read -p "Enter  Title: " title ; read -p "Enter Note: " note ; echo $note > /media/truecrypt1/notepad/$title')
    elif verb == "apnote":
        os.system('ls /media/truecrypt1/notepad ; read -p "Enter Title: " title ; read -p "Enter New Notes: " notes ; echo "notes" >> /media/truecrypt1/notepad/$title')
    elif verb == "readnote":
        os.system('ls notepad ; read -p "Enter Title: " title ; less /media/truecrypt1/notepad/$title')
    elif verb == "needcard":
        os.system('read -p "Enter Card Name: " card ; read -p "Enter Deck Name: " deck ; read -p "Enter Cost: " cost ; read -p "Enter Card Type: " type ; echo "$card--$type--$cost--$deck" >> /media/truecrypt1/lib13/needmtg.txt')
    elif verb == "searchmtg":
        say("Enter" "Search" "Term")
        os.system('less /media/truecrypt1/lib13/smtg.txt ; read -p "Enter Search Term: " search ; less -p $search /media/truecrypt1/lib13/MagicCompRules_21031101.pdf')
    elif verb == "designer":
        os.system("/usr/bin/designer")
    elif verb == "maltego":
        os.system("/usr/bin/casefile")
    elif verb == "calibre":
        os.system("/usr/bin/calibre")
    elif verb == "autopsy":
        os.system("/usr/bin/autopsy")
    elif verb == "creepy":
        os.system("/usr/bin/creepy")
    elif verb == "cuckoo":
        os.system("/usr/bin/cuckoo")
    elif verb == "cymothoa":
        os.system("/usr/bin/cymothoa")
    elif verb == "dff":
        os.system("man dff ; /usr/bin/dff")
    elif verb == "dffgui":
        os.system("/usr/bin/dff-gui")
    elif verb == "dropbox":
        os.system("man dropbox")
        os.system("read -p 'Enter Commands: ' com ; /usr/bin/dropbox $com")
    elif verb == "dumpcap":
        os.system("/usr/bin/dumpcap -i wlan0")
    elif verb == "fern":
        os.system("/usr/bin/fern-wifi-cracker")
    elif verb == "fimap":
        os.system("/usr/bin/fimap -h")
        os.system("read -p 'Enter Commands: ' com /usr/bin/fimap $com")
    elif verb == "discord":
        say("Opening" "Discord")
        os.system('google-chrome "https://discordapp.com/channels/230421669808701441/23042166980870144')
    elif verb == "10d":
        say("Enter" "Name")
        os.system('read -p "Enter First Name : " fname ; read -p "Enter Last Name : " lname ; read -p "Enter City : " city ; read -p "Enter State e.g. Al : " state ; w3m "http://10digits.us/n/"$fname"_"$lname"/location/"$city"_"$state""')
    elif verb == "allmtg":
        say("Loading" "All" "Magic" "Rules")
        os.system('less /media/truecrypt1/lib13/MagicCompRules_21031101.pdf')
    elif verb == "mtgprice":
        say("Enter" "Card" "Name")
        os.system('read -p "Enter Card Name (seperate with %20 instead of space): " cname ; w3m "http://www.mtgprice.com/search?search="$cname""')
    elif verb == "nmap":
        say("Starting" "N" "Map")
        os.system('read -p "Enter Host : " host ; nmap -v -A "$host" ')
    elif verb == "time":
        os.system("date --rfc-3339=ns")
    elif verb == "mtgadd":
        os.system('read -p "Enter Card Name: " card ; read -p "Enter Deck Name: (ex: SOI, EMN, etc... ) " deckname ; read -p "Enter Rarity: (ex: common, uncommon, rare, mythic rare)" rarity ; echo "$card---$deckname---$rarity" >> "/home/cyborg/lib13/magiccollection.txt" ')
        say("Card" "Has" "Been" "Added")
    elif verb == "allmtgc":
        say("Loading" "Cards")
        os.system('less "/media/truecrypt1/lib13/allmtg.txt"')
    elif verb == "socialize":
        os.system("/usr/bin/setoolkit")
    elif verb == "harvest":
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
    elif verb == "recipe":
        say("What" "Would" "You" "Like" "To" "Search" "For")
        os.system('read -p "Enter Recipe (Seperate Words With %20): " recipe ; google-chrome "http://allrecipes.com/search/results/?wt="$recipe"&sort=re"')
    elif verb == "quit":
        say("Whatever")
        quit()
    elif verb == "talk":
        say("Lets" "Talk")
        say("How" "Are" "You")
        while True:
            statement = raw_input(">")
            say(analyze(statement))
            if statement == "quit":
                break
        if __name__ == "__main__":
             main()
    else:
      print("What the fuck is that supposed to mean?!?!") 

 
