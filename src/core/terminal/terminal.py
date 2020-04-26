# Imports.
import platform
from core.CrossShell import *
from framework.cli import *

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
        if platform.system() == "Linux":
            import readline
            pass
        cprint(CYAN,self.CurrentPath + f">")
        cprint(RED,self.SysShell + " ")
        val = input("")
        return val
        pass

    pass
