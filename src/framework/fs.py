class fs:
    @staticmethod
    def readAllText(path: str, encoding: str) -> str:
        file = open(path, mode="r", encoding=encoding)
        content = ""
        for line in file.readlines():
            content += line
            pass
        file.close()
        return content
        pass
    pass
