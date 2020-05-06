# Imports.
import re
from script.objects.variable import *
from engine.values.Eng_string import *
from engine.values.Eng_char import *
from core.CrossShell import *
from framework.cli import *

class valueProcessor:
    @staticmethod
    def process(base, cmd: str) -> str:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        parts =  re.split("(?![^{]*\})\\+", cmd, flags = re.UNICODE | re.MULTILINE)
        val = ""
        for part in parts:
            part = part.strip()
            if variable.exists(base.variables, part) == True:
                val += variable.getByName(base.variables, part).Value
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

            if funcProcessor.isFunc(part):
                fpresult = funcProcessor.process(base, part)
                if fpresult == ERROR:
                    return ERROR
                    pass
                if fpresult == None:
                    werr(scriptRuntimeErrors, "The function that does not return a value was used in the value conversion!", 1)
                    return ERROR
                    pass

                val += fpresult
                continue
                pass
            if funcProcessor.isFuncCode(part):
                fpresult = funcProcessor.processCode(base, part)
                if fpresult == ERROR:
                    return ERROR
                    pass
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
