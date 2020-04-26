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

    @staticmethod
    def writeAllText(path: str, content: str, encoding: str) -> None:
        file = open(path, mode="w", encoding=encoding)
        file.write(content)
        file.close()
        pass

    pass
