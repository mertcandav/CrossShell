# CrossShell
VERSION = "0.0.1"

# Content of commands
ABOUT = f"""CrossShell ~ [ Version: {VERSION} ]
Copyright (c) 2020 Mertcan Davulcu"""

# States
ERROR = "$ERROR"
NO_ERROR = "$NONERROR"

# Terminal Styles
RED = "\033[1;31m"  
BLUE = "\033[1;34m"
GRAY = "\033[1;30m"
ALLBOLD = "\033[1;38m"
BLACK = "\033[30m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
WHITE = '\033[0m'
YELLOW = '\033[1;33m'
PURPLE = '\033[1;35m'
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
NRED  = "\033[31m"
NBLUE = "\033[34m"
NGRAY = "\033[30m"
NCYAN = "\033[36m"
NGREEN = "\033[32m"
NWHITE = '\033[0m'
NYELLOW = '\033[33m'
NPURPLE = '\033[35m'

# External
SysIntegrationMark = "$"

# Dictionaries.
HELP = {
    "help":              "                            Show help of CrossShell commands.",
    "exit":              "                            Exit from CrossShell.",
    "about":             "                           Show about info of CrossShell.",
    "clear":             "                           Clear the CLI screen.",
    "pause":             "                           This module stops inputting commands until you press the ``enter`` key.",
    "echo":              "                            Show message on screen.\n",
    "$":                 "                               Use and manage system shell integration.\n",
    "cd":                "                              Allows you to manage the current location.",
    "ls":                "                              This module allows you to list the contents of the location at the current location.",
    "netinfo":           "                         This module is a module that allows you to get information about the network.",
    "sysinfo":           "                         This module is a module that allows you to get information about the system.",
    "print":             "                           This module reads and displays the contents of the specified file.",
    "rmdir":             "                           This module is a module that allows you to delete directories.",
    "rmtree":             "                          This module is a module that allows you to delete directories and childs."
}

errors = {
    1:  "ffffff0x1"
}