# Imports.
import os
from core.CrossShell import *
from engine.paramProcessor import paramProcessor
from core.terminal import terminal
from engine.values.Eng_string import *
from framework.fs import *
from framework.cli import *
from framework.drawing import *

class func_more:
    @staticmethod
    def process(term: terminal, cmd: str) -> None:
        params = paramProcessor.getParams(cmd)
        if params == ERROR:
            return
            pass

        path = os.path.join(term.CurrentPath, paramProcessor.getNonParam(cmd))
        if os.path.isfile(path) == False:
            if params.__len__() > 1 & params.count("help") > 0:
                cprintln(RED,"The -help parameter can only be used alone!")
                return
                pass

            if cmd == "-help":
                print(
                    f"{CYAN}more{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-ec:<string>{WHITE}             Set encoding."
                )
                return
                pass

            cprintln(RED,"There is no such file in this directory!")
            return
            pass
        
        msg = ""
        encoding = "utf-8"
        for element in params:
            if element.startswith("ec:"):
                encoding = Eng_string.process(element[3:])
                continue
                pass

            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        if (msg != ERROR) & (encoding != ERROR):
            lines = fs.readAllLines(path,encoding)
            lineslen = lines.__len__()
            for dex in range(0, lineslen):
                line = lines[dex]
                print(f"{CLI_BACKPREVLINE}{CLI_CLEARLINE}", end="")
                print(line, end="\r")
                if lineslen - dex != 1:
                    input(f"{ORANGE}----------{BOLD} {dex + 1}{BLUE}/{BOLD}{lineslen} {ORANGE}----------{WHITE}")
                    pass
                pass
            pass

        pass

    pass
