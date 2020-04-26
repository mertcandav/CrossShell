# Imports.
import sys
from core.CrossShell import *

# Functions.
def cprint(style,val: str) -> None:
    sys.stdout.write(style)
    print(val, end = '')
    sys.stdout.write(RESET)
    pass

def cprintln(style,val: str) -> None:
    sys.stdout.write(style)
    print(val)
    sys.stdout.write(RESET)
    pass