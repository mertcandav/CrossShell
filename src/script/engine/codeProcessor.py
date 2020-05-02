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

    pass
