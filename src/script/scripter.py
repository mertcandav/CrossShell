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
    def execScriptCommand(term: terminal, paths: list, cmd: str) -> bool:
        cmd = cmd.strip()
        lcmd = cmd.lower()
        if lcmd == "break":
            return False
            pass
        if lcmd == "cdbasepath":
            term.CurrentPath = paths[0]
            term.Shell.Update()
            return True
            pass
        if lcmd == "cdscriptpath":
            term.CurrentPath = paths[1]
            term.Shell.Update()
            return True
            pass
        
        werr(scriptRuntimeErrors, f"'{ORANGE}{cmd}{RED}' Script command not recognized!", 0)

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
                if scripter.execScriptCommand(term, [ basePath, func_cd.process(path, "..") ], command[1:]) == False:
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

        pass

    pass
