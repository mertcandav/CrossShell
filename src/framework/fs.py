# Imports.
import os

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

    @staticmethod
    def getFiles(path: str) -> list:
        dirs = os.listdir(path)
        dirs = (val for val in dirs if os.path.isfile(val) == True)
        return dirs
        pass

    @staticmethod
    def getDirectories(path: str) -> list:
        dirs = os.listdir(path)
        dirs = (val for val in dirs if os.path.isfile(val) == False)
        return dirs
        pass

    pass
