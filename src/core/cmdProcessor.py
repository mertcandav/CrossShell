class cmdProcessor:
    @staticmethod
    def clearCmd(cmd: str):
        return cmd.strip()
        pass

    @staticmethod
    def process(cmd: str):
        if cmd.__eq__(""):
            return
            pass

        print("Command not recognized!")
        pass

    pass