import time, sys, random, curses


def start():
    printSlow(
        "You wake up in bed, not having a clue where you are. A little Troll appears from below the bed, and tries to talk to you. Kill the troll?")
    ch = input("").lower()
    print(ch)
    if ch == "yes" or ch == "y" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc" or ch == "kill":
        printSlow("Congratulations! You killed a Troll!")
        navigateWithoutTroll()
    elif ch == "no" or ch == "n" or ch == "nah" or ch == "im good" or ch == "nope":
        printSlow(
            "The troll tells you that you are trapped in King Island and that you are trying to escape from the dragon, and leave the island for home, The troll also asks you if you want to keep the troll, to guide you.")
        trollTellsYouStuff()
    else:
        printSlow("Not So sure what you meant")
        start()


def navigateWithoutTroll():
    printSlow("Navigate to Egg Lagoon, Currie, Loorana, Grassy, Naracoopa")
    ch = input("Where do you want to go?").lower()
    if ch == "naracoopa" or ch == "nacoopa" or ch == "naara" or ch == "coopa":
        printSlow("Nice Job! You collected all your supplies.")
        navigateAfterSupplies()
    elif ch == "egg lagoon" or ch == "loorana" or ch == "grassy" or ch == "currie":
        printSlow("You ran out of supplies and died")
        die()
    else:
        printSlow("Not So sure what you meant")
        navigateWithoutTroll()


def trollTellsYouStuff():
    printSlow(
        "The troll tells you that you are trapped in King Island and that you are trying to escape from the dragon, and leave the island for home, The troll also asks you if you want to keep the troll, to guide you.")
    ch = input("Would you like to keep the troll?").lower()
    if ch == "yes" or ch == "y" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc":
        printSlow(
            "The troll tells you that you are in Grassy, which is far from the dragon who is at Egg Lagoon. The first thing you need to do it stock up some supplies, which are at Naracoopa, which it between Grassy and Egg Lagoon, and you both proceed to collect supplies, The Troll tells you that the dragon has a special power during the day, which is destroyed by a special sword, found somewhere in the island. There is time to go to 2 places during the day.")
        navigateAfterSupplies()
    elif ch == "no" or ch == "n" or ch == "nah" or ch == "im good" or ch == "nope":
        printSlow("You ditched a Troll!")
        navigateWithoutTroll()
    else:
        printSlow("Not So sure what you meant")
        trollTellsYouStuff()


def navigateAfterSupplies():
    printSlow("Where do you wanna go? Egg Lagoon, Curie, Loorana or Grassy")
    ch = input("").lower()
    if ch == "curie" or ch == "grassy" or ch == "grass" or ch == "curry":
        printSlow("Nothing Here you wasted your time.")
        navigateAfterSupplies()
    elif ch == "loorana" or ch == "loor" or ch == "ana":
        printSlow("You find the sword!")
        navigateAfterSword()
    elif ch == "egg" or ch == "lagoon" or ch == "egg lagoon":
        if random.choice([1, 4]) == "1":
            findDrag()
        else:
            hole()
    else:
        printSlow("Not So sure what you meant")
        navigateAfterSupplies()


def navigateAfterSword():
    printSlow("Where do ya wanna go? Egg Lagoon or Grassy")
    ch = input("").lower()
    if ch == "grass" or ch == "grassy" or ch == "glassy":
        printSlow("It's Night time at grassy! Acidic grass falls on top of you which causes you to die!")
        die()
    elif ch == "egg laggon" or ch == "egg" or ch == "laggon":
        printSlow("You reach Egg Laggon but do not see the dragon.")
        lookWithSword()
    else:
        printSlow("Not So sure what you meant")
        navigateAfterSupplies()


def lookWithSword():
    printSlow("Do you wanna look for the dragon?")
    ch = input("").lower()
    if ch == "yes":
        printSlow(
            "You waited till night time and kill the dragon. Looks like the Troll was wrong! You needed the sword during the night!")
        winHeckYa()
    elif ch == "":
        printSlow(
            "You find the dragon without the sword, during the day, but the troll was wrong about the sword, the dragon kills you!.")
        die()
    else:
        printSlow("Not So sure what you meant")
        lookWithSword()


def hole():
    printSlow("There is a hole in the ground. Do you want want to go inside?")
    ch = input("").lower()
    if ch == "yes" or ch == "y" or ch == "yep" or ch == "yea" or ch == "yeah" or ch == "duh" or ch == "ofc":
        printSlow("You go in the hole and die.")
        die()
    elif ch == "nah":
        printSlow("Smart Boi/Gal")
        findDrag()
    else:
        printSlow("Not So sure what you meant")
        sample()


def findDrag():
    printSlow("You reach Egg Lagoon, but do not see the dragon. Find the dragon?")
    ch = input("").lower()
    if ch == "yup":
        printSlow(
            "You find the dragon without the sword, during the day, but the troll was wrong about the sword, so you kill the dragon.")
        winHeckYa()
    elif ch == "nah":
        printSlow(
            "You waited till night time and the dragon kills you. Looks like the Troll was wrong! You needed the sword during the night!")
        die()
    else:
        printSlow("Not So sure what you meant")
        findDrag()


def die():
    printSlow("Congratulations! You died!")


def winHeckYa():
    printSlow("Congratulations! You won the game and killed the dragon!")


def printSlow(text):
    curses.setupterm()
    charLeft = curses.tigetnum('cols')
    listOfWords = text.split(' ')
    for word in listOfWords:
        if len(word) >= charLeft:
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


start()  # sdjg;sgds;yhjhaertghjkjhgdsfjklkjghtgddwsfedgrhtfjygkjlk,jhng


def sample():
    printSlow("")
    ch = input("").lower()
    if ch == "":
        printSlow("")
        #
    elif ch == "":
        printSlow("")
        #
    else:
        printSlow("Not So sure what you meant")
        sample()
