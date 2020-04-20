class terminal:
    # Fields.
    CurrentPath = ""

    def __init__(self,currentPath):
        self.CurrentPath = currentPath
        pass

    # Set current path.
    def setPath(self,path: str):
        self.CurrentPath = path
        pass

    # Get input.
    def getInput(self):
        return input(self.CurrentPath + ">")
        pass

    pass
