# Imports.
import platform
import os
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
        if cmd == "exit":
            exit(0)
            pass
        if cmd == "clear":
            if platform.system() == "Windows":
                os.system("cls")
                pass
            else:
                os.system("clear")
                pass
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