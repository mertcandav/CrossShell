# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from script.functions.setForeColor import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_print:
    @staticmethod
    def process(term, paths: list, functions: list, variables: list, content: str) -> None:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        params = funcProcessor.getParams(content)
        if params.__len__() > 2:
            werr(scriptRuntimeErrors, "More parameters have been sent to the function than you can take!", 3)
            return ERROR
            pass
        
        val = content
        if params.__len__() == 2:
            if scfunc_setForeColor.process(term, paths, functions, variables, params[0]) == ERROR:
                return ERROR
                pass

            val = params[1]
            pass

        val = valueProcessor.process(term, paths, functions, variables, val)
        if val == ERROR:
            return ERROR
            pass
        
        print(val)

        if params.__len__() == 2:
            scfunc_setForeColor.process(term, paths, functions, variables, "\"Default\"")
            pass

        pass

    pass
