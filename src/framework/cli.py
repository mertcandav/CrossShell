# Imports.
import sys
from core.CrossShell import *

# Functions.

def setTitle(val: str) -> None:
    sys.stdout.write(f"\x1b]2;{val}\x07")
    pass

def cprint(style: str, val: str) -> None:
    sys.stdout.write(style)
    print(val, end = '')
    sys.stdout.write(RESET)
    pass

def cprintln(style: str, val: str) -> None:
    sys.stdout.write(style)
    print(val)
    sys.stdout.write(RESET)
    pass