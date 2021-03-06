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
import json
from core.CrossShell import *
from core.terminal import terminal
from engine.cmdProcessor import *
from framework.fs import *
from framework.cli import *

# Fields.
term = terminal.terminal(os.getcwd())

# Process start arguments.
def process_Args() -> bool:
    args = sys.argv[1:]
    argslen = args.__len__()
    if argslen > 1:
        exitwerr(errors, "At most one initial argument can be given!", 2)
        return False
        pass
    if argslen == 1:
        term.Shell.onecmd(f"script {args[0]}")
        return False
        pass

    return True
    pass

# Read CrossShellJSON.
def process_CrossShellJSON() -> None:
    if os.path.exists("CrossShell.json") == False:
        return
        #exitwerr(errors, "CrossShell.json not found!", 1)
        pass

    csjson = json.loads(fs.readAllText("CrossShell.json", "utf-8"))

    # System Shell Integration
    if csjson["SysIntegration"] == True:
        term.SysShell = "$"
        pass

    pass

# Entry Point.
def main() -> None:
    # Command input loop.
    while True:
        term.startLoop()
        try:
            term.startLoop()
            pass
        except Exception:
            for error in sys.exc_info():
                cprintln(RED, error)
                pass
            pass
        pass
    pass

# Main point.
if __name__ == "__main__":
    setTitle("CrossShell")
    
    if platform.system() == "Windows":
        cmdProcessor.process(term,"clear")
        pass

    print(ABOUT)
    
    process_CrossShellJSON()
    if process_Args() == True:
        main()
        pass
    
    pass
