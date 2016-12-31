#1/usr/bin/env python3

commands = { 
              "weather" : os.system("curl wttr.in/42220"),
              "library" : os.system("ls ~/lib13"),
           }
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

print("Enter A Command:")
print("type '?' for help")

while True:
    command = raw_input(">").split()
    if len(command) == 0:
        continue
    if verb == "?":
        for key in commands:
            print(key + " : " + commands[key])
        print("\n")
    elif verb == "weather":
        os.system("curl wttr.in/42220")
        print("\n")
    elif verb == "library":
        print("Loading Bookshelf...")
        os.system("ls ~/lib13")
        else:
            print("you can't")
    else:
        print("Good bye")
        break  
