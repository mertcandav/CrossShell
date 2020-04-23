# Imports.
import platform
import os
from core.CrossShell import *
from core.paramProcessor import paramProcessor
from core.moduleProcessor import moduleProcessor
from core.terminal.terminal import *

class func_sysinfo:
    @staticmethod
    def process(cmd: str):
        params = paramProcessor.getParams(cmd)
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
                "sysinfo:\n"
                "   -help: Show help of module. This parameter can only be used alone.\n"
                "   -all: Show all informations of system. This parameter can only be used alone.\n"
                "   -cpu: Show about of processor.\n"
                "   -cpuc: Show core count of processor.\n"
                "   -platform: Show platform name.\n"
                "   -node: Show network name of current pc.\n"
                "   -rls: Show release of system.\n"
                "   -ver: Show version of system release.\n"
                "   -machine: Show machine type."
            )
            return
            pass
        if cmd == "-all":
            print(
                "Platform: " + platform.system() + "\n"
                "Version: " + platform.version() + "\n"
                "Release: " + platform.release() + "\n"
                "Node: " + platform.node() + "\n"
                "Machine: " + platform.machine() + "\n"
                "CPU: " + platform.processor() + "\n"
                "CPU~Cores: " + platform.os.cpu_count().__str__()
            )
            return
            pass
        msg = ""
        for element in params:
            if element == "platform":
                msg += "Platform: " + platform.system() + "\n"
                continue
                pass
            if element == "ver":
                msg += "Version: " + platform.version() + "\n"
                continue
                pass
            if element == "rls":
                msg += "Release: " + platform.release() + "\n"
                continue
                pass
            if element == "node":
                msg += "Node: " + platform.node() + "\n"
                continue
                pass
            if element == "machine":
                msg += "Machine: " + platform.machine() + "\n"
                continue
                pass
            if element == "cpu":
                msg += "CPU: " + platform.processor() + "\n"
                continue
                pass
            if element == "cpuc":
                msg += "CPU~Cores: " + platform.os.cpu_count().__str__() + "\n"
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
