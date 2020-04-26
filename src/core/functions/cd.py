# Imports.
import os
import shutil
from pathlib import *
from core.terminal.terminal import *

class func_cd:
    @staticmethod
    def process(path: str,cmd: str):
        pth = Path(path)
        seperator = os.path.sep
        pth = pth.joinpath(cmd + seperator)
        pthstr = pth.__str__()
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
        if os.path.isdir(pthstr) == False | os.path.exists(pthstr) == False:
            cprintln(RED,"There is no directory with this name!")
            return pth.parent
            pass
        return pthstr[0:pthstr.__len__()]
        pass
    pass

    pass
