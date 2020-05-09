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

        def readFunc(commands) -> list:
            fcommand = ""
            openBracketCount = 0
            counter = 0
            for command in commands:
                counter += 1
                dex = command.find("{")
                if dex != -1:
                    openBracketCount += 1
                    pass
                fdex = command[dex:].find("}")
                if fdex != -1:
                    if openBracketCount > 0:                   
                        openBracketCount -= 1

                        if openBracketCount == 0:
                            fcommand += command + ";"
                            break
                            pass
                        pass
                    
                    pass

                fcommand += command + ";"
                pass

            return [ fcommand[:fcommand.__len__()-1].strip(), commands[counter-1:] ]
            pass

        parts = code.split(";")
        dex = -1
        while(dex < parts.__len__()-1):
            dex += 1
            command = parts[dex].strip()

            if command.find("{") != -1:
                result = readFunc(parts[dex:])
                command = result[0]
                parts = result[1]
                dex = 0
                pass

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
