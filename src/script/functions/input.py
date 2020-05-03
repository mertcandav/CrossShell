# Imports.
from script.objects.variable import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_input:
    @staticmethod
    def process(variables: list, val: str) -> [ str, variable ]:
        parts = val.split("<-")
        if parts.__len__() > 2:
            werr(scriptRuntimeErrors, "The 'input' command cannot be processed!", 1)
            return ERROR
            pass
        
        parts[0] = parts[0].strip()
        parts[1] = parts[1].strip()
        
        parts[1] = Eng_string.process(parts[1])
        if parts[1] == ERROR:
            removeLastLine()
            werr(scriptRuntimeErrors, "Error in value conversion by 'input' command!", 2)
            return ERROR
            pass

        var = variable(parts[0], parts[1])

        return var
        pass

    pass
