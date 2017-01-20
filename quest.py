from enter import enter
questLog = [] #list of finished quests
currentQuests = [] #list of current quests

class Quest:
    def __init__(self, name, steps, active): #steps is a list of strings
        self.name = name
        self.steps = steps
        self.stepNum = 0 #current step number
        self.currentStep = self.steps[self.stepNum]
        self.active = active #active quest or not (True or False)
    def startQuest(self):
        self.active = True
        currentQuests.append(self)
    def endQuest(self):
        self.active = False
        currentQuests.remove(self)
        questLog.append(self)
    def nextStep(self):
        self.stepNum += 1
        self.currentStep = self.steps[self.stepNum]
    def showCurrentQuests(ShowEnter=True):
        for i in currentQuests:
            j = 0
            while j < i.stepNum:
                print(i.name + " [" + str(j) + "]" + ": " + str(i.steps[j]))
                j += 1
            print(i.name + " [" + str(j) + "]" + ": " + i.currentStep)
        print()
        if ShowEnter:
            enter()

### QUESTS ###
#There are seven quests. The extra variables assigned help with step regulation in the main.py and npc.py

# QUEST 1
q1 = Quest("First Steps", ["Tell Hermione about your problem.", "Talk to the librarian.", "Read the 'Book of Potions'."], False)
q1.startQuest()

# QUEST 2
q2 = Quest("Squill Bulb", ["Obtain a bucket of water and a pail of dirt.", "Go to the greenhouse.", "Find some squill seed.", "Craft squill bulb."], False)
q2step1finished = False
q2step2finished = False
q2step3finished = False

# QUEST 3
q3 = Quest("Occamy Eggshell", ["Ask Hagrid about occamy eggs.", "Unlock Umbridge's office to see if there are any occamy eggshells lying around.", "Find some occamy eggshells."], False)
q3occamyegg=False
q3step2finished = False
q3step3finished = False

# QUEST 4
q4 = Quest("Tincture of Thyme", ["Talk to Ron about thyme tinctures.", "Obtain 50 coins and make a trade with Ron."], False)
q4pixies=False

# QUEST 5
q5 = Quest("Murtlap Tentacle", ["Ask Hermione about finding a murtlap tentacle.", "Obtain some gillyweed.", "Take a dip and obtain a murtlap tentacle."], False)
q5gillyweed=False
q5step2finished = False
q5step3finished = False
#Event: Umbridge removes Hagrid

# QUEST 6
q6 = Quest("Ashwinder Egg", ["Talk to someone who might know about ashwinder eggs.", "Find and talk to the hooded creature in the Dark Forest.", "Obtain some unicorn blood but don't kill a unicorn.", "Make a trade with the hooded creature."], False)
q6unicornblood = False
q6step3finished = False

# QUEST 7
q7 = Quest("Craft Felix Felicis", ["Find the Potions classroom.", "Find some powdered common rue and craft Felix Felicis."], False)
q7step1finished = False
endgame = False