from Product import *
from Shipping_Address import *
from copy import copy
class Account:
     def __init__(self, username, password, email, phone_number,online_status:bool=None):
          self.__username = username
          self.__password = password #must be hash before store
          self.__email = email
          self.__phone_number = phone_number
          self.__online_status = online_status
    
     def get_Email(self):
          return self.__email
    
     def get_username(self):
          return self.__username
     
     def get_online_status(self):
          return self.__online_status
    
     def set_online_status(self,new_online_status):
          if isinstance(new_online_status,bool):
               self.__online_status = new_online_status
               return True
          return False
     
     def set_username(self,new_username):
          if isinstance(new_username,str):
               self.__username = new_username
               return True
          return False
     
     def get_password(self):
          return self.__password
     
     def get_phone_number(self):
          return self.__phone_number
     
     def set_phone_number(self,new_phone_number):
          if isinstance(new_phone_number,int):
               self.__phone_number = new_phone_number
               return True
          return False          

         
class Admin(Account):
     __product_catalog = []
     def __init__(self, username, password, email, phone_number, product_catalog, coupon, promotion, order):
            Account.__init__(self, username, password, email, phone_number)
            self.__product_catalog = product_catalog # ProductCataog object
            self.__coupon = coupon # Coupon object
            self.__promotion = promotion # Promotion object
            self.__order = order # Order object (specific user) 
          
class User(Account):
     def __init__(self, username, password, email, phone_number:int=None, person_data=None, address=None, cart=None, order=None,  order_history=None, coupon=None):
        Account.__init__(self, username, password, email, phone_number)
        self.__person_data = person_data
        self.__address = [] # List of Shipping_Address Object 
        self.__cart = cart # Cart object
        self.__order_history = order_history # OrderHistory object
        self.__user_coupons = [] # List for store Coupon object
        self.__used_user_coupons = []
     
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
         item = Item(product, quantity)
         self.__cart.add_item(item)
         return self.__cart

     def get_order_history(self):
          return self.__order_history

     def get_user_coupons(self):
          return self.__coupons
    
     def user_used_coupon(self,Coupon):
          if Coupon in self.__user_coupons:
               self.__used_user_coupons.append(copy(Coupon))
               self.__user_coupons.remove(Coupon)
               return True
          else:
               return False
               
     def add_user_coupon(self,coupon_Id,system_coupon_catalog):
          if coupon_Id in system_coupon_catalog:
               self.__user_coupons.append(copy(system_coupon_catalog[coupon_Id]))
          else:
               return "Invaild Coupon ID"
     
     def add_address(self,name_surname, phone_number, address, sub_district, district, province, postal_code):
          self.__address.append(Shipping_Address(name_surname,phone_number,address,sub_district,district,province,postal_code))
          return True
     
     def delete_address(self,address):
          if len(self.__address)>1:
               self.__address.remove(address)
               return "Remove address success"
          else:
               return"You must have at least 1 address for delivery"

"""momo = User("momo","1234","65010244@gmail.com")
momo.add_address("ที่อยู่แรก","adsad","Sdadsad","ASdasdsa","asdasdsa","asdasdsa","Adsadsa")
momo.add_address("ที่อยู่2","adsad","Sdadsad","ASdasdsa","asdasdsa","asdasdsa","Adsadsa")
print([i.get_name_surname() for i in momo.get_address()])
print("-----------Add Address-----------")
momo.get_address()[0].set_shipping_address("ที่อยู่3","adsad","Sdadsad","ASdasdsa","asdasdsa","asdasdsa","Adsadsa")
print([i.get_name_surname() for i in momo.get_address()])
print("-----------Set Address-----------")
momo.delete_address(momo.get_address()[0])
print([i.get_name_surname() for i in momo.get_address()])
print(momo.delete_address(momo.get_address()[0]))
print([i.get_name_surname() for i in momo.get_address()])
print("-----------Delete Address-----------")"""