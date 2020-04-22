# Imports.
import platform
import os
from core.CrossShell import *
from core.paramProcessor import paramProcessor
from core.moduleProcessor import moduleProcessor

class func_sysinfo:
    @staticmethod
    def process(cmd: str):
        params = paramProcessor.getParams(cmd)
        if moduleProcessor.checkParams(params,1) == ERROR:
            return
            pass
        if params.count("all") > 0:
            print("The -all parameter can only be used alone!")
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
            print("'sysinfo' command cannot processed!")
            pass
        pass

    pass
