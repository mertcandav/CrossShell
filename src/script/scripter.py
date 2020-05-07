# Imports.
import os
import re
from core.functions.cd import *
from core.terminal import terminal
from core.CrossShell import *
from script.engine.codeProcessor import *
from script.engine.variableProcessor import *
from script.engine.keywordProcessor import *
from script.engine.funcProcessor import funcProcessor
from framework.cli import *
from framework.fs import *
from script.functions.input import *

class scripter:
    term = None
    basePath = None
    scriptPath = None
    functions = None
    variables = None

    @staticmethod
    def processRange(base, commands: list) -> [ None, str ]:
        for command in commands:
            kpresult = keywordProcessor.process(base, command)
            if kpresult == True:
                continue
                pass
            if kpresult == ERROR:
                return
                pass
            if command.startswith("return"):
                if command.startswith("return "):
                    val = valueProcessor.process(base, command[7:].strip())
                    if val == ERROR:
                        return ERROR
                        pass

                    return val
                    pass

                return None
                pass
            if command.startswith(">"):
                if base.execScriptCommand(command[1:]) == False:
                    return
                    pass
                continue
                pass
            if command.startswith("@") == True:
                command = command[1:]
                operatorDex = command.find("<-")
                if operatorDex != -1:
                    valuePart = command[operatorDex+2:].strip()
                    val = valueProcessor.process(base.variables, valuePart)
                    if val == ERROR:
                        return
                        pass

                    command = command[:operatorDex] + val
                    pass

                base.term.Shell.onecmd(command)
                continue
                pass
            else:
                if funcProcessor.isFunc(command):
                    fpresult = funcProcessor.process(base, command)
                    if fpresult == ERROR:
                        return
                        pass
                    if fpresult != ERROR:
                        continue
                        pass
                if variableProcessor.isVariableCode(command):
                    if variableProcessor.process(base, command) == ERROR:
                        return
                        pass

                    continue
                    pass
                if (
                    funcProcessor.isFuncCode(command) |
                    funcProcessor.isFuncDefination(command) |
                    funcProcessor.isFuncOverride(command)):
                    if funcProcessor.processCode(base, command) == ERROR:
                        return
                        pass

                    continue
                    pass

                operatorDex = command.find("<-")
                if operatorDex != -1:
                    valuePart = command[operatorDex+2:].strip()
                    val = valueProcessor.process(base, valuePart)
                    if val == ERROR:
                        return
                        pass

                    command = command[:operatorDex] + val
                    pass

                base.term.onecmd(command)
                pass

            pass

        return None
        pass

    def execScriptCommand(self, cmd: str) -> bool:
        cmd = cmd.strip()
        lcmd = cmd.lower()
        if lcmd == "break":
            return False
            pass
        if lcmd == "cdbasepath":
            self.term.CurrentPath = self.basePath
            self.term.Shell.Update()
            return True
            pass
        if lcmd == "cdscriptpath":
            self.term.CurrentPath = self.scriptPath
            self.term.Shell.Update()
            return True
            pass
        
        werr(scriptRuntimeErrors, f"'{ORANGE}{cmd}{RED}' Script command not recognized!", 0)
        return
        pass

    def interpret(self, term: terminal, path: str) -> None:
        # Read code.
        code = fs.readAllText(path, "utf-8")
        
        # Prepare the code.
        code = codeProcessor.clearComments(code)

        self.basePath = term.CurrentPath
        self.scriptPath = func_cd.process(path, "..")

        self.term = term
        term.CurrentPath = self.scriptPath
        term.Shell.Update()

        self.variables = []
        self.functions = []
        commands = codeProcessor.getCommands(code)

        scripter.processRange(self, commands)
        pass

    pass
