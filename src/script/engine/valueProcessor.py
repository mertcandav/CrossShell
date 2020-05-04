# Imports.
from script.objects.variable import *
from script.engine.listProcessor import *
from engine.values.Eng_string import *
from engine.values.Eng_char import *
from core.CrossShell import *
from framework.cli import *

class valueProcessor:
    @staticmethod
    def process(variables: list, cmd: str) -> str:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        parts = cmd.split('+')
        val = ""
        for part in parts:
            part = part.strip()
            if part.startswith("&") == True:
                if part == "&":
                    werr(scriptRuntimeErrors, "Variable is not specified!", 4)
                    return ERROR
                    pass
                if listProcessor.exists(variables, part[1:]) == False:
                    werr(scriptRuntimeErrors, "The variable tried to be reached is not defined!", 5)
                    return ERROR
                    pass
                val += lsitProcessor.getByName(variables, part[1:]).Value
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

            fpresult = funcProcessor.process(variables, part)
            if fpresult == ERROR:
                return ERROR
                pass
            if fpresult != ERROR:
                if fpresult == None:
                    werr(scriptRuntimeErrors, "The function that does not return a value was used in the value conversion!", 1)
                    return ERROR
                    pass

                val += fpresult
                continue
                pass

            werr(scriptRuntimeErrors, "Error in value conversion!", 2)
            return ERROR
            pass

        return val
        pass

    pass
