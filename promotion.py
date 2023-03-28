from datetime import date

class Promotion:
    # due_date format = DD-MM-YYYY
    def __init__(self, due_date, minimum_price, description=""):
        self.__due_date = due_date
        self.__minimum_price = minimum_price
        self.__description = description

    def is_available_price(self, price):
        today = date.today()
        d, m, y = [int(x) for x in self.__due_date.split('-')]
        due_date = date(y, m, d)
        if today > due_date:
            return False
        if price < self.__minimum_price:
            return False
        return True
    
    def get_description(self):
        return self.__description

class FlatDiscount(Promotion):
    def __init__(self, due_date, minimum_price, discount, description=""):
        Promotion.__init__(self, due_date, minimum_price, description)
        self.__discount = discount

    def get_discount(self, price):
        if self.is_available_price(price):
            return self.__discount
        return 0

class PercentageDiscount(Promotion):
    def __init__(self, due_date, minimum_price, discount_percent, max_discount, description=""):
        Promotion.__init__(self, due_date, minimum_price, description)
        self.__discount_percent = discount_percent
        self.__max_discount = max_discount
    
    def get_discount(self, price):
        if self.is_available_price(price):
            discount = (100 - self.__discount_percent) * price / 100
            if discount > self.__max_discount:
                return self.__max_discount
            return discount
        return 0

class Coupon(Promotion):
    def __init__(self, quantity, code_id, ban_products=[], ban_types=[], types="All", brands="All"):
        self.__quantity = quantity
        self.__code_id = code_id
        self.__ban_products = ban_products
        self.__ban_types = ban_types
        self.__types = types
        self.__brands = brands

    def get_id(self):
        return self.__code_id

    def is_available_type(self, data):
        if self.__quantity < 1:
            return False
        # data = product.get_type_brand_id()
        if data["type"] in self.__ban_types:
            return False
        if data["id"] in self.__ban_products:
            return False
        if self.__types == "All":
            if self.__brands == "All":
                return True
            if data["brand"] in self.__brands:
                return True
        if data["type"] in self.__types:
            if self.__brands == "All":
                return True
            if data["brand"] in self.__brands:
                return True
        return False

class FlatCoupon(FlatDiscount, Coupon):
    def __init__(self, due_date, minimum_price, discount, quantity, code_id, description="", ban_products=[], ban_types=[], types="All", brands="All"):
        FlatDiscount.__init__(self, due_date, minimum_price, discount, description)
        Coupon.__init__(self, quantity, code_id, ban_products=[], ban_types=[], types="All", brands="All")
    
    def is_available(self, price, data):
        if self.is_available_price(price) and self.is_available_type(data):
            return True
        return False

class PercentageCoupon(PercentageDiscount, Coupon):
    def __init__(self, due_date, minimum_price, discount_percent, max_discount, quantity, code_id, description="", ban_products=[], ban_types=[], types="All", brands="All"):
        PercentageDiscount.__init__(self, due_date, minimum_price, discount_percent, max_discount, description)
        Coupon.__init__(self, quantity, code_id, ban_products=[], ban_types=[], types="All", brands="All")
    
    def is_available(self, price, data):
        if self.is_available_price(price) and self.is_available_type(data):
            return True
        return False


class CouponCatalog:
    def __init__(self):
        self.__coupons = {}

    def get_available_coupon(self, price, data):
        available_coupon = []
        for coupon in self.__coupons:
            if coupon.is_available(price, data):
                available_coupon.append(coupon)
        return available_coupon

    def add_coupon(self, coupon):
        self.__coupons[coupon.get_id()] = coupon
        return True

    def delete_coupon(self, id):
        del self.__coupons[id]
        return True

# data = {"type": "keyboard", "brand": "razor", "id": "1234"}
# price = 200

# my_coupon = FlatCoupon("26-3-2023", 100, 50, 1, "asdf", "123")
# my_pc_coupon = PercentageCoupon("23-3-2023", 100, 20, 10, 1, "12301294")
# my_coupon_catalog = CouponCatalog()
# my_coupon_catalog.add_coupon(my_coupon)
# my_coupon_catalog.add_coupon(my_pc_coupon)
# print(my_coupon_catalog.get_available_coupon(price, data)[1].get_discount(price))


