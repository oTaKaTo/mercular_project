class Promotion:
    def __init__(self, duration, description):
        self.__duration = duration
        self.__description = description

    def is_available(self):
        pass


class FlatDiscount(Promotion):
    def __init__(self, duration, description, discount):
        Promotion.__init__(self, duration, description)
        self.__discount = discount

    def get_discount():
        pass


class PercentageDiscount(Promotion):
    def __init__(self, duration, description, discount_percent, max_discount):
        Promotion.__init__(self, duration, description)
        self.__discount_percent = discount_percent
    
    def get_discount():
        pass


class Coupon(Promotion):
    def __init__(self, quantity, duration, code_id, discount, description):
        Promotion.__init__(self, duration, description)
        self.__discount = discount
        self.__quantity = quantity
        self.__code_id = code_id
    
    def get_discount():
        pass


class CouponCatalog():
    def __init__(self):
        self.__coupons = []

    def get_available_coupon(self):
        pass


p = Promotion(12, 1)

print(p.__description)
