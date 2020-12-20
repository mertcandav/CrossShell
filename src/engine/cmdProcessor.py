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
        lcmd = cmd.lower()

        if lcmd == "clear":
            print("\e[1;1H\e[2J",end="")
            pass

        pass

    pass
