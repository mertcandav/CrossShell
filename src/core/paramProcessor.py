class paramProcessor:
    @staticmethod
    def getParams(val: str):
        params = []
        while(val.find("-") != -1):
            dex = val.find("-")
            if dex+1 == val.__len__():
                print("The parameter must be defined after the parameter declaration!")
                return "$ERROR"
                pass
            spacedex = val.find(" ",dex)
            param = ""
            if spacedex == -1:
                param = val[dex+1:]
                pass
            else:
                if dex + 1 == spacedex:
                    print("Cannot space after the parameter declaration!")
                    return "$ERROR"
                    pass
                else:
                    param = val[dex+1:spacedex]
                    pass
                pass
            
            if param in params:
                print(param + "\nA parameter cannot be defined more than once!")
                return "$ERROR"
                pass
            params.append(param)
            val = val[spacedex:]
            if spacedex == -1:
                break
                pass
            pass
        return params
        pass
    pass