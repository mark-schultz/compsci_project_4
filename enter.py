import os

def enter():
    input("Press enter to continue...")
    return True
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
        
def numcheck(s):
    try:
        return int(s)
    except ValueError:
        return False