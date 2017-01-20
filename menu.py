from enter import clear, num, enter, numcheck
from updater import updateAll
class Menu:
    def __init__(self):
        self.itemsperpage=10
        self.commandlist=[]
        self.displaylist=[]
        self.outputlist=[]
        self.helplist=[]
        self.abbrevlist=[]
        self.expectedinput=[]             #Used to put the <direction> in the help menu "Go <direction> -- Goes in that direction."
    def addMenuOption(self,displayname,commandname,outputfunc,helpdescription,expectedinput,abbreviation=None):      #Name as a string, OutputFunc as a func that acts on strings (go("north"), etc), HelpDescrip as a string
        self.commandlist.append(commandname)                                           #Note - string passed to output func is already string.lower(), so using .lower() again unnecessary
        self.outputlist.append(outputfunc)
        self.displaylist.append(displayname)                                    #expectedinput - don't write it with < Stuff >, just as a string "stuff"
        self.helplist.append(helpdescription)
        self.abbrevlist.append(abbreviation)
        if expectedinput==None:
            self.expectedinput.append(expectedinput)
        else:
            self.expectedinput.append("<"+expectedinput+">")
        return True
    def removeMenuOption(self,displayname):                                    #name as a string
        indextodelete=False
        for i in len(self.displaylist):
            if name.lower()==displaylist[i].lower():
                indextodelete=i
                break
        if indextodelete!=False:
            del commandlist[indextodelete]
            del outputlist[indextodelete]
            del helplist[indextodelete]
            del expectedinput[indextodelete]
            del displaylist[indextodelete]
            del abbrevlist[indextodelete]
            return True                             #Returns true if it could delete successfully
        else:
            return False                            #False if the item wasn't on the commandlist
    def runHelp(self,string):
        clear()
        page=1
        length=len(self.helplist)
        if string=="":
            page = 1
        elif not numcheck(string):
            print("Invalid page number, displaying page 1")
            page=1
        elif int(num(string))==num(string):
            if num(string)<1:
                page=1
                print("Invalid page number, displaying page 1")
            else:
                page=num(string)
        if not numcheck(string) and page!=1:
            print("Invalid page number, displaying page 1")
            page=1
        elif page>len(self.helplist)//self.itemsperpage+1:
            print("Page out of range, displaying page 1")
            page=1
        for i in range((page-1)*self.itemsperpage,min(page*self.itemsperpage,len(self.helplist))):
            if self.expectedinput[i]==None:
                expected=""
            else:
                expected=" "+self.expectedinput[i]
            if self.abbrevlist[i]==None:
                abbrev=""
            else:
                abbrev="("+self.abbrevlist[i]+")"
            print(self.displaylist[i]+abbrev+expected+" -- "+self.helplist[i])
        pagecount=int(len(self.helplist)/self.itemsperpage)-len(self.helplist)/self.itemsperpage
        if pagecount!=0:
            pagecount=1
        pagecount+=len(self.helplist)//self.itemsperpage
        print("Page "+str(page)+" of "+str(pagecount))
        enter()
        return [False,False]
    def runMenu(self):
        command=input("What would you like to do? ")
        commandSplit=command.split()
        if commandSplit==[]:
            return [False,False]
        index=len(commandSplit[0])          #To allow "Command" - "string that's multiple words".  Before it has to be 1 word
        argument=command[index+1:]
        commandWords=[commandSplit[0]]+[argument]     #Breaks command up into ["First word", "Rest of command"]
        if commandWords[0].lower()=="help":
            self.runHelp(commandWords[1])
            return [True,False]
        else:
            for i in range(len(self.commandlist)):
                if commandWords[0].lower() == self.commandlist[i].lower() or commandWords[0].lower() == self.abbrevlist[i].lower():   #cannot handle multi-word directions (MAY BE ABLE TO NOW)
                    return self.outputlist[i](commandWords[1].lower())       #outputlist - list of functions that take strings as arguments, i.e. go("north")
        print("Not a valid command.")
        return [False,False]