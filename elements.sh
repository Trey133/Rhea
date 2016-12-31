#!/bin/bash
trap '' 2  # ignore control + c
while true
do
  clear
  echo "================================================================="
echo "                    sZZZZ.          ,I,"  
echo "                   ZZ. ..sZ:    .Zss?.7s7.   "    
echo "                  .s.     ..  .Zs:     .s.   "    
echo "                  IZ.        Zs         s~   "   
echo "                  IZ       7ZI         .s:   "    
echo "                  .s.    .Zs            s    "    
echo "                  .sZZZsZsssZZsssss,         "    
echo "              sZZsZsZ...ZZ   ......?Zssss7   "    
echo "           .Zs~.    s.:s               ..?sZZ."    
echo "          +s.       Zss:     .     Zs.     .,ss."  
echo "          ZZ        .s?    sssss   .s=        ?s. "
echo "          .ss       sZs    7ssss    ,s         Z: "
echo "            Zss    ZZ.Zs.   ...      ZZ      .ss. "
echo "             .=.  +s.  Zs             Z.  .7Zs? "  
echo "                  s=    sZ            Zs  .~.   "  
echo "                 =Z      ss           ~s         " 
echo "                 ZZ      .sZ.         .s.         "
echo "                 s,       .ZZ.         s+         "
echo "                 s.         ?$+        Z?         "
echo "                 sZ     ss7  .ss      .Z.         "
echo "                  ssZssss.    .,ss,   Zs     "
toilet 13Elements ;
  echo  "================================================================"

echo "Enter q to quit q:"
  echo -e "Please Select Difficulty Level Now And Press <return> .. c"
  echo "Beginner |  Normal |  Expert"
  read answer  # create variable to retains the answer
  case "$answer" in
   Beginner) python "13elements.py" ;;
   Normal) python "13elements(normal).py" ;;
   Expert) python "13elements(expert).py" ;;
   q) exit ;;
  esac
  echo -e "Hit the <return> key to continue.. c"
  read input ##This causes a pause so we can read the output
  #of the selection before the loop clear the screen
done

