# CrossShell
VERSION = "0.0.1"

# Content of commands
ABOUT = f"""CrossShell ~ [ Version: {VERSION} ]
Copyright (c) 2020 Mertcan Davulcu"""
HELP = """HELP              Show help of CrossShell commands.
EXIT              Exit from CrossShell.
ABOUT             Show about info of CrossShell.
CLEAR             Clear the CLI screen.

ECHO              Show message on screen.
CD                Allows you to manage the current location.
LS                This module allows you to list the contents of the location at the current location.
NETINFO           This module is a module that allows you to get information about the network.
SYSINFO           This module is a module that allows you to get information about the system."""

# States
ERROR = "$ERROR"
NO_ERROR = "$NONERROR"

# Terminal Styles
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
WHITE  = '\033[0m'
YELLOW  = '\033[33m'
PURPLE  = '\033[35m'
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
