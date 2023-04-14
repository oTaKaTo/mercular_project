from account import Account,User,Admin,shipping_adress
from promotion import Promotion,Coupon,CouponCatalog
from Product import Product,Item,ProductCatalog
from tkinter import Tk
from fastapi import FastAPI
from typing import Union
import json
class System:

    def __init__(self):
        self.__user_lst = [] 
        self.__coupon_catalog = CouponCatalog()
        self.__product_catalog = ProductCatalog()

    def search_user_by_email(self,email):
        for ID in self.__user_lst:
            if ID.get_email() == email:
                return ID
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
    
    def get_product_catalog(self):
        return self.__product_catalog        
    
    def login(self,email,password):
        
        ID = self.check_id_password(email,password)
        
        if ID != False:
            ID.set_online_status(True)
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
        
        
x = shipping_adress("HO","225","SAdasd","asdsad","sada","ASDASDS","asdasdsad")
mySystem = System()
mySystem.create_account("MOMO@gmail.com","1234")
mySystem.search_user_by_email("MOMO@gmail.com").add_address("1234","fgfgs","SAdasd","asdsad","sada","ASDASDS","asdasdsad")
mySystem.search_user_by_email("MOMO@gmail.com").add_address("5678","sdsds","SAdasd","asdsad","sada","ASDASDS","asdasdsad")
print(mySystem.login("MOMO@gmail.com","1234"))
print(mySystem.check_id_password("MOMO@gmail.com","1234"))
"""price= 300
my_coupon = FlatCoupon("26-4-2023", 100, 50, 1)
my_pc_coupon = PercentageCoupon("23-4-2023", 100, 20, 10, 1)
mySystem.get_coupon_catalog().add_coupon(my_coupon)
mySystem.get_coupon_catalog().add_coupon(my_pc_coupon)
print(mySystem.get_coupon_catalog().get_coupon())
mySystem.get_user_lst()["MOMO@gmail.com"].add_user_coupon("2",mySystem.get_coupon_catalog().get_coupon())
mySystem.get_user_lst()["MOMO@gmail.com"].get_user_coupon()
print(mySystem.get_user_lst()) 
print(mySystem.create_account("momo","1234","MOMO@gmail.com"))
print(mySystem.create_account("momo","1234","MOMO@gmail.com"))
print(mySystem.login("MOMO@gmail.com","1234"))
print(mySystem.login("MOMO3@gmail.com","1234"))
print(mySystem.login("MOMO@gmail.com","12345678"))
account_list = mySystem.get_user_lst()
print(account_list["MOMO@gmail.com"].get_online_status())
mySystem.logout(mySystem.get_user_lst()["MOMO@gmail.com"])
print(account_list["MOMO@gmail.com"].get_online_status())"""

"""  
    def Register(email,username,password):
            for ID in self.user_lst:
                if ID.get_email() == email:
                    print ("Email is already use")
                    break;
            else:
                    user_lst.append(User(username,password,email))

    def Login(email,password):
            for ID in user_lst:
                if (ID.get_email() == email)  and ID.get_password()==password:
                    print("Login success")
                    break;
            else:
                    print("invail Email or password")
    def Logout():
            print("Logout Confirm\nY/N")
            while(True):
                Input = input()
                if  Input=="Y":
                    print("Logout Success")
                    break;
                elif Input=="N":
                    print("Continue Login")
                    break;
                else:
                    print("Error!!!!\nPlease Enter Y or N")
Register("momo@gmail.com","momo","1234")
Register("momo@gmail.com","momo","1234")
Login("momo@gmail.com","1234")
"""
#test coupon
"""
#test admin class
price= 300
my_coupon = FlatCoupon("26-4-2023", 100, 50, 1)
my_pc_coupon = PercentageCoupon("23-4-2023", 100, 20, 10, 1)
my_coupon_catalog = CouponCatalog()
my_coupon_catalog.add_coupon(my_coupon)
my_coupon_catalog.add_coupon(my_pc_coupon)
mySystem.get_user_lst()[0].add_user_coupon("2",my_coupon_catalog.get_coupon())
print(mySystem.get_user_lst()[0].add_user_coupon("2",my_coupon_catalog.get_coupon()))
print(mySystem.get_user_lst()[0].get_user_coupon()[0].get_id())
print(mySystem.get_user_lst()[0].user_used_coupon(mySystem.get_user_lst()[0].get_user_coupon()[0]))
print(mySystem.get_user_lst()[0].get_used_user_coupons())
mySystem.get_user_lst().append(Admin("Admin","Admin","Admin@gmail.com"))
"""

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World My friend"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "Hi"):
    return {"item_id": item_id, "q": q}

@app.get("/account/profile",tags=["account"])
def read_user_infor():
    return {
            "Username":mySystem.search_user_by_email("MOMO@gmail.com").get_username(),
            "PhoneNumber":mySystem.search_user_by_email("MOMO@gmail.com").get_phone_number(),
            "Email":mySystem.search_user_by_email("MOMO@gmail.com").get_email()
            }

@app.get("/account/shipping_address",tags=["account"])
def read_user_shipping_address_infor():
    shipping_address_dict = {}
    k= 1
    for i in mySystem.search_user_by_email("MOMO@gmail.com").get_address():
        x = {"name_surname" : i.get_name_surname(),
             "phone_number":i.get_phone_number(),
             "address":i.get_address(),
             "sub_district":i.get_sub_district(),
             "district":i.get_district(),
             "province":i.get_province(),
             "postal_code":i.get_postal_code()}
        shipping_address_dict[f"Address{k}"] = x
        k +=1
    return shipping_address_dict 

@app.post("/login",tags=["account"])
def  login(data:dict):
     email = data["email"]
     password = data["password"]
     x = mySystem.login(email,password)
     if x != False:
         return {"Login":f"{email} Login Success"}
     else:
         return {"Login":"email or password invaild"}

@app.post("/register",tags=["account"])
def register(data:dict):
    email = data["email"]
    password = data["password"]
    x = mySystem.create_account(email,password)
    if x == True :
        return {"Register":len(mySystem.get_user_lst())}
    else :
        return {"Register":"failed email is already use"}


@app.post("/{email}/account/add_shipping_address" , tags=["account"])
def add_shipping_address(email:str,data:dict):
    name_surname = data["name_surname"]
    phone_number = data["phone_number"]
    address = data["address"]
    sub_district = data["sub_district"]
    district = data["district"]
    province = data["province"] 
    postal_code = data["postal_code"]
    print("Hi")
    id =mySystem.search_user_by_email(email)
    if id !=False:
        id.add_address(name_surname, phone_number, address, sub_district, district, province, postal_code)
        return {"Success":f"address number {address} add complete in to {email}"}
    else:
        return {"Failed":"Email Not found"}

@app.put("/{email}/account/{address_id}/delete_shipping_address",tags=["account"])
def delete_shipping_address(email:str,address_id:int):
    id = mySystem.search_user_by_email(email)
    if id!=False:
        if address_id < len(id.get_address()) and address_id>=0:
            responce = id.delete_address(id.get_address()[address_id])
            if responce == True:
                return {"Success":f"delete address number {address_id +1} form {email}"}
            else:
                return {"failed":f"You Much have at least 1 address for shipping"}
        else:
            return {"failed":f"Address_id not found"}
    else:
        return {"failed":f"Email not found"}

@app.put("/{email}/account/{address_id}/edit_shipping_address",tags=["account"])
def edit_shipping_address(email:str,address_id:int,data:dict):
        new_name_surname = data["new_name_surname"]
        new_phone_number = data["new_phone_number"]
        new_address = data["new_address"]
        new_sub_district = data["new_sub_district"]
        new_district = data["new_district"]
        new_province = data["new_province"] 
        new_postal_code = data["new_postal_code"]
        id = mySystem.search_user_by_email(email)
        if id!=False:
            if address_id < len(id.get_address()) and address_id>=0:
                id.get_address()[address_id].edit_shipping_address(new_name_surname,new_phone_number,new_address,new_sub_district,new_district,new_province,new_postal_code)
                return {"Success":f"edit address number {address_id +1} form {email}"}
            else:
                return {"failed":f"Address_id not found"}
        else:
            return {"failed":f"Email not found"}

@app.put("/{email}/account/edit_username",tags=["account"])
def edit_username(email:str,data:dict):
    new_username = data["new_username"]
    id = mySystem.search_user_by_email(email)
    if id!= False:
        if id.edit_username(new_username):
            return {"Success":f"edit username from {email}"}
        else:
            return {"failed":"Something but i dont know"}
    else:
        return {"failed":"email not found"}
