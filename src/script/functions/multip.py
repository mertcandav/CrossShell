# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_multip:
    @staticmethod
    def process(base, content: str) -> str:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        val = 1
        params = funcProcessor.getParams(content)
        for param in params:
            cval = valueProcessor.process(base, param)
            if cval == ERROR:
                return ERROR
                pass
            if type(cval) != int:
                werr(scriptRuntimeErrors, "Error in value conversion!", 2)
                return ERROR
                pass
            if val == 0:
                val = cval
                continue
                pass
            val = val * cval
            pass

        return val
        pass
    pass
