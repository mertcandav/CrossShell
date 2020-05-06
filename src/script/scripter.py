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
    def processRange(term: terminal, paths: list, functions: list, variables: list, commands: list) -> [ None, str ]:
        for command in commands:
            if command.startswith("return"):
                if command.startswith("return "):
                    val = valueProcessor.process(term, paths, functions, variables, command[7:].strip())
                    if val == ERROR:
                        return ERROR
                        pass

                    return val
                    pass

                return None
                pass
            if command.startswith(">"):
                if scripter.execScriptCommand(term, paths, command[1:]) == False:
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
                    fpresult = funcProcessor.process(term, paths, functions, variables, command)
                    if fpresult == ERROR:
                        return
                        pass
                    if fpresult != ERROR:
                        continue
                        pass
                if variableProcessor.isVariableCode(command):
                    if variableProcessor.process(term, paths, functions, variables, command) == ERROR:
                        return
                        pass

                    continue
                    pass
                if (
                    funcProcessor.isFuncCode(command) |
                    funcProcessor.isFuncDefination(command) |
                    funcProcessor.isFuncOverride(command)):
                    if funcProcessor.processCode(term, paths, functions, variables, command) == ERROR:
                        return
                        pass

                    continue
                    pass

                operatorDex = command.find("<-")
                if operatorDex != -1:
                    valuePart = command[operatorDex+2:].strip()
                    val = valueProcessor.process(term, paths, functions, variables, valuePart)
                    if val == ERROR:
                        return
                        pass

                    command = command[:operatorDex] + val
                    pass

                term.onecmd(command)
                pass

            pass

        return None
        pass

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
        functions = []
        commands = codeProcessor.getCommands(code)

        scripter.processRange(term, [ basePath, func_cd.process(path, "..") ], functions, variables, commands)
        pass

    pass
