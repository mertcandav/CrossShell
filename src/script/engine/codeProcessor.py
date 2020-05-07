# Imports.
import re
from core.CrossShell import *
from framework.cli import *

class codeProcessor:
    @staticmethod
    def clearComments(code: str) -> str:
        # Multi line.
        code = re.sub("#>.*<#|#>.*", "", code, flags = re.UNICODE | re.S)

        # Single Line.
        code = re.sub("#.*$", "", code, flags = re.UNICODE | re.MULTILINE)

        return code
        pass

    @staticmethod
    def getCommands(code: str) -> list:
        commands = []
        for command in re.split("(?![^{]*\});", code, flags = re.UNICODE | re.MULTILINE):
            command = command.strip()

            if (command == "") | (command == "@") | (command == ">"):
                continue
                pass
            
            commands.append(command)
            pass

        return commands
        pass

    @staticmethod
    def isBannedName(code: str) -> bool:
        if (re.match("(^[0-9].*)|True|False|.*( |\\$|#|\\-|<|>|\\?|\\*|\\\\|\\{|\\}|\\[|\\]|\\(|\\)|\\&|`|´|=|%|\\+|'|\"|\\^|!|/|\\.|;|¨|~|:|₺|€|\\||£).*", code,
            flags = re.UNICODE | re.IGNORECASE | re.UNICODE | re.S)):
            werr(scriptRuntimeErrors, "Forbidden character was used in the definition!", 11)
            return True
            pass

        return False
        pass

    pass
