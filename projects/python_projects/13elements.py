#1/usr/bin/env python3

commands = { 
              "i" : "see inventory",
              "craft [item]" : "craft something from inventory items",
           }
#an inventory of items
items = { 
              "God" : 1,
              "flint" : 0,
              
              "grass" : 0,
              "hay" : 0,
              
              "tree" : 0,
              "log" : 0,
      
              "sapling" : 0,
              "twig" : 0,

              "boulder" : 0,
              "rock" : 0,

              "pickaxe" : 0,
              "axe" : 0,
             
              "firepit" : 0,
              "tent" : 0,
 
              "torch" : 0,
              "fire" : 500,
 
              "air" : 500,
              "electricity" : 0,
         
              "dirt" : 500,
              "seed" : 0,

              "water" : 500,
              "metal" : 0,

              "magnet" : 0,
              "copper" : 0,

              "saw" : 0,
              "sword" : 0,

              "energy" : 500,
              "brick" : 0,
              
              "mud" : 0,
              "metalore" : 0,

              "life" : 0,           
              "sand" : 0,

              "house" : 0,
              "rain" : 0,
          
              "storm" : 0,
        }
#rules to make new objects

craft = {
              "hay" : { "grass" : 1 },
              "twig" : { "sapling" : 1 },
              "log" : { "axe" : 1, "tree" : 1 },
              "axe" : { "twig" : 3, "metal" : 1 },
              "tent" : { "twig" : 10, "hay" : 15 },
              "firepit" : { "boulder" : 5, "log" : 3, "twig" : 1, "torch" : 1 },
              "torch" : { "fire" : 1, "grass" : 1, "twig" : 1 }, 
              "pickaxe" : { "rock" : 2, "twig" : 1 },
              "mud" : { "water" : 1, "dirt" : 1 },
              "brick" : { "mud" : 1, "fire" : 1 },
              "metalore" : { "pickaxe" : 1, "dirt" : 1 },
              "tree" : { "sapling" : 2 },
              "sapling" : { "seed" : 1, "grass" : 1 },
              "grass" : { "dirt" : 1, "rain" : 1 },
              "seed" : { "dirt" : 1, "grass" : 1 },
              "boulder" : { "rock" : 2 },
              "rock" : { "dirt" : 1, "dirt" : 1 },
              "metal" : { "metalore" : 1, "fire" : 1 },
              "flint" : { "water" : 1, "rock" : 1 },
              "sand" : { "dirt" : 1, "water" : 1 },
              "house" : { "brick" : 100 }
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

print("SEE WHAT YOU CAN CREATE!")
print("type '?' for help")

while True:
    command = raw_input(">").split()
    if len(command) == 0:
        continue
    if len(command) > 0:
        verb = command[0].lower()
    if len(command) > 1:
        item = command[1].lower()
    if verb == "?":
        for key in commands:
            print(key + " : " + commands[key])
        print("\n")
    elif verb == "i":
        for key in items:
            print(key + " : " + str(items[key]))
        print("\n")
    elif verb == "craft":
        print("making " + item + ":")
        if item in craft:
            for i in craft[item]:
                print(" you need : " + str(craft[item][i]) + " " + i + " and you have " + str(items[i]))
            canBeMade =  True
            for i in craft[item]:
                if craft[item][i] > items[i]:
                    print("item cannot be crafted\n")
                    canBeMade = False
                    break
            if canBeMade == True:
                for i in craft[item]:
                    items[i] == craft[item][i]
                items[item] += 1
                print("item crafted\n")
            if items["life"] < 0 and items["God"] >=2:
                print("\n**YOU HAVE MANAGED TO SURVIVE1\nWELL DONE!")
                break
        else:
            print("you can't")
    else:
        print("you can't")
  
