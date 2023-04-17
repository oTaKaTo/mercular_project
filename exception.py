class AccountNotFoundException(Exception):
    def __init__(self):
        self.__msg = "Account Not Found"
    
    @property
    def msg(self):
        return self.__msg
    
class CartErrorException(Exception):
    def __init__(self, msg: str):
        self.__msg = msg
    
    @property
    def msg(self):
        return self.__msg