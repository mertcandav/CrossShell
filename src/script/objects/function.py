# Imports.

class function:
    Name = ""
    Commands = []

    def __init__(self, name: str, commands: str) -> None:
        self.Name = name
        self.Commands = commands
        pass

    @staticmethod
    def exists(lst: list, name: str) -> bool:
        return list(func for func in lst if func.Name == name).__len__() > 0
        pass

    @staticmethod
    def getByName(lst: list, name: str):
        for func in lst:
            if func.Name == name:
                return func
                pass
            pass
        pass

    @staticmethod
    def indexOf(lst: list, name: str):
        for dex in range(0, lst.__len__()):
            if lst[dex].Name == name:
                return dex
                pass
            pass

        return -1
        pass

    pass
