class ProductCatalog:
    def __init__(self):
        self.__products = []

    @property
    def products(self):
        return self.__products
    
    def add_product(self, product):
        for i in self.__products:
            if product.product_id in i.product_id:
                return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id):
        for i in self.__products:
            if product_id in i.product_id:
                del self.__products[product_id]
                return True
        return False

    def edit_product(self, product):
        id = product.product_id
        if id in self.__products:
            self.__products[id] = product
            return True
        return False

    def add_promotion(self, product_id, promotion):
        self.__products[product_id].add_promotion(promotion)
        return True
    
    def get_product_info(self):
        return [x.name for x in self.__products]

    # search box that can search by id, name
    def search_keyword(self, keyword=""):
        search_result = []
        for i in self.__products:
            if keyword.lower() == i.product_id:
                return i
            if keyword.lower() in (i.name).lower():
                search_result.append(i)     
        return search_result

    
    def search_by_catagories(self,keyword=""):
        search_result = []
        for i in self.__products:
            for t in reversed(i.type):
                if keyword == t:
                    search_result.append(i)
        return search_result


class Product:
    # type MUST order by big --> small catagory 
    def __init__(self, product_id:str, object_id:str, name:str, type:list, brand:str, price:int, quantity:int, detail="",image=[], option=[]):
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
    
    @property    
    def price(self):
        return self.__price
    
    @property 
    def product_id(self):
        return str(self.__product_id)
    
    @property 
    def quantity(self):
        return self.__quantity
    
    @property 
    def type(self):
        return self.__type

    @property 
    def type_brand_id(self):
        return {"type": self.__type, "brand": self.__brand, "id": self.__product_id}

    @property 
    def name(self):
        return self.__name 
    
    @quantity.setter
    def quantity(self,value):
        self.__quantity = value

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
        return str(self.__product.get_name()) + ' ' + str(self.__quantity)
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        self.__quantity = quantity
        return True
    