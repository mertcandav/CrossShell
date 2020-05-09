# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_concat:
    @staticmethod
    def process(base, content: str) -> str:
        # Imports.
        from script.engine.funcProcessor import funcProcessor

        val = ""
        for param in funcProcessor.getParams(content):
            cval = valueProcessor.process(base, param)
            if cval == ERROR:
                return ERROR
                pass
            val += cval.__str__()
            pass

        return val
        pass
    pass
