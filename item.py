import os
import quest
from room import Room
from enter import enter
import magic
import updater

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
class Item:
    def __init__(self, name, desc, weight):
        self.weight=weight
        self.name = name
        self.desc = desc
        self.loc = None
        self.key=False      #All these attributes allow us to pick the right function by calling just "use(item)" function in main
        self.container=False
        self.food=False
        self.spellbook=False
        self.book=False
    def describe(self):
        print()
        print(self.desc)
        print()
        enter()
    def putInRoom(self, room, quantity):
        self.loc = room
        for i in range(quantity):
            room.addItem(self)
    def function(self,optional=None):
        print("Cannot use.")
        enter()

class Key(Item): #universal, one-time-use key
    def __init__(self,name,desc,weight):
        Item.__init__(self,name,desc,weight)
        self.key=True       #Allows the "use" function in main to know it's a key
    def function(self,targetName=None):
        if targetName==None:
            targetName = input("What do you want to unlock? ").lower()  #gets the name of the room to unlock from the player
        target = Room.getRoomByName(targetName)     #Changes from a string associated with the room to the room object itself
        nextTo = target in self.loc.location.getExits() #can unlock only nearby room
        if target and nextTo:
            if target.lock:
                target.lock = False
                print("You've unlocked " + target.name + ".")
                return True
            elif not target.lock:
                print("Already unlocked.")
                enter()
            else:
                print("Cannot unlock.")
                enter()
        elif target and not nextTo:
            print("You're too far away from your target.")
            enter()
        else:
            print("Cannot unlock.")
            enter()

class Spellbook(Item):
    def __init__(self,spellname,manacost,damage,weight):
        super().__init__(spellname,None,weight)
        self.desc="A spellbook for "+spellname.lower()+"."
        self.manacost=manacost
        self.damage=damage
        self.spellbook=True
    def function(self,optional=None):             #Add way to actually learn spell
        for i in range(len(magic.spells)):          #Checks if you already know it
            if magic.spells[i].name==self.name:
                return False
        magic.Magic(self.name,self.manacost,self.damage)    #If not, you learn it
        print("You learn the spell "+"\""+str(self.name)+"\".")
        enter()
        return True

class Book(Item):
    def __init__(self, name, desc, text, weight): #text is a list
        super().__init__(name, desc, weight)
        self.text = text
        self.read = False
        self.book=True
    def displayText(self):
        for line in self.text:
            print(line)
        if self.read == False:
            quest.q1.endQuest()
            quest.q2.startQuest()
            self.read = True
        enter()

class Consumable(Item): #potion-type things
    def __init__(self, name, desc, weight, Addhealth, Addmana):
        super().__init__(name, desc, weight)
        self.addhealth=Addhealth
        self.addmana=Addmana
        self.food=True
    def function(self,optional=None):
        return [self.addhealth,self.addmana] #returns the health and mana to add (can't access the player object here without circular importing or major code changes, so we did this)

class Container(Item): #containers are just items you can't pick up (so they're stored in rooms the same way).  
    def __init__(self, name,locked=False,NameWhenUnlocked=None):
        Item.__init__(self,name,None,200)
        self.lock=locked
        self.items=[]
        self.loc = None
        self.container=True
        self.unlockedname=NameWhenUnlocked
    def addItem(self,item,quantity):
        for i in range(quantity):
            self.items.append(item)
            item.loc = self
    def listItems(self):
        itemsCount = {}
        for i in self.items:
            if i.name not in itemsCount:
                itemsCount[i.name] = 1
            else:
                itemsCount[i.name] +=1
        for n in itemsCount:
            print(n + " (" + str(itemsCount[n]) + ")")
        return itemsCount
    def removeItem(self,item):
        self.items.remove(item)
        item.loc = None
    def describe(self):
        if self.lock==False:
            print("Contents:")
            print()
            self.listItems()
            print()
            return self.items
        else:
            return []
    def unlock(self,key):
        if self.lock==False:
            pass
        else:
            if key.key==True:
                self.lock=False
                self.name=self.unlockedname
                return True
            else:
                return False
        return False

class Corpse(Container):
    def __init__(self,name):
        super().__init__(name)
        updater.register(self)
        self.timeleft=10
    def update(self): #corpses disappear after a while
        self.timeleft-=1
        if self.timeleft<0 or self.items==[]:
            updater.deregister(self)
            self.loc.removeItem(self)

### ITEMS GIVEN BY NPCS ###

# BOOK OF POTIONS
b1 = Book("Book of Potions", "Need a cure for boils?", ["FELIX FELICIS", "Effects: A period of luck in all endeavors.", "Ingredients:", "1 ashwinder egg", "1 squill bulb", "1 murtlap tentacle", "tincture of thyme", "1 occamy eggshell", "powdered common rue"], 5)

# TINCTURE OF THYME
t1 = Item("Tincture of Thyme", "This is an ingredient for Felix Felicis.", 0)

# ASHWINDER EGG
a1 = Item("Ashwinder Egg", "This is an ingredient for Felix Felicis.", 0)

# CENTAUR'S POTION
P1 = Consumable("Centaur's potion", "What a light potion. Heals 10 health.", 0, 10, 3)

