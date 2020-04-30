# Imports.
import os
from core.CrossShell import *
from engine.paramProcessor import paramProcessor
from core.terminal import terminal
from core.functions.more import *
from engine.values.Eng_string import *
from framework.fs import *
from framework.cli import *

class func_print:
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
                    f"{CYAN}print{RESET}\n"
f"   {NGREEN}-help{WHITE}                    Show help of module. This parameter can only be used alone.\n"
f"   {NGREEN}-ec:<string>{WHITE}             Set encoding.\n"
f"   {NGREEN}-more{WHITE}                    Show line by line."
                )
                return
                pass

            cprintln(RED,"There is no such file in this directory!")
            return
            pass
        
        msg = ""
        encoding = "utf-8"
        more = False
        for element in params:
            if element.startswith("ec:"):
                encoding = Eng_string.process(element[3:])
                continue
                pass
            if element.startswith("more"):
                more = True
                continue
                pass

            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        if (msg != ERROR) & (encoding != ERROR):
            if more:
                func_more.process(term, f"{path} -ec:\"{encoding}\"")
                pass
            else:
                print(fs.readAllText(path,encoding))
                pass

            return
            pass

        pass

    pass
