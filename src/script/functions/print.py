# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_print:
    @staticmethod
    def process(variables: list, content: str) -> None:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        if funcProcessor.getParams(content).__len__() > 1:
            werr(scriptRuntimeErrors, "More parameters have been sent to the function than you can take!", 3)
            return ERROR
            pass

        val = valueProcessor.process(variables, content)
        if val == ERROR:
            return ERROR
            pass
        
        print(val)
        pass

    pass
