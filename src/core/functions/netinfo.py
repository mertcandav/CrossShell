# Imports.
import socket
import os
import uuid
from core.CrossShell import *
from engine.paramProcessor import paramProcessor
from engine.moduleProcessor import moduleProcessor
from core.terminal.terminal import *
from framework.cli import *

class func_netinfo:
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
                f"{CYAN}netinfo{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-all{WHITE}                     Show all informations of network. This parameter can only be used alone.\n"
f"   {NGREEN}-hostname{WHITE}                Show hostname.\n"
f"   {NGREEN}-ip{WHITE}                      Show IPv4 address.\n"
f"   {NGREEN}-mac{WHITE}                     Show physical address."
            )
            return
            pass
        if cmd == "-all":
            print(
f"{NGREEN}Hostname{WHITE}                    {socket.gethostname()}\n"
f"{NGREEN}IPv4 Address{WHITE}                {socket.gethostbyname(socket.gethostname())}\n"
f"{NGREEN}Physical Address{WHITE}            " + ':'.join(("%012X" % uuid.getnode()) [i:i+2] for i in range(0,12,2))
            )
            return
            pass

        msg = ""
        for element in params:
            if element == "hostname":
                msg += f"{NGREEN}Hostname{WHITE}                    {socket.gethostname()}\n"
                continue
                pass
            if element == "ip":
                msg += f"{NGREEN}IPv4 Address{WHITE}                {socket.gethostbyname(socket.gethostname())}\n"
                continue
                pass
            if element == "mac":
                msg += f"{NGREEN}Physical Address{WHITE}            " + ':'.join(("%012X" % uuid.getnode()) [i:i+2] for i in range(0,12,2)) + "\n"
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
