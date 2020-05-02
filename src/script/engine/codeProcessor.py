# Imports.
import re

class codeProcessor:
    @staticmethod
    def clearComments(code: str) -> str:
        # Multi line.
        code = re.sub("#\>.*\<#", "", code, flags = re.UNICODE | re.S)

        # Single Line.
        code = re.sub("#.*$", "", code, flags = re.UNICODE | re.MULTILINE)

        return code
        pass

    @staticmethod
    def getCommands(code: str) -> list:
        commands = []
        for command in code.split(";"):
            command = command.strip()

            if (command == "") | (command == "@"):
                continue
                pass
            
            commands.append(command)
            pass

        return commands
        pass

    pass
