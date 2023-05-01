from datetime import date
from itertools import count

class Promotion:
    # due_date format = DD-MM-YYYY
    def __init__(self, due_date:str, minimum_price:int, title:str="", description:str=""):
        self.__due_date = due_date
        self.__minimum_price = minimum_price
        self.__description = description
        self.__title = title

    def is_available_date(self):
        today = date.today()
        d, m, y = [int(x) for x in self.__due_date.split('-')]
        due_date = date(y, m, d)
        if today > due_date:
            return False
        return True

    def is_available_price(self, price):
        if price < self.__minimum_price:
            return False
        return True
    
    def get_description(self):
        return self.__description
    
    def get_minimum_price(self):
        return self.__minimum_price
    
    def get_minimum_price_str(self):
        return str(self.__minimum_price) + '.-'
    
    def get_due_date_str(self):
        month = ["ม.ค.", 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.']
        dmy = self.__due_date.split('-')
        return dmy[0] + ' ' + month[int(dmy[1]) - 1] + ' ' + dmy[2]
    
    def get_title(self):
        return self.__title

class FlatDiscount(Promotion):
    def __init__(self, due_date:str, minimum_price:int, discount:int, title:str="", description:str=""):
        Promotion.__init__(self, due_date, minimum_price, title, description)
        self.__discount = discount

    def get_discount(self, price):
        if self.is_available_price(price):
            return self.__discount
        return 0
    
    def get_discount_str(self):
        return str(self.__discount) + '.-'

class PercentageDiscount(Promotion):
    def __init__(self, due_date:str, minimum_price:int, discount_percent:int, max_discount:int, title:str="", description:str=""):
        Promotion.__init__(self, due_date, minimum_price, title, description)
        self.__discount_percent = discount_percent
        self.__max_discount = max_discount
    
    def get_discount(self, price):
        if self.is_available_price(price):
            discount = (100 - self.__discount_percent) * price / 100
            if discount > self.__max_discount:
                return self.__max_discount
            return discount
        return 0
    
    def get_discount_str(self):
        return str(self.__discount_percent) + '%'
    
coupon_id_gen = count()

class Coupon(Promotion):
    
    def __init__(self, quantity:int, coupon_type:str, ban_products:list=[], ban_types:list=[], types:list=[], brands:list=[]):
        self.__quantity = quantity
        self.__code_id = next(coupon_id_gen)
        self.__ban_products = ban_products
        self.__ban_types = ban_types
        self.__types = types
        self.__brands = brands
        self.__coupon_type = coupon_type

    def use(self):
        if self.__quantity > 0:
            self.__quantity -= 1
        return True

    def get_id(self):
        return str(self.__code_id)
    
    def get_coupon_type(self):
        return self.__coupon_type
    
    def get_types(self):
        if(self.__types == []):
            return ["ทั้งหมด"]
        return self.__types

    def use_coupon(self):
        self.__quantity -= 1
        return self.__quantity

    def is_available_type(self, data):
        if self.__quantity < 1:
            return False
        # data = product.get_type_brand_id()
        if data["type"] in self.__ban_types:
            return False
        if data["id"] in self.__ban_products:
            return False
        if self.__types == []:
            if self.__brands == []:
                return True
            if data["brand"] in self.__brands:
                return True
        if data["type"] in self.__types:
            if self.__brands == []:
                return True
            if data["brand"] in self.__brands:
                return True
        return False
    
    def is_available(self, price, data):
        if self.is_available_price(price) and self.is_available_type(data) and self.is_available_date():
            return True
        return False

class FlatCoupon(FlatDiscount, Coupon):
    def __init__(self, due_date:str, minimum_price:int, discount:int, quantity:int, coupon_type:str, title:str="", description:str="", ban_products:list=[], ban_types:list=[], types:list=[], brands:list=[]):
        FlatDiscount.__init__(self, due_date, minimum_price, discount, title, description)
        Coupon.__init__(self, quantity, coupon_type, ban_products, ban_types, types, brands)

class PercentageCoupon(PercentageDiscount, Coupon):
    def __init__(self, due_date:str, minimum_price:int, discount_percent:int, max_discount:int, quantity:int, coupon_type:str, title:str="", description:str="", ban_products:list=[], ban_types:list=[], types:list=[], brands:list=[]):
        PercentageDiscount.__init__(self, due_date, minimum_price, discount_percent, max_discount, title, description)
        Coupon.__init__(self, quantity, coupon_type, ban_products, ban_types, types, brands)

class CouponCatalog:
    def __init__(self):
        self.__coupons = []

    def get_available_coupon(self, price, data):
        available_coupon = []
        for coupon in self.__coupons:
            if coupon.is_available(price, data):
                available_coupon.append(coupon)
        return available_coupon
    
    def get_coupons(self):
        return self.__coupons

    def add_coupon(self, coupon):
        self.__coupons.append(coupon)
        return True
    
    def edit_coupon(self, coupon):
        id = int(coupon.get_id())
        if id < len(self.__coupons):
            self.__coupons[id] = coupon
            return True
        return False

    def delete_coupon(self, id):
        self.__coupons[int(id)] = None
        return True
    
    def get_coupons_sorted_by_coupon_type(self):
        sorted_coupon = {'exclusive':[], 'speaker':[], 'gaming':[], 'computer':[], 'table':[]}
        for coupon in self.__coupons:
            coupon_type = coupon.get_coupon_type()
            if coupon_type in sorted_coupon:
                sorted_coupon[coupon_type].append(coupon)
        return sorted_coupon
            



