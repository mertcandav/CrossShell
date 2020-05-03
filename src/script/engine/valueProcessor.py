# Imports.
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
            if part.startwith("&") == True:
                
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
