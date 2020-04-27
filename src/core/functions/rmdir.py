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

class func_rmdir:
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
                "rmdir:\n"
                "   -help: Show help of module. This parameter can only be used alone.\n"
                "   -rgx: Use regular expressions.\n"
                "   -tree: Include child items."
            )
            return
            pass
        
        cmd = paramProcessor.getNonParam(cmd)
        cmd = Eng_string.process(cmd)
        if cmd == ERROR:
            return
            pass

        msg = ""
        regex = False
        tree = False
        print(params.__len__().__str__())
        for element in params:
            if element.startswith("rgx"):
                regex = True
                continue
                pass
            if element.startswith("tree"):
                tree = True
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
                    
                    if tree:
                        shutil.rmtree(_dir)
                        pass
                    else:
                        os.rmdir(_dir)
                        pass
                    pass
                pass
            else:
                if tree:
                    shutil.rmtree(cmd)
                    pass
                else:
                    os.rmdir(cmd)
                    pass
                pass
            return
            pass

        pass

    pass
