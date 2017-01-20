import os
import updater
import magic
import menu
import quest
from item import Item, Key, Spellbook, Book, t1, a1
from enter import enter

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.invmaxsize=30
        self.location = None
        self.items = []
        self.maxhealth=50
        self.health = self.maxhealth
        self.alive = True
        self.maxmana = 5                 #Starting max mana size
        self.mana = self.maxmana
        self.healthcounter = 0
        self.manacounter = 0
        self.healthperiod = 1
        self.manaperiod = 3
        updater.register(self)
        self.boost=False
    def getWeight(self): #for display in inventory
        total=0
        for i in self.items:
            total+=i.weight
        return total
    def craftRecipe(self,recipe):
        itemslist=self.items[:]
        missinglist=[] #display what items, if any, are missing when crafting a recipe
        for n in recipe[:-1]:
            if n in itemslist:
                itemslist.remove(n)
            else:
                missinglist.append(n)
        if len(missinglist)>0:
            print("You're missing:")
            for i in missinglist:
                print(i.name)
            enter()
        else:
            for i in recipe[:-1]:
                self.items.remove(i)
            self.items.append(recipe[-1])
            #related to q2, step 4
            if recipe[-1].name == "Squill Bulb":
                quest.q2.endQuest()
                quest.q3.startQuest()
            #related to end game
            if recipe[-1].name == "Felix Felicis":
                quest.endgame = True
            print("You just got a "+recipe[-1].name+"!")
            enter()
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)
    def pickup(self, item, quantity): #considers max carrying capacity
        if item.container==True:
            print("You can't pick that up!")
            enter()
        else:
            if self.invmaxsize>self.getWeight():
                if self.getWeight()+quantity*item.weight<=self.invmaxsize:
                    pass #if we can fit the items, don't modify quantity
                elif self.getWeight()+quantity*item.weight>=self.invmaxsize:
                    spaceleft=self.invmaxsize-self.getWeight()
                    quantity=item.weight//spaceleft
                    print("Nearly full inventory! Picking up "+str(quantity)+" items instead.")
                    enter()
                if self.location.items.count(item) >= quantity:
                    for i in range(quantity):
                        self.items.append(item)
                        item.loc = self
                        self.location.removeItem(item)
                else:
                    print("There are only " + str(self.location.items.count(item)) + ".")
                    enter()
            else:
                print("You're carrying too many items already!")
                enter()
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def drop(self, item, quantity):
        if self.items.count(item) >= quantity:
            while quantity>0:
                for i in self.items:
                    if quantity==0:
                        break
                    elif i.name==item.name:
                        self.items.remove(i)
                        i.loc = None
                        self.location.addItem(i)
                        quantity-=1
        else:
            print("You have only " + str(self.items.count(item)) + ".")
            enter()
    def tradewith(self, target):
        itemsCount = {} #see how many of each item the player has
        for i in self.items:
            if i.name not in itemsCount:
                itemsCount[i.name] = 1
            else:
                itemsCount[i.name] += 1
        if target.tradeCondition == {}: #if npc doesn't have any trade conditions
            print("Trade conditions not met.")
        for j in target.tradeCondition: #tradeCondition is a dictionary giving item name and quantity, an NPC can make only one kind of transaction
            if j in itemsCount: #if player has item at all
                if itemsCount[j] >= target.tradeCondition[j]: #if player has enough of item
                    difference = itemsCount[j] - target.tradeCondition[j]
                    for k in range(difference):
                        self.items.remove(self.getItemByName(j))
                    #related to q4, step 3
                    if quest.q4.active and quest.q4.stepNum == 1:
                        print()
                        print("You've obtained a tincture of thyme!")
                        print()
                        quest.q4.endQuest()
                        quest.q5.startQuest()
                        self.items.append(t1)
                    #related to q6, step 4
                    elif quest.q6.active and quest.q6.stepNum == 3:
                        print()
                        print("You've obtained an ashwinder egg!")
                        print()
                        quest.q6.endQuest()
                        quest.q7.startQuest()
                        self.items.append(a1)
                    else:
                        print("Trade conditions not met.")
                else:
                    print("Trade conditions not met.")
            else:
                print("Trade conditions not met.")
    def showStatus(self,ShowEnter=True):
        print("Health: "+str(self.health)+"/"+str(self.maxhealth))
        print("Mana: "+str(self.mana)+"/"+str(self.maxmana))
        if ShowEnter:
            enter()
    def use(self, item,optional=None):
        if item.key:
            if item.function(optional):
                self.items.remove(item)
                item.loc = None
            enter()
        elif item.food:
            ls=item.function()      #ls is [Health to add, Mana to add]
            initial=[self.health,self.mana]
            self.health+=ls[0]
            self.mana+=ls[1]
            if self.health>self.maxhealth:
                self.health=self.maxhealth
            if self.mana>self.maxmana:
                self.mana=self.maxmana
            self.items.remove(item)
            print("You healed "+str(self.health-initial[0])+" health and "+str(self.mana-initial[1])+" mana.")
            enter()
        elif item.spellbook:
            if item.function(optional):
                self.items.remove(item)
            else:
                print("You already know that spell.")
                enter()
    def talkto(self, npc):
        return npc.respond()
    def read(self, book):
        if book.book==True:
            return book.displayText()
        elif book.spellbook==True:
            return book.function()
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        itemsCount = {}
        for i in self.items:
            if i.name not in itemsCount:
                itemsCount[i.name] = 1
            else:
                itemsCount[i.name] +=1
        listToPrint=[]
        weightList=[]
        maxlen=0
        for n in itemsCount:
            listToPrint.append(n + " (" + str(itemsCount[n]) + "): " + self.getItemByName(n).desc) 
            weightList.append(itemsCount[n]*self.getItemByName(n).weight)
            if len(listToPrint[-1])>maxlen:
                maxlen=len(listToPrint[-1])
        for n in range(len(listToPrint)):
            while len(listToPrint[n])<maxlen:
                listToPrint[n]=listToPrint[n]+" "
        for n in range(len(listToPrint)):
            print(listToPrint[n]+"   Total Weight:"+str(weightList[n]))
        print()
        print("Inventory Spaces: "+str(self.getWeight())+"/"+str(self.invmaxsize))
        enter()
    def attackMonster(self, mon):
        if mon.room == self.location:
            clear()
            print("You are attacking " + mon.name + ".")
            print()
            attacking=True
            maxhealth=mon.health
            while attacking:
                self.showStatus(False)
                print(mon.name + "'s health is " + str(mon.health) + "/"+str(maxhealth)+".")
                print()
                spellcast=False
                while not spellcast:
                    spellcast=False
                    temp=magic.magicMenu.runMenu() #[manacost,damage]
                    if temp==[False,False]:
                        pass
                    elif temp==["Run",False]:
                        return "run"
                    elif temp==[True,False]:
                        pass
                    else:
                        if self.mana-temp[0]>=0:
                            spellcast=True
                            self.mana-=temp[0]
                        else:
                            print("Not enough mana!")
                        spelldamage=temp[1]
                if spelldamage:
                    mon.health-=spelldamage
                    self.health-=mon.damage                   #mon.damage goes here once it's made
                if self.health<=0 or mon.health<=0:
                    attacking=False
                    if mon.health<=0:
                        mon.die()
                        print("You killed "+mon.name+"!")
                        enter()
                        return [True,True]
                    else:
                        return ["DEA","TH"]
        else:
            print("Monster not found.")
            return [False,False]
    def update(self):                           #Regens mana, currently as a percent of max mana
        if self.healthcounter==0:
            self.healthcounter=self.healthperiod
            self.health+=1
            if self.health>self.maxhealth:
                self.health=self.maxhealth
        if self.manacounter==0:
            self.manacounter=self.manaperiod
            self.mana+=1
            if self.mana>self.maxmana:
                self.mana=self.maxmana
        self.healthcounter-=1
        self.manacounter-=1
    def checkNumber(number,query=False):    #If the input is a number, returns that number.
        try:                                #Otherwise returns False, or queries for another number.
            num = float(number)
            return number
        except Exception as e:
            if query==False:                #if not given the optional input, returns false
                return False
            else:                           #Queries for a number again - careful, easy to get stuck in a loop if user is being stupid.
                num=input("That wasn't a number.  Please enter a number.")
                return checkNumber(num,True)