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
        # Read code.
        code = fs.readAllText(path, "utf-8")
        
        # Prepare the code.
        code = codeProcessor.clearComments(code)

        variables = []
        commands = codeProcessor.getCommands(code)

        

        pass

    pass
