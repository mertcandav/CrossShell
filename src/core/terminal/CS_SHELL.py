# Imports.
import sys
import os
import platform
import json
import cmd
from cmd import *
from engine.paramProcessor import *
from core.functions.cd import *
from core.functions.sysinfo import *
from core.functions.netinfo import *
from core.functions.pause import *
from core.functions.ls import *
from core.functions.print import *
from core.functions.rmdir import *
from engine.values.Eng_string import *
from engine.values.Eng_char import *
from core.CrossShell import *
from framework.fs import *
from framework.cli import *

class CS_SHELL(Cmd):
    # Fields.
    term = None

    def Update(self) -> None:
        self.prompt = CYAN + self.term.CurrentPath + f">" + RED + self.term.SysShell + " " + RESET
        pass

    #########################################################
    #########################################################

    def do_exit(self, args: str) -> None:
        exit(0)
        pass

    def do_clear(self, args: str) -> None:
        if platform.system() == "Windows":
            os.system("cls")
            pass
        else:
            os.system("clear")
            pass
        pass

    def do_about(self, args: str) -> None:
        print(ABOUT)
        pass

    def do_help(self, args: str) -> None:
        print(HELP)
        pass

    def do_echo(self, args: str) -> None:
        message = ""
        if args.startswith("'"):
            message = Eng_char.process(args)
            pass
        else:
            message = Eng_string.process(args)
            pass
        if message == ERROR:
            return
            pass

        print(message)
        pass

    def do_cd(self, args: str) -> None:
        self.term.CurrentPath = func_cd.process(self.term.CurrentPath,args).__str__()
        self.Update()
        pass

    def do_ls(self, args: str) -> None:
        func_ls.process(self.term, args)
        pass

    def do_pause(self, args: str) -> None:
        func_pause.process(args)
        pass

    def do_print(self, args: str) -> None:
        func_print.process(self.term, args)
        pass

    def do_sysinfo(self, args: str) -> None:
        func_sysinfo.process(args)
        pass

    def do_netinfo(self, args: str) -> None:
        func_netinfo.process(args)
        pass

    def do_rmdir(self, args: str) -> None:
        func_rmdir.process(self.term, args)
        pass

    def default(self, line: str) -> None:
        # System Shell Integration
        if line.startswith(SysIntegrationMark):
            if line == SysIntegrationMark:
                csjson = json.loads(fs.readAllText("CrossShell.json", "utf-8"))
                if self.term.SysShell == "":
                    self.term.SysShell = SysIntegrationMark
                    csjson["settings"]["SysIntegration"] = True
                    pass
                else:
                    self.term.SysShell = ""
                    csjson["settings"]["SysIntegration"] = False
                    pass
                fs.writeAllText("CrossShell.json", json.dumps(csjson, indent=4), "utf-8")
                self.Update()
                return
                pass
            else:
                os.system(line[1:])
                pass
            return
            pass

        if self.term.SysShell == "":
            line = paramProcessor.removeParams(line)
            cprintln(RED,f"'{line}' command not recognized!")
            pass
        else:
            os.system(line)
            pass
        pass

    pass