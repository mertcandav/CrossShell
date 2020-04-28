# Imports.
import platform
import os
from core.CrossShell import *
from engine.paramProcessor import paramProcessor
from engine.moduleProcessor import moduleProcessor
from core.terminal.terminal import *
from framework.cli import *

class func_sysinfo:
    @staticmethod
    def process(cmd: str) -> None:
        params = paramProcessor.getParams(" " + cmd)
        if params == ERROR:
            return
            pass
        if params.__len__() > 1 & params.count("help") > 0:
            cprintln(RED,"The -help parameter can only be used alone!")
            return
            pass
        if params.__len__() > 1 & params.count("all") > 0:
            cprintln(RED,"The -all parameter can only be used alone!")
            return
            pass

        # ---

        if cmd == "-help":
            print(
                f"{CYAN}sysinfo{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-all{WHITE}                     Show all informations of system. This parameter can only be used alone.\n"
f"   {NGREEN}-cpu{WHITE}                     Show about of processor.\n"
f"   {NGREEN}-cpuc{WHITE}                    Show core count of processor.\n"
f"   {NGREEN}-platform{WHITE}                Show platform name.\n"
f"   {NGREEN}-node{WHITE}                    Show network name of current pc.\n"
f"   {NGREEN}-rls{WHITE}                     Show release of system.\n"
f"   {NGREEN}-ver{WHITE}                     Show version of system release.\n"
f"   {NGREEN}-machine{WHITE}                 Show machine type."
            )
            return
            pass
        if cmd == "-all":
            print(
f"{NGREEN}Platform{WHITE}                    {platform.system()}\n"
f"{NGREEN}Version{WHITE}                     {platform.version()}\n"
f"{NGREEN}Release{WHITE}                     {platform.release()}\n"
f"{NGREEN}Node{WHITE}                        {platform.node()}\n"
f"{NGREEN}Machine{WHITE}                     {platform.machine()}\n"
f"{NGREEN}CPU{WHITE}                         {platform.processor()}\n"
f"{NGREEN}CPU~Cores{WHITE}                   {platform.os.cpu_count().__str__()}"
            )
            return
            pass
        msg = ""
        for element in params:
            if element == "platform":
                msg += f"{NGREEN}Platform{WHITE}                    {platform.system()}\n"
                continue
                pass
            if element == "ver":
                msg += f"{NGREEN}Version{WHITE}                     {platform.version()}\n"
                continue
                pass
            if element == "rls":
                msg += f"{NGREEN}Release{WHITE}                     {platform.release()}\n"
                continue
                pass
            if element == "node":
                msg += f"{NGREEN}Node{WHITE}                        {platform.node()}\n"
                continue
                pass
            if element == "machine":
                msg += f"{NGREEN}Machine{WHITE}                     {platform.machine()}\n"
                continue
                pass
            if element == "cpu":
                msg += f"{NGREEN}CPU{WHITE}                         {platform.processor()}\n"
                continue
                pass
            if element == "cpuc":
                msg += f"{NGREEN}CPU~Cores{WHITE}                   {platform.os.cpu_count().__str__()}\n"
                continue
                pass

            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        if msg != ERROR:
            print(msg[0:msg.__len__()-1])
            return
            pass
        pass

    pass
