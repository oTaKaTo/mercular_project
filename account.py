from product import Product,ProductCatalog
from shipping_address import ShippingAddress
from promotion import Coupon,CouponCatalog,Promotion
from cart import Cart
from copy import copy
from uuid import uuid4
from order import Order
from order_history import OrderHistory
from product import Item

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
          if isinstance(new_phone_number,str):
               self.__phone_number = new_phone_number
               return True
          return False

class Admin(Account):
     def __init__(self, username, password, email, phone_number=""):
          Account.__init__(self, username, password, email, phone_number)

          
     def add_item_to_product_catalog(self, product: Product, product_catalog):
          if product_catalog.add_product(product):
               return True
          return False
     
     def edit_item_in_product_catalog(self,product_id:str, new_product:Product, product_catalog):
          if product_catalog.edit_product(product_id,new_product):
               return True
          return False
     
     def del_item_in_product_catalog(self, product: Product, product_catalog):
          if product_catalog.remove_product(product):
               return True
          return False
     
     def add_coupon_to_coupon_catalog(self,coupon:Coupon, coupon_catalog: CouponCatalog):
          if coupon_catalog.add_coupon(coupon):
               return True
          return False
     
     def edit_coupon_in_coupon_catalog(self, coupon_id, new_coupon:Coupon, coupon_catalog: CouponCatalog):
          if coupon_catalog.edit_coupon(coupon_id,new_coupon):
               return True
          return False
     
     def del_coupon_in_coupon_catalog(self, coupon_id, coupon_catalog: CouponCatalog):
          if coupon_catalog.delete_coupon(coupon_id):
               return True
          return False
     
     def add_product_promotion(self, product: Product, promotion: Promotion):
          if product.add_promotion(promotion):
               return True
          return False
class User(Account):
     
     def __init__(self, username, password, email, phone_number:int="", person_data="", address=[], cart="",order_history="", order=[], coupon=[]):
        Account.__init__(self, username, password, email, phone_number)
        self.__person_data = person_data
        self.__address = [] # List of Shipping_Address Object 
        self.__cart = cart# Cart object
        self.__order_history = order_history # OrderHistory object
        self.__user_coupons = [] # List for store Coupon object
        self.__used_user_coupons = []
        self.__expire_user_coupons = []
        
     def get_user_data(self):
          return self.__person_data

     def get_user_coupon(self):
          return self.__user_coupons
     
     def get_used_user_coupon(self):
          return self.__used_user_coupons
     
     def get_expire_coupon(self):
          return self.__expire_user_coupons

     def get_address(self):
          return self.__address

     def get_person_data(self):
          return self.__person_data

     def get_user_cart(self):
          return self.__cart
     
     def add_item_to_cart(self, items: Item):
         self.__cart.add_item(items)
         return self.__cart
     
     def get_order_history(self):
          return self.__order_history
          
     def check_coupon_id_in_user_coupon(self,coupon_id):
          for coupon in self.__user_coupons:
               if coupon.get_id()==coupon_id:
                    return coupon
          for coupon in self.__used_user_coupons:
               if coupon.get_id()== coupon_id:
                    return coupon
          for coupon in self.__expire_user_coupons:
               if coupon.get_id()== coupon_id:
                    return coupon
          return False
     
     def user_used_coupon(self,used_Coupon_id):
          for Coupon in self.__user_coupons:
               if used_Coupon_id == str(Coupon.get_id()):
                    if Coupon.use_coupon()<1:
                         self.__used_user_coupons.append(copy(Coupon))
                         self.__user_coupons.remove(Coupon)
                    return True
          else:
               return False
               
     def add_user_coupon(self, coupon_id, system_coupon_catalog):
          for coupon in system_coupon_catalog:
               if str(coupon.get_id()) == coupon_id:
                    if self.check_coupon_id_in_user_coupon(coupon_id)!=False:
                         return "This coupon has in already in your coupon"
                    else:
                         self.__user_coupons.append(copy(coupon))
                         return True
          return "Invaild Coupon ID"
     
     def add_address(self,name_surname, phone_number, address, sub_district, district, province, postal_code):
          self.__address.append(ShippingAddress(name_surname,phone_number,address,sub_district,district,province,postal_code))
          return True
     
     def delete_address(self,address):
          self.__address.remove(address)
          return True
     
     def create_order(self, payment_method, total_price, discounted_price, status, selected_shipping_address, system_order_container):
          items_list = copy(self.__cart.get_selected_items())
          
          new_order = Order(payment_method, 
                         total_price,
                         discounted_price,
                         status,
                         items_list,
                         selected_shipping_address)
          
          self.__cart.get_selected_items().clear()  
          system_order_container.append(new_order)
          self.__order_history.add_order(new_order)
          print(self.__order_history.get_order_info())
          
          
          return new_order