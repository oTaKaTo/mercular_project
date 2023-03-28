class ProductCatalog:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        if product.get_product_id() in self.__products:
            return False
        self.__products[product.get_product_id()] = product
        return True

    def search_by_id(self, product_id):
        return self.__products[product_id]

    def remove_product(self, product_id):
        if product_id in self.__products:
            del self.__products[product_id]
            return True
        return False

    def edit_product(self, product):
        id = product.get_product_id()
        if id in self.__products:
            self.__products[id] = product
            return True
        return False
    
    def add_promotion(self,product_id,promotion):
        self.__products[product_id].add_promotion(promotion)
        return True

    def get_product_info(self):
        return [self.__products[x].get_name() for x in self.__products]
    
    def update_quantity(self, quantity):
        pass
    
    
    def search_keyword(self,keyword=""):
        search_result = []
        for i in self.__products:
            print(keyword.lower(), (self.__products[i].get_name()).lower() )
            if keyword.lower() in (self.__products[i].get_name()).lower():
                search_result.append(self.__products[i])
            if keyword.lower() == self.__products[i].get_product_id():
                return self.__products[i]   
        return search_result
                
    
class Item:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_price(self):
        return self.__product.get_price() * self.__quantity
    
    def get_item(self):
        return str(self.__product.get_name()) + ' ' + str(self.__quantity)
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        self.__quantity = quantity
        return True



class Product:
    def __init__(self, product_id, object_id, name, type, brand, price,amount, detail="",image=[], option=[]):
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
    
    def add_promotion(self, promotion):
        self.__promotion.append(promotion)
        return True
    
    def get_price(self):
        return self.__price
    
    def get_product_id(self):
        return str(self.__product_id)
    
    def get_type_brand_id(self):
        return {"type": self.__type, "brand": self.__brand, "id": self.__product_id}

    def get_name(self):
        return self.__name
    
    def edit(self):
        pass