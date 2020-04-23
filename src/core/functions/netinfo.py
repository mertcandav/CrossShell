# Imports.
import socket
import os
from core.CrossShell import *
from core.paramProcessor import paramProcessor
from core.moduleProcessor import moduleProcessor
from core.terminal.terminal import *

class func_netinfo:
    @staticmethod
    def process(cmd: str):
        params = paramProcessor.getParams(cmd)
        if params == ERROR:
            return
            pass
        if params.__len__() > 1 & params.count("all") > 0:
            cprintln(RED,"The -all parameter can only be used alone!")
            return
            pass
        if params.__len__() > 1 & params.count("help") > 0:
            cprintln(RED,"The -help parameter can only be used alone!")
            return
            pass

        # ---

        if cmd == "-help":
            print(
                "netinfo:\n"
                "   -help: Show help of module. This parameter can only be used alone.\n"
                "   -all: Show all informations of network. This parameter can only be used alone.\n"
                "   -hostname: Show hostname.\n"
                "   -ip: Show ip address."
            )
            return
            pass
        if cmd == "-all":
            print(
                "Hostname: " + socket.gethostname() + "\n"
                "IP: " + socket.gethostbyname(socket.gethostname())
            )
            return
            pass
        msg = ""
        for element in params:
            if element == "hostname":
                msg += "Hostname: " + socket.gethostname() + "\n"
                continue
                pass
            if element == "ip":
                msg += "IP: " + socket.gethostbyname(socket.gethostname()) + "\n"
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
