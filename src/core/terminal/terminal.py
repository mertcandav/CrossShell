# Imports.
from core.CrossShell import *
from core.terminal.CS_SHELL import *
from framework.cli import *

class terminal:
    # Fields.
    CurrentPath = ""
    SysShell = "$"
    Shell = CS_SHELL()

    def __init__(self, currentPath):
        self.CurrentPath = currentPath
        self.Shell.term = self
        pass

    # Set current path.
    def setPath(self,path: str):
        self.CurrentPath = path
        pass

    # Start input loop.
    def startLoop(self) -> str:
        self.Shell.Update()
        self.Shell.cmdloop()
        pass

    # Process one command.
    def onecmd(self, cmd: str) -> None:
        self.Shell.Update()
        print(f"{self.Shell.prompt}{cmd}")
        self.Shell.onecmd(cmd)
        pass

    pass
