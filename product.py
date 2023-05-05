from promotion import *

class ProductCatalog:
    def __init__(self):
        self.__products = []

    def get_products(self):
        return self.__products
    
    def get_object_products(self):
        product_list = []
        product_list.append(self.__products[0])
        for i in self.__products:
            status = False
            for j in product_list:
                if i.get_object_id() in  j.get_object_id():
                    status = True
            if status == True:
                status = False
                continue
            product_list.append(i)
        return product_list    
    
    def get_object_products_by_brand(self,brand):
        product_list = []
        for i in self.__products:
            status = False
            for j in product_list:
                if i.get_object_id() in  j.get_object_id():
                    status = True
            if status == True:
                status = False
                continue        
            if brand.lower() in (i.get_brand()).lower():
                product_list.append(i)
        return product_list    
    
    def get_object_products_by_type(self,type):
        product_list = []
        for i in self.__products:
            status = False
            for j in product_list:
                if i.get_object_id() in  j.get_object_id():
                    status = True
            if status == True:
                status = False
                continue        
            if type in (i.get_type()):
                product_list.append(i)
        return product_list    
    
    def get_promotional_products(self,type:str):
        promotional_products = []
        for i in self.__products:
            if i.get_type() == type:
                if i.get_promotions() != None:
                    promotional_products.append(i)
        return promotional_products

    def get_product_info(self,object_id:str):
         for i in self.__products:
            if object_id in i.get_object_id():
                return i

    def search_by_id(self,product_id:str):
        for i in self.__products:
            if product_id in i.get_product_id():
                return i

    def get_option(self,object_id):
        option=[]
        for i in self.__products:
            if object_id in i.get_object_id():
                option.append({"product_id" : i.get_product_id(), "option": i.get_option()})
        return option 
    
    def add_product(self, product):
        for i in self.__products:
            if product.get_product_id() in i.get_product_id():
                return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id):
        for i in self.__products:
            if product_id in i.get_product_id():
                del self.__products[product_id]
                return True
        return False

    def checkout_product(self,product_id,quantity):
        for pd in self.__products:
            if product_id in pd.get_product_id():
                pd.checkout_quantity(quantity)
        return True
                


    def edit_product(self, product_id,new_product):
        for pd in self.__products:
            if product_id in pd.get_product_id():
                pd = new_product
                return {"status":"edited success"}
        return {"status": "No product"}

    def add_promotion(self, product_id, promotion):
        self.__products[product_id].add_promotion(promotion)
        return True
    
    

 

    # search box that can search by id, name
    def search(self,keyword=""):
        search_result = []
        for pd in self.get_object_products():
            if keyword in pd.get_name() or keyword in pd.get_type() or keyword in pd.get_product_id():
                search_result.append(pd)
        return search_result


class Product:
    # type MUST order by big --> small catagory 
    def __init__(self, product_id:str, object_id:str, name:str, type:str, brand:str, price:int, quantity:int, detail={},image=[], option="",promotion=None):
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
        self.__promotion = promotion
    
            
    def get_price(self):
        return float(self.__price)
         
    def get_product_id(self):
        return str(self.__product_id)
    
    def get_object_id(self):
        return str(self.__object_id)
    
    def get_brand(self):
        return self.__brand
    
    def get_quantity(self):
        return int(self.__quantity)
    
    def get_discounted_price(self):
        if self.__promotion:
            discounted_price = self.__price - self.__promotion.get_discount(self.__price)
            return discounted_price
        return self.__price
    
    def get_image(self):
        return self.__image
    
    def get_type(self):
        return self.__type
 
    def get_type_brand_id(self):
        return {"type": self.__type, "brand": self.__brand, "id": self.__product_id}
    
    def get_option(self):
        return self.__option
     
    def get_name(self):
        return self.__name 
    
    def get_detail(self):
        return self.__detail
    
    def get_promotion(self):
        return self.__promotion

    def add_promotion(self, promotion:Promotion):
        self.__promotion = promotion
        return True

    def edit_quantity(self,value):
        self.__quantity = value

    # decreasing stock
    def checkout_quantity(self,amount):
        self.__quantity -= amount
        return True
        


class Item:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_price(self):
        return self.__product.get_discounted_price()
    
    def get_item(self):
            item_info = {
                "product_option": self.__product.get_option(), 
                "quantity": int(self.__quantity)
                }
            brand_id = self.__product.get_type_brand_id()
            for KEY in brand_id.keys():
                item_info[KEY] = brand_id[KEY]

            return {self.__product.get_name() : item_info}
    
    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        self.__quantity = quantity
        return True
    
    def get_type_brand_id(self):
        return self.__product.get_type_brand_id()
    
    def get_amount(self):
        return self.__product.get_quantity()