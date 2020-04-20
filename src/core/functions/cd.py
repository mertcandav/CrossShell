# Imports.
from pathlib import *

class func_cd:
    @staticmethod
    def process(path: str,cmd: str):
        pth = Path(path)
        if(cmd == ".."): # Go parent directory
            if len(pth.parents) == 0:
                return path
                pass
            else:
                return pth.parent
                pass
            pass
        pass

    pass