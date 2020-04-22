# Imports.
import sys
from core.CrossShell import *

class terminal:
    # Fields.
    CurrentPath = ""

    def __init__(self,currentPath):
        self.CurrentPath = currentPath
        pass

    # Set current path.
    def setPath(self,path: str):
        self.CurrentPath = path
        pass

    # Get input.
    def getInput(self) -> str:
        sys.stdout.write(CYAN)
        print(self.CurrentPath + ">", end = '')
        sys.stdout.write(RESET)
        val = input()
        return val
        pass

    @staticmethod
    def cprint(style,val: str):
        sys.stdout.write(style)
        print(val)
        sys.stdout.write(RESET)
        pass

    pass
