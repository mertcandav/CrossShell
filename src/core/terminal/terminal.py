# Imports.
from core.CrossShell import *
from core.terminal.CS_SHELL import *
from framework.cli import *

class terminal:
    # Fields.
    CurrentPath = ""
    SysShell = ""
    Shell = CS_SHELL()

    def __init__(self, currentPath):
        self.CurrentPath = currentPath
        self.Shell.term = self
        pass

    # Set current path.
    def setPath(self,path: str):
        self.CurrentPath = path
        pass

    # Get input.
    def startLoop(self) -> str:
        self.Shell.prompt = CYAN + self.CurrentPath + f">" + RED + self.SysShell + " " + RESET
        self.Shell.cmdloop()
        pass

    pass
