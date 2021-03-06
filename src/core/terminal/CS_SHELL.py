# Imports.
import sys
import os
import platform
import json
import subprocess
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
from core.functions.rmtree import *
from core.functions.fdel import *
from core.functions.mkdir import *
from core.functions.exec import *
from core.functions.touch import *
from core.functions.script import *
from core.functions.more import *
from engine.values.Eng_string import *
from engine.values.Eng_char import *
from core.CrossShell import *
from core.csJSON import *
from framework.fs import *
from framework.cli import *

class CS_SHELL(cmd.Cmd):
    # Fields.
    term = None

    def Update(self) -> None:
        self.prompt = f"{CROSSSHELL_YELLOW}C{CROSSSHELL_BLUE}S {PROMPT}{self.term.CurrentPath}>{RED}{self.term.SysShell} {RESET}"
        pass

    def Break(self) -> bool:
        return True
        pass

    #########################################################
    #########################################################

    def emptyline(self) -> None:
        return
        pass

    def precmd(self, line: str) -> str:
        param = paramProcessor.getNonParam(line)
        if line.startswith("cd") == False:
            param = param.lower()
        if line.find(" -") != -1:
            line = f"{param} {paramProcessor.removeNonParam(line)}"
            pass
        else:
            line = param
            pass
        return line
        pass

    def do_exit(self, args: str) -> None:
        sys.exit(0)
        pass

    def do_clear(self, args: str) -> None:
        if platform.system() == "Windows":
            os.system("cls")
            pass
        else:
            os.system("clear")
            pass
        pass

    def do_cls(self, args: str) -> None:
        if platform.system() == "Windows":
            os.system("cls")
            pass
        else:
            os.system("clear")
            pass
        pass

    def do_about(self, args: str) -> None:
        print(FULL_ABOUT)
        pass

    def do_help(self, args: str) -> None:
        for key in HELP.keys():
            value = HELP[key]
            print(f"{NGREEN}{key}{WHITE}{value}")
            pass
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

    def do_rmtree(self, args: str) -> None:
        func_rmtree.process(self.term, args)
        pass

    def do_mkdir(self, args: str) -> None:
        func_mkdir.process(self.term, args)
        pass

    def do_more(self, args: str) -> None:
        func_more.process(self.term, args)
        pass

    def do_exec(self, args: str) -> None:
        func_exec.process(self.term, args)
        pass

    def do_del(self, args: str) -> None:
        func_del.process(self.term, args)    
        pass

    def do_touch(self, args: str) -> None:
        func_touch.process(self.term, args)
        pass

    def do_script(self, args: str) -> None:
        func_script.process(self.term, args)
        pass

    def default(self, line: str) -> None:
        # System Shell Integration
        if line.startswith(SysIntegrationMark):
            if line == SysIntegrationMark:
                if self.term.SysShell == "":
                    self.term.SysShell = SysIntegrationMark
                    updateJSON("SysIntegration", True)
                    pass
                else:
                    self.term.SysShell = ""
                    updateJSON("SysIntegration", False)
                    pass
                self.Update()
                return
                pass
            else:
                subprocess.call(line[1:], shell=True, cwd=self.term.CurrentPath)
                pass
            return
            pass

        if self.term.SysShell == "":
            line = paramProcessor.removeParams(line)
            cprintln(RED,f"'{ORANGE}{line}{RED}' command not recognized!")
            pass
        else:
            subprocess.call(line, shell=True, cwd=self.term.CurrentPath)
            pass
        pass

    pass
