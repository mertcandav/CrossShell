# MIT License
# 
# Copyright (c) 2020 Mertcan Davulcu
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Imports.
import sys
import os
import platform
from core.terminal.terminal import *
from core.cmdProcessor import *

# Fields.
_terminal = terminal(os.getcwd())

# Entry Point
def main():
    # Command input loop.
    while True:
        _input = cmdProcessor.clearCmd(_terminal.getInput())
        cmdProcessor.process(_terminal,_input)
        pass
    pass

# Main point
if __name__ == "__main__":
    sys.stdout.write("\x1b]2;CrossShell\x07")
    if platform.system() == "Windows":
        cmdProcessor.process(_terminal,"clear")
        pass
    main()
    pass
