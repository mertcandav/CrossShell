# Imports.
from core.CrossShell import *
from core.terminal.terminal import *
from framework.cli import *

class paramProcessor:
    @staticmethod
    def removeParams(val: str) -> str:
        dex = val.find(" -")
        if dex != -1:
            val = val[0:dex]
            pass
        return val
        pass

    @staticmethod
    def getParams(val: str) -> [str, list]:
        params = []
        while(val.find(" -") != -1):
            dex = val.find("-")
            if dex+1 == val.__len__():
                cprintln(RED,"The parameter must be defined after the parameter declaration!")
                return ERROR
                pass
            spacedex = val.find(" ",dex)
            param = ""
            if spacedex == -1:
                param = val[dex+1:]
                pass
            else:
                if dex + 1 == spacedex:
                    cprintln(RED,"Cannot space after the parameter declaration!")
                    return ERROR
                    pass
                else:
                    param = val[dex+1:spacedex]
                    pass
                pass
            
            if param in params:
                cprintln(RED,"A parameter cannot be defined more than once!")
                return ERROR
                pass
            params.append(param)
            val = val[spacedex:]
            if spacedex == -1:
                break
                pass
            pass
        return params
        pass
    pass
