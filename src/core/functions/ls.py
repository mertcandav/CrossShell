# Imports.
import os
from core.paramProcessor import *
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

        params = paramProcessor.getParams(cmd)
        if params == ERROR:
            return
            pass
        if params.__len__() > 1 & params.count("help") > 0:
            cprintln(RED,"The -help parameter can only be used alone!")
            return
            pass

        if cmd == "-help":
            print(
                "ls:\n"
                "   -help: Show help of module. This parameter can only be used alone.\n"
                "   -d: Show directories.\n"
                "   -f: Show files."
            )
            return
            pass

        msg = ""
        for element in params:
            if element == "d":
                alldir = os.listdir(term.CurrentPath)
                dirs = (val for val in alldir if os.path.isdir(val) == True)
                for val in dirs:
                    cprint(PURPLE,f"[DIR]")
                    cprintln(WHITE,val)
                    pass
                continue
                pass
            if element == "f":
                alldir = os.listdir(term.CurrentPath)
                dirs = (val for val in alldir if os.path.isfile(val) == True)
                for val in dirs:
                    cprint(BLUE,f"[FILE]")
                    cprintln(WHITE,val)
                    pass
                continue
                pass

            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        pass
    pass
