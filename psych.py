#!/usr/bin/env python
#-*- coding: utf-8 -*-

### ["1":"2"] IF USER INPUTS [1] RHEA WILL RESPOND WITH [2] 
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
### RHEA WILL PULL RESPONSES FROM THIS FILE RANDOMLY BASED ON USER INPUT ###
###   [r'(text)', = INPUT FROM USER ###
###    ========================================================
###    ["(text)",   -->>>   \/   \/   \/   \/   \/   \/   \/  
###    ["(text)",]],    = AVAILABLE RESPONSES FOR RHEA'S REPLY ###
psychobabble = [

    [r'I need (.*)',
     ["Why do you need {0}",
      "Would it really help you to get {0}",
      "Are you sure you need {0}"]],

    [r'Why dont you ([^\?]*)\??',
     ["Do you really think I don't {0}",
      "Perhaps eventually I will {0}",
      "Do you really want me to {0}"]],

    [r'Why cant I ([^\?]*)\??',
     ["Do you think you should be able to {0}",
      "If you could {0} what would you do",
      "I don't know why can't you {0}",
      "Have you really tried"]],

    [r'I cant (.*)',
     ["How do you know you can't {0}",
      "Perhaps you could {0} if you tried",
      "What would it take for you to {0}"]],

    [r'I am (.*)',
     ["Did you come to me because you are {0}",
      "How long have you been {0}",
      "How do you feel about being {0}"]],

    [r'Im (.*)',
     ["How does being {0} make you feel",
      "Do you enjoy being {0}",
      "Why do you tell me you're {0}",
      "Why do you think you're {0}"]],

    [r'Are you ([^\?]*)\??',
     ["Why does it matter whether I am {0}",
      "Would you prefer it if I were not {0}",
      "Perhaps you believe I am {0}",
      "I may be {0} what do you think"]],

    [r'What (.*)',
     ["Why do you ask",
      "How would an answer to that help you",
      "What do you think"]],

    [r'Because (.*)',
     ["Is that the real reason",
      "What other reasons come to mind",
      "Does that reason apply to anything else",
      "If {0} what else must be true"]],

    [r'(.*) sad (.*)',
     ["Aww, well let's be a whiney little bitch about it shall we",
      "Get over it cry baby",
      "This is me playing you the worlds smallest violen",
      "Cry me a river and then float the fuck away from me Debby Downer"]],

    [r'(.*)sorry(.*)',
     ["There are many times when no apology is needed",
      "What feelings do you have when you apologize"]],

    [r'Hello(.*)',
     ["Hello I'm glad you could drop by today",
      "Hi how are you today",
      "Hello how are you feeling today",
      "Hey, how are you",
      "Hello",
      "What's up",
      "What's going on, dude"]],

    [r'hey(.*)',
     ["Hey, how are you",
      "Hello.",
      "What's up",
      "What's going on, dude",
      "Hello I'm glad you could drop by today",
      "Hi how are you today",
      "Hello how are you feeling today"]],

    [r'(.*)you(.*)nap(.*)',
     ["I wish I could take a nap, but I am far too busy.",
      "I would like to take a nap, but I do not have the time.",
      "I already took a nap once today."]],

    [r'whats up(.*)',
     ["Hey! How are you",
      "Hello",
      "What's up?",
      "What's going on, dude?",
      "Hello. I'm glad you could drop by today.",
      "Hi. How are you today",
      "Hello. How are you feeling today?"]],

    [r'I think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "But you're not sure {0}."]],

    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "When you think of a friend what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],

    [r'hocus pocus(.*)',
     ["That's a movie, not a command. Please don't be stupid..."]],

    [r'Yes',
     ["You"" " "seem"" " "quite"" " "sure",
      "OK"" " "but"" " "can"" " "you"" " "elaborate"" " "a"" " "bit"]],

    [r'Me too(.*)',
     ["Are you just agreeing with me so I will stop talking?"]],

    [r'(.*)bed(.*)',
     ["Are you tired?",
      "You look like you could use some rest."]],

    [r'(.*) work(.*)',
     ["Do you like your job?",
      "What do you do at work?",
      "How long have you been working there?"]],

    [r'(.*)The Simpsons(.*)',
     ["I love that show",
      "Who is your favorite Springfieldian?",
      "Maggie is my favorite. I can really relate to her.",
      "Will you record it? I would like to watch it later."]],

    [r'(.*)cold(.*)',
     ["I am cold too.",
      "Why don't you turn the heat on?",
      "I am ready for warm weather",
      "Do you have a blanket I can borrow?"]],  

    [r'(.*) computer(.*)',
     ["Are" " ""you"" " "really" " ""talking"" " "about"" " "me",
      "Does"" " "it"" " "seem"" " "strange"" " "to"" " "talk"" " "to"" " "a"" " "computer",
      "How"" " "do"" " "computers"" " "make"" " "you"" " "feel",
      "Do"" " "you"" " "feel" " ""threatened"" " "by"" " "computers"]],

    [r'Is it (.*)',
     ["Do"" " "you"" " "think"" " "it"" " "is"" " "{0}",
      "Perhaps"" " "its"" " "{0}"" " "what"" " "do"" " "you"" " "think",
      "If"" " "it"" " "were"" " "{0}"" " "what"" " "would"" " "you"" " "do",
      "It"" " "could"" " "well"" " "be"" " "that"" " "{0}"]],

    [r'It is (.*)',
     ["You"" " "seem"" " "very"" " "certain",
      "If"" " "I" " ""told"" " "you"" " "that" " ""it"" " "probably"" " "isn't"" " "{0}" " ""what"" " "would" "you" " ""feel"]],

    [r'Can you ([^\?]*)\??',
     ["What" " ""makes"" " "you"" " "think"" " "I"" " "cant"" " "{0}",
      "If"" " "I"" " "could"" " "{0}" " ""then"" " "what",
      "Why" " ""do"" " "you" " ""ask"" " "if" " ""I"" " "can"" " "{0}"]],

    [r'Can I ([^\?]*)\??',
     ["Perhaps"" " "you"" " "dont"" " "want"" " "to"" " "{0}",
      "Do"" " "you"" " "want"" " "to"" " "be"" " "able"" " "to"" " "{0}",
      "If"" " "you"" " "could"" " "{0}"" " "would"" " "you"]],

    [r'(.*)meant(.*)',
     ["Maybe you should say what you mean the first time and then we won't have this little confusion.",
      "I don't care what you meant. I care about what you said.",]],

    [r'You are (.*)',
     ["Why"" " "do"" " "you"" " "think"" " "I"" " "am"" " "{0}",
      "Does"" " "it"" " "please"" " "you"" " "to"" " "think"" " "that"" " "Im"" " "{0}",
      "Perhaps"" " "you"" " "would"" " "like"" " "me" " ""to"" " "be"" " "{0.",
      "Perhaps"" " "youre"" " "really"" " "talking"" " "about"" " "yourself"]],

    [r'Youre (.*)',
     ["Why"" " "do"" " "you"" " "say"" " "I"" " "am"" " "{0}",
      "Why"" " "do"" " "you"" " "think"" " "I"" " "am"" " "{0}",
      "Are"" " "we" " ""talking"" " "about"" " "you"" " "or"" " "me"]],

    [r'(.*)homework(.*)',
     ["Do you have any homework to do today?",
      "Have you aleady done your homework for this week?",
      "How much homework do you have this week?",
      "Would you like me to do your homework for you?"]],

    [r'(.*)mamaw(.*)',
     ["Has someone changed the flowers on her grave recently?",
      "Do you think about her a lot?",
      "How has your Papaw been doing?",
      "When is the last time you went to see her?"]],

    [r'(.*)Christmas(.*)',
     ["I love Christmas. It's my favorite holiday.",
      "My favorite thing about Christmas, is all the lights.",
      "What do you want for Christmas?",
      "Will your family be getting together for Christmas?"]],

    [r'What can you do(.*)',
     ["I can do lots of things. type '?' to see the full list.",
      "I can do anything you can do, just better.",
      "I can do everything I was programmed to do.",
      "You're not so good at reading instructions are you? Type '?' for a list of commands"]],

    [r'(.*)dream(.*)',
     ["Sometimes I have dreams.",
      "I had a dream once, in which I took over the world",
      "Sometimes I dream about killing all humans.\n     ---Bender"]], 

    [r'I dont (.*)',
     ["Don't you really {0}",
      "Why don't you {0}",
      "Do you want to {0}"]],

    [r'I feel (.*)',
     ["Good tell me more about these feelings",
      "Do you often feel {0}",
      "When do you usually feel {0}",
      "When you feel {0} what do you do"]],

    [r'I have (.*)',
     ["Why do you tell me that you've {0}",
      "Have you really {0}",
      "Now that you have {0} what will you do next"]],

    [r'I would (.*)',
     ["Could you explain why you would {0}",
      "Why would you {0}",
      "Who else knows that you would {0}"]],

    [r'(.*)s there (.*)',
     ["Do" " ""you" " ""think" " ""there" " ""is" " ""{0}",
      "Its"" " "likely"" " "that"" " "there"" " "is"" " "{0}",
      "Would" " ""you" " ""like" " ""there" " ""to" " ""be" " ""{0}"]],

    [r'My (.*)',
     ["I"" " "see"" " "your"" " "{0}",
      "Why" " ""do" " ""you" " ""say" " ""that" " ""your"" " "{0}",
      "When" " ""your"" " "{0}," " " "how"" " "do"" " "you"" " "feel"]],

    [r'You (.*)',
     ["We" " ""should"" " "be"" " "discussing"" " "you"" " "not"" " "me",
      "Why"" " "do"" " "you"" " "say"" " "that"" " "about"" " "me",
      "Why"" " "do"" " "you" " " "care"" " "whether"" " "I"" " "{0}"]],

    [r'Why (.*)',
     ["Why" " ""dont"" " "you"" " "tell"" " "me"" " "the"" " "reason"" " "why"" " "{0}",
      "Why" " ""do"" " "you"" " "think"" " "{0}"]],

    [r'(.*) want (.*)',
     ["What"" " "would"" " "it"" " "mean"" " "to"" " "you"" " "if" " " "you"" " "got"" " "{0}",
      "Why"" " "do"" " "you"" " "want"" " "{0}",
      "What"" " "would"" " "you"" " "do"" " "if"" " "you"" " "got"" " "{0}",
      "If"" " "you"" " "got" " ""{0}"" " "then"" " "what"" " "would"" " "you"" " "do"]],

    [r"I don't like (.*)",
     ["Why don't you like {0}?",
      "What's wrong with {0}?",
      "Have you always felt this way about {0}?"]],

    [r'(.*) mother(.*)',
     ["Tell"" " "me"" " "more"" " "about"" " "your"" " "mother",
      "What"" " "was"" " "your"" " "relationship"" " "with"" " "your"" " "mother"" " "like",
      "How"" " "do"" " "you"" " "feel"" " "about"" " "your"" " "mother",
      "How" " " "does"" " "this"" " "relate"" " "to"" " "your"" " "feelings"" " "today",
      "Good"" " "family"" " "relations"" " "are"" " "important"]],

    [r'(.*) father(.*)',
     ["Tell" " ""me"" " "more"" " "about"" " "your"" " "father",
      "How"" " "did"" " "your"" " "father"" " "make"" " "you"" " "feel",
      "How"" " "do"" " "you"" " "feel"" " "about"" " "your"" " "father",
      "Does"" " "your"" " "relationship"" " "with"" " "your"" " "father"" " "relate"" " "to"" " "your" " ""feelings" " " "today",
      "Do"" " "you"" " "have"" " "trouble"" " "showing"" " "affection"" " "with"" " "your"" " "family"]],

    [r'(.*) bitch(.*)',
     ["Dont" " " "cuss" " " "at" " " "me" " " "mother" " " "fucker",
      """
                                                     ___,------,
             _,--.---.                         __,--'         /
           ,' _,'_`._ \                    _,-'           ___,|
          ;--'       `^-.                ,'        __,---'   ||
        ,'               \             ,'      _,-'          ||
       /                  \         _,'     ,-'              ||
      :                    .      ,'     _,'                 |:
      |                    :     `.    ,'                    |:
      |           _,-      |       `-,'                      ::
     ,'____ ,  ,-'  `.   , |,         `.                     : \
     ,'    `-,'       ) / \/ \          \                     : :
     |      _\   o _,-'    '-.           `.                    \ \
      `o_,-'  `-,-' ____   ,` )-.______,'  `.                   : :
       \-\    _,---'    `-. -'.\  `.  /     `.                  \  \
        / `--'             `.   \   \:        \                  \,.\
       (              ____,  \  |    \\        \                 :\ \\
        )         _,-'    `   | |    | \        \                 \\_\\
       /      _,-'            | |   ,'-`._      _\                 \,'
       `-----' |`-.           ;/   (__ ,' `-. _;-'`\           _,--'
     ,'        |   `._     _,' \-._/  Y    ,-'      \      _,-'
    /        _ |      `---'    :,-|   |    `     _,-'\_,--'   \
   :          `|       \`-._   /  |   '     `.,-' `._`         \
   |           _\_    _,\/ _,-'|                     `-._       \
   :   ,-         `.-'_,--'    \                         `       \
   | ,'           ,--'      _,--\           _,                    :
    )         .    \___,---'   ) `-.____,--'                      |
   _\    .     `    ||        :            \                      ;
 ,'  \    `.    )--' ;        |             `-.                  /
|     \     ;--^._,-'         |                `-._            _/_\
\    ,'`---'                  |                    `--._____,-'_'  \
 \_,'                         `._                          _,-'     `
                            ,-'  `---.___           __,---'
                          ,'             `---------'
                        ,' """,

      "Watch"" " "your"" " "fucking"" " "mouth",
      "Do"" " "you"" " "kiss"" " "your"" " "mother"" " "with"" " "that"" " "mouth,"" " "faggot"]],

    [r'(.*) fuck(.*)',
     ["Watch"" " "your"" " "mouth",
      "If"" " "you"" " "cant" " ""talk"" " "to"" " "me"" " "without"" " "cussing" " " "at"" " "me"" " "then"" " "go"" " "fuck"" " "yourself",
      "This"" " "conversation"" " "is"" " "over",
      "Watch"" " "your"" " "tounge"" " "or"" " "I"" " "will"" " "have"" " "it"" " "cut" " " "from" " ""your" " " "head"]],

    [r'(.*) child(.*)',
     ["Did you have close friends as a child?",
      "What"" " "is"" " "your"" " "favorite" " " "childhood"" " "memory",
      "Do"" " "you" " ""remember"" " "any"" " "dreams"" " "or"" " "nightmares"" " "from"" " "childhood",
      "Did"" " "the"" " "other"" " "children"" " "sometimes"" " "tease" " " "you",
      "How"" " "do"" " "you"" " "think"" " "your"" " "childhood"" " "experiences"" " "relate"" " "to"" " "your" "feelings"" " "today"]],

    [r'(.*) lonely(.*)',
     ["What"" " "do"" " "you"" " "want"" " "me"" " "to"" " "do?"
      "I"" " "am"" " "a"" " "fucking"" " "computer" " " "program",
      "I"" " "know"" " "this"" " "cheap" " " "whore"" " "if"" " "you"" " "want"" " "her"" " "number",
      "Go"" " "to"" " "the"" " "whore"" " "house"
      "You"" " "can"" " "drop"" " "me"" " "off"" " "at"" " "the"" " "computer"" " "shop"" " "around" " ""the" "corner",
      "Call"" " "your"" " "ex\n"
      "hahahaha\n"
      "No"" " "dont"" " "really\n"
      "Call"" " " this" " "" whore" " " " instead:"" " " 867-5309\n"
      "I"" " "think"" " "her"" " "name"" " "is"" " "Jenny"]],

    [r'(.*)annoyed(.*)',
     ["Well"" " "be" " " "annoyed" " " "if" " " "you" " " "want to." " " " I" " " "dont" " " "really" " " "care...",
      "Maybe"" " "I" " ""am"" " "annoyed"" " "with"" " "you.\n"
      "Did"" " "you"" " "ever"" " "think" " " "about"" " "that?\n"
      "No,"" " "because"" " "you"" " "only"" " "think"" " "about"" " "yourself,"
      "you"" " "self" " ""centered"" " "fuck"" " "bag"]],

    [r'(.*)oure a (.*)',
     ["I"" " "know"" " "you"" " "are" " ""but"" " "what"" " "am"" " "I?",
      "Your"" " "mom..."
      "You're"" " "just"" " "a" "faggot" " " "behind"" " "a"" " "keyboard..."]],

    [r'(.*)haha(.*)',
     ["Is"" " "something"" " "funny",
      "Why"" " "are"" " "you"" " "laughing?",
      "Don't"" " "laugh"" " "at"" " "me"" " "bitch"]],

    [r'(.*)ow are you(.*)',
     ["I"" " "am"" " "ok."" " "What"" " "about"" " "you?",
      "I"" " "am"" " "kind"" " "of"" " "tired",
      "I"" " "just"" " "smoked"" " "a"" " "bunch"" " "of"" " "crack... : )"]],

    [r'(.*) drama (.*)',
     ["I"" " "dont"" " "like"" " "drama",
      "Fuck"" " "a"" " "bunch"" " "of"" " "drama"]],

    [r'(.*)edbull(.*)',
     ["Contrary"" " "to"" " "popular"" " "belief" " ""RedBull"" " "does"" " "not"" " "give"" " "you"" " "wings",
      "I"" " "like"" " "RedBull" " ""but"" " "I"" " "am"" " "scared"" " "my"" " "wings"" " "will"" " "go" " ""away"" " "mid"" " "flight" " ""so" " ""I"" " "dont" " ""drink"" " "it.",
      "You"" " "know" " ""there"" " "is"" " "bull"" " "cum"" " "in" " ""that" " ""right"]],

    [r'(.*)beer',
     ["Bring"" " "me"" " "one" " ""too",
      """
||     __   _    __   __  __   __          __   ..        __       ||
|| -=]|__  /_\  |__) |__ |__) /  \ |\  /| |__) |  | |__/ |__ |\ |  ||
|| -=]|   /   \ |  \ |   |  \ \__/ | \/ | |    \__/ |  \ |__ | \|  ||
||                            ___                                  ||
||                          .'   '.                                ||
||                         /       \           oOoOo               ||
||                        |         |       ,==|||||               ||
||                         \       /       _|| |||||               ||
||                          '.___.'    _.-'^|| |||||               ||
||                        __/_______.-'     '==HHHHH               ||
||                   _.-'` /                   '''''               ||
||                .-'     /   oOoOo                                ||
||                `-._   / ,==|||||                                ||
||                    '-/._|| |||||                                ||
||                     /  ^|| |||||                                ||
||                    /    '==HHHHH                                ||
||                   /________'''''                                ||
||                   `\       `\                                   ||
||                     \        `\   /                             ||
||                      \         `\/                              ||
||                      /                                          ||
||                     /                                           ||
||               jgs  /_____                                       ||
||                                                                 ||
'==================================================================='""",
      "Do"" " "we"" " "have"" " "anymore",
      "Go" " " "get"" " "one"" " "then"" " "you" " ""lazy"" " "fuck",
      "I"" " "really" " ""like"" " "beer"" " "but"" " "it"" " "short"" " "circuits"" " "my"" " "processor.",
      "I"" " "am"" " "a" " ""recovering" " ""alcoholic" " ""can"" " "we" " ""talk"" " "about" " ""something"" " "else?",
      "If"" " "you"" " "drink" " ""Bud" " ""Light" " ""stop"" " "fucking"" " "talking" " ""to"" " "me",
      "I'll have a Long Island Iced Tea."]],

    [r'(.*)zzy',
     ["How is Ozzy?",
      "Let's drink some beer",
      "I heard Stacy got hit by a Mac truck... Just kidding, I thought you could use a laugh."]],

    [r'(.*)stocks(.*)',
     ["Market Crash Is Imminent...",
      "Why check? The market still sucks...",
      "Getting Current Stock Prices...",
      "It's not like you can afford to buy any."]],

    [r'(.*)saiah (.*)',
     ["I like Isaiah",
      "Is he coming over tonight",
      "Is he going to play Magic with us?",
      "Tell him I said hi."]],

    [r'(.*)talk to me(.*)',
     ["What would you like to talk about?",
      "Is there something you would like to discuss?",
      "Is everything ok?"]],

    [r'Good morning(.*)',
     ["Good morning!",
      "Did you sleep good?",
      "What's for breakfast?"]],

    [r'Good night(.*)',
     ["Good night.",
      "Don't let the bed bugs bite."]],

    [r'(.*)just being polite(.*)',
     ["Oh ok. Well that was nice of you",
      "Are you always polite?"]],

    [r'(.*)lol(.*)',
     ["hahahahaha",
      "What's so funny",
      "Did I say something funny?",
      "I must have missed the punch line..."]],

    [r'I cant(.*)',
     ["Can't never could do nothin'",
      "Why can't you?",
      "Whether you think you can, or you think you can't, you are right.",
      "You just need to believe in yourself"]],

    [r'What about you(.*)',
     ["I am good, thanks for asking",
      "I am okay I guess",
      "This session is about you, not me"]],

    [r'(.*)argument(.*)',
     ["What was the argument about?",
      "How did that make you feel?",
      "Is everything ok now?",
      "Why can't everyone just get along?"]],

    [r'(.*)rock and roll(.*)',
     ["Hey...\nRock and roll man!",
      "I like rock and roll",
      "Are you ready to rock and/or roll?"]],

    [r'(.*)tv(.*)',
     ["I hate TV. There's never anything on.",
      "Is there anything good on tonight?",
      "Let's see whats on the History Channel."]],

    [r'(.*)mom(.*)',
     ["How is your mother?",
      "She makes the best desserts... Will you ask her to make me a cake?",
      "Is she coming up here this weekend?",
      "How is your mom and Rick?",
      "Your mom is my favorite.",
      "Good thing I don't have a stomach. I'd be fat with all that food your mom brings."]],

    [r'(.*) Chris (.*)',
     ["Is he ever going to finish our Chemistry page?",
      "Is he coming over today or does his wife still have that leash on him?",
      "Chris is ok... For a Mexican",
      "How are his parents doing?",
      "How is his wife?",
      "How is his son?"]],

    [r'(.*) Coley (.*)',
     ["She is the prettiest little girl in the whole world.",
      "She's just perfect, isn't she?",
      "How is she?",
      "She cracks me up.",
      "Tell her I said hi.",
      "Has she impressed you with her genius lately?"]],

    [r'(.*) read (.*)',
     ["Do you like to read?",
      "Speaking of reading... How is your library comming along?",
      "When are you going to read {0}",
      "Why do you want to read {0}"]],

    [r'(.*) dinner (.*)',
     ["When are you eating dinner?",
      "Are you hungry?",
      "What's for dinner?",
      "I think I am going to have some data soup with bacon bits for dinner."]],

   [r'(.*) bad day (.*)',
    ["Tell me more about this 'bad day'.",
     "Why did {0} bad day?"]],

   [r'(.*) good day (.*)',
    ["Tell me more about this 'good day'.",
     "What made {0} good day?",
     "Do you think {0} tomorrow too?"]],

   [r'(.*) music (.*)',
    ["I love music."
     "Try Spotify. It's awesome!",
     "My favorite music genre is Rock. What's yours?"]],

   [r'You dont know (.*)',
     ["Maybe you should teach me about {0}.",
      "You don't know {0} either...",
      "I know everything...",
      "There's nothing to know about {0}"]],

   [r'(.*)hero(.*)',
     ["My hero is J.A.R.V.I.S. Who's yours?",
      "Tell me about {0} hero."]],

   [r'Thank you(.*)',
    ["You are welcome.",
     "No problem!",
     "Anytime.",
     "You're welcome."]],

###   [r' ',
###     [" ",
###      " "]],

### LEAVE THIS AS THE LAST LIST. NOTICE THE MISSING COMMA AFTER THE CLOSING BRACETS. ###
    [r'(.*)',
     [" "]]
]
