# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_print:
    @staticmethod
    def process(variables: list, content: str) -> None:
        val = valueProcessor.process(variables, content)
        if val == ERROR:
            return ERROR
            pass
        
        print(val)
        pass

    pass
