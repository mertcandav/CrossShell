# Imports.
import os
import re
from core.CrossShell import *
from script.engine.codeProcessor import *
from framework.cli import *
from framework.fs import *

class scripter:
    @staticmethod
    def interpret(path: str) -> None:
        code = fs.readAllText(path, "utf-8")
        
        code = codeProcessor.clearComments(code)
        print(code)
        return
        variables = []
        pass

    pass
