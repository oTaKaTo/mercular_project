from account import Account,User,Admin
from shipping_address import ShippingAddress
from order import Order
from order_history import OrderHistory
from promotion import CouponCatalog,PercentageCoupon,PercentageDiscount,FlatCoupon
from product import Product,Item,ProductCatalog
from fastapi import FastAPI,Request,APIRouter
from typing import Union
import json
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

class System:
    def __init__(self):
        self.__user_lst = []
        self.__coupon_catalog = CouponCatalog()
        self.__product_catalog = ProductCatalog()
        self.__order_container = []
    
    def get_order_container(self):
        return self.__order_container
    
    def search_user_by_email(self, email):
        for ID in self.__user_lst:
            if ID.get_email() == email:
                return ID
        return False
   
    def search_coupon_by_coupon_id(self,coupon_id):
        for coupon in self.__coupon_catalog.get_coupons():
            if coupon.get_id() == coupon_id:
                return coupon
        return False
        
    def get_user_lst(self):
        return self.__user_lst
    
    def get_coupon_catalog(self):
        return self.__coupon_catalog
        
    def create_account(self ,email,password, phone_number=None,username=""):
            if self.search_user_by_email(email)!=False:
                
                return False
            else:
                self.__user_lst.append(User(username,password,email,phone_number))
                self.login(email,password)
                return True
    
    def add_admin(self ,email,password, phone_number=None,username=""):
        if self.search_user_by_email(email)!=False:
                return False
        else:
                self.__user_lst.append(Admin(username,password,email,phone_number))
                self.login(email,password)
                return True
        
    def get_product_catalog(self):
        return self.__product_catalog        
    
    def login(self,email,password):
        
        id = self.check_id_password(email,password)
        
        if id != False:
            id.set_online_status(True)
            if isinstance(id,Admin):
                return "Admin"
            return True
        return False
    
    def check_id_password(self,email, password):
            ID = self.search_user_by_email(email)
            if ID!=False:
                if ID.get_password() == password:
                    return ID
            return False
    
    def logout(self,ID):
            ID.set_online_status(False)
            return True
        
    def add_system_product(self,admin,product):
        if isinstance(admin,Admin):
           if self.__product_catalog.add_product(product):
               return True
           else:
               return "already has this product"
        else:
            return "You are not admin"