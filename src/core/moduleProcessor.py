class moduleProcessor:
    @staticmethod
    def checkParams(params: list,max = None):
        if max == None:
            if params.__len__() < 0:
                print("At least one parameter must be declared in the modules!")
                return "$ERROR"
                pass
            pass
        else:
            if params.__len__() < 0:
                print("At least one parameter must be declared in the modules!")
                return "$ERROR"
                pass
            if params.__len__() > max:
                print("A maximum of " + max.__str__() + " parameter can be entered.")
                return "$ERROR"
                pass
            pass
        return "$NONERROR"
        pass

    pass
