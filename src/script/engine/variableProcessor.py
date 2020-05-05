# Imports.
from script.engine.codeProcessor import *
from script.objects.variable import *
from script.engine.valueProcessor import *
from core.CrossShell import *
from framework.cli import *

class variableProcessor:
    @staticmethod
    def process(term, paths: list, functions: list, variables: list, cmd: str) -> [ str, list ]:

        parts = cmd.split("=")
        if parts.__len__() > 2:
            werr(scriptRuntimeErrors, "Error in variable definition!", 9)
            return ERROR
            pass

        parts[0] = parts[0].strip()
        parts[1] = parts[1].strip()

        if variableProcessor.isVariableDefination(parts[0]) == True:
            name = parts[0][4:].strip()
            if variable.exists(variables, name) == True:
                werr(scriptRuntimeErrors, "An attempt was made to define a variable that has already been defined!", 10)
                return ERROR
                pass

            if codeProcessor.isBannedName(name) == True:
                return ERROR
                pass

            value = valueProcessor.process(term, paths, functions, variables, parts[1])
            if value == ERROR:
                return ERROR
                pass

            variables.append(variable(name, value))
            pass
        else:
            name = parts[0]
            if variable.exists(variables, name) == False:
                werr(scriptRuntimeErrors, "The variable tried to be reached is not defined!", 5)
                return ERROR
                pass

            value = valueProcessor.process(term, paths, functions, variables, parts[1])
            if value == ERROR:
                return ERROR
                pass

            variables[variable.indexOf(variables, name)].Value = value
            pass

        pass

    @staticmethod
    def isVariableCode(cmd: str) -> bool:
        return cmd.find("=") != -1
        pass

    @staticmethod
    def isVariableDefination(cmd: str) -> bool:
        return cmd.startswith("var ")
        pass

    pass
