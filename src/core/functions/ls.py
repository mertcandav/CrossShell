# Imports.
import os
from core.CrossShell import *
from core.terminal.terminal import *

class func_ls:
    @staticmethod
    def process(term: terminal,cmd: str):
        if cmd == "":
            alldir = os.listdir(term.CurrentPath)
            dirs = (val for val in alldir if os.path.isdir(val) == True)
            files = (val for val in alldir if os.path.isfile(val) == True)
            for val in dirs:
                cprint(PURPLE,f"[DIR]")
                cprintln(WHITE,val)
                pass
            for val in files:
                cprint(BLUE,f"[FILE]")
                cprintln(WHITE,val)
                pass
            return
            pass

        pass
    pass