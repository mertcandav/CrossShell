# Imports.
import os
import re
import shutil
from engine.paramProcessor import *
from engine.values.Eng_string import *
from core.terminal.CS_SHELL import *
from core.terminal import terminal
from core.CrossShell import *
from framework.fs import *
from framework.cli import *

class func_exec:
    @staticmethod
    def process(term: terminal, cmd: str) -> None:
        params = paramProcessor.getParams(" " + paramProcessor.removeNonParam(cmd))
        if params == ERROR:
            return
            pass

        if params.__len__() > 1 & params.count("help") > 0:
            cprintln(RED,"The -help parameter can only be used alone!")
            return
            pass

        if cmd == "-help":
            print(
                f"{CYAN}exec{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-merge{WHITE}                   Disable merging with current location."
            )
            return
            pass
        
        cmd = paramProcessor.getNonParam(cmd)

        msg = ""
        merge = True
        for element in params:
            if element.startswith("merge"):
                regex = False
                continue
                pass

            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        if (msg != ERROR):
            path = ""
            if merge == True:
                path = os.path.join(term.CurrentPath, cmd)
                pass
            else:
                path = cmd
                pass
            os.startfile(path)
            return
            pass

        pass

    pass
