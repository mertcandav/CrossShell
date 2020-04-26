# Imports.
import sys
from core.CrossShell import *

# Functions.
def cprint(style,val: str):
    sys.stdout.write(style)
    print(val, end = '')
    sys.stdout.write(RESET)
    pass

def cprintln(style,val: str):
    sys.stdout.write(style)
    print(val)
    sys.stdout.write(RESET)
    pass