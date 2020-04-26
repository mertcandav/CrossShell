# Imports.
import platform
import os
import json
from core.terminal.terminal import *
from core.functions.cd import *
from core.functions.sysinfo import *
from core.functions.netinfo import *
from core.functions.pause import *
from core.functions.ls import *
from core.functions.print import *
from core.functions.rmdir import *
from engine.values.Eng_string import *
from framework.fs import *
from framework.cli import *

class cmdProcessor:
    @staticmethod
    def clearCmd(cmd: str) -> str:
        return cmd.strip()
        pass

    @staticmethod
    def readyCmd(title: str,cmd: str) -> str:
        cmd = cmd[title.__len__():]
        cmd = cmdProcessor.clearCmd(cmd)
        return cmd
        pass

    @staticmethod
    def process(term: terminal,cmd: str) -> None:
        if cmd == "":
            return
            pass

        lcmd = cmd.lower()
        if lcmd.startswith(SysIntegrationMark):
            if lcmd == SysIntegrationMark:
                csjson = json.loads(fs.readAllText("CrossShell.json", "utf-8"))
                if term.SysShell == "":
                    term.SysShell = SysIntegrationMark
                    csjson["settings"]["SysIntegration"] = True
                    pass
                else:
                    term.SysShell = ""
                    csjson["settings"]["SysIntegration"] = False
                    pass
                fs.writeAllText("CrossShell.json", json.dumps(csjson, indent=4), "utf-8")
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
            val = cmdProcessor.readyCmd("echo ",cmd)
            if val.startswith("'"):
                val = Eng_char.process(val)
                pass
            else:
                val = Eng_string.process(val)
                pass
            if val == ERROR:
                return
                pass
            print(val)
            return
            pass
        if lcmd.startswith("cd "):
            lcmd = cmdProcessor.readyCmd("cd ",cmd)
            term.CurrentPath = func_cd.process(term.CurrentPath,lcmd).__str__()
            return
            pass
        if lcmd.startswith("sysinfo "):
            lcmd = cmdProcessor.readyCmd("sysinfo ",cmd)
            func_sysinfo.process(lcmd)
            return
            pass
        if lcmd.startswith("netinfo "):
            lcmd = cmdProcessor.readyCmd("netinfo ",cmd)
            func_netinfo.process(lcmd)
            return
            pass
        if lcmd.startswith("print "):
            lcmd = cmdProcessor.readyCmd("print ",cmd)
            func_print.process(term,lcmd)
            return
            pass
        if lcmd.startswith("pause"):
            lcmd = cmdProcessor.readyCmd("pause",cmd)
            func_pause.process(lcmd)
            return
            pass
        if lcmd.startswith("ls"):
            func_ls.process(term,cmd)
            return
            pass
        if lcmd.startswith("rmdir "):
            lcmd = cmdProcessor.readyCmd("rmdir ",cmd)
            func_rmdir.process(term,lcmd)
            return
            pass

        dex = cmd.find(" ")
        fcmd = cmd
        if dex != -1:
            fcmd = cmd[0:dex]
            pass

        if term.SysShell == "":
            cprintln(RED,f"'{fcmd}' command not recognized!")
            pass
        else:
            os.system(cmd)
            pass

        pass

    pass
