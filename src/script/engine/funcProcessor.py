# Imports.
from script.functions.input import *
from core.CrossShell import *
from framework.cli import *

class funcProcessor:
    @staticmethod
    def process(variables: list, cmd: str) -> str:
        dex = cmd.find("(")
        if dex == -1:
            return NO_ERROR
            pass
        if cmd.endswith(")") == False:
            werr(scriptRuntimeErrors, "The function is turned on but not turned off!", 6)
            return ERROR
            pass

        name = cmd[:dex]
        if funcs.keys().__contains__(name) == False:
            werr(scriptRuntimeErrors, "Function not recognized!", 7)
            return ERROR
            pass

        content = cmd[dex+1:]
        content = content[:content.__len__()-1]
        return funcs[name].process(variables, content)
        pass

    @staticmethod
    def check(val: str) -> str:
        if val.endswith(")") == False:
            werr(scriptRuntimeErrors, "The function is turned on but not turned off!", 6)
            return ERROR
            pass

        return NO_ERROR
        pass

    @staticmethod
    def getContent(val: str) -> str:
        return val[1:val.__len__()-1]
        pass

    pass

# Dictionaries.
funcs = {
    "input":    scfunc_input
}
