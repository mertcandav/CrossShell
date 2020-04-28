# Imports.
import os
from engine.paramProcessor import *
from core.CrossShell import *
from core.terminal import terminal
from framework.fs import *
from framework.cli import *

class func_ls:
    @staticmethod
    def process(term: terminal, cmd: str) -> None:
        if cmd == "":
            alldir = os.listdir(term.CurrentPath)
            dirs = fs.getDirectories(term.CurrentPath)
            files = fs.getFiles(term.CurrentPath)
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
                f"{CYAN}ls{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-d{WHITE}                       Show directories.\n"
f"   {NGREEN}-f{WHITE}                       Show files."
            )
            return
            pass

        msg = ""
        for element in params:
            if element == "d":
                for val in fs.getDirectories(term.CurrentPath):
                    cprint(PURPLE,f"[DIR]")
                    cprintln(WHITE,val)
                    pass
                continue
                pass
            if element == "f":
                for val in fs.getFiles(term.CurrentPath):
                    cprint(CYAN,f"[FILE]")
                    cprintln(WHITE,val)
                    pass
                continue
                pass

            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        pass
    pass
