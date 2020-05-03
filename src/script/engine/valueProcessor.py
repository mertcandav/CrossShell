# Imports.
from script.objects.variable import *
from engine.values.Eng_string import *
from engine.values.Eng_char import *
from core.CrossShell import *
from framework.cli import *

class valueProcessor:
    @staticmethod
    def process(variables: list, cmd: str) -> str:
        parts = cmd.split('+')
        val = ""
        for part in parts:
            part = part.strip()
            if part.startswith("&") == True:
                if part == "&":
                    werr(scriptRuntimeErrors, "Variable is not specified!", 4)
                    return ERROR
                    pass
                if variable.exists(variables, part[1:]) == False:
                    werr(scriptRuntineErrors, "The variable tried to be reached is not defined!", 5)
                    return ERROR
                    pass
                val += variable.getByName(variables, part[1:]).Value
                continue
                pass  
            if part.startswith("\"") == True:
                cval = Eng_string.process(part)
                
                if cval == ERROR:
                    return ERROR
                    pass

                val += cval
                continue
                pass
            if part.startswith("'") == True:
                cval = Eng_char.process(part)

                if cval == ERROR:
                    return ERROR
                    pass
                
                val += cval
                continue
                pass

            werr(scriptRuntimeErrors, "Error in value conversion!", 2)
            return ERROR
            pass

        return val
        pass

    pass