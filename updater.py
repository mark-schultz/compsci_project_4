
updates = []

def updateAll():
    for u in updates:
        u.update()

def register(thing):
    updates.append(thing)

def deregister(thing):
    updates.remove(thing)
    
class Count:
    def __init__(self):
        self.count=0
        register(self)
    def update(self):
        self.count+=1
    def getCount(self):
        return self.count