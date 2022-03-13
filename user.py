class User:
    def __init__(self):
        self.__userName = None
        self.__passKey = None
    def getUserName(self):
        return self.__userName
    def setUserName(self,username:str):
        self.__userName = username
    def getPassKey(self):
        return self.__passKey
    def setPassKey(self,passkey:str):
        self.__passKey = passkey
    