class ProductCatalog:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        if product.get_product_id() in self.__products:
            return False
        self.__products[product.get_product_id()] = product
        return True

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

    def add_promotion(self, product_id, promotion):
        self.__products[product_id].add_promotion(promotion)
        return True

    def get_product_info(self):
        return [self.__products[x].get_name() for x in self.__products]

    # Checkout then decrease stock
    def update_quantity(self,product_id,amount):
        if self.__products[product_id].get_quantity() < amount:
            return False
        elif self.__products[product_id].get_quantity() >= amount:
            self.__products[product_id].update_quantity(amount)
            return True
    
    def check_quantity(self,product_id,amount):
        if self.__products[product_id].get_quantity() < amount:
            return False
        elif self.__products[product_id].get_quantity() >= amount:
            return True


    def search_keyword(self, keyword=""):
        search_result = []
        for i in self.__products:
            if keyword.lower() in (self.__products[i].get_name()).lower():
                search_result.append(self.__products[i])
            if keyword.lower() == self.__products[i].get_product_id():
                return self.__products[i]
        return search_result

    def search_by_id(self, product_id:str):
        return self.__products[product_id]
    
    def search_by_catagories(self,keyword=""):
        search_result = []
        for i in self.__products:
            for t in reversed((self.__products[i].get_type())):
                if keyword == t:
                    search_result.append(self.__products[i])
        return search_result


class Product:
    # type MUST order by big --> small catagory 
    def __init__(self, product_id:str, object_id:str, name:str, type:list, brand:str, price:int, quantity:int, detail="",image=[], option = ""):
        self.__product_id = product_id
        self.__object_id = object_id
        self.__name = name
        self.__type = type
        self.__brand = brand
        self.__price = price
        self.__quantity = quantity
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
    
    def get_quantity(self):
        return self.__quantity
    
    def get_type(self):
        return self.__type

    def get_type_brand_id(self):
        return {"type": self.__type, 
                "brand": self.__brand, 
                "id": self.__product_id}

    def get_name(self):
        return self.__name 
    
    def get_option(self):
        return self.__option
    
    # decreasing stock
    def update_quantity(self,amount):
        self.__quantity -= amount
        return True
        
    def edit(self):
        pass


class Item:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_price(self):
        return self.__product.get_price() * self.__quantity
    
    def get_item(self):
        item_info = {
            "quantity": self.__quantity,
            "price" : self.__product.get_price(),
            "option": self.__product.get_option()
            }
        return {self.__product.get_name() : item_info}
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        self.__quantity = quantity
        return True
    
    def get_product(self):
        return self.__product
    