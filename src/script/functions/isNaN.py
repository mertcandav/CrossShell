# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_isNaN:
    @staticmethod
    def process(base, content: str) -> str:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        if funcProcessor.getParams(content).__len__() > 1:
            werr(scriptRuntimeErrors, "More parameters have been sent to the function than you can take!", 3)
            return ERROR
            pass

        val = valueProcessor.process(base, content)
        if val == ERROR:
            return ERROR
            pass

        if type(val) == str:
            if val.isdigit():
                return 1
                pass
            return 0
            pass
        if type(val) == int:
            return 1
            pass

        return 0
        pass
    pass
