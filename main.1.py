from room import Room, Forest, forestrooms, rooms
from player import Player
from item import Key, Spellbook, Book, Container, Consumable, Item
from monster import Monster, LootTable, monsterlist
from enter import enter, clear, num
from menu import Menu
from magic import Magic, spelllist
import quest
import npc
import os
import updater
import random

player = Player()
recipelist=[]

def createWorld(firstgenerate=True):
    ### ITEMS ###
    i = Item("Rock", "This is just a rock.", 10)
    i2 = Key("Magic Key", "This is a single-use key that can unlock most doors.", 1)
    i3 = Item("Coin", "This is money.", 0)
    i4 = Spellbook("Stupefy",2,15, 1)
    i5 = Container("Seed Box" , False)
    i6 = Item("Squill Bulb", "This is an ingredient for Felix Felicis.",0)
    i7 = Item("Squill Seed", "This can grow into a squill bulb.",0)
    i8 = Item("Bucket of Water", "Looks wet!", 2)
    i9 = Item("Pail of Dirt", "Looks dirty.", 2)
    i10= Container("Locked Box", True,"Box")
    i11= Consumable("Potion of Healing and Mana restore","This kind of does everything. +10 Health +5 Mana",1,10,5)
    i12= Consumable("Raw Meat","... I guess you could eat this? +4 Health",1, 4, 0)
    i13= Item("Werewolf Hide", "Maybe this does something?", 0)
    i14= Consumable("Small Health Potion","A small potion. +10 Health",1,10,0)
    i15= Container("Box", False)
    i16= Consumable("Chocolate Frogs", "Looks tasty! +15 Health",1,15,0)
    i17= Consumable("Butterbeer", "Nothing better than a cold butterbeer. +5 Mana",1,0,5)
    i18 = Container("Desk", False)
    i19 = Item("Occamy Eggshell", "This is an ingredient for Felix Felicis.", 0)
    i20= Consumable("Health Potion", "A health potion.  +25 Health",1,25,0)
    i21= Spellbook("Hex",2,20,1)
    i22= Consumable("Mana Potion", "A mana potion.  +5 Mana",1,0,5)
    i23= Item("Vial of Water", "Use to craft potions!",1)
    i24= Item("Rat Tail","Use (with a vial of water) to craft a health potion.",1)
    i25 = Item("Gillyweed", "Yummy.", 1)
    i26= Item("Pixie Dust","Use (with a vial of water) to craft a mana potion.",1)
    i27 = Item("Murtlap Tentacle", "This is an ingredient for Felix Felicis.", 0)
    b2 = Book("Crafting Common Items", "An introductory course in crafting.",["Rat Tail + Vial of Water = Health potion","Pixie dust + Vial of Water = Mana potion"],1)
    i28 = Item("Powdered Common Rue", "This is an ingredient for Felix Felicis.",0)
    t1 = Item("Tincture of Thyme", "This is an ingredient for Felix Felicis.", 0)
    i29 = Item("Felix Felicis", "A luck potion.",0)
    i30 = Item("Unicorn Blood", "Don't drink it.", 1)
    i31 = Container("Trophy Case",False)
    i32 = Item("Feather", "This dropped from an owl",0)
    i33 = Item("Weed", "Apparantly the Dark Forest doesn't have a gardener.",0)
    i34 = Item("Rock", "This rock looks strangly like Bob the Monster",5)
    ### LOOT TABLES ###     L1.add(item, chance, quantity), chance between 0 and 1
    # Spiders #
    L1=LootTable()
    L1.addItem(i12,.8,1)
    L1.addItem(i3,.8,12)
    L1.addItem(i2,.1,1)
    L1.addItem(i20,.6,2)
    # Werewolves #
    L2=LootTable()
    L2.addItem(i13,1,1)
    L2.addItem(i3,.9,18)
    L2.addItem(i2,.1,1)
    L2.addItem(i14,.4,2)
    L2.addItem(i20,.8,1)
    # Rats #
    L3=LootTable()
    L3.addItem(i3,.9,3)
    L3.addItem(i12,.6,1)
    L3.addItem(i14,.5,1)
    L3.addItem(i2,.1,1)
    L3.addItem(i24,1,1)
    # Pixies #
    L4=LootTable()
    L4.addItem(i21,.3,1)
    L4.addItem(i2,.1,1)
    L4.addItem(i3,.7,15)
    L4.addItem(i20,.4,2)
    L4.addItem(i22,.7,1)
    L4.addItem(i26,1,1)
    if quest.q4 in quest.questLog and not quest.q4pixies:
        L4.addItem(i25,1,1)
        quest.q4pixies=True
    # The Murtlap #
    L5=LootTable()
    L5.addItem(i2,.1,1)
    L5.addItem(i3,1,20)
    L5.addItem(i20,.8,2)
    L5.addItem(i27,1,1)
    ### MONSTERS ###     #Monster(name, health, damage, loottable), moveTo(room) also adds to room
    M1=Monster("Giant Spider",20,8,L1)
    M2=Monster("Werewolf",30,5,L2)
    M3=Monster("Rat",15,3,L3)
    M4=Monster("Pixie",12,10,L4)
    M5=Monster("Murtlap",25,10,L5)
    if firstgenerate == True: #create the map only once, else run update functions
        ### ROOMS ###
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
        r14 = Room("Umbridge's Office", "You are in Umbridge's office. You hope Umbridge doesn't find you here.", True)
        r15 = Room("Hospital Wing", "You are in the hospital wing.", False)
        r16 = Room("Clock Tower", "You are in the clock tower.", False)
        r17 = Room("Clock Tower Courtyard", "You are in the clock tower courtyard.", False)
        r18 = Room("Stone Circle", "You are in the stone circle. Creepy.", False)
        r19 = Room("Hagrid's Hut", "You are in Hagrid's hut.", False)
        r20 = autogenerateForest(r19)
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
        r36 = Room("Water", "You are in the water!", True)
        ### CONNECT ROOMS ###
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
        Room.connectRooms(r5, "into the water", r36, "out of the water")
        ### NPCS ###
        n1 = npc.Hermione("Hermione", {})
        n2 = npc.Librarian("Librarian", {})
        n3 = npc.Centaur("Centaur", {})
        n4 = npc.Hagrid("Hagrid", {})
        n5 = npc.Ron("Ron", {"Coin":50})
        n6 = npc.HoodedCreature("Hooded Creature",{"Unicorn Blood":1})
        n7 = npc.Luna("Luna", {})
        n8 = npc.Umbridge("Umbridge", {})
        n9 = npc.Harry("Harry", {})
        ### RECIPES ###
        makeRecipe("Squill Bulb", [i7,i8,i9,i6])
        makeRecipe("Health Potion",[i23,i24,i20])
        makeRecipe("Mana Potion",[i23,i26,i22])
        makeRecipe("Felix Felicis",[i27,i28,i19,i6,t1,i29])
        ### PLACEMENT OF ITEMS, NPCS, PLAYER ###
        player.location = r1
        i16.putInRoom(r2, 2)
        i17.putInRoom(r2,1)
        i2.putInRoom(r1,1)
        n1.putInRoom(r1)
        n2.putInRoom(r27)
        i5.putInRoom(r29, 1)
        b2.putInRoom(r34,1)
        b2.putInRoom(r27,1)
        i8.putInRoom(r30,1)
        i8.putInRoom(r34,1)
        i8.putInRoom(r22,1)
        i9.putInRoom(r28,1)
        i5.addItem(i7,1)
        i4.putInRoom(r31,1)
        n4.putInRoom(r19)
        i18.putInRoom(r14, 1)
        n5.putInRoom(r35)
        i28.putInRoom(r34,1)
        n7.putInRoom(r16)
        n9.putInRoom(r25)
        i32.putInRoom(r21,random.randint(0,8))
        classlist=[r13,r23,r24,r27,r28,r31,r34] #possible rooms to put containers
        containerlist=[]
        for i in classlist: #put containers in rooms randomly
            if random.random()<.8:
                containerlist.append(Container("Box", False))
                containerlist[-1].putInRoom(i,1)
        keysleft=5 #up to five keys in all containers
        for i in containerlist: #put items in containers randomly
            quantity=int(15*random.random())    #Number of coins to put in container
            i.addItem(i3,quantity)
            if keysleft>0:  #If we haven't given out 5 keys yet, potentially put 1 in the container
                quantity=int(2*random.random()-.001)
                i.addItem(i2,quantity)
                keysleft-=1
            if random.random()<.7:      #Other items to maybe add to containers randomly
                i.addItem(i14,1)
            if random.random()<.4:
                i.addItem(i23,1)
        for i in forestrooms:       #Adding certain items to rooms i the forest randomly ("Rocks" and "Weeds")
            if random.random()<.1:
                i33.putInRoom(i,1)
            if random.random()<.1:
                i34.putInRoom(i,random.randint(1,2))
    ### THINGS THAT GET UPDATED ###
    else:
        if time.getCount()%5==0:        #Spawns monsters in the forest periodically
            count=0
            for i in monsterlist:
                if i.room in forestrooms:
                    count+=1
            if count<10:
                templist=[]
                if random.random()<.5:
                    templist.append(Monster("Giant Spider",20,8,L1))
                else:
                    templist.append(Monster("Werewolf",30,5,L2))
                templist[0].moveTo(random.choice(forestrooms))
        if time.getCount()%10==0:       #Spawns monsters in the castle periodically
            searching=True
            while searching:
                i=random.choice(rooms)
                if i not in forestrooms:
                    target=i
                    break
            templist=[]
            ratcounter=0
            pixiecounter=0
            murtlap=False
            for i in monsterlist:
                if i.name.lower()=="rat":
                    ratcounter+=1
                elif i.name.lower()=="pixie":
                    pixiecounter+=1
                elif i.name.lower()=="murtlap":
                    murtlap=True
            if random.random()<.8 and ratcounter<20:
                templist.append(Monster("Rat",15,3,L3))
            elif pixiecounter<5:
                templist.append(Monster("Pixie",12,10,L4))
            if templist!=[]:
                templist[-1].moveTo(target)
            if not murtlap:
                templist.append(Monster("Murtlap",25,10,L5))
                templist[-1].moveTo(Room.getRoomByName("Water"))
        #unicorn blood appears in the Dark Forest only when you need it for quest 6.
        if quest.q6.stepNum==2 and quest.q6unicornblood==False:
            for i in forestrooms:
                if i.name.lower()=="dark forest":
                    templist=[]
                    templist.append(Item("Unicorn Blood", "Don't drink it.", 1))
                    templist[0].putInRoom(i,1)
                    quest.q6unicornblood=True    
                    break
        #the occamy eggshell appears in in Umbridge's office only when you need it for quest 3.
        if quest.q3.active and not quest.q3occamyegg:
            target=Room.getRoomByName("Umbridge's Office")
            container=target.getItemByName("Desk")
            container.addItem(i19,1)
            quest.q3occamyegg=True
        #gillyweed appears in the prefect's bathroom only when you need it for quest 5.
        if quest.q5.active and not quest.q5gillyweed:
            target=Room.getRoomByName("Prefect's Bathroom")
            i25.putInRoom(target, 1)
            quest.q5gillyweed=True
        #If Umbridge is in the same room as you, she sends you to the Gryffindor Common Room.
        umbridge=player.location.getNPCByName("Umbridge")
        if umbridge!=False:
            player.location=Room.getRoomByName("Gryffindor Common Room")
            print("Umbridge sends you back to your commmon room.  You're not entirely sure why.")
            enter()
            umbridge.remove()
        #Umbridge removes Hagrid from school grounds after quest 5.
        if quest.q5 in quest.questLog:
            for i in rooms:
                hagrid=False
                hagrid=i.getNPCByName("Hagrid")
                if hagrid!=False:
                    i.removeNPC(hagrid)
                    break
def makeRecipe(name, listOfItems):
    recipelist.append(listOfItems)
def autogenerateForest(room):   #Room is the object corresponding to Hagrid's hut
    center=Forest("Edge of the Forest","You can see the path to Hagrid's Hut.",[0,0])
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
        forestlist.append(Forest("Dark Forest","You are in the  Forest.",pointer[:]))
        pointslist.append(pointer[:])
    connectedlist=[]
    for j in forestlist:
        jlocation=j.getLocation()
        for k in forestlist:
            if [j,k] in connectedlist:
                break
            elif [k,j] in connectedlist:
                break
            elif k==j:
                break
            klocation=k.getLocation()
            if jlocation[0]-klocation[0]==0:
                if jlocation[1]-klocation[1]==1:
                    Room.connectRooms(j, "south", k, "north")
                    connectedlist.append([j,k])
                elif jlocation[1]-klocation[1]==-1:
                    Room.connectRooms(j, "north", k, "south")
                    connectedlist.append([j,k])
            elif jlocation[1]-klocation[1]==0:
                if jlocation[0]-klocation[0]==1:
                    Room.connectRooms(j, "east", k, "west")
                    connectedlist.append([j,k])
                elif jlocation[0]-klocation[0]==-1:
                    Room.connectRooms(j, "west", k, "east")
                    connectedlist.append([j,k])
    Room.connectRooms(room,"to the forest",center,"to hagrid's hut")
    forestlist.sort(key=lambda x: x.distance)     #Sorts the forestlist based on distance from Hagrid's Hut
    count=1
    for i in forestlist:                        #Partitions the forest list based on distance from Hagrid's hut
        if count<len(forestlist)//3:
            i.name="Edge of Forest"
            i.desc="You are at the edge of the Dark Forest."
        elif count<2*len(forestlist)//3:
            i.name="Dark Forest"
            i.desc="You are in the Dark Forest."
        else:
            i.name="Center of Forest"
            i.desc="You are in the center of the Dark Forest."
        count+=1
    forestlist[0].desc="You can see the path to Hagrid's Hut."
    forestlist[0].name="Center"
    centaurlist=[]
    for i in forestlist:
        if random.random()<.2:      #Puts centaurs in 1 in 5 rooms
            centaurlist.append(npc.Centaur("Centaur", {}))
            centaurlist[-1].putInRoom(i)
    temp=[]
    temp.append(npc.HoodedCreature("Hooded Creature",{"Unicorn Blood":1}))
    temp[0].putInRoom(forestlist[-1])
    return forestlist[-1]
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
    
### FUNCTIONS PLAYER CALLS WITH COMMANDS DETAILED IN MENU SYSTEM BELOW ###

def go(string):
    if string.lower() not in player.location.exitNames():
        print("Invalid direction.")
        enter()
        return [False,False]
    else:
        if player.location.getDestination(string).lock == False: #if room is unlocked
            player.goDirection(string)
            #full health when entering the hospital
            if player.location.name == "Hospital Wing":
                if player.health != player.maxhealth:
                    player.health=player.maxhealth    
                    print("You get the nurse to heal your wounds.")
            #full mana when entering the trophy room
            if player.location.name == "Trophy Room":
                print("Seeing all these past Hogwarts legends really lifts your spirits.")
                print("Your health and mana fully restore.")
                if player.boost==False:
                    print()
                    print("You notice something in one of the trophy cases.")
                    temp=Container("Trophy Case",False)
                    temp.putInRoom(player.location,1)
                    temp.addItem(Key("Magic Key", "This is a single-use key that can unlock most doors.", 1),1)
                    temp.addItem(Item("Coin", "This is money.", 0),20)
                    player.boost=True
                enter()
            #related to q2, step 2
            if player.location.name == "Greenhouse" and quest.q2.active:
                if quest.q2step2finished == False:
                    quest.q2step2finished = True
                    quest.q2.nextStep()
            #related to q3, step 2
            if player.location.name == "Umbridge's Office" and quest.q3.active:
                if quest.q3step2finished == False:
                    quest.q3step2finished = True
                    quest.q3.nextStep()
            #related to q3, step 1
            if player.location.name == "Potions Classroom" and quest.q7.active:
                if quest.q7step1finished == False:
                    quest.q7step1finished = True
                    quest.q7.nextStep()
            return [True,True]
        #related to q5, step 3. Can enter the water only when player has gillyweed.
        gw = player.getItemByName("Gillyweed")
        if gw and string.lower() == "into the water":
            player.items.remove(gw)
            player.goDirection(string)
            return [True, True]
        elif not gw and string.lower() == "into the water":
            print("Probably not a good idea.")
            enter()
            return [False, False]
        else: #if room is locked
            print(player.location.getDestination(string).name + " is locked.")
            unlock=False
            for i in range(len(player.items)):
                if player.items[i].key==True:
                    temp=input("Unlock with a key? ")
                    if temp.lower()=="yes":
                        unlock=True
                        player.use(player.items[i], player.location.getDestination(string).name)
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
    #related to q2, step 1
    if quest.q2step1finished == False:
        water = player.getItemByName("Bucket of Water")
        dirt = player.getItemByName("Pail of Dirt")
        if water and dirt:
            quest.q2.nextStep()
            quest.q2step1finished = True
    #related to q3, step 3
    if quest.q3step3finished == False:
        eggshell = player.getItemByName("Occamy Eggshell")
        if eggshell:
            quest.q3step3finished = True
            quest.q3.endQuest()
            quest.q4.startQuest()
    #related to q5, step 2
    if quest.q5step2finished == False:
        gillyweed = player.getItemByName("Gillyweed")
        if gillyweed:
            quest.q5.nextStep()
            quest.q5step2finished = True
    #related to q6, step 3
    if quest.q6step3finished == False:
        unicornblood = player.getItemByName("Unicorn Blood")
        if unicornblood:
            quest.q6step3finished = True
            quest.q6.nextStep()
    return [commandSuccess, False]     
def use(string,itemtarget=None): #itemtarget - the door to use a key on
    targetName = string
    target = player.getItemByName(targetName)
    if target == False:
        print("Can't find that item.")
        return [False,False]
    elif target.book==True:
        return read(string)
    elif target in player.items:
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
        #if crafting Felix, end game
        if quest.endgame:
            return victory()
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
def trade(string):
    if string[3] == "h":
        targetName = string[5:]
    else:
        targetName = string
    target = player.location.getNPCByName(targetName)
    if target in player.location.npcs:
        player.tradewith(target)
        enter()
        return [True,False]
    else:
        print("Can't trade.")
        enter()
    return [False, False]
def attack(string):
    targetName = string
    target = player.location.getMonsterByName(targetName)
    if target != False:
        if player.attackMonster(target)=="run":
            player.location=player.location.randomNeighbor()
            print("You escape to an adjacant room.  That was close!")
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
                        while len(x)>0:                     #Using a for loop was causing issues, as we're modifying the size of the list within this loop
                            #related to q2, step 3
                            if x[0].name == "Squill Seed" and quest.q2step3finished == False:
                                quest.q2step3finished = True
                                quest.q2.nextStep()
                            #related to q3, step 3
                            if x[0].name == "Occamy Eggshell" and quest.q3step3finished == False:
                                quest.q3step3finished = True
                                quest.q3.endQuest()
                                quest.q4.startQuest()
                            #related to q5, step 3
                            if x[0].name == "Murtlap Tentacle" and quest.q5step3finished == False:
                                quest.q5step3finished = True
                                quest.q5.endQuest()
                                quest.q6.startQuest()
                                clear()
                                print("Oh no! Umbridge removes Hagrid from school grounds! Looks like you'll have to ask someone else about ashwinder eggs.")
                                print()
                                enter()
                            player.items.append(x[0])
                            x[0].loc = player
                            x.remove(x[0])
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
                                        print("Invalid input.")
                                        break
                                if query<=0:
                                    break
                                elif query>itemdict[i.name]:
                                    query=itemdict[i.name]
                                    print("Not that many items in the container! Attempting to add "+str(query)+".")
                                elif query==1:
                                    if i.name == "Squill Seed" and quest.q2step3finished == False:
                                        quest.q2step3finished = True
                                        quest.q2.nextStep()
                                    if i.name == "Occamy Eggshell" and quest.q3step3finished == False:
                                        quest.q3step3finished = True
                                        quest.q3.endQuest()
                                        quest.q4.startQuest()
                                    if i.name == "Murtlap Tentacle" and quest.q5step3finished == False:
                                        quest.q5step3finished = True
                                        quest.q5.endQuest()
                                        quest.q6.startQuest()
                                    target.removeItem(i)
                                    player.items.append(i)
                                else:
                                    freeweight=player.invmaxsize-player.getWeight()
                                    toAdd=query
                                    if toAdd*i.weight>freeweight:
                                        toAdd=freeweight//i.weight
                                    while toAdd>0:
                                        if i.name == "Squill Seed" and quest.q2step3finished == False:
                                            quest.q2step3finished = True
                                            quest.q2.nextStep()
                                        if i.name == "Occamy Eggshell" and quest.q3step3finished == False:
                                            quest.q3step3finished = True
                                            quest.q3.endQuest()
                                            quest.q4.startQuest()
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
            except ValueError:
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
    quest.Quest.showCurrentQuests()
    print()
    return [True,False]
def wait(string):
    if string!="":    
        try:
            times=int(string)-1
            for i in range(times):
                updater.updateAll()
                createWorld(True)
            print("You waited "+str(times+1)+"turns.")
        except ValueError:
            print("Invalid number!")
        finally:
            enter()
    return [True,True]

### BEGINNING AND END OF GAME ###

class Voldemort(Exception):
    pass
def exit(string):
    raise Voldemort("Voldemort took over your game. Oh well.")
def startingMessage():
    clear()
    print("Potions today was interesting - you learned about Felix Felicis,")
    print("or 'liquid luck'.  You've always been sort of clumsy, but this would change that.")
    print("This would change everything.  People would look up to Neville Longbottom.")
    print("It's supposed to be terribly difficult to make though.")
    print()
    enter()
    print()
    print("You wonder if Hermione could help.")
    print()
    enter()
def victory():
    clear()
    print("You wait six months for it to brew.")
    print()
    enter()
    print("You wait.")
    print()
    enter()
    print("And wait.")
    print()
    enter()
    print("And wait.")
    print()
    enter()
    print("Yay! It's done.")
    print()
    enter()
    print("You take a sip.")
    print()
    enter()
    print("Feeling lucky?")
    print()
    enter()
    exit("END")
    
### MENU SYSTEM ###

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
MainMenu.addMenuOption("inspect","inspect",inspect,"inspects an object (item or container)","object","ins")
MainMenu.addMenuOption("read", "read", read, "reads a book", "book", "r")
MainMenu.addMenuOption("quests", "quests", quests, "views current quests", None,"q")
MainMenu.addMenuOption("wait", "wait", wait, "waits a round", "number", "w")
MainMenu.addMenuOption("craft", "craft", craft, "crafts an item", "item", "c")
MainMenu.addMenuOption("spell list","spell",spelllist,"lists currently known spells",None,"sl")
MainMenu.addMenuOption("trade with", "trade", trade, "trades with an npc", "npc", "tr")

### WORLD CREATION AND UPDATE ###

createWorld()
playing = True
situation=[False,False] #[Command Success, timePasses]
time=updater.Count()
startingMessage()
while playing and player.alive:
    printSituation()
    situation=[False,False]
    while not situation[0]:
        situation=[True,False]
        situation=MainMenu.runMenu()
        if situation[0] == "E" and situation[1] == "ND":
            print("Thanks for playing!")
            playing = False
            situation=[True,True]
        if player.health<=0:
            player.alive=False
            situation[0]=True
        elif situation[1] == True:
            updater.updateAll()
            createWorld(False)
    if not player.alive:
        commandSuccess = False
        while commandSuccess == False:
            answer = input("Oh dear, you are dead! Respawn in the hospital wing? ")
            if answer.lower() == "yes":
                player.alive = True
                player.health = player.maxhealth
                player.location = Room.getRoomByName("Hospital Wing")
                commandSuccess = True
            elif answer.lower() == "no":
                exit()
                commandSuccess = True
            else:
                print()
                print("Invalid input.")
                print()
                commandSuccess = False