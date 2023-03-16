class ProductCatalog:
    def __init__(self):
        self.__product = []

    def add_product(self, product):
        pass

    def remove_product(self,product):
        pass

    def edit_product(self):
        pass


class Product:
    def __init__(self, product_id, object_id, name, type, brand, price, detail="", promotion=[], image=[], option=[]):
        self.__product_id = product_id
        self.__object_id = object_id
        self.__name = name
        self.__type = type
        self.__brand = brand
        self.__price = price
        self.__image = image
        self.__option = option
        self.__detail = detail
        self._promotion = promotion
        
    def add_promotion(promotion):
        self._promotion.append(promotion)
