# Imports.
from core.CrossShell import *

class colorizer:
    @staticmethod
    def byRGB(r: int, g: int, b: int) -> str:
        return f'\033[38;2;{r};{g};{b}m'
        pass
    pass
