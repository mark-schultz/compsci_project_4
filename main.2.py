from room import Room, Forest
from player import Player
from item import Key, Spellbook, Book, Container, Consumable, Item
from monster import Monster, LootTable
from enter import enter, clear, num
from menu import Menu
from magic import Magic, spelllist
from quest import Quest
import npc
import os
import updater
import random

player = Player()
recipelist=[]
def createWorld():
#ROOMS
    r1 = Room("Entrance Hall", "You are in the Entrance Hall.", False)
    r2 = Room("Great Hall", "You are in the Great Hall.", False)
    r3 = Room("Trophy Room", "You are in trophy room.", False)
    r4 = Room("Entrance Courtyard", "You are in the Entrance Courtyard.", False)
    r5 = Room("Boat House", "You are in the boat house.", True)
    r6 = Room("Dungeon", "You are in the dungeon.", True)
    r7 = Room("Moving Staircase (Level 1)", "You are by the moving staircase (level 1).", False)
    r8 = Room("Moving Staircase (Level 2)", "You are by the moving staircase (level 2).", False)
    r9 = Room("Moving Staircase (Level 3)", "You are by the moving staircase (level 3).", False)
    r10 = Room("Moving Staircase (Level 4)", "You are by the moving staircase (level 4).", False)
    r11 = Room("Moving Staircase (Level 5)", "You are by the moving staircase (level 5).", False)
    r12 = Room("Moving Staircase (Level 6)", "You are by the moving staircase (level 6).", False)
    r13 = Room("Defense Against the Dark Arts Classroom", "You are in the Defense Against the Dark Arts classroom.", False)
    r14 = Room("Umbridge's Office", "You are in Umbridge's office.", True)
    r15 = Room("Hospital Wing", "You are in the hospital wing.", False)
    r16 = Room("Clock Tower", "You are in the clock tower.", False)
    r17 = Room("Clock Tower Courtyard", "You are in the clock tower courtyard.", False)
    r18 = Room("Stone Circle", "You are in the stone circle.", False)
    r19 = Room("Hagrid's Hut", "You are in Hagrid's hut.", True)
    r20 = Room("Dark Forest", "You are in the Dark Forest.", False)
    r21 = Room("Owlery", "You are in the owlery.", False)
    r22 = Room("Prefect's Bathroom", "You are in the prefect's bathroom.", False)
    r23 = Room("Room of Rewards", "You are in the Room of Rewards.", False)
    r24 = Room("Divination Classroom", "You are in the Divination classroom.", False)
    r25 = Room("Room of Requirement", "You are in the Room of Requirement.", True)
    r26 = Room("Stone Bridge", "You are on the stone bridge.", False)
    r27 = Room("Library", "You are in the library.", False)
    r28 = Room("Transfiguration Courtyard", "You are in the transfiguration courtyard.", False)
    r29 = Room("Greenhouse", "You are in the greenhouse.", False)
    r30 = Room("Myrtle's Bathroom", "You are in Myrtle's bathroom. I won't ask you why.", False)
    r31 = Room("Charms Classroom", "You are in the Charms classroom.", False)
    r32 = Room("Viaduct", "You are on the viaduct.", False)
    r33 = Room("Entrance to the Viaduct", "You are at the entrance the viaduct.", False)
    r34 = Room("Potions Classroom", "You are in the Potions classroom.", False)
    r35 = Room("Gryffindor Common Room", "You are in the Gryffindor Common Room.", False)
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
    Room.connectRooms(r26, "north", r28, "south")
    Room.connectRooms(r28, "north", r29, "south")
    Room.connectRooms(r8, "north", r27, "south")
    Room.connectRooms(r8, "south", r30, "north")
    Room.connectRooms(r8, "west", r31, "east")
    Room.connectRooms(r4, "east", r32, "west")
    Room.connectRooms(r32, "east", r33, "west")
    Room.connectRooms(r33, "downstairs", r34, "upstairs")
    Room.connectRooms(r12, "east", r35, "west")
    autogenerateForest(r19)
#ITEMS
    i = Item("Rock", "This is just a rock.", 10)
    i2 = Key("Magic Key", "This is a single-use key that can unlock most doors.", 1)
    i3 = Item("Coin", "This is money.", 0)
    i4 = Spellbook("Stupefy",2,10, 1)
    i5 = Container("Box" , False)
    i6 = Item("Squill Bulb", "An ingrediant for Felix Felicis",0)
    i7 = Item("Squill Seed", "This can grow into a Squill Bulb",0)
    i8 = Item("Bucket of Water", "This looks wet!", 2)
    i9 = Item("Pail of Dirt", "Looks dirty͡°).",2)
    i10= Container("Locked Box", True,"Box")
    i11= Consumable("Potion of Healing and Mana restore","This kind of does everything",1,10,5)
    i12= Consumable("Raw Meat","... I guess you could eat this?",1, 4, 0)
#NPCS
    n1 = npc.Hermione("Hermione")
    n2 = npc.Librarian("Librarian")
#MONSTERS
    l1=LootTable()
    l1.addItem(i3,.5,6)
    l1.addItem(i,.3,1)
    l1.addItem(i12,1,1)
    c=Monster("Bob the Monster", 20, r1,5,l1)
#RECIPES
    makeRecipe("Squill Bulb", [i7,i8,i9,i6])
#PLACEMENT
    for elephant in range(4):
        player.items.append(i3)
    i.putInRoom(r2, 2)
    i2.putInRoom(r1, 3)
    i.putInRoom(r1,10)
    #i4.putInRoom(r1,1)
    n1.putInRoom(r1)
    n2.putInRoom(r27)
    i5.putInRoom(r29, 1)
    player.location = r1
    i8.putInRoom(r30,1)
    i9.putInRoom(r28,1)
    i5.addItem(i7,1)
    i10.putInRoom(r1,1)
    i10.addItem(i3,10)
    i11.putInRoom(r1,1)
    i4.putInRoom(r1,1)
def makeRecipe(name, listOfItems):
    recipelist.append(listOfItems)
def autogenerateForest(room):   #Room is the object corresponding to Hagrid's hut
    center=Forest("Edge of the Forest","You are at the edge of the Forest.",[0,0])
    roomsToGen=20
    forestlist=[]
    pointslist=[]
    pointer=[0,0]
    forestlist.append(center)
    pointslist.append(pointer)
    for i in range(roomsToGen):
        directionchose=False
        while not directionchose:
            testdir=checkDirection(pointslist,pointer)
            if testdir!=[]:
                direction=random.choice(testdir)
                directionchose=True
            else:
                pointer=random.choice(pointslist)
        pointer[0]+=direction[0]
        pointer[1]+=direction[1]
        distance=(pointer[0]**2+pointer[1]**2)**(1/2)
        if distance>8:
            forestlist.append(Forest("Deep Forest","You are in the center of the Forest.",pointer))
        elif distance>5:
            forestlist.append(Forest("Forest","You are in the Forest.",pointer))
        else:
            forestlist.append(Forest("Meadow","You are in a small meadow near the Forest.",pointer))
    connectedlist=[]
    for j in forestlist:
        jlocation=j.getLocation()
        for k in forestlist:
            if [j,k] in connectedlist:
                break
            elif [k,j] in connectedlist:
                break
            klocation=k.getLocation()
            if jlocation[0]-klocation[0]==0:
                if jlocation[1]-klocation[1]==1:
                    Room.connectRooms(j, "south", k, "north")
                elif jlocation[1]-klocation[1]==-1:
                    Room.connectRooms(j, "north", k, "south")
            elif jlocation[1]-klocation[1]==0:
                if jlocation[0]-klocation[0]==1:
                    Room.connectRooms(j, "east", k, "west")
                elif jlocation[0]-klocation[0]==-1:
                    Room.connectRooms(j, "west", k, "east")
    Room.connectRooms(room,"to the forest",center,"to hagrid's hut")
def checkDirection(pointslist,pointer):
    safedirections=[]
    temppointer=pointer[:]
    temppointer[0]+=1
    if temppointer not in pointslist:
        safedirections.append([1,0])
    temppointer=pointer[:]
    temppointer[0]-=1
    if temppointer not in pointslist:
        safedirections.append([-1,0])
    temppointer=pointer[:]
    temppointer[1]+=1
    if temppointer not in pointslist:
        safedirections.append([0,1])
    temppointer=pointer[:]
    temppointer[1]-=1
    if temppointer not in pointslist:
        safedirections.append([0,-1])
    return safedirections
def getRecipe(name):
    for i in recipelist:
        if name.lower()==i[-1].name.lower():
            return i
    print("Can't craft that item!")
    return False
def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasNPCs():
        print("This room has the following NPCs:")
        for n in player.location.npcs:
            print(n.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        player.location.showItems()
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def go(string):
    if string.lower() not in player.location.exitNames():
        print("Invalid direction.")
        enter()
        return [False,False]
    else:
        if player.location.getDestination(string).lock == False: #if room is unlocked
            player.goDirection(string) 
            return [True,True]
        else: #if room is locked
            print(player.location.getDestination(string).name + " is locked.")
            unlock=False
            for i in range(len(player.items)):
                if player.items[i].key==True:
                    temp=input("Unlock with a key? ")
                    if temp.lower()=="yes":
                        unlock=True
                        player.use( player.items[i], player.location.getDestination(string).name)
                    else:
                        unlock=False
                    break
            if unlock==True:
                return go(string)
            else:
                return [False,False]
def inventory(string):
    player.showInventory()
    return [True,False]
def pickup(string):
    temp=string[:]
    temp2=temp.split()
    if "up"==temp2[0]:
        string=string[3:]
    else:
        pass
    targetName=string
    target = player.location.getItemByName(targetName)
    if target != False:
        if player.location.items.count(target) == 1:
            player.pickup(target,1)
            commandSuccess = True
        else:
            try:
                quantity = int(input("How many? "))
                player.pickup(target, quantity)
                commandSuccess = True
            except ValueError:
                print("Not a valid number.")
                enter()
                commandSuccess = False
    else:
        print("No such item.")
        enter()
        commandSuccess = False
    return [commandSuccess, False]     
def use(string,itemtarget=None):      #Itemtarget - the door to use a key on
    targetName = string
    target = player.getItemByName(targetName)
    if target in player.items:
        player.use(target,itemtarget)
        return [True,False]
    else:
        print("Cannot use.")
        enter()
        return [False,False]
def craft(string):
    x = getRecipe(string)
    if x:
        player.craftRecipe(x)
        return [True, False]
    else:
        print("Can't craft.")
        enter()
        return [False, False]
def status(string):
    player.showStatus()
    return [True,False]
def talkto(string):
    if string[1]=="o":
        targetName = string[3:]
    else:
        targetName=string
    target = player.location.getNPCByName(targetName)
    if target in player.location.npcs:
        gift = player.talkto(target)
        enter()
        if gift:
            player.items.append(gift)
        else:
            pass
        return [True,False]
    else:
        print("Can't talk.")
        enter()
    return [False, False]
def attack(string):
    targetName = string
    target = player.location.getMonsterByName(targetName)
    if target != False:
        player.attackMonster(target)
        return [True,True]
    else:
        print("No such monster.")
        enter()
        return [False,False]
def read(string):
    target = player.getItemByName(string)
    if target in player.items:
        player.read(target)
        return [True, False]
    else:
        print("Can't read.")
        enter()
        return [False, False]
def inspect(string):
    target = player.location.getItemByName(string)
    if target in player.location.items:
        x = target.describe() #list of item objects
        if target.container: #if inspecting a container
            if target.lock==True:
                query=input("The "+target.name+" is locked.  Use a key to unlock it?")
                if query.lower()=="yes":
                    for i in player.items:
                        if target.unlock(i):
                            player.items.remove(i)
                    if target.lock==True:
                        print("You have no keys!")
                        enter()
                        return [True,False]
                    else:
                        print(target.name+" is unlocked now!")
                        enter()
                        return [True, True]
                else:
                    return [True, False]
            else:
                totalWeight = 0
                for i in x:
                    totalWeight += i.weight
                query=input("Type an item name to pick up an item, or 'all' to attempt to pick up all of them. ")
                if query.lower()=="all":    
                    if player.getWeight()+totalWeight<=player.invmaxsize:
                        for i in x:
                            player.items.append(i)
                            target.removeItem(i)
                    else:
                        print("Not enough space in your inventory.")
                elif query.lower()!="":
                    itemdict=target.listItems()
                    inTheBox=False
                    for i in x:
                        if query.lower()==i.name.lower():
                            inTheBox=True
                            if i.weight+player.getWeight()<=player.invmaxsize:
                                if itemdict[i.name]==1:
                                    query=1
                                else:
                                    try:
                                        query=int(input("How many? "))
                                    except ValueError:
                                        print("That was not an integer")
                                        break
                                if query<=0:
                                    break
                                elif query>itemdict[i.name]:
                                    query=itemdict[i.name]
                                    print("Not that many items in the container! Attempting to add "+str(query)+".")
                                elif query==1:
                                    target.removeItem(i)
                                    player.items.append(i)
                                else:
                                    freeweight=player.invmaxsize-player.getWeight()
                                    toAdd=query
                                    if toAdd*i.weight>freeweight:
                                        toAdd=freeweight//i.weight
                                    while toAdd>0:
                                        target.removeItem(i)
                                        player.items.append(i)
                                        toAdd-=1
                            break
                    if inTheBox==False:
                        print("Not in the container.")
                elif query.lower()=="no" or query.lower()=="":
                    return [True,False]
        return [True,False]
    else:
        print("Can't inspect.")
        enter()
        return [False,False]
def drop(string):
    targetName = string
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
                enter()
                commandSuccess = False
    else:
        print("No such item.")
        enter()
        commandSuccess = False
    return [commandSuccess, False]
def quests(string):
    print()
    Quest.showCurrentQuests()
    print()
    return [True,False]
def wait(string):
    return [True,True]
def exit(string):
    return ["E","ND"]
    
MainMenu=Menu()     #(self,displayname,commandname,outputfunc,helpdescription,expectedinput)
MainMenu.addMenuOption("go","go",go,"moves you in the given direction", "direction","g")
MainMenu.addMenuOption("exit","exit",exit,"ends the game", None,"ex")
MainMenu.addMenuOption("inventory","inventory",inventory,"opens your inventory",None,"i")
MainMenu.addMenuOption("pick up","pick", pickup, "picks up the item","item","p",)
MainMenu.addMenuOption("talk to", "talk", talkto, "talks to the npc", "npc","t")
MainMenu.addMenuOption("use","use",use,"uses the item", "item","u")
MainMenu.addMenuOption("status","status",status, "checks health and mana levels",None,"s")
MainMenu.addMenuOption("attack","attack",attack, "attacks a monster","monster name","a")
MainMenu.addMenuOption("drop","drop",drop, "drops an item(s)", "item","d")
MainMenu.addMenuOption("inspect","inspect",inspect,"inspects an item","item","ex")
MainMenu.addMenuOption("read", "read", read, "reads a book", "book", "r")
MainMenu.addMenuOption("quests", "quests", quests, "views current quests", None,"q")
MainMenu.addMenuOption("wait", "wait", wait, "waits a round", None, "w")
MainMenu.addMenuOption("craft", "craft", craft, "crafts an item", "item", "c")
MainMenu.addMenuOption("spell list","spell",spelllist,"lists currently known spells",None,"sl")
createWorld()
playing = True
situation=[False,False] #[Command Success, timePasses]

while playing and player.alive:
    printSituation()
    situation=[False,False]
    while not situation[0]:
        situation=[True,False]
        situation=MainMenu.runMenu()
        if situation == ["DEA","TH"]:
            print("Oh dear, you are dead!")
            player.alive=False
            situation=[True,True]
        elif situation[0] == "E" and situation[1] == "ND":
            print("Thanks for playing!")
            playing = False
            situation=[True,True]
        elif situation[1] == True:
            updater.updateAll()