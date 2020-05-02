# Imports.
import os
from core.terminal import terminal
from engine.paramProcessor import *
from core.CrossShell import *
from script.scripter import *
from framework.fs import *
from framework.cli import *

class func_script:
    @staticmethod
    def process(term: terminal, cmd: str) -> None:
        params = paramProcessor.getParams(" " + paramProcessor.removeNonParam(cmd))
        if params == ERROR:
            return
            pass
        
        cmd = paramProcessor.getNonParam(cmd)
        msg = ""
        for element in params:
            cprintln(RED,f"'{element}' parameter cannot processed!")
            msg = ERROR
            pass

        if (msg != ERROR):
            if cmd.endswith(SCRIPT_EXTENSION) == False:
                werr(scriptErrors, "The extension of the specified script file was not correct!", 1)
                return
                pass

            path = os.path.join(term.CurrentPath, cmd)
            if os.path.exists(path) == False:
                werr(scriptErrors, "The specified path does not exist!", 2)
                return
                pass
            if os.path.isfile(path) == False:
                werr(scriptErrors, "There is no such CrossShell Script file in the specified path!", 3)
                return
                pass

            scripter.interpret(path)
            return
            pass

        pass

    pass
