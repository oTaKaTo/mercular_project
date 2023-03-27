class ProductCatalog:
    def __init__(self):
        self.__product = []

    def add_product(self, product):
        pass

    def remove_product(self, product):
        pass

    def edit_product(self):
        pass

    def add_promotion(self, product_id, promotion):
        pass

    def get_product_info(self):
        pass

    def check_product_amount(product_id):
        pass

    def update_quantity(self):
        pass

    def search_product(self):
        pass


class Product:
    def __init__(self, product_id, object_id, name, type, brand, price, amount, detail="", image=[], option=[]):
        self.__product_id = product_id
        self.__object_id = object_id
        self.__name = name
        self.__type = type
        self.__brand = brand
        self.__price = price
        self.__amount = amount
        self.__image = image
        self.__option = option
        self.__detail = detail
        self.__promotion = []

    def add_promotion(self):
        pass

    def edit(self):
        pass

    def get_price(self):
        return self.__price
    
    def get_name(self):
        return self.__name

class Item:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_price(self):
        return self.__product.get_price() * self.__quantity
    
    def get_item(self):
        return f"{self.__product.get_name()}: {self.__quantity} item(s)"
    