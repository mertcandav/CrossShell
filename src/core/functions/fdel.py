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

class func_del:
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
                f"{CYAN}del{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-rgx{WHITE}                     Use regular expressions."
            )
            return
            pass

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
                cmd = paramProcessor.removeParams(cmd)
                cmd = Eng_string.process(cmd)
                if cmd == ERROR:
                    return
                    pass

                dirs = fs.getFiles(term.CurrentPath)
                dirs = (val for val in dirs if re.match(cmd, val))
                for _dir in dirs:
                    os.remove(os.path.join(term.CurrentPath, _dir))
                    pass
                pass
            else:
                cmd = paramProcessor.getNonParam(cmd)
                path = os.path.join(term.CurrentPath, cmd)
                os.remove(os.path.join(term.CurrentPath, path))
                pass
            return
            pass

        pass

    pass
