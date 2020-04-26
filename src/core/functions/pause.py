# Imports.
from core.CrossShell import *
from engine.values.Eng_string import *
from framework.cli import *

class func_pause:
    @staticmethod
    def process(cmd: str) -> None:
        if cmd == "":
            input("Press enter for continue...")
            return
            pass
        else:
            message = Eng_string.process(cmd)
            if message != ERROR:
                input(message)
                pass
            return
            pass

        pass

    pass
