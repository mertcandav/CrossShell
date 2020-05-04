# Imports.
import os
import re
from core.functions.cd import *
from core.terminal import terminal
from core.CrossShell import *
from script.engine.codeProcessor import *
from script.engine.funcProcessor import funcProcessor
from framework.cli import *
from framework.fs import *
from script.functions.input import *

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
        return
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
                if funcProcessor.isFunc(command):
                    fpresult = funcProcessor.process(variables, command)
                    if fpresult == ERROR:
                        return
                        pass
                    if fpresult != ERROR:
                        continue
                        pass

                term.onecmd(command)
                pass

            pass

        pass

    pass
