# Imports.
import os
from core.CrossShell import *
from engine.paramProcessor import paramProcessor
from core.terminal.terminal import *
from engine.values.Eng_string import *
from framework.fs import *

class func_print:
    @staticmethod
    def process(term: terminal, cmd: str):
        params = paramProcessor.getParams(cmd)
        if params == ERROR:
            return
            pass

        dex = cmd.find(" ")
        cmd = cmd
        if dex != -1:
            cmd = cmd[0:dex]
            pass

        path = os.path.join(term.CurrentPath,cmd)
        if os.path.isfile(path) == False:
            if params.__len__() > 1 & params.count("help") > 0:
                cprintln(RED,"The -help parameter can only be used alone!")
                return
                pass

            if cmd == "-help":
                print(
                    "print:\n"
                    "   -help: Show help of module. This parameter can only be used alone.\n"
                    "   -ec:<string>: Encoding."
                )
                return
                pass

            cprintln(RED,"Not exists")
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
            print(fs.readAllText(path,encoding))
            return
            pass

        pass

    pass
