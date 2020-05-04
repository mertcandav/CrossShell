class listProcessor:
    @staticmethod
    def exists(lst: list, name: str) -> bool:
        return list(var for var in lst if var.Name == name).__len__() > 0
        pass

    @staticmethod
    def getByName(lst: list, name: str):
        for var in lst:
            if var.Name == name:
                return var
                pass
            pass
        pass

    pass
