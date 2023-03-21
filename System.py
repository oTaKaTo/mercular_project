from Product import Item
from cart import Cart

my_cart = Cart()

class System:
    def __init__(self, product_catalog = []):
        self.__product_catalog = product_catalog
        self.__account_list = []
    
    def find_current_promotion(self):
        pass
    
    def buy_product(self, product_id):
        pass
    
    def create_account(self, username, password, email, phone_number):
        pass
    def check_exists_account(self, username, email):
        pass
    def update_account_list(self, account):
        pass
    def check_id_password(self, user_id, password):
        pass
    
    def request_QR(self, total_price, user_address, cart):
        pass
    def request_credit_debit(self, total_price, card_info, user_address, cart):
        pass
    def request_COD(self, total_price, user_address, cart):
        pass

    def addtocart(self, product, quantity):
        my_cart.add_item_to_cart(Item(product, quantity))
        print("add success")
        return True

