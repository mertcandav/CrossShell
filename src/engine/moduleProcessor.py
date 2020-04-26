#Imports.
from core.CrossShell import *
from core.terminal.terminal import *
from framework.cli import *

class moduleProcessor:
    @staticmethod
    def checkParams(params: list,max = None):
        if max == None:
            if params.__len__() < 0:
                cprintln(RED,"At least one parameter must be declared in the modules!")
                return ERROR
                pass
            pass
        else:
            if params.__len__() < 0:
                cprintln(RED,"At least one parameter must be declared in the modules!")
                return ERROR
                pass
            if params.__len__() > max:
                cprintln(RED,"A maximum of " + max.__str__() + " parameter can be entered.")
                return ERROR
                pass
            pass
        return NO_ERROR
        pass 

    pass
