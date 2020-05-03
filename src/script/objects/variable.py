class variable:
    # Fields.
    Name = None
    Value = None

    def __init__(self, name: str, val) -> None:
        self.Name = name
        self.Value = val
        pass

    @staticmethod
    def exists(variables: list, name: str) -> bool:
        return list(var for var in variables if var.Name == name).__len__() > 0
        pass

    @staticmethod
    def getByName(variables: list, name: str):
        for var in variables:
            if var.Name == name:
                return var
                pass
            pass
        pass

    pass
