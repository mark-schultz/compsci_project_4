import random

rooms = []
forestrooms=[]      #All rooms in here randomly generated.  Lets me say "pick a room, make sure it's not a randomly generated one".
class Room:
    def __init__(self, name, description, lock):
        self.name = name
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.npcs = []
        self.lock = lock
        self.allowmons=False        #Doesn't allow monsters to enter room
        rooms.append(self)
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def exitNames(self):        #Use in printSituation - visual only
        return [x[0] for x in self.exits]
    def getExits(self):         #Returns list of exits for use in program
        return [x[1] for x in self.exits]
    def getRoomByName(name):    #allows us to go from name to the room object
        for i in rooms:
            if i.name.lower() == name.lower():
                return i
        return False
    def addItem(self, item):
        self.items.append(item)
    def addNPC(self, npc):
        self.npcs.append(npc)
    def removeItem(self, item):
        self.items.remove(item)
    def removeNPC(self, npc):
        self.npcs.remove(npc)
        npc.loc = None
    def removeAllNPCs(self):
        self.npcs = []
    def showItems(self):    #Used in print situation
        itemsCount = {}
        containerCount={}
        for i in self.items:
            if not i.container:    
                if i.name not in itemsCount:
                    itemsCount[i.name] = 1
                else:
                    itemsCount[i.name] +=1
            else:
                if i.name not in containerCount:
                    containerCount[i.name] = 1
                else:
                    containerCount[i.name] +=1
        if itemsCount != {}:
            for n in itemsCount:
                print(n + " (" + str(itemsCount[n]) + ")")
        if containerCount != {}:
            print()
            print("This room contains the following containers:")
            for n in containerCount:
                print(n)
    def addMonster(self, monster):
        self.monsters.append(monster)
    def removeMonster(self, monster):
        self.monsters.remove(monster)
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):  #goes from item name (attribute) to the object
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasNPCs(self):
        return self.npcs != []
    def getNPCByName(self, name):   #goes from NPC name to object
        for i in self.npcs:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasMonsters(self):
        return self.monsters != []
    def getMonsterByName(self, name):  #Goes from monster name to object
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def randomNeighbor(self):       #used Monster/Umbridge (specific NPC) movement
        return random.choice(self.exits)[1]
class Forest(Room):     #Special rooms that have coordinates - used to generate the forest.  Distance is used to have descriptions based on
    def __init__(self, name, description,coordinates):      #How far into the forest you are
        super().__init__(name,description,False)
        self.allowmons=True
        self.coordinates=coordinates
        self.distance=(coordinates[0]**2+coordinates[1]**2)**(1/2)
        forestrooms.append(self)
    def getLocation(self):
        return self.coordinates