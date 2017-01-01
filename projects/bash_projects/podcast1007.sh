#!/bin/bash
clear
echo "Welcome to another installment of the Program13 podcast..."
sleep 7
echo "Today we will be discussing"
sleep 3
echo "Bash Scripting: Creating your own bash commands."
sleep 7
clear
echo "We will be working with gedit and .bashrc"
sleep 7
clear
echo "gedit is simply a text editor that can be used to create all types of files"
sleep 7
clear
echo "If you do not already have gedit installed on your Linux machine please do so now by opening your terminal"
sleep 3
echo "and entering 'sudo apt-get install gedit' without the quotes."
sleep 10
clear
echo "Once you have gedit installed enter the following command into the terminal to open your .bashrc file"
sleep 3
echo "sudo gedit .bashrc"
sleep 10
clear
echo "gedit can be used without the sudo command but you can not save any changes made to your .bashrc file unless you are root user."
sleep 9
clear
echo "Once you have your .bashrc file opened in gedit, scroll to the bottom of the page until you see "
sleep 3
echo "# Alias definitions."
echo "# You may want to put all your additions into a separate file like"
echo "# ~/.bash_aliases, instead of adding them here directly."
echo "# See /usr/share/doc/bash-doc/examples in the bash-doc package."

echo "if [ -f ~/.bash_aliases ]; then"
echo "    . ~/.bash_aliases"
echo "fi"
sleep 9
clear
echo "We will be creating our commands on the following lines."
sleep 7
clear
echo "If there is not already a new line after 'fi' press enter twice. If there is a blank line following 'fi' press enter once.We will define our commands on the last blank line under 'fi'."
sleep 9
clear
echo "To define a custom command in Linux we use the 'alias' command. It is very easy to use and once you figure it out you can write commands to do just about anything you would like to do. "
sleep 9
clear
echo "What we will do today is use 'alias' to combine commands we use offten or really long commands to save time."
sleep 7
clear
echo "The first thing you have to do when creating an alias is to define the alias."
sleep 7
clear
echo "We do this by 'alias [aliasname]='[commands]' "
sleep 7
clear
echo "Please note that you must have the single quotes around your command or the alias will give you an error message when trying to run your new command"
sleep 9
clear
echo "An example of this would be:"
sleep 3
echo "alias program13='google-chrome http://program13.me' "
sleep 7
clear
echo "This alias would open our website in the Google Chrome web browser."
sleep 7
clear
echo "If we wanted to use a proxy service to visit the site instead of just Google Chorme,"
echo "we could do alias program13='proxychains firefox http://program13.me"
sleep 10
clear
echo "Let's say we want to add multiple commands to our alias."
sleep 7
clear
echo "To do this all we would need to do is add a semicolon in between the commands."
sleep 3
echo "Ex: service tor start ; proxychains firefox http://program13.me"
sleep 9
clear
echo "Your can continue to experiment and dicover new ways to use the 'alias' command to make your life easier."
sleep 9
clear
echo "Once you have created your alias, save the file and close gedit"
sleep 7
clear
echo "Then go back to your teminal and type 'source ~/.bashrc'"
sleep 7
clear
echo "This will update your bash without having to log out and then log back in."
sleep 7
clear
echo "You can combine as many commands as you'd like to your alias but if you have an excessively large number of commands you would like to add, I recommend creating multiple aliases to make maintenece easier in the future. Then just create another alias with your other commands and type in the first alias name where you would like it to run."
sleep 10
clear
echo "You can link together as many aliases as you need to by adding other alias names into the [command] section of your alias."
sleep 10
clear
echo "Ex: alias alias1='[commands]'"
echo "alias program13='[commands];[commands];[alias1]'"
sleep 10
clear
echo "Experiment a little bit and see what kind of cool commands you can come up with."
sleep 7
clear
echo "Once you run source ~/.bashrc , type in the name of your alias in your terminal and the commands you defined will run."
sleep 8
echo "If you create some cool commands, please feel free to share them with us via our website http://program13.me"
sleep 10
clear
echo "That is all we will be covering on bash scripts today."
sleep 7
clear
echo "There is alot more to learn but we can't cover everything in one podcast so please stay tunned for more great info about Linux commands and bash scripting"
sleep 10
clear
echo "Please subscribe to our youtube channel so you can stay up to date on all the cool stuff Program13 will be releaseing"
sleep 10
clear
echo "Thanks for joining us. If you have an idea for a future video you'd like to see, send us a message on our website and we will try to make a video about whatever it is you would like to learn more about."
sleep 7
clear
exit 0
