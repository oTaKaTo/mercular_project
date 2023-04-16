from Product import Product
from shipping_address import shipping_adress
from cart import Cart
from copy import copy
from uuid import uuid4
class Account:
     def __init__(self, username, password, email, phone_number="",online_status:bool=False):
          self.__username = username
          self.__password = password #must be hash before store
          self.__email = email
          self.__phone_number = phone_number
          self.__online_status = online_status
          self.__user_id = uuid4()
     
     def get_email(self):
          return self.__email
     
     def get_id(self):
          return self.__user_id
     
     def get_username(self):
          return self.__username
     
     def get_online_status(self):
          return self.__online_status
     
     def set_online_status(self,new_online_status):
          if isinstance(new_online_status,bool):
               self.__online_status = new_online_status
               return True
          return False
     
     def edit_username(self,new_username):
          if isinstance(new_username,str):
               self.__username = new_username
               return True
          return False
     
     def get_password(self):
          return self.__password
     
     def get_phone_number(self):
          return self.__phone_number
     
     def edit_phone_number(self,new_phone_number):
          if isinstance(new_phone_number,int):
               self.__phone_number = new_phone_number
               return True
          return False          

class Admin(Account):
     __product_catalog = []
     def __init__(self, username, password, email, phone_number="", product_catalog={}, coupon={}, promotion ={}, order=[]):
            Account.__init__(self, username, password, email, phone_number)
            self.__product_catalog = product_catalog # ProductCataog object
            self.__coupon = coupon # Coupon object
            self.__promotion = promotion # Promotion object
            self.__order = order # Order object (specific user) 
            
          
     def add_item_to_product_catalog(self,product:Product,product_catalog:dict):
          product_catalog[product.get_product_id()] = product
     
     def edit_item_in_product_catalog(self,product:Product,product_catalog:dict):
          pass
     
     def del_item_in_product_catalog(self,product:Product,product_catalog:dict):
          product_catalog.pop(product_catalog[product.get_product_id()])   
          
class User(Account):
     
     def __init__(self, username, password, email, phone_number:int="", person_data="", address=[], cart="", order=[],  order_history=[], coupon=[]):
        Account.__init__(self, username, password, email, phone_number)
        self.__person_data = person_data
        self.__address = [] # List of Shipping_Address Object 
        self.__cart = Cart()# Cart object
        self.__order_history = order_history # OrderHistory object
        self.__user_coupons = [] # List for store Coupon object
        self.__used_user_coupons = []
        self.__expire_user_coupons = []
     
     def get_used_user_coupons(self):
          return self.__used_user_coupons
     
     def get_user_data(self):
          return self.__person_data

     def get_user_coupon(self):
          return self.__user_coupons

     def get_address(self):
          return self.__address

     def get_person_data(self):
          return self.__person_data

     def get_user_cart(self):
          return self.__cart

     def add_item_to_cart(self, product, quantity):
         item = item(product, quantity)
         self.__cart.add_item(item)
         return self.__cart

     def get_order_history(self):
          return self.__order_history

     def get_user_coupons(self):
          return self.__coupons
    
     def check_coupon_id_in_user_coupon(self,coupon_id):
          for coupon in self.__user_coupons:
               if coupon.get_id()==coupon_id:
                    return coupon
          else:
               return False
       
     def user_used_coupon(self,Coupon):
          if self.check_coupon_id_in_user_coupon(Coupon.get_id())!=False:
               if Coupon.use_coupon()<1:
                    self.__used_user_coupons.append(copy(Coupon))
                    self.__user_coupons.remove(Coupon)
               print(Coupon.get_quantity())
               return True
          else:
               return False
               
     def add_user_coupon(self,coupon_Id,system_coupon_catalog):
          if coupon_Id in system_coupon_catalog:
               if self.check_coupon_id_in_user_coupon(coupon_Id)!=False:
                    return "This coupon has in already in your coupon"
               else:
                    self.__user_coupons.append(copy(system_coupon_catalog[coupon_Id]))
                    return True     
          else:
               return "Invaild Coupon ID"
     
     def add_address(self,name_surname, phone_number, address, sub_district, district, province, postal_code):
          self.__address.append(shipping_adress(name_surname,phone_number,address,sub_district,district,province,postal_code))
          return True
     
     def delete_address(self,address):
          if len(self.__address)>1:
               self.__address.remove(address)
               return True
          else:
               return False
