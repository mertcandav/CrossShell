# Imports.
import re
from core.terminal import terminal
from script.engine.codeProcessor import *
from script.objects.function import *
from script.functions.input import *
from script.functions.print import *
from script.functions.isNaN import *
from script.functions.trim import *
from script.functions.trimLeft import *
from script.functions.trimRight import *
from script.functions.lowerCase import *
from script.functions.upperCase import *
from script.functions.setForeColor import *
from script.functions.avg import *
from script.functions.concat import *
from core.CrossShell import *
from framework.cli import *

class funcProcessor:
    @staticmethod
    def process(base, cmd: str) -> str:
        # Imports.
        from script.scripter import scripter

        dex = cmd.find("(")
        if dex == -1:
            return NO_ERROR
            pass
        if cmd.endswith(")") == False:
            werr(scriptRuntimeErrors, "The function is turned on but not turned off!", 6)
            return ERROR
            pass

        name = cmd[:dex]
        if funcs.keys().__contains__(name) == False | function.exists(base.functions, name) == False:
            werr(scriptRuntimeErrors, "Function not recognized!", 7)
            return ERROR
            pass

        if funcs.keys().__contains__(name) == True:
            content = cmd[dex+1:]
            content = content[:content.__len__()-1]
            return funcs[name].process(base, content)
            pass
        else:
            return scripter.processRange(base,
                function.getByName(base.functions, name).Commands)
            pass
        pass

    @staticmethod
    def processCode(base, cmd: str) -> [ None, str ]:
        # Imports.
        from script.scripter import scripter
        
        # Define function.
        if funcProcessor.isFuncDefination(cmd) == True:
            cmd = cmd[5:]

            name = funcProcessor.getName(cmd)
            if codeProcessor.isBannedName(name) == True:
                return ERROR
                pass

            if function.exists(base.functions, name) | funcs.keys().__contains__(name):
                werr(scriptRuntimeErrors, "An attempt was made to define a function that has already been defined!", 13)
                return ERROR
                pass

            commands = funcProcessor.getBody(cmd)
            if commands == ERROR:
                return ERROR
                pass

            base.functions.append(function(name, commands))
            return
            pass
        # Run defination.
        if funcProcessor.isFuncCode(cmd) == True:
            commands = funcProcessor.getBody(cmd)
            if commands == ERROR:
                return ERROR
                pass

            return scripter.processRange(base, commands)
            pass
        # Overriding.
        if funcProcessor.isFuncOverride(cmd) == True:
            name = funcProcessor.getName(cmd)
            if funcs.keys().__contains__(name):
                werr(scriptRuntimeErrors, f"'{name}' function cannot be overrideed!", 14)
                return ERROR
                pass

            if function.exists(base.functions, name) == False:
                werr(scriptRuntimeErrors, f"Attempt to override the non-existent function!", 15)
                return ERROR
                pass

            commands = funcProcessor.getBody(cmd)
            if commands == ERROR:
                return ERROR
                pass

            base.functions[function.indexOf(base.functions, name)].Commands = commands
            pass

        pass

    @staticmethod
    def check(val: str) -> str:
        if val.endswith(")") == False:
            werr(scriptRuntimeErrors, "The function is turned on but not turned off!", 6)
            return ERROR
            pass

        return NO_ERROR
        pass

    @staticmethod
    def getContent(val: str) -> str:
        return val[1:val.__len__()-1]
        pass

    @staticmethod
    def isFunc(val: str) -> bool:
        return re.match("\\w*(\\s*)\\(.*", val, flags = re.UNICODE | re.S)
        pass

    @staticmethod
    def getParams(val: str) -> list:
        params = re.split("(?![^->{]*\}),", val)
        return params
        pass

    @staticmethod
    def isFuncCode(cmd: str) -> bool:
        return cmd.startswith("->")
        pass

    @staticmethod
    def isFuncDefination(cmd: str) -> bool:
        return cmd.startswith("func") | cmd.startswith("func\n")
        pass

    @staticmethod
    def isFuncOverride(cmd: str) -> bool:
        return re.match("(\\s*|;(\\s*))\w+(\\s*)\->.*", cmd, flags = re.UNICODE | re.S) is not None
        pass

    @staticmethod
    def getBody(val: str) -> str:
        dex = val.find("->")
        if dex == -1:
            werr(scriptRuntimeErrors, "Body error, '->' operator not found in function definition!", 5)
            return ERROR
            pass
        val = val[dex+2:].strip()
        if val.startswith("{") == False:
            werr(scriptRuntimeErrors, "The function body is turned not on!", 6)
            return ERROR
            pass
        if val.endswith("}") == False:
            werr(scriptRuntimeErrors, "The function body is turned on but not turned off!", 6)
            return ERROR
            pass

        val = val[1:]
        val = val[:val.__len__()-1]
        val = val.strip()

        commands = codeProcessor.getCommands(val)
        return commands
        pass

    @staticmethod
    def getName(val: str) -> str:
        dex = val.find("->")
        if dex != -1:
            val = val[:dex]
            pass

        val = val.strip()
        return val
        pass

    pass

# Dictionaries.
funcs = {
    "input":                scfunc_input,
    "print":                scfunc_print,
    "setForeColor":         scfunc_setForeColor,
    "isNaN":                scfunc_isNaN,
    "trim":                 scfunc_trim,
    "trimLeft":             scfunc_trimLeft,
    "trimRight":            scfunc_trimRight,
    "lowerCase":            scfunc_lowerCase,
    "upperCase":            scfunc_upperCase,
    "concat":               scfunc_concat,
    "avg":                  scfunc_avg,
}
