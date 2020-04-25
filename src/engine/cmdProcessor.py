# Imports.
import platform
import os
from core.terminal.terminal import *
from core.functions.cd import *
from core.functions.sysinfo import *
from core.functions.netinfo import *
from core.functions.ls import *
from engine.shared.Eng_string import *

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

        lcmd = cmd.lower()
        if lcmd.startswith("$"):
            if lcmd == "$":
                if term.SysShell == "":
                    term.SysShell = "$"
                    pass
                else:
                    term.SysShell = ""
                    pass
                return
                pass
            else:
                os.system(lcmd[1:])
                pass
            return
            pass

        if lcmd == "exit":
            exit(0)
            pass
        if lcmd == "clear":
            if platform.system() == "Windows":
                os.system("cls")
                pass
            else:
                os.system("clear")
                pass
            return
            pass
        if lcmd == "about":
            print(ABOUT)
            return
        if lcmd == "help":
            pass
            print(HELP)
            return
            pass
        if lcmd.startswith("echo "):
            val = Eng_string.process(cmdProcessor.readyCmd("echo ",cmd))
            if val == ERROR:
                return
                pass
            print(val)
            return
            pass
        if lcmd.startswith("cd "):
            lcmd = cmdProcessor.readyCmd("cd ",lcmd)
            term.CurrentPath = func_cd.process(term.CurrentPath,lcmd).__str__()
            return
            pass
        if lcmd.startswith("sysinfo "):
            lcmd = cmdProcessor.readyCmd("sysinfo ",lcmd)
            func_sysinfo.process(lcmd)
            return
            pass
        if lcmd.startswith("netinfo "):
            lcmd = cmdProcessor.readyCmd("netinfo ",lcmd)
            func_netinfo.process(lcmd)
            return
            pass
        if lcmd.startswith("ls"):
            lcmd = cmdProcessor.readyCmd("ls",lcmd)
            func_ls.process(term,lcmd)
            return
            pass

        if term.SysShell == "":
            cprintln(RED,f"'{lcmd}' command not recognized!")
            pass
        else:
            os.system(lcmd)
            pass

        pass

    pass
