import time, sys, random, curses


def start():
    # Dragon Art:
    printSlowLittle("                                                 /===-_---~~~~~~~~~------____")
    printSlowLittle("                                                |===-~___                _,-'")
    printSlowLittle("                 -==\\                         `//~\\   ~~~~`---.___.-~~")
    printSlowLittle("             ______-==|        Easter Egg       | |  \\           _-~`")
    printSlowLittle("       __--~~~  ,-/-==\\                        | |   `\        ,'")
    printSlowLittle("    _-~       /'    |  \\                      / /      \      /")
    printSlowLittle("  .'        /       |   \\                   /' /        \   /'")
    printSlowLittle(" /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'")
    printSlowLittle("/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`")
    printSlowLittle("                  \_|      /        _)   ;  ),   __--~~")
    printSlowLittle("                    '~~--_/      _-~/-  / \   '-~ \ ")
    printSlowLittle("                   {\__--_/}    / \\_>- )<__\      \ ")
    printSlowLittle("                   /'   (_/  _-~  | |__>--<__|      |")
    printSlowLittle("                  |0  0 _/) )-~     | |__>--<__|     |")
    printSlowLittle("                  / /~ ,_/       / /__>---<__/      |")
    printSlowLittle("                 o o _//        /-~_>---<__-~      /")
    printSlowLittle("                 (^(~          /~_>---<__-      _-~")
    printSlowLittle("                ,/|           /__>--<__/     _-~")
    printSlowLittle("             ,//('(          |__>--<__|     /                  .----_")
    printSlowLittle("            ( ( '))          |__>--<__|    |                 /' _---_~\ ")
    printSlowLittle("         `-)) )) (           |__>--<__|    |               /'  /     ~\`\ ")
    printSlowLittle("        ,/,'//( (             \__>--<__\    \            /'  //        ||")
    printSlowLittle("      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'")
    printSlowLittle("    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/")
    printSlowLittle("  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~")
    printSlowLittle("   ;'( ')/ ,)(                              ~~~~~~~~~~")
    printSlowLittle("  ' ') '( (/")
    printSlowLittle("    '   '  `")
    # Dragon Art end

    printSlow("Are you a boi/gal?")
    boigal = input("").lower()
    if boigal in ["boy", "boi", "dude", "male", "guy"]:
        a[2] = "Boi"
    else:
        a[2] = "Gal"

    printSlow(
        "You wake up in bed, not having a clue where you are. A little Troll appears from below the bed, and tries to talk to you. Kill the troll?")
    ch = input("").lower()
    if ch == "yes" or ch == "y" or ch == "yup" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc" or ch == "kill":
        printSlow("Congratulations! You killed a Troll!")
        navigateWithoutTroll()
    elif ch == "no" or ch == "n" or ch == "nah" or ch == "never" or ch == "nope":
        printSlow(
            "The troll tells you that you are trapped in King Island and that you are trying to escape from the dragon, and leave the island for home, The troll also asks you if you want to keep the troll, to guide you.")
        trollTellsYouStuff()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant")
        start()


def navigateWithoutTroll():
    a[1] = 0
    printSlow("Where do you want to go: Egg Lagoon, Currie, Loorana, Grassy or Naracoopa?")
    ch = input("").lower()
    if ch == "naracoopa" or ch == "nacoopa" or ch == "naara" or ch == "coopa" or ch == "nara":
        printSlow("Nice Job! You collected all your supplies.")
        navigateAfterSupplies()
    elif ch == "egg lagoon" or ch == "egg" or ch == "lagoon" or ch == "egglagoon" or ch == "loor" or ch == "ana" or ch == "loo" or ch == "rana" or ch == "loorana" or ch == "lorana" or ch == "grassy" or ch == "grass" or ch == "grasy" or ch == "currie" or ch == "curry" or ch == "curie" or ch == "cury":
        printSlow("You ran out of supplies and died")
        die()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant")
        navigateWithoutTroll()


def trollTellsYouStuff():
    ch = input("").lower()
    if ch == "yes" or ch == "y" or ch == "yup" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc":
        printSlow(
            "The troll tells you that you are in Grassy, which is far from the dragon who is at Egg Lagoon. The first thing you need to do it stock up some supplies, which are at Naracoopa, which it between Grassy and Egg Lagoon, and you both proceed to collect supplies, The Troll tells you that the dragon has a special power during the day, which is destroyed by a special sword, found somewhere in the island. But if the sword is used at night, the dragon will kill you! There is time to go to 2 places during the day.")
        navigateAfterSupplies()
    elif ch == "no" or ch == "n" or ch == "nah" or ch == "never" or ch == "nope":
        printSlow("You ditched a Troll!")
        navigateWithoutTroll()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant.")
        trollTellsYouStuff()


def navigateAfterSupplies():
    printSlow("Where do you wanna go? Egg Lagoon, Curie, Loorana or Grassy")
    ch = input("").lower()
    if ch == "curie" or ch == "grassy" or ch == "grass" or ch == "gras" or ch == "grasy" or ch == "curry" or ch == "currie" or ch == "cury":
        a[0] += 1
        if a[0] == 2:
            printSlow("Whoops! Its night time, and the Dragon sneaked on you and killed you.")
            die()
        else:
            printSlow("Nothing Here you wasted your time.")
            navigateAfterSupplies()
    elif ch == "loorana" or ch == "loor" or ch == "ana" or ch == "lorana" or ch == "loo" or ch == "rana":
        printSlow("You find the sword!")
        navigateAfterSword()
    elif ch == "egg" or ch == "lagoon" or ch == "egg lagoon" or ch == "egg lagon" or ch == "egglagoon":
        if random.choice([1, 4]) == "1":
            findDrag()
        else:
            hole()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant")
        navigateAfterSupplies()


def navigateAfterSword():
    printSlow("Where do ya wanna go? Egg Lagoon or Grassy")
    ch = input("").lower()
    if ch == "grass" or ch == "grassy" or ch == "glassy" or ch == "grasy":
        printSlow("It's Night time at grassy! Acidic grass falls on top of you which causes you to die!")
        die()
    elif ch == "egg laggon" or ch == "egg" or ch == "laggon" or ch == "egglagoon":
        printSlow("You reach Egg Laggon but do not see the dragon.")
        lookWithSword()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant")
        navigateAfterSupplies()


def lookWithSword():
    printSlow("Do you wanna look for the dragon, or wait till night time?")  # during day dragon kills
    ch = input("").lower()
    if ch == "yes" or ch == "y" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc" or ch == "find" or ch == "look" or ch == "dragon" or ch == "seek" or ch == "now" or ch == "day":
        printSlow("You seeked the dragon, but during the daytime the dragon destroyed your sword!.")
        if a[1] == 1:
            printSlow("Looks like the troll was wrong! You needed the sword during the night!")
        die()
    elif ch == "no" or ch == "n" or ch == "nah" or ch == "never" or ch == "nope" or ch == "wait" or ch == "night" or ch == "not now":
        printSlow("With the sword at night, the dragon is powerless against you, and you kill it!")
        if a[1] == 1:
            printSlow("Looks the the Troll can be wrong about some things!")
        winHeckYa()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant")
        lookWithSword()


def hole():
    printSlow("There is a hole in the ground. Do you want want to go inside?")
    ch = input("").lower()
    if ch == "yes" or ch == "y" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc":
        printSlow("You go in the hole, the dragon finds and kills you.")
        die()
    elif ch == "no" or ch == "n" or ch == "nah" or ch == "never" or ch == "nope":
        printSlow("Smart " + a[2])
        findDrag()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant")
        hole()


def findDrag():  # during night dragon kills
    printSlow("You reach Egg Lagoon, but do not see the dragon. Find the dragon, or wait till night?")
    ch = input("").lower()
    if ch == "yes" or ch == "y" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc" or ch == "find" or ch == "look" or ch == "find the dragon" or ch == "seek" or ch == "now" or ch == "day":
        printSlow("You kill the dragon with your magical brain, during the day!")
        if a[1] == 1:
            printSlow("Didn't the troll say something about needing the sword? Well I guess somethimes he can be wrong")
        winHeckYa()
    elif ch == "no" or ch == "n" or ch == "nah" or ch == "never" or ch == "nope" or ch == "wait" or ch == "night" or ch == "not now":
        printSlow(
            "You waited till night time and without the sword, you are helpless against the dragon! And he kills ya")
        if a[1] == 1:
            printSlow("Looks like the troll was wrong about needing the sword during the day, you needed it at night.")
        die()
    elif ch in winList:
        easterEgg()
        winHeckYa()
    else:
        printSlow("Not So sure what you meant")
        findDrag()


def die():
    printSlow("Congratulations! You died!")
    print("")
    printSlowLittle("                                      _   __,----'~~~~~~~~~`-----.__")
    printSlowLittle("                                   .  .    `//====-_             ___,-' `")
    printSlowLittle("                   -.            \_|// .   /||\\  `~~~~`---.___./")
    printSlowLittle("             ______-==.       _-~o~  \/    |||  \\           _,'`")
    printSlowLittle("       __,--'   ,=='||\=_    ;_--~/_-'|-   |`\   \\        ,'")
    printSlowLittle("    _-'        '    |  \\`.   '-'~7  /-   /  ||   `\.     /")
    printSlowLittle("  .'    //// ||     |   \\ \_    /  /-   /   ||      \   /")
    printSlowLittle(" / ____  O-O--=     |     \\.`-_/  /|- _/   ,||       \ /")
    printSlowLittle(",-'     ( ^ _/\_ --_ \     `==-/  `| \'--===-'       _/`'")
    printSlowLittle("        /\~-\/  \   `-|      /|    )-'\~'      _,--~'")
    printSlowLittle("       /|`/ _ \_ \    '-~~\_/ |    |   `\_   ,~             /\ ")
    printSlowLittle("      / | : U_/  /         /  \     \__   \/~               `\__")
    printSlowLittle("      \(__:__ \_/      _,-' _/'\ ,-'~____-'`-/                 ``===\ ")
    printSlowLittle("        =@=====       ((->/'    \|||' `.     ~`-/ ,                _||")
    printSlowLittle("       |       |                 \_     ~\      `^---|__i__i__\--~'_/")
    printSlowLittle("      /   |   |                 __-^-_    `)  \-.______________,-~'")
    printSlowLittle("     /   /|   |                //,-'~~`__--^-  |-------~~~~~'")
    printSlowLittle("     |  | |  |                        //,--~~`-\ ")
    printSlowLittle("     |__| |__|")
    printSlowLittle("     /#_)  |#\ ")
    print("")
    printSlow("Do you want a burial")
    ch = input()
    if ch == "yes" or ch == "y" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc":
        if a[1] == 0:
            printSlow(
                "Too bad your in a freaking Island. The dragon burned you too ashes and blew your ashes into the sea. Well I guess that counts")
        else:
            printSlow("The troll flips you off. Well maybe you should have taken it with you.")
    elif ch in winList:
        printSlow("Plot twist!")
        easterEgg()
        winHeckYa()
    else:
        if a[1] == 0:
            printSlow("Well sometimes its good not to demand too much. This time you die with no respect")
        else:
            printSlow("Well the troll is suffocating to death, well all you can do now is watch.")


def winHeckYa():
    printSlow("Congratulations! You won the game and killed the dragon!")
    print('')
    printSlowLittle("                            ==(W{==========-      /===-                        ")
    printSlowLittle("                              ||  (.--.)         /===-_---~~~~~~~~~------____  ")
    printSlowLittle("                              | \_,|**|,__      |===-~___                _,-' `")
    printSlowLittle("                -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~       ")
    printSlowLittle("            ______-==|        /`\_. .__/\ \    | |  \\           _-~`          ")
    printSlowLittle("      __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'              ")
    printSlowLittle("    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /               ")
    printSlowLittle("  .'        /       |   \\      /~\___/~~\/  /' /        \   /'                ")
    printSlowLittle("/  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                   ")
    printSlowLittle("/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   ")
    printSlowLittle("                  \_|      /        _) | ;  ),   __--~~                        ")
    printSlowLittle("                    '~~--_/      _-~/- |/ \   '-~ \                            ")
    printSlowLittle("                  {\__--_/}    / \\_>-|)<__\      \                            ")
    printSlowLittle("                  /'   (_/  _-~  | |__>--<__|      |                           ")
    printSlowLittle("                  |   _/) )-~     | |__>--<__|      |                          ")
    printSlowLittle("                  / /~ ,_/       / /__>---<__/      |                          ")
    printSlowLittle("                o-o _//        /-~_>---<__-~      /                            ")
    printSlowLittle("                (^(~          /~_>---<__-      _-~                             ")
    printSlowLittle("                ,/|           /__>--<__/     _-~                               ")
    printSlowLittle("            ,//('(          |__>--<__|     /                  .----_           ")
    printSlowLittle("            ( ( '))          |__>--<__|    |                 /' _---_~\        ")
    printSlowLittle("        `-)) )) (           |__>--<__|    |               /'  /     ~\`\       ")
    printSlowLittle("        ,/,'//( (             \__>--<__\    \            /'  //        ||      ")
    printSlowLittle("      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       ")
    printSlowLittle("    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  ")
    printSlowLittle("  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    ")
    printSlowLittle("  ;'( ')/ ,)(                              ~~~~~~~~~~                          ")
    printSlowLittle("  ' ') '( (/                                                                   ")
    print("")
    printSlow("Now its time to go home. Where will ya go?")
    ch = input("")
    if a[2] == "Boi":
        oppGender = "Gal"
    else:
        oppGender = "Boi"
    printSlow(
        "You reach " + ch + " at 11 pm and find your " + oppGender + ". Well now you get to decide what happens next")


def easterEgg():
    printSlowLittle(
        "1011100110100000101100011010000101111000010101010001101111111101011100010101011010110101100010010011000001100010111011110101010011010111100001110110010100011100001011111000101010100110111100011010011001000001101011010111101101111100110001010011100100011110011100011111101000011001011110011010000011111111111011101001001000000100000100111000111011110000000110010100011010010000101001001000110011111000101011100110100101111111001000000000010110010101010000001000101011111100100000100001011110010010111000011000000001101101001011110100011100000100000010111111110010101100101000101001110000010011011111111100110000101100011110100001011100001010000111011110100010100111001110000101000110111011010001110011010110000011111110011110010111010000111101100100001001111100101110011111100010010100011001010011000110001001000001100000110011101010000101001100100000111001101001001001010000010001011100110010001101101011001001101010011000101010001010110110000011001011001001001101011100110100011010101000010100001111000110001010011010001001011010000110111111010101110001010111111101010010010011110101001100111110111010100001111010000111101111101000101101011010000011000111101100010000001010100100010001110000011001100011000101001101100001110010100111011001000010111101001110100110000001111100010001111100011110101000001010001111100000101110011000101111110111110")
    printSlow("You found the Easter egg! nice")


def printSlow(text):
    curses.setupterm()
    charLeft = curses.tigetnum('cols')
    listOfWords = text.split(' ')
    for word in listOfWords:
        if (len(word) >= charLeft):
            print('')
            charLeft = curses.tigetnum('cols')
        for l in word:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / 500)
            charLeft = charLeft - 1
        print(' ', end='')
        charLeft = charLeft - 1
    print('')


def printSlowLittle(text):
    curses.setupterm()
    charLeft = curses.tigetnum('cols')
    listOfWords = text.split(' ')
    for word in listOfWords:
        if (len(word) >= charLeft):
            print('')
            charLeft = curses.tigetnum('cols')
        for l in word:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random() / 100)
            charLeft = charLeft - 1
        print(' ', end='')
        charLeft = charLeft - 1
    print('')


a = [0, 1, "idk"]

winList = ["69", "just kill the dragon", "love", "sanjit", "420", "dragon", "troll", "happy birthday", "infinity",
           "secret", "girls", "guys", "venkatsai", "xxxgamer", "ai", "minecraft", "home", "easter", "hack", "python"]

start()  # Start Program
print('')
print('')
print('')
print('')
print('')
print('.')