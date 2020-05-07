# Imports.
from script.objects.variable import *
from script.objects.function import *
from core.CrossShell import *
from framework.cli import *

class keywordProcessor:
    @staticmethod
    def process(base, cmd: str) -> [ bool, str ]:
        if cmd.startswith("delete ") == True:
            cmd = cmd[7:].strip()
            if cmd.endswith("()"):
                name = cmd[:cmd.__len__()-2].strip()
                if function.exists(base.functions, name) == False:
                    werr(scriptRuntimeErrors, "An attempt was made to delete the undefined function from memory!", 16)
                    return ERROR
                    pass
                
                base.functions.remove(function.getByName(base.functions, name))
                return True
                pass
            
            if variable.exists(base.variables, cmd) == False:
                werr(scriptRuntimeErrors, "An attempt was made to delete the undefined variable from memory!", 17)
                return ERROR
                pass    

            base.variables.remove(variable.getByName(base.variables, cmd))
            return True
            pass
        
        return False
        pass

    pass
