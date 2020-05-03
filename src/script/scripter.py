# Imports.
import os
import re
from core.functions.cd import *
from core.terminal import terminal
from core.CrossShell import *
from script.engine.codeProcessor import *
from framework.cli import *
from framework.fs import *

class scripter:
    @staticmethod
    def execScriptCommand(term: terminal, cmd: str) -> bool:
        cmd = cmd.lower()
        if cmd == "break":
            return False
            pass
        pass

    @staticmethod
    def interpret(term: terminal, path: str) -> None:
        # Read code.
        code = fs.readAllText(path, "utf-8")
        
        # Prepare the code.
        code = codeProcessor.clearComments(code)

        basePath = term.CurrentPath

        term.CurrentPath = func_cd.process(path, "..")
        term.Shell.Update()

        variables = []
        commands = codeProcessor.getCommands(code)

        for command in commands:
            if command.startswith(">"):
                if scripter.execScriptCommand(term, command[1:]) == False:
                    return
                    pass
                continue
                pass
            if command.startswith("@") == True:
                term.Shell.onecmd(command[1:])
                pass
            else:
                term.onecmd(command)
                pass

            pass
        
        term.CurrentPath = basePath
        term.Shell.Update()

        pass

    pass
