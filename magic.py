from menu import Menu
from enter import enter
spells=[]

def spelllist(string=None):     #Shows currently available spells, their damage, their manacost, etc
    for i in spells:
        print(i.name+" -- "+i.desc)
    enter()
    return [False, False]
def cast(string):               #Used to pass the manacost and damage to main so the player's current mana can be modified there
    for i in spells:
        if i.name.lower()==string.lower():
            return [i.manacost,i.damage]
    return [False, False]
def run(string):        #Run defined here as the "Magic Menu" is the menu called in combat
    return ["Run", False]
class Magic:            #Cast not a method so it's compatible with Menu - it needed to be of the form func(string), so string.method()
    def __init__(self,name,manacost,damage=None):       #was proving difficult to make work with the menu class
        self.name=name
        self.manacost=manacost
        spells.append(self)
        self.damage=damage
        if damage==None:
            string="Costs "+str(manacost)+" mana."
        else:
            string="Costs "+str(manacost)+" mana to do "+str(damage)+" damage."
        self.desc=string
a=Magic("Sparks",0,4)
a=Magic("Confringo",1,8)
magicMenu=Menu()    #addMenuOption(displayname,commandname,outputfunc,helpdescription,expectedinput,abbreviation=None)
magicMenu.addMenuOption("cast","cast",cast,"casts a spell -- see spell list for options","spell","c")
magicMenu.addMenuOption("spell list","spell",spelllist,"lists currently known spells",None,"sl")
magicMenu.addMenuOption("run","run",run,"escapes into an adjacent room",None,"r")