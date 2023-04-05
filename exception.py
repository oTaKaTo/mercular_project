from enum import Enum

class AccountNotFoundException(Exception):
    msg = "User Not Found"
     
class CartErrorException(Exception):
     msg = "Cart is empty"