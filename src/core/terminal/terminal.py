class terminal:
    # Fields.
    CurrentPath = ""

    def __init__(self,currentPath):
        self.CurrentPath = currentPath
        pass

    # Get input.
    def getInput(self):
        return input(self.CurrentPath + ">")
        pass

    pass
