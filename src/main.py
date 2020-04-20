# Imports.
import sys
import os
from core.terminal.terminal import *
from core.cmdProcessor import *

# Fields.
_terminal = terminal(os.getcwd())

# Entry Point
def main():
    # Command input loop.
    while True:
        _input = _terminal.getInput()
        cmdProcessor.process(_input)
        pass
    pass

# Main point
if __name__ == "__main__":
    main()
    pass
