# Imports.
from script.engine.valueProcessor import *
from script.objects.variable import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.cli import *

class scfunc_input:
    @staticmethod
    def process(variables: list, content: str) -> str:
        val = valueProcessor.process(variables, content)
        if val == ERROR:
            return ERROR
            pass
        
        _input = input(val)

        return _input
        pass

    pass
