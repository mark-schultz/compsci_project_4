from room import Room
from player import Player
from item import Item
from item import Key
from monster import Monster
from enter import enter, showStatus
import os
import updater

player = Player()

def createWorld():
    r1 = Room("Entrance Hall", "You are in the Entrance Hall.", False)
    r2 = Room("Great Hall", "You are in the Great Hall.", False)
    r3 = Room("Trophy Room", "You are in trophy room.", False)
    r4 = Room("Entrance Courtyard", "You are in the Entrance Courtyard.", False)
    r5 = Room("Boat House", "You are in the boat house.", True)
    r6 = Room("Dungeons", "You are in the dungeons.", True)
    r7 = Room("Moving Staircase (Level 1)", "You are by the moving staircase (Level 1).", False)
    r8 = Room("Moving Staircase (Level 2)", "You are by the moving staircase (Level 2).", False)
    r9 = Room("Moving Staircase (Level 3)", "You are by the moving staircase (Level 3).", False)
    r10 = Room("Moving Staircase (Level 4)", "You are by the moving staircase (Level 4).", False)
    r11 = Room("Moving Staircase (Level 5)", "You are by the moving staircase (Level 5).", False)
    r12 = Room("Moving Staircase (Level 6)", "You are by the moving staircase (Level 6).", False)
    r13 = Room("Defense Against the Dark Arts Classroom", "You are in the Defense Against the Dark Arts classroom.", False)
    r14 = Room("Umbridge's Office", "You are in Umbridge's office.", True)
    r15 = Room("Hospital Wing", "You are in the hospital wing.", False)
    r16 = Room("Clock Tower", "You are in the clock tower.", False)
    r17 = Room("Clock Tower Courtyard", "You are in the clock tower courtyard.", False)
    r18 = Room("Stone Circle", "You are in the stone circle.", False)
    r19 = Room("Hagrid's Hut", "You are in Hagrid's hut.", True)
    r20 = Room("Dark Forest", "You are in the Dark Forest.", False)
    r21 = Room("Owlery", "You are in the Owlery.", False)
    r22 = Room("Prefect's Bathroom", "You are in the prefect's bathroom.", False)
    r23 = Room("Room of Rewards", "You are in the Room of Rewards.", False)
    r24 = Room("Divination Classroom", "You are in the Divination classroom.", False)
    r25 = Room("Room of Requirement", "You are in the Room of Requirement.", True)
    r26 = Room("Stone Bridge", "You are on the Stone Bridge.", False)
    r27 = Room("Library", "You are in the library.", False)
    Room.connectRooms(r1, "west", r2, "east")
    Room.connectRooms(r2, "south", r3, "north")
    Room.connectRooms(r1, "east", r4, "west")
    Room.connectRooms(r4, "south", r5, "north")
    Room.connectRooms(r1, "north", r7, "south")
    Room.connectRooms(r7, "downstairs", r6, "upstairs")
    Room.connectRooms(r7, "upstairs", r8, "downstairs")
    Room.connectRooms(r8, "upstairs", r9, "downstairs")
    Room.connectRooms(r9, "upstairs", r10, "downstairs")
    Room.connectRooms(r10, "upstairs", r11, "downstairs")
    Room.connectRooms(r11, "upstairs", r12, "downstairs")
    Room.connectRooms(r8, "east", r13, "west")
    Room.connectRooms(r13, "upstairs", r14, "downstairs")
    Room.connectRooms(r9, "south", r15, "north")
    Room.connectRooms(r15, "west", r16, "east")
    Room.connectRooms(r16, "west", r17, "east")
    Room.connectRooms(r17, "west", r18, "east")
    Room.connectRooms(r18, "south", r19, "north")
    Room.connectRooms(r19, "west", r20, "east")
    Room.connectRooms(r18, "north", r21, "south")
    Room.connectRooms(r10, "west", r22, "east")
    Room.connectRooms(r11, "west", r23, "east")
    Room.connectRooms(r12, "west", r24, "east")
    Room.connectRooms(r12, "north", r25, "south")
    Room.connectRooms(r7, "north", r26, "south")
    i = Item("Rock", "This is just a rock.")
    i2 = Key("Magic Key", "This is a single-use key that can unlock most doors.")
    i.putInRoom(r2, 2)
    i2.putInRoom(r1, 3)
    player.location = r1
    c=Monster("Bob the monster", 20, r2)
    c.money=5

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        player.location.showItems()
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("use <item> -- uses the item")
    print("status -- checks health and mana levels")
    print("attack <monster name> -- Attacks a monster")
    print()
    enter()

createWorld()
playing = True
while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()
        if commandWords == []:
            pass
        elif commandWords[0].lower() == "go":   #cannot handle multi-word directions
            if commandWords[1].lower() not in player.location.exitNames():
                print("Invalid direction.")
                enter()
                commandSuccess = False
            else:
                if player.location.getDestination(commandWords[1]).lock == False: #if room is unlocked
                    player.goDirection(commandWords[1]) 
                    timePasses = True
                else: #if room is locked
                    print(player.location.getDestination(commandWords[1]).name + " is locked.")
                    commandSuccess = False
        elif commandWords[0].lower() == "pick" and commandWords[1].lower() == "up":  #can handle multi-word objects
            targetName = command[8:]
            target = player.location.getItemByName(targetName)
            if target != False:
                if player.location.items.count(target) == 1:
                    player.pickup(target)
                    commandSuccess = True
                else:
                    try:
                        quantity = int(input("How many? "))
                        player.pickup(target, quantity)
                        commandSuccess = True
                    except ValueError:
                        print("Not a valid number.")
                        commandSuccess = False
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "drop":
            targetName = command[5:]
            target = player.getItemByName(targetName)
            if target != False:
                if player.items.count(target) == 1:
                    player.drop(target, 1)
                    commandSuccess = True
                else:
                    try:
                        quantity = int(input("How many? "))
                        player.drop(target, quantity)
                        commandSuccess = True
                    except:
                        print("Not a valid number.")
                        commandSuccess = False
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "use":
            targetName = command[4:]
            target = player.getItemByName(targetName)
            if target in player.items:
                player.use(target)
                commandSuccess = True
            else:
                print("Cannot use.")
                commandSuccess = False
        elif commandWords[0].lower() == "status":
            showStatus()
        elif commandWords[0].lower() == "inventory":
            player.showInventory()       
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:]
            target = player.location.getItemByName(targetName)
            if target in player.location.items:
                print(target.desc)
                enter()
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False
        else:
            print("Not a valid command.")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()

    


