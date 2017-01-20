import room
import quest
import enter
import item
import updater
import random

class NPC:
    def __init__(self, name, tradeCondition): #Trade condition is a dictionary with item names as keys and integer quantities as values. The player can make a trade with an npc only if tradeCondition is met.
        self.name = name
        self.tradeCondition = tradeCondition
        self.loc = None
    def putInRoom(self, room):
        self.loc = room
        room.addNPC(self)
    def respond(self):
        print("Doesn't want to talk to you.")
    def getNPCByName(self, name):
        for i in room.Room.npcs:
            if i.name.lower() == name.lower():
                return i
        return False

#There are nine NPCs in the game. Their responses defined here, as well as the player's speaking options, mostly depend on the player's current task in a particular quest.

class Hermione(NPC):
    def respond(self):
        if quest.q1.active and quest.q1.stepNum == 0:
            print("(1) Say hi.")
            print("(2) Tell her your problem.")
            print("(3) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("What's up?")
                    print()
                    print("(1) Shrug.")
                    print("(2) Panic.")
                    commandSuccess2 = False
                    while commandSuccess2 == False:
                        print()
                        x2 = input("Choose a number. ")
                        print()
                        print("Well, I'm always here if you want to say hi! And if you need help, type 'help'. Type 'help 2' for page 2 of help.")
                        commandSuccess2 = True
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Felix Felicis? It would take six months. Are you sure?")
                    print()
                    print("(1) Yes.")
                    print("(2) Yes?")
                    commandSuccess2 = False
                    while commandSuccess2 == False:
                        print()
                        x2 = input("Choose a number. ")
                        print()
                        print("Ok. You can find the recipe in the library. If you talk to one of the librarians, you probably shouldn't say what you're using it for!")
                        commandSuccess2 = True
                    print()
                    quest.q1.nextStep()
                    commandSuccess = True
                elif x == "3":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
        elif quest.q5.active and quest.q5.stepNum == 0:
            print("(1) Say hi.")
            print("(2) Ask her about finding a murtlap tentacle.")
            print("(3) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Hi, Neville.")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("I'm not sure where they're sold. If you're going to fight a murtlap, I would suggest finding some gillyweed.")
                    print()
                    quest.q5.nextStep()
                    commandSuccess = True
                elif x == "3":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
        else:
            print("(1) Say hi.")
            print("(2) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Hi, Neville.")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    commandSuccess = False
                    
class Librarian(NPC):
    def respond(self):
        if quest.q1.active and quest.q1.stepNum == 1:
            print("(1) Ask for informaton about Felix Felicis.")
            print("(2) Ask about the restricted section.")
            print("(3) Run away.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Ah, tricky potion. I believe the 'Book of Potions' has the recipe.")
                    print()
                    print("(1) Ask for the book.")
                    print("(2) Run away.")
                    commandSuccess2 = False
                    while commandSuccess2 == False:
                        print()
                        x2 = input("Choose a number. ")
                        if x2 == "1":
                            print()
                            print("You now have the 'Book of Potions'.")
                            quest.q1.nextStep()
                            commandSuccess2 = True
                        elif x2 == "2":
                            commandSuccess2 = True
                        else:
                            print()
                            print("Not a valid number.")
                            commandSuccess2 = False
                        commandSuccess = True
                    print()
                    if x2 == "1":
                        return item.b1
                elif x == "2":
                    print()
                    print("Nope.")
                    print()
                    commandSuccess = True
                elif x == "3":
                    print()
                    print("...")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
        else:
            print("(1) Ask about the restricted section.")
            print("(2) Run away.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Nope.")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Bye?")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False

class Umbridge(NPC):
    def __init__(self,name,tradeCondition):
        super().__init__(name,{})
        updater.register(self)
        self.active=False
        self.timer=40
        self.respawntime=40
        self.loc=None
    def remove(self):
        if self.loc!=None:
            self.loc.removeNPC(self)    
        self.loc=None
        self.timer=self.respawntime
        self.active=False
        
    def update(self):
        if self.active==True:
            notarget=True
            while notarget:
                target = self.loc.randomNeighbor()
                if target.name.lower()!="hagrid's hut" and target.name.lower()!="water":
                    notarget=False
            self.loc.npcs.remove(self)
            self.putInRoom(target)
        else:
            if self.timer==0:
                self.active=True
                self.timer=self.respawntime
                while True:
                    i=random.choice(room.rooms)
                    if i not in room.forestrooms and i.name.lower()!="hagrid's hut" and i.name.lower()!="water":
                        self.putInRoom(i)
                        break
            else:
                self.timer-=1
        
class Ron(NPC):
    def respond(self):
        if quest.q4.active and quest.q4.stepNum == 0:
            print("(1) Say hi.")
            print("(2) Ask if he as a tincture of thyme.")
            print("(3) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("What are you up to?")
                    print()
                    print("(1) Say you're up to absolutely nothing.")
                    print("(2) Ask him the same question.")
                    commandSuccess2 = False
                    while commandSuccess2 == False:
                        print()
                        x2 = input("Choose a number. ")
                        if x == "1":
                            print()
                            print("I'm always up to no good.")
                            commandSuccess2 = True
                        elif x == "2":
                            print()
                            print("Gah, leave me alone.")
                            commandSuccess2 = True
                        else:
                            print()
                            print("Not a valid number.")
                            print()
                            commandSuccess2 = False
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("For 50 coins.")
                    print()
                    quest.q4.nextStep()
                    commandSuccess = True
                elif x == "3":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
        elif quest.q4.active and quest.q4.stepNum == 1:
            print("(1) Say hi.")
            print("(2) Attempt a trade.")
            print("(3) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Hi, Neville.")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Use the trade command to initiate the trade.")
                    print()
                    commandSuccess = True
                elif x == "3":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
        else:
            print("(1) Say hi.")
            print("(2) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Hi, Neville.")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False

class Hagrid(NPC):
    def respond(self):
        if quest.q3.active and quest.q3.stepNum == 0:
            print("(1) Ask for information about occamy eggs.")
            print("(2) Talk about the weather.")
            print("(3) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Occamy eggs are hard to come by. For one, occamies are very protective of their eggs! When I was in India, the bloody--")
                    print()
                    print("(1) Interrupt and ask where to find occamy eggshells.")
                    print("(2) Keep listening.")
                    commandSuccess2 = False
                    while commandSuccess2 == False:
                        print()
                        x2 = input("Choose a number. ")
                        if x2 == "1":
                            print()
                            print("Hmm. If I remember correctly, Gilderoy Lockhart used the eggshells to make a shampoo. If there were any eggshells around Hogwarts, they would probably have been up in his office. But Umbridge is there now. Don't go near her. She's bad business.")
                            print()
                            quest.q3.nextStep()
                            commandSuccess2 = True
                        elif x2 == "2":
                            print()
                            print("--creature nearly took my head off! I was lucky enough to catch a glimpse of an egg. Pure silver! Beautiful! But listen to me, Neville. Don't mess with them.")
                            print()
                            commandSuccess2 = True
                        else:
                            print()
                            print("Not a valid number.")
                            commandSuccess2 = False
                        commandSuccess = True
                elif x == "2":
                    print()
                    print("A fine day.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    commandSuccess = False
        else:
            print("(1) Talk about the weather.")
            print("(2) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("A fine day.")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Bye?")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False

class HoodedCreature(NPC):
    def respond(self):
        if quest.q6.active and quest.q6.stepNum == 1:
            print("(1) Approach cautiously.")
            print("(2) Run away.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("What do you want?")
                    print()
                    print("(1) Ask if he has an ashwinder egg.")
                    print("(2) Run away.")
                    commandSuccess2 = False
                    while commandSuccess2 == False:
                        print()
                        x2 = input("Choose a number. ")
                        if x2 == "1":
                            print()
                            print("It comes at a price. You know of unicorn's blood?")
                            print()
                            print("(1) Nod.")
                            print("(2) Run away.")
                            commandSuccess3 = False
                            while commandSuccess3 == False:
                                print()
                                x3 = input("Choose a number. ")
                                if x3 == "1":
                                    print()
                                    print("OK. Fetch some for me. It must be around here somewhere. My old bones...")
                                    print()
                                    quest.q6.nextStep()
                                    commandSuccess3 = True
                                elif x3 == "2":
                                    print()
                                    print("Hey.")
                                    print()
                                    commandSuccess3 = True
                                else:
                                    print()
                                    print("Not a valid number.")
                                    commandSuccess3 = False
                                commandSuccess2 = True
                        elif x2 == "2":
                            commandSuccess2 = True
                        else:
                            print()
                            print("Not a valid number.")
                            commandSuccess2 = False
                        commandSuccess = True
                    print()
                elif x == "2":
                    print()
                    print("...")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
        else:
            print("(1) Introduce yourself.")
            print("(2) Run away.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Leave me alone.")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("...")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
    
class Luna(NPC):
    def respond(self):
        if quest.q6.active and quest.q6.stepNum == 0:
            print("(1) Say hi.")
            print("(2) Ask if she knows anything about ashwinder eggs.")
            print("(3) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Hi!")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Ashwinder eggs are extremely rare. There was once this lovely creature I met in the forest. He seemed to be in the business of rare objects. Perhaps you could find him.")
                    print()
                    quest.q6.nextStep()
                    commandSuccess = True
                elif x == "3":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
        else:
            print("(1) Say hi.")
            print("(2) Leave.")
            commandSuccess = False
            while commandSuccess == False:
                print()
                x = input("Choose a number. ")
                if x == "1":
                    print()
                    print("Hi!")
                    print()
                    commandSuccess = True
                elif x == "2":
                    print()
                    print("Bye.")
                    print()
                    commandSuccess = True
                else:
                    print()
                    print("Not a valid number.")
                    print()
                    commandSuccess = False
                    
class Harry(NPC):
    def respond(self):
        print("(1) Ask him what he's doing.")
        print("(2) Leave.")
        commandSuccess = False
        while commandSuccess == False:
            print()
            x = input("Choose a number. ")
            if x == "1":
                print()
                print("Practicing! We can't beat the dementors if we don't practice!")
                print()
                print("(1) Say you've been practicing.")
                print("(2) Tell him to stop yelling.")
                commandSuccess2 = False
                while commandSuccess2 == False:
                    print()
                    x2 = input("Choose a number. ")
                    if x2 == "1":
                        print()
                        print("Good.")
                        print()
                        print("(1) Say you're cooking up something that will change your life forever.")
                        print("(2) Leave.")
                        commandSuccess3 = False
                        while commandSuccess3 == False:
                            print()
                            x3 = input("Choose a number. ")
                            if x3 == "1":
                                print()
                                print("Tell me about it later! MUST KEEP PRACTICING!")
                                commandSuccess3 = True
                            elif x3 == "2":
                                commandSuccess3 = True
                            else:
                                print()
                                print("Not a valid number.")
                                commandSuccess3 = False
                            commandSuccess2 = True
                    elif x2 == "2":
                        print()
                        print("Sorry.")
                        print()
                        commandSuccess2 = True
                    else:
                        print()
                        print("Not a valid number.")
                        commandSuccess2 = False
                    commandSuccess = True
                print()
            elif x == "2":
                print()
                print("Bye?")
                print()
                commandSuccess = True
            else:
                print()
                print("Not a valid number.")
                print()
                commandSuccess = False
                    
class Centaur(NPC):
    def __init__(self, name, tradeCondition):
        super().__init__(name, tradeCondition)
        self.heal=True
        self.tradeCondition = tradeCondition
    def respond(self):
        print("(1) Help, I'm lost.")
        print("(2) Help, I'm hurt.")
        print("(3) Run away.")
        commandSuccess = False
        while commandSuccess == False:
            print()
            x = input("Choose a number. ")
            if x == "1":
                print()
                room=self.loc.getLocation()
                maximum=max(abs(room[0]),abs(room[1]))
                if maximum==abs(room[0]):
                    if room[0]>0:
                        say="west"
                    else:
                        say="east"
                else:
                    if room[1]>0:
                        say="south"
                    else:
                        say="north"
                print("Hagrid's Hut is to the "+say+".")
                print()
                commandSuccess=True
            elif x == "2":
                if self.heal==True:
                    print()
                    print("Here, have my last potion.")
                    self.heal=False
                    print()
                    return item.P1
                else:
                    print()
                    print("Sorry, I have no potions left.")
                    print()
                    commandSuccess=True
            elif x == "3":
                commandSuccess=True