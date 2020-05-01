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

class func_touch:
    @staticmethod
    def process(term: terminal, cmd: str) -> None:
        path = os.path.join(term.CurrentPath, cmd)
        open(path, 'x')
        
        pass

    pass
