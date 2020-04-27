# Imports.
import re
from core.CrossShell import *
from core.terminal.terminal import *
from framework.cli import *

class Eng_char:
    @staticmethod
    def process(cmd: str) -> str:
        cmd = cmd.strip()
        if cmd == "":
            cprintln(RED,"Char is not defined!")
            return ERROR
            pass
        if cmd.startswith("'") == False:
            cprintln(RED,"Char is not declare!")
            return ERROR
            pass

        val = cmd[1:]

        # Control.
        def control() -> str:
            cval = val
            for key in escapes:
                cval = re.sub(escapes[key], "", cval, flags=re.MULTILINE|re.UNICODE)
                pass
            
            if cval.endswith("'") == False:
                cprintln(RED,"Char end is not declared!")
                return ERROR
                pass
            
            cval = cval[0:cval.__len__()-1]
            
            if cval.__len__() > 1:
                cprintln(RED,"Char can be at most one character!")
                return ERROR
                pass

            for key in escapes_check:
                if cval.find(key) != -1:
                    cprintln(RED, f"'{key}' invalid value!")
                    return ERROR
                    pass
                pass

            return NO_ERROR
            pass

        if control() == ERROR:
            return ERROR
            pass
        
        val = val[0:val.__len__()-1]
        for key in escapes:
            val = re.sub(escapes[key], key, val, flags=re.MULTILINE|re.UNICODE)
            pass

        return val
        pass
    pass

escapes = {
    "\\\\":   "\\\\\\\\",
    "\"":   "\\\\\"",
    "\'":   "\\\\\'",
    "\n":   "\\\\n",
    "\r":   "\\\\r",
    "\t":   "\\\\t",
    "\b":   "\\\\b",
    "\f":   "\\\\f",
    "\a":   "\\\\a",
    "\v":   "\\\\v"
}

escapes_check = [ "\\", "\"" ]
