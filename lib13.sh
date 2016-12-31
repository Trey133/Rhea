#!/bin/bash
trap '' 2  # ignore control + c
while true
do
  clear # clear screen for each loop of menu
  echo "==========================================="
		echo "          sZZZZ.          ,I,"           
		echo "         ZZ. ..sZ:    .Zss?.7s7.   "    
		echo "        .s.     ..  .Zs:     .s.   "    
		echo "        IZ.        Zs         s~   "    
		echo "        IZ       7ZI         .s:   "    
		echo "        .s.    .Zs            s    "    
		echo "        .sZZZsZsssZZsssss,         "    
		echo "    sZZsZsZ...ZZ   ......?Zssss7   "    
		echo " .Zs~.    s.:s               ..?sZZ."    
		echo "+s.       Zss:     .     Zs.     .,ss."  
		echo "ZZ        .s?    sssss   .s=        ?s. "
		echo ".ss       sZs    7ssss    ,s         Z: "
		echo "  Zss    ZZ.Zs.   ...      ZZ      .ss. "
		echo "   .=.  +s.  Zs             Z.  .7Zs? "  
		echo "        s=    sZ            Zs  .~.   "  
		echo "       =Z      ss           ~s         " 
		echo "       ZZ      .sZ.         .s.         "
		echo "       s,       .ZZ.         s+         "
		echo "       s.         ?$+        Z?         "
		echo "       sZ     ss7  .ss      .Z.         "
		echo "        ssZssss.    .,ss,   Zs     "
toilet Lib13 ;
  echo  "=========================================="
  echo "Enter shelf to show a list of available documents."
  echo -e "Enter checkout and type the name of the document you would like to read or type q to go back and hit <return> .. c"
  echo "Enter take to view file in external viewer"
  echo "Enter photo to view pictures"
  read answer  # create variable to retains the answer
  case "$answer" in
   shelf)ls /home/cyborg/lib13 ;;
   take) read -p "Enter File Name: " file ; gpg -d $file ; okular /home/cyborg/lib13/"$file" ;;
   photo) read -p "Enter Photo Name: " photo ; gpg -d $photo ; eog /home/cyborg/lib13/"$photo" ;;
   checkout) read -p "Enter Document Title: " name ; gpg -d $name ; less /home/cyborg/lib13/"$name" ;;
   q)exit ;;
  esac
  echo -e "Hit the <return> key to continue.. c"
  read input ##This causes a pause so we can read the output
  #of the selection before the loop clear the screen
done
