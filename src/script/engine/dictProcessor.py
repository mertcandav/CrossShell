class dictProcessor:
    @staticmethod
    def existsKey(dictionary: dict, name: str) -> bool:
        return list(key for key in dictionary.keys() if key == name).__len__() > 0
        pass

    @staticmethod
    def getValue(dictionary: dict, name: str) -> str:
        for key in dictionary.keys():
            if key == name:
                return dictionary[key]
                pass
            pass
        pass

    pass
