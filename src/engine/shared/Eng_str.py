# Imports.
from core.CrossShell import *
from core.terminal.terminal import *

class Eng_str:
    @staticmethod
    def process(cmd: str):
        cmd = cmd.strip()
        if cmd == "":
            cprintln(RED,"String is not defined!")
            return ERROR
            pass
        if cmd.startswith('"') == False:
            cprintln(RED,"String is not declare!")
            return ERROR
            pass
        if cmd.endswith('"') == False:
            cprintln(RED,"String end is not declared!")
            return ERROR
            pass

        val = cmd[1:cmd.__len__()-1]
        return val
        pass
    pass
