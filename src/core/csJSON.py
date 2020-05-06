# Imports.
import os
import json
from framework.fs import *

def updateJSON(path: str, value):
    if os.path.exists("CrossShell.json") == False:
        return

    csjson = json.loads(fs.readAllText("CrossShell.json", "utf-8"))
    csjson[path] = value
    fs.writeAllText("CrossShell.json", json.dumps(csjson, indent=4), "utf-8")

    pass
