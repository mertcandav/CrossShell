# Imports.
import platform
import os

class func_sysinfo:
    @staticmethod
    def process(cmd: str):
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
