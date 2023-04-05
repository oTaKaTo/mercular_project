class AccountNotFoundException(Exception):
    msg = "Account Not Found"
    
class CartEmptyException(Exception):
    msg = "Cart is empty"

class ItemNotFoundException(Exception):
    msg = "Item not found"