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

class func_rmtree:
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
                f"{CYAN}rmtree{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-rgx{WHITE}                     Use regular expressions."
            )
            return
            pass
        
        cmd = paramProcessor.getNonParam(cmd)

        msg = ""
        regex = False
        for element in params:
            if element.startswith("rgx"):
                regex = True
                continue
                pass

            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        if (msg != ERROR):
            if regex == True:
                dirs = fs.getDirectories(term.CurrentPath)
                dirs = (val for val in dirs if re.match(cmd, val))
                for _dir in dirs:
                    if re.match(cmd, _dir) == False:
                        continue
                        pass
                
                    shutil.rmtree(_dir)
                    pass
                pass
            else:
                path = os.path.join(term.CurrentPath, cmd)
                shutil.rmtree(path)
                pass
            return
            pass

        pass

    pass
