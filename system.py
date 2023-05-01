from account import Account,User,Admin
from shipping_address import ShippingAddress
from Order import Order
from OrderHistory import OrderHistory
from promotion import Promotion,Coupon,CouponCatalog,PercentageCoupon,PercentageDiscount,FlatCoupon,FlatDiscount
from Product import Product,Item,ProductCatalog
from tkinter import Tk
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

    def search_user_by_email(self,email):
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
        
    def add_system_product(self,admin,product):
        if isinstance(admin,Admin):
           if self.__product_catalog.add_product(product):
               return True
           else:
               return "already has this product"
        else:
            return "You are not admin"
    
               
app = FastAPI()
product = Product("1","2","3","4","5","6","7","8","9","10","11")
item = Item(product,2)
order = Order("Order1","1",99,10,"110","22",[item])
templates = Jinja2Templates(directory="template")  
x = ShippingAddress("HO","225","SAdasd","asdsad","sada","ASDASDS","asdasdsad")
a = ShippingAddress('1','2','2','4','5','6','7')
Coupon_test = FlatCoupon("26-4-2023", 100, 50, 1,"")
my_pc_coupon = PercentageCoupon("23-4-2023", 100, 20, 10, 1,"")
mySystem = System()
mySystem.get_coupon_catalog().add_coupon(Coupon_test)
mySystem.get_coupon_catalog().add_coupon(my_pc_coupon)
mySystem.create_account("MOMO@gmail.com","1234")
print(mySystem.add_admin("Admin","11","0","sd"))
mySystem.search_user_by_email("MOMO@gmail.com").get_order_history().add_order(order)
mySystem.search_user_by_email("MOMO@gmail.com").add_user_coupon('0',mySystem.get_coupon_catalog().get_coupons())
mySystem.get_coupon_catalog().add_coupon(FlatCoupon("26-4-2023", 100, 50, 1,""))
mySystem.get_coupon_catalog().add_coupon(FlatCoupon("26-4-2023", 100, 50, 1,""))
mySystem.search_user_by_email("MOMO@gmail.com").edit_phone_number("1234")
mySystem.search_user_by_email("MOMO@gmail.com").add_address("Address1","225","SAdasd","asdsad","sada","ASDASDS","asdasdsad")
mySystem.search_user_by_email("MOMO@gmail.com").add_address("Address2","225","SAdasd","asdsad","sada","ASDASDS","asdasdsad")
mySystem.search_user_by_email("MOMO@gmail.com").user_used_coupon('0')
css_folder = "template/style"  # folder that contain your css file
css_path = "/" + css_folder  # MAJIK
app.mount(css_path, StaticFiles(directory=css_folder), name="Style")
origins = [
    "http://localhost/",
    "http://localhost:8000/"
    "http://localhost:5173/",
    "http://localhost:8000/template/login.html",
    "http://localhost:8000/coupon.html"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="")
@app.get("/")
def read_root():
    return {"Hello": "World My friend"}

@app.get("/{email}/account/profile",tags=["account"])
def read_user_infor(request:Request,email:str):
    id = mySystem.search_user_by_email(email)
    if id!=False:
        username = id.get_username()
        email = id.get_email()
        phone_number=id.get_phone_number()
        return {'username': username,'email':email,'phone':phone_number}
    #templates.TemplateResponse('profile.html', context={'request': request, 'username': username,'email':email,'phone':phone_number})
    else:
        return {'result': "failed"}
    #templates.TemplateResponse('profile.html', context={'request': request, 'result': "failed"})

@app.get("/{email}/account/view_shipping_address",tags=["account"])
def read_user_shipping_address_infor(email:str):
    shipping_address_dict = {}
    id = mySystem.search_user_by_email(email)
    if id!=False:
        k= 1
        for i in id.get_address():
            x = {
                "name_surname" : i.get_name_surname(),
                "phone_number":i.get_phone_number(),
                "address":i.get_address(),
                "sub_district":i.get_sub_district(),
                "district":i.get_district(),
                "province":i.get_province(),
                "postal_code":i.get_postal_code()}
            shipping_address_dict[k] = x
            k +=1
        return shipping_address_dict
    else:
        return {"failed":"ID not found"} 

@app.post("/login",tags=["account"])
def  login(data:dict):
     email = data["email"]
     password = data["password"]
     x = mySystem.login(email,password)
     if x != False:
         return {'result': "success"}
     else:
         return {'result': "failed"}
    #templates.TemplateResponse('login.html', context={'request': "failed", 'result': "failed"})

@app.post("/register",tags=["account"])
def register(data:dict):
    email = data["email"]
    password = data["password"]
    x = mySystem.create_account(email,password)
    if x == True :
         return {'request': "success", 'result': "success"}
    else :
        return {'request': "failed", 'result': "failed"}

@app.post("/{email}/account/add_shipping_address" , tags=["account"])
def add_shipping_address(email:str,data:dict):
    name_surname = data["new_name_surname"]
    phone_number = data["new_phone_number"]
    address = data["new_address"]
    sub_district = data["new_sub_district"]
    district = data["new_district"]
    province = data["new_province"] 
    postal_code = data["new_postal_code"]
    id =mySystem.search_user_by_email(email)
    if id !=False:
        id.add_address(name_surname, phone_number, address, sub_district, district, province, postal_code)
        return {"result":f"success"}
    else:
        return {"Failed":"Email Not found"}

@app.put("/{email}/account/{address_id}/delete_shipping_address",tags=["account"])
def delete_shipping_address(email:str,address_id:int):
    id = mySystem.search_user_by_email(email)
    address_id = address_id-1
    if id!=False:
        if address_id < len(id.get_address()) and address_id>=0:
            responce = id.delete_address(id.get_address()[address_id])
            if responce == True:
                return {"Success":f"delete address number {address_id +1} form {email}"}
        else:
            return {"failed":f"Address_id not found"}
    else:
        return {"failed":f"Email not found"}

@app.put("/{email}/account/{address_id}/edit_shipping_address",tags=["account"])
def edit_shipping_address(email:str,address_id:int,data:dict):
        address_id = address_id-1
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
                return {"result":"success"}
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
            return {"result":"success"}
        else:
            return {"result":"Something but i dont know"}
    else:
        return {"result":"email not found"}

@app.put("/{email}/account/edit_phonenumber",tags=["account"])
def edit_phonenumber(email:str,data:dict):
    new_phone_number = data["new_phone_number"]
    id = mySystem.search_user_by_email(email)
    if id!=False:
        if id.edit_phone_number(new_phone_number):
            return {"result":f"success"}
        else:
            return{"result":f"failed"}
    else:
        return{"Failed":"Email not found"}

@app.post("/{email}/account/add_coupon",tags=["account"])
def add_coupon(email:str,data:dict):
    new_coupon = data["new_coupon"]
    id = mySystem.search_user_by_email(email)
    if id!=False:
        response = id.add_user_coupon(new_coupon,mySystem.get_coupon_catalog().get_coupons())
        if response == True:
            return {"result":"success"}
        else:
            return {"result":response}
    else:
        return {"result":f"Email not found"}

@app.get("/{email}/account/view_user_coupon",tags=["account"],name="/account")
async def view_user_coupon(request:Request,email:str):

    id = mySystem.search_user_by_email(email)
    if id!=False:
        user_coupon_dict = {}
        user_coupon_id = []
        for coupon in id.get_user_coupon():
            user_coupon_id.append(coupon)
        user_coupon_dict["user_coupon"] = user_coupon_id
        used_coupon =[]
        for coupon in id.get_used_user_coupon():
            used_coupon.append(coupon)
        user_coupon_dict["used_coupon"] = used_coupon
        expire_coupon =[]
        for coupon in id.get_expire_coupon():
            expire_coupon.append(coupon)
        user_coupon_dict["expire_coupon"] = expire_coupon
        return templates.TemplateResponse('template/coupon.html',{"request":request,"user_coupon_dict": user_coupon_dict})
    else:
        return {"Failed":"Email Not Found"}

@app.put("/{email}/account/user_used_coupon",tags=["account"])
def  user_used_coupon(email:str,data:dict):
    used_coupon_id = data["used_coupon_id"]
    id = mySystem.search_user_by_email(email)
    if id != False:
        used_coupon = mySystem.search_coupon_by_coupon_id(used_coupon_id)
        if used_coupon!=False:    
            if id.user_used_coupon(used_coupon):
                return {"Success":f"Use coupon {used_coupon.get_id()}"}
            else:
                return {"Failed":f"you has already used this coupon"}
        else:
            return {"Failed":"Coupon Not Found"}
    else:
        return {"Failed":"Email Not Found"}
    
@app.get("/{email}/account/view_order",tags=["account"])
def view_order(request:Request,email:str):
    id = mySystem.search_user_by_email(email)
    if id!=False:
        response = id.get_order_history().get_order_info()
        return templates.TemplateResponse('template/order.html',{"request":request,"Order":response})
    else:
        return {"Failed":"Email Not Found"}