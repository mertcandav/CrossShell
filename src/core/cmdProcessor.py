# Imports.
from core.terminal.terminal import *
from core.functions.cd import *

class cmdProcessor:
    @staticmethod
    def clearCmd(cmd: str):
        return cmd.strip()
        pass

    @staticmethod
    def readyCmd(title: str,cmd: str):
        cmd = cmd[title.__len__():]
        cmd = cmdProcessor.clearCmd(cmd)
        return cmd
        pass

    @staticmethod
    def process(term: terminal,cmd: str):
        if cmd == "":
            return
            pass
        if cmd.startswith("cd "):
            cmd = cmdProcessor.readyCmd("cd ",cmd)
            term.CurrentPath = func_cd.process(term.CurrentPath,cmd).__str__()
            return
            pass

        print("Command not recognized!")
        pass

    pass