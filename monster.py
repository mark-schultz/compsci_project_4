import random
import updater
import item
import player
import room

monsterlist=[] #monsters in the game

class LootTable: #items a particular type of monster can drop, along with drop rate, and quantity
    def __init__(self):
        self.loottable=[]
        self.index=0
    def addItem(self,item,chance,quantity):
        self.loottable.append([item,chance,quantity])
    def lookupItem(self,item):
        for i in self.loottable:
            if i[0]==item:
                return i[1:2]
        return [False,False]
    def listItems(self):
        print(self.loottable[0])
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==len(self.loottable):
            raise StopIteration
        self.index+=1
        return self.loottable[self.index-1]

class Monster:
    def __init__(self, name, health,damage,LootTable):
        self.name = name
        self.health = health
        self.room = None
        self.damage=damage
        self.LootTable=LootTable.loottable       #Need some way to populate this with items (maybe [item, percent chance], depends on how we want to do it)
        self.items=[]            #Maybe random amount around some range.
        for i in self.LootTable:
            item=i[0]
            lootdrop=i[1:]  #[Chance it drops, Expected quantity to drop]
            if random.random() < lootdrop[0]:
                quantity=int(lootdrop[1]*(1+random.uniform(0,.75)))
                for j in range(quantity):    
                    self.items.append(item)
    def update(self):
        if self.name.lower()=="murtlap":
            pass
        elif random.random() < .5:
            validtarget=False
            timer=10
            while not validtarget:
                target=self.room.randomNeighbor()
                timer-=1
                validtarget=target.allowmons
                if timer<0:   #Shouldn't come into play, doens't hurt to be careful though
                    break
            if validtarget==True:
                self.moveTo(target)
    def moveTo(self, room):
        if self.room==None:
            self.room=room
            room.addMonster(self)
            updater.register(self)
            monsterlist.append(self)
        else:
            self.room.removeMonster(self)
            self.room = room
            room.addMonster(self)
    def die(self):
        self.dropLoot()                 #Added loot dropping
        self.room.removeMonster(self)
        updater.deregister(self)
        monsterlist.remove(self)
    def dropLoot(self): #dead monster becomes a container which can be looted
        maxnum=0
        for i in self.room.items:
            if i.container==True:
                temp=i.name.split()
                basename=temp[0]+temp[1]
                if basename==self.name:
                    if maxnum==0:
                        maxnum=1
                    elif len(temp)==3:
                        if int(temp[2])>maxnum:
                            maxnum=int(temp[2])
        maxnum+=1
        if maxnum==1:
            string=self.name+"'s body"
        else:
            string=self.name+"'s body "+str(maxnum)
        a=item.Corpse(string)
        a.putInRoom(self.room,1)
        for j in self.items:     
            a.addItem(j,1)
