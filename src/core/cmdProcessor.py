# Imports.
import platform
import os
from core.terminal.terminal import *
from core.functions.cd import *
from core.functions.sysinfo import *
from core.functions.netinfo import *
from core.functions.ls import *

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
        if cmd.startswith("sysinfo "):
            cmd = cmdProcessor.readyCmd("sysinfo ",cmd)
            func_sysinfo.process(cmd)
            return
            pass
        if cmd.startswith("netinfo "):
            cmd = cmdProcessor.readyCmd("netinfo ",cmd)
            func_netinfo.process(cmd)
            return
            pass
        if cmd.startswith("ls"):
            cmd = cmdProcessor.readyCmd("ls",cmd)
            func_ls.process(term,cmd)
            return
            pass

        cprintln(RED,f"'{cmd}' Command not recognized!")
        pass

    pass
