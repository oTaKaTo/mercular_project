class Account:
    def __init__(self, username, password, email, phone_number):
        self.__username = username
        self.__password = password #must be hash before store
        self.__email = email
        self.__phone_number = phone_number

class Admin(Account):
    __product_catalog = []

    def __init__(self, username, password, email, phone_number, product_catalog, coupon, promotion, order):
            Account.__init__(self, username, password, email, phone_number)
            self.__product_catalog = product_catalog # ProductCataog object
            self.__coupon = coupon # Coupon object
            self.__promotion = promotion # Promotion object
            self.__order = order # Order object (specific user) 
   
        
class User(Account):
     def __init__(self, username, password, email, phone_number, person_data, address, cart, order,  order_history, coupon):
        Account.__init__(self, username, password, email, phone_number)
        self.__person_data = person_data
        self.__address = [] # List of Shipping_Address Object 
        self.__cart = cart # Cart object
        self.__order_history = order_history # OrderHistory object
        self.__coupons = [] # List for store Coupon object
     
     def get_user_data(self):
          return self.__person_data
     def get_user_coupon(self):
          return self.__coupons
     def get_address(self):
          return self.__address
