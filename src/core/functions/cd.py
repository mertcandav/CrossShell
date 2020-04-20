# Imports.
from pathlib import *
import os

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
        else: # Open directory
            pth = pth.joinpath(cmd)
            if pth.is_dir() == False & os.path.exists(pth.__str__()) == False:
                print("There is no directory with this name!")
                return pth.parent
                pass
            return pth.__str__()
            pass
        pass

    pass
