# Imports.
import os
import re
import shutil
from engine.paramProcessor import *
from engine.values.Eng_string import *
from core.terminal.CS_SHELL import *
from core.terminal import terminal
from core.CrossShell import *
from framework.fs import *
from framework.cli import *

class func_mkdir:
    @staticmethod
    def process(term: terminal, cmd: str) -> None:
        params = paramProcessor.getParams(" " + paramProcessor.removeNonParam(cmd))
        if params == ERROR:
            return
            pass
        
        cmd = Eng_string.process(cmd)
        if cmd == ERROR:
            return
            pass
        
        path = os.path.join(term.CurrentPath, cmd)
        os.mkdir(path)

        pass

    pass
