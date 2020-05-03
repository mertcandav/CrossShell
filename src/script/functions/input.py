# Imports.
from script.engine.valueProcessor import *
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
        
        parts[1] = valueProcessor.process(variables, parts[1])
        if parts[1] == ERROR:
            return ERROR
            pass

        if variable.exists(variables, parts[0]):
            werr(scriptRuntimeErrors, "A variable has already been defined with the same name!", 3)
            return ERROR
            pass

        _input = input(parts[1])

        var = variable(parts[0], _input)

        return var
        pass

    pass
