# CrossShell
VERSION = "0.0.1"
SCRIPT_EXTENSION = ".cs1"

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
CONTRAST = "\033[1;100m"
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
PINK = '\033[1;95m'
NPINK = '\033[95m'
DIMBLUE = '\033[1;94m'
NDIMBLUE = '\033[94m'
LIGHTGREEN = '\033[1;92m'
NLIGHTGREEN = '\033[92m'
UNDERLINE = '\033[4m'
PROMPT = '\033[38;2;250;240;140m'
ORANGE = '\033[38;2;245;170;66m'
CROSSSHELL_YELLOW = '\033[38;2;255;195;95m'
CROSSSHELL_BLUE = '\033[38;2;45;180;185m'

# CLI
CLI_BACKPREVLINE = "\033[F"
CLI_CLEARLINE = "\033[K"

# Content of commands
ABOUT = f"""{CROSSSHELL_YELLOW}Cross{CROSSSHELL_BLUE}Shell{WHITE} ~ {CYAN}[{BLUE} Version{WHITE} {VERSION} {CYAN}]{WHITE}
Copyright (c) 2020 Mertcan Davulcu
"""

FULL_ABOUT = f"""
{CROSSSHELL_YELLOW}             WWWWWW
        WNNXXKKKKKKXN
     WNXKK000000K00KXW
   WNXK000000KKKKKKXN
  WXK0000KKXNNWWWWW
 WXK000KKXWW             {CROSSSHELL_BLUE}WNK0000XW{CROSSSHELL_YELLOW}
WNK0000XNW             {CROSSSHELL_BLUE}NKkdoooooxKW{CROSSSHELL_YELLOW}
WX0000KN             {CROSSSHELL_BLUE}WXkdoooooooxKW{CROSSSHELL_YELLOW}
NK00K0XW             {CROSSSHELL_BLUE}NkoooooxO0KXW{CROSSSHELL_YELLOW}
NK0000XW             {CROSSSHELL_BLUE}KxooookXW{CROSSSHELL_YELLOW}
WXK000KNW            {CROSSSHELL_BLUE}KxooooON{CROSSSHELL_YELLOW}
 NK0000KNW           {CROSSSHELL_BLUE}KxooooON{CROSSSHELL_YELLOW}
 WNK0000KXNW        {CROSSSHELL_BLUE}WKdooooON{CROSSSHELL_YELLOW}
  WNKK0000KKXNNNNN{CROSSSHELL_BLUE}XK0xooood0W{CROSSSHELL_YELLOW}
   WWXKK0000000kx{CROSSSHELL_BLUE}ddoooooodON{CROSSSHELL_YELLOW}
      WNXKK0000{CROSSSHELL_BLUE}xooooooodkKN{CROSSSHELL_YELLOW}
         WNNXXX{CROSSSHELL_BLUE}0OOkkkO0XN{CROSSSHELL_YELLOW}
            WWWW{CROSSSHELL_BLUE}WWWWWW{CROSSSHELL_YELLOW}
            
{WHITE}{ABOUT}"""

# States
ERROR = "$ERROR"
NO_ERROR = "$NONERROR"

# External
SysIntegrationMark = "$"

# Dictionaries.
HELP = {
    "HELP":              "                            Show help of CrossShell commands.",
    "EXIT":              "                            Exit from CrossShell.",
    "ABOUT":             "                           Show about info of CrossShell.",
    "CLEAR/CLS":         "                       Clear the CLI screen.",
    "PAUSE":             "                           This module stops inputting commands until you press the ``enter`` key.",
    "ECHO":              "                            Show message on screen.",
    "SCRIPT":            "                          Run CrossShell script.\n",
    "$":                 "                               Use and manage system shell integration.\n",
    "CD":                "                              Allows you to manage the current location.",
    "LS":                "                              This module allows you to list the contents of the location at the current location.",
    "TOUCH":             "                           This module allows you to create files.",
    "DEL":               "                             This module allows you to delete files.",
    "MKDIR":             "                           This module is a module that allows you to create directories.",
    "RMDIR":             "                           This module is a module that allows you to delete directories.",
    "RMTREE":            "                          This module is a module that allows you to delete directories and childs.",
    "PRINT":             "                           This module reads and displays the contents of the specified file.",
    "MORE":              "                            This module reads and displays the contents of the specified file line by line.",
    "EXEC":              "                            This module allows you to run a file.\n",
    "NETINFO":           "                         This module is a module that allows you to get information about the network.",
    "SYSINFO":           "                         This module is a module that allows you to get information about the system.",
}

errors = {
    1:  "ffffff0x1",        # NOT USED! || CrossShell.json not found!
    2:  "ffffff0x2",        # At most one initial argument can be given!
}

scriptErrors = {
    1: "scffff0x1",         # The extension of the specified script file was not correct!
    2: "scffff0x2",         # The specified path does not exist!
    3: "scffff0x3",         # There is no such CrossShell Script file in the specified path!
}

scriptRuntimeErrors = {
    0:      "scffff1x0",         # Script command not recognized!
    1:      "scffff1x1",         # The function that does not return a value was used in the value conversion!
    2:      "scffff1x2",         # Error in value conversion!
    3:      "scffff1x3",         # More parameters have been sent to the function than you can take!
    4:      "scffff1x4",         # Variable is not specified!
    5:      "scffff1x5",         # Body error, '->' operator not found in function definition!
    6:      "scffff1x6",         # The function is turned on but not turned off!
    7:      "scffff1x7",         # Function not recognized!
    8:      "scffff1x8",         # No color found!
    9:      "scffff1x9",         # Error in variable definition!
    10:     "scffff1x10",        # An attempt was made to define a variable that has already been defined!
    11:     "scffff1x11",        # Forbidden character was used in the definition!
    12:     "scffff1x12",        # The function body is turned not on!
    13:     "scffff1x13",        # An attempt was made to define a function that has already been defined!
    14:     "scffff1x14",        # '<name>' function cannot be overrideed!
    15:     "scffff1x15",        # Attempt to override the non-existent function!
}
