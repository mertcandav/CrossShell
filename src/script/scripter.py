# Imports.
import os
import re
from core.functions.cd import *
from core.terminal import terminal
from core.CrossShell import *
from script.engine.codeProcessor import *
from script.engine.variableProcessor import *
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
                command = command[1:]
                operatorDex = command.find("<-")
                if operatorDex != -1:
                    valuePart = command[operatorDex+2:].strip()
                    val = valueProcessor.process(variables, valuePart)
                    if val == ERROR:
                        return
                        pass

                    command = command[:operatorDex] + val
                    pass

                term.Shell.onecmd(command)
                continue
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
                if variableProcessor.isVariableCode(command):
                    if variableProcessor.process(variables, command) == ERROR:
                        return
                        pass

                    continue
                    pass
                
                operatorDex = command.find("<-")
                if operatorDex != -1:
                    valuePart = command[operatorDex+2:].strip()
                    val = valueProcessor.process(variables, valuePart)
                    if val == ERROR:
                        return
                        pass

                    command = command[:operatorDex] + val
                    pass

                term.onecmd(command)
                pass

            pass

        pass

    pass
