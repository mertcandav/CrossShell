# Imports.
import os
import shutil
from pathlib import *
from core.terminal.terminal import *
from framework.cli import *

class func_cd:
    @staticmethod
    def process(path: str, cmd: str) -> str:
        pth = Path(path)
        if cmd == "":
            cprintln(WHITE,path)
            return path
            pass
        
        seperator = os.path.sep
        pth = pth.joinpath(cmd)
        pthstr = pth.__str__()
        if (os.path.isfile(pthstr) == True) | (os.path.exists(pthstr) == False):
            cprintln(RED,"There is no directory with this name!")
            return path
            pass
        parts = pthstr.split(seperator)
        pth = Path(parts[0] + seperator)
        for element in parts:
            if element == "..":
                pth = pth.parent
                continue
                pass
            pth = pth.joinpath(element + seperator)
            pass
        pthstr = pth.__str__()
        return pthstr
        pass

    pass
