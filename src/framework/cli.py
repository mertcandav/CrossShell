# Imports.
import sys
from core.CrossShell import *

# Functions.

# Exit with error message and code.
def exitwerr(collection: dict, err: str, code: int) -> None:
    cprint(RED, f"Ops! An error has occurred!\nError: " +
        err + RED + "\nCode: { " + YELLOW + collection[code] + RED + " }")
    input("\n\nPress enter for close... ")
    exit(1)
    pass

def werr(collection: dict, err: str, code: int) -> None:
    cprintln(RED, f"Ops! An error has occurred!\nError: " +
        err + RED + "\nCode: { " + YELLOW + collection[code] + RED + " }")
    pass

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