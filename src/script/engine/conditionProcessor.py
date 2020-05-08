# Imports.
import re
from script.engine.funcProcessor import *
from script.engine.valueProcessor import *
from script.engine.dictProcessor import *
from script.engine.objects.condition import *
from script.scripter import *
from core.CrossShell import *
from framework.cli import *

class conditionProcessor:
    @staticmethod
    def process(base, cmd: str) -> str:
        funcDex = cmd.find("->>")
        if funcDex == -1:
            werr(scriptRuntimeErrors, "Condition function is not defined!", 18)
            return ERROR
            pass

        condition = cmd[0:funcDex].strip()
        pcresult = conditionProcessor.processCondition(base, cmd[0:funcDex].strip())

        if pcresult == ERROR:
            return ERROR
            pass

        if pcresult == True:
            pcresult = funcProcessor.processCode(base, "->" + cmd[funcDex+3:].strip())
            if pcresult == ERROR:
                return ERROR
                pass
            pass

        return NO_ERROR
        pass

    @staticmethod
    def processCondition(base, cmd: str) -> [ str, bool ]:
        conditions = conditionProcessor.decomposeConditions(cmd)

        def getState(base, parts: list, _type: str) -> [ str, bool ]:
            parts[0] = valueProcessor.process(base, parts[0])
            if parts[0] == ERROR:
                return ERROR
                pass

            if _type == "boolean single":
                return parts[0] == 1
                pass

            parts[1] = valueProcessor.process(base, parts[1])
            if parts[1] == ERROR:
                return ERROR
                pass

            try:
                if _type == "equal":
                    return parts[0] == parts[1]
                    pass
                if _type == "not equal":
                    return parts[0] != parts[1]
                    pass
                if _type == "bigger":
                    return parts[0] > parts[1]
                    pass
                if _type == "lower":
                    return parts[0] < parts[1]
                    pass
                if _type == "bigger or equal":
                    return parts[0] >= parts[1]
                    pass
                if _type == "lower or equal":
                    return parts[0] <= parts[1]
                    pass
            except:
                werr(scriptRuntimeErrors, "Error in condition compare!", 19)
                return ERROR
                pass

            pass

        if conditions.__len__() == 1:
            parts = conditionProcessor.decomposeOperator(conditions[0].Condition)
            _type = parts[1]
            parts = parts[0]
            state = getState(base, parts, _type)
            if state == ERROR:
                return ERROR
                pass

            return state
            pass

        for condition in conditions:
            parts = conditionProcessor.decomposeOperator(condition.Condition)
            _type = parts[1]
            parts = parts[0]
            if condition.Type == "or":
                state = getState(base, parts, _type)
                if state == ERROR:
                    return ERROR
                    pass

                if state == True:
                    return True
                    pass

                continue
                pass
            else:
                state = getState(base, parts, _type)
                if state == ERROR:
                    return ERROR
                    pass

                if state == False:
                    return False
                    pass

                continue
                pass
            pass

        return True
        pass

    @staticmethod
    def decomposeConditions(cmd: str) -> [ str, list ]:
        conditions = []
        while(True):
            mustDex = cmd.find("|")
            _type = "or"
            if mustDex == -1:
                mustDex = cmd.find("&")
                _type = "and"
                pass
            if mustDex != -1:
                must = cmd[0:mustDex].strip()
                cmd = cmd[mustDex+1:].strip()

                conditions.append(condition(_type, must))
                continue
                pass
            
            conditions.append(condition(_type, cmd))
            break
            pass

        return conditions
        pass

    @staticmethod
    def decomposeOperator(cmd: str):
        for operator in conditionOperators:
            operatorDex = cmd.find(operator)
            if operatorDex != -1:
                parts = cmd.split(operator)
                return [ parts , dictProcessor.getValue(conditionOperators, operator).lower() ]
                pass

            pass
        return [ [ cmd, None ] , "boolean single" ]
        pass

    @staticmethod
    def isConditionStart(cmd: str) -> bool:
        return re.match("if(\\s+).+(?=->).*", cmd, flags = re.UNICODE | re.S) is not None
        pass

    pass

# Dictionaries
conditionOperators = {
    "==":         "Equal",
    "!=":         "Not equal",
    ">":          "Bigger",
    "<":          "Lower",
    ">=":         "Bigger or equal",
    "<=":         "Lower or equal",
    "Boleean":    "Boolean signle"
}

conditionSeperators = [ "|", "&" ]
