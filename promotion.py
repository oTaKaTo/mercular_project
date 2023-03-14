class Promotion:
    def __init__(self, duration, description, relevant_products):
        self.__duration = duration
        self.__description = description
        self.__relevant_products = relevant_products

    def is_available(duration):
        pass


class FlatDiscount(Promotion):
    def __init__(self, duration, description, discount):
        Promotion.__init__(self, duration, description)
        self.__discount = discount


class PercentageDiscount(Promotion):
    def __init__(self, duration, description, discount_percent):
        Promotion.__init__(self, duration, description)
        self.__discount_percent = discount_percent


class Coupon(Promotion):
    def __init__(self, quantity, duration, code_id, discount, description):
        Promotion.__init__(self, duration, description)
        self.__discount = discount
        self.__quantity = quantity
        self.__code_id = code_id


class CouponCatalog():
    def __init__(self):
        self.__coupons = []

    def get_available_coupon(self):
        pass


p = Promotion(12, 1)

print(p.__description)
