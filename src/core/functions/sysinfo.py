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
        if moduleProcessor.checkParams(params,1) == ERROR:
            return
            pass
        if params.count("all") > 0:
            cprintln(RED,"The -all parameter can only be used alone!")
            return
            pass

        # ---

        if cmd == "-help":
            print(
                "sysinfo:\n"
                "   -all: Show all informations of system."
            )
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
            pass
        else:
            cprintln(RED,"'sysinfo' command cannot processed!")
            pass
        pass

    pass
