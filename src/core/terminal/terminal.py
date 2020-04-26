# Imports.
import sys
from core.CrossShell import *

class terminal:
    # Fields.
    CurrentPath = ""
    SysShell = ""

    def __init__(self,currentPath):
        self.CurrentPath = currentPath
        pass

    # Set current path.
    def setPath(self,path: str):
        self.CurrentPath = path
        pass

    # Get input.
    def getInput(self) -> str:
        cprint(CYAN,self.CurrentPath + f">")
        cprint(RED,self.SysShell + " ")
        val = input("")
        return val
        pass

    pass

# Functions.
def cprint(style,val: str):
    sys.stdout.write(style)
    print(val, end = '')
    sys.stdout.write(RESET)
    pass

def cprintln(style,val: str):
    sys.stdout.write(style)
    print(val)
    sys.stdout.write(RESET)
    pass
