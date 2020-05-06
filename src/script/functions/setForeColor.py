# Imports.
import sys
from script.engine.valueProcessor import *
from script.engine.dictProcessor import *
from engine.values.Eng_string import *
from core.CrossShell import *
from framework.drawing import *
from framework.cli import *

class scfunc_setForeColor:
    @staticmethod
    def process(base, content: str) -> None:
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

        val = val.lower()
        if val == "default":
            sys.stdout.write(RESET)
            return None
            pass

        if dictProcessor.existsKey(colors, val) == False:
            werr(scriptRuntimeErrors, "No color found!", 8)
            return ERROR
            pass

        sys.stdout.write(colors[val])

        pass

    pass
