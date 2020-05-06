# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from script.functions.setForeColor import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_print:
    @staticmethod
    def process(base, content: str) -> None:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        params = funcProcessor.getParams(content)
        if params.__len__() > 2:
            werr(scriptRuntimeErrors, "More parameters have been sent to the function than you can take!", 3)
            return ERROR
            pass
        
        val = content
        if params.__len__() == 2:
            if scfunc_setForeColor.process(base, params[0]) == ERROR:
                return ERROR
                pass

            val = params[1]
            pass

        val = valueProcessor.process(base, val)
        if val == ERROR:
            return ERROR
            pass
        
        print(val)

        if params.__len__() == 2:
            scfunc_setForeColor.process(base, "\"Default\"")
            pass

        pass

    pass
