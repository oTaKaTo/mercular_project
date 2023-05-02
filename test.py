from product import *
from tkinter import *
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import productdata
import numpy as np
from promotion import Promotion,Coupon,CouponCatalog,PercentageCoupon,PercentageDiscount,FlatCoupon,FlatDiscount
from tkinter import Tk
from fastapi import FastAPI,Request
from typing import Union
import json
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from system import System

from promotion import FlatCoupon, PercentageCoupon, CouponCatalog,PercentageDiscount

pd_catalog = ProductCatalog()

# my_product = Product("123", "321", "keyboardRGB", ["keyboard"], "razor", 920,345)
# my_second_product = Product("12341", "4123", "SuperSteal", ["mouse"], "stellseries", 200,3454)
# coco = Product("14341", "2313", "Stolenmouse", ["mousepad"], "stellseries", 200,534)
# bobo = Product("14741", "2323", "SDFeadsetRGB", ["headset","gaming headset"], "lowtech", 1032,3)
# lolo = Product("23121","9213","LOL Mouse",["mouse","gaming mouse"],"LOL", 2300,454 ,"The best mouse in Chiland")
# yoyo = Product("34321","3114","HEADSET GOD",["headset","indy headset"],"razor",2490,45,"Headset for god")
# ssolo = Product("2312213","9233","Keyboarduse",["keyboard","rgb key"],"LrtrL", 2210,44 ,"The best keyboard in Chiland")
 
# pd_catalog.add_product(my_product)
# pd_catalog.add_product(my_second_product)
# pd_catalog.add_product(coco)
# pd_catalog.add_product(bobo)
# pd_catalog.add_product(lolo)
# pd_catalog.add_product(yoyo)
# pd_catalog.add_product(ssolo)

# search_pd = pd_catalog.search_keyword("headset")
# search_pd2 = pd_catalog.search_by_catagories("gaming headset")
# print(pd_catalog.get_product_info())
# print([x.name for x in search_pd])
# print([x.name for x in search_pd2])

# print(pd_catalog.products)


my_system = System()
my_system.create_account(email='qwer', password='1234')


my_system.add_admin("qwe","123")

my_promotion = PercentageDiscount("6-6-2023", 200, 12, 300)

coupon1 = FlatCoupon("15-4-2024", 100, 50, 3, "exclusive", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
coupon2 = PercentageCoupon("15-4-2024", 100, 5, 20, 3, "exclusive", title="คอมพิวเตอร์ ลดเพิ่ม 600.-", description="คูปองอันใดอันหนึ่งอันนั้น")
coupon3 = PercentageCoupon("15-4-2024", 100, 10, 20, 3, "exclusive", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon4 = PercentageCoupon("15-4-2024", 100, 15, 20, 3, "exclusive", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon5 = PercentageCoupon("15-4-2024", 100, 20, 20, 3, "exclusive", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon6 = PercentageCoupon("15-4-2024", 100, 20, 20, 3, "table", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon7 = FlatCoupon("15-4-2024", 100, 50, 3, "gaming", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
coupon8 = FlatCoupon("15-4-2024", 100, 50, 3, "computer", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
coupon9 = FlatCoupon("15-4-2024", 100, 50, 3, "speaker", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
my_system.get_coupon_catalog().add_coupon(coupon1)
my_system.get_coupon_catalog().add_coupon(coupon2)
my_system.get_coupon_catalog().add_coupon(coupon3)
my_system.get_coupon_catalog().add_coupon(coupon4)
my_system.get_coupon_catalog().add_coupon(coupon5)
my_system.get_coupon_catalog().add_coupon(coupon6)
my_system.get_coupon_catalog().add_coupon(coupon7)
my_system.get_coupon_catalog().add_coupon(coupon8)
my_system.get_coupon_catalog().add_coupon(coupon9)




pd_catalog_dict = ProductCatalog()
template = Jinja2Templates(directory="templates")
templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount('/styles', StaticFiles(directory='styles'), name='styles')

for i in productdata.data["data"]:
    promo_handle = None
    promo = i["promotion"]
    
    if bool(promo) == True:
        promo_handle = Promotion(promo["date"],promo["price"],promo["title"],promo["description"])

    x = Product(i["product_id"],i["object_id"],i["name"],i["type"],i["brand"],i["price"],i["quantity"],i["detail"],i["image"],i["option"],promo_handle)
    pd_catalog_dict.add_product(x)


def handle_products_page_request(brand="",type="",search=""):
    list = []
    cnt = 0
    inner_list = []
    if search != "":
        for i in pd_catalog_dict.search(search):
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    elif type != "":
        for i in pd_catalog_dict.get_object_products_by_type(type):
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    elif brand != "":
        for i in pd_catalog_dict.get_object_products_by_brand(brand):
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    else:
        for i in pd_catalog_dict.get_object_products():
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    return list




class ProductModel(BaseModel):
    product_id:str
    object_id:str
    name:str
    type:str
    brand:str
    price:int
    quantity:int
    image:list
    option:str
    detail:dict
    promotion:dict




# All product API
@app.get("/",response_class=HTMLResponse)
async def get_products(request: Request):
    return template.TemplateResponse("index.html",{"request":request,"products": handle_products_page_request()})
@app.get("/{email}/",response_class=HTMLResponse)
async def get_products(request: Request,email:str):
    return template.TemplateResponse("index.html",{"request":request,"products": handle_products_page_request(),"email":email})


@app.get("/{email}/products/type/{product_type}",response_class=HTMLResponse)
async def get_products(request: Request, product_type:str,email:str):
    return template.TemplateResponse("product_type.html",{"request":request,"products":handle_products_page_request(type = product_type),"type":product_type,"email":email})

@app.get("/products/type/{product_type}",response_class=HTMLResponse)
async def get_products(request: Request, product_type:str):
    return template.TemplateResponse("product_type.html",{"request":request,"products":handle_products_page_request(type = product_type),"type":product_type})


@app.get("/products/brand/{brand}",response_class=HTMLResponse)
async def get_brand(request: Request, brand:str):
    return template.TemplateResponse("product_brand.html",{"request":request, "products":handle_products_page_request(brand = brand),"brand": brand})

@app.get("/{email}/products/brand/{brand}",response_class=HTMLResponse)
async def get_brand(request: Request, brand:str,email:str):
    return template.TemplateResponse("product_brand.html",{"request":request, "products":handle_products_page_request(brand = brand),"brand": brand,"email":email})

@app.get("/{email}/product/{object_id}",response_class=HTMLResponse)
async def get_product(request: Request, object_id:str,email:str):
    print(pd_catalog_dict.get_option(object_id))
    return template.TemplateResponse("product.html",{"request":request, "product": pd_catalog_dict.get_product_info(object_id),"option": pd_catalog_dict.get_option(object_id),"email":email})

@app.get("/product/{object_id}",response_class=HTMLResponse)
async def get_product(request: Request, object_id:str):
    return template.TemplateResponse("product.html",{"request":request, "product": pd_catalog_dict.get_product_info(object_id),"option": pd_catalog_dict.get_option(object_id)})


@app.put("/{email}/add_item_to_cart", tags = ["View Product"])
async def add_item(email: str, product_id: str, quantity: int):
    user = my_system.check_exists_account(email)
    product = pd_catalog_dict.search_by_id(product_id) 
    item = Item(product, quantity)
    user.add__item_to_cart(item)

@app.post("/createproduct")
async def add_products(product:dict):
    product_id = product["product_id"]
    object_id = product["object_id"]
    name = product["name"]
    type = product["type"]
    brand = product["brand"]
    price = product["price"]
    quantity = product["quantity"]
    image = product["image"]
    option = product["option"]
    detail = product["detail"]
    promotion = product["promotion"]
    pd_catalog.add_product(Product(product_id,object_id,name,type,brand,price,quantity,detail,image,option,promotion))
    return {name : "add success"}


@app.post("/search/{keyword}",tags=["search"])
async def search(keyword:str,request: Request):
    return template.TemplateResponse("product_search.html",{"request":request,"products":handle_products_page_request(search=keyword)})
       


@app.get("/{email}/admin", response_class=HTMLResponse)
async def view_admin_page(request: Request, email:str):
    return templates.TemplateResponse("admin.html", {"request": request, 'email': email})

@app.post("/{email}/admin/search_coupon_infor_by_id")
async def search_coupon_infor_by_id(data:dict):
    try:
        id = str(data["id"])
        print(my_system.get_coupon_catalog().get_coupons())
        for coupon in my_system.get_coupon_catalog().get_coupons():
            if coupon != None and coupon.get_id()==id:
                return coupon
        return "ID Invaild"
    except:
        return None

@app.get("/coupon-special", response_class=HTMLResponse)
async def view_coupon(request: Request):
  coupons = my_system.get_coupon_catalog().get_coupons_sorted_by_coupon_type()
  return templates.TemplateResponse("coupon_no_email.html", {"request": request, 'coupons': coupons, 'email':''})

@app.get("/{email}/coupon-special", response_class=HTMLResponse)
async def view_coupon_email(request: Request, email: str):
  email
  coupons = my_system.get_coupon_catalog().get_coupons_sorted_by_coupon_type()
  return templates.TemplateResponse("coupon.html", {"request": request, 'coupons': coupons, 'email': email})

@app.get("/monthly-promotion", response_class=HTMLResponse)
async def view_promotion(request: Request):
  return templates.TemplateResponse("promotion_no_email.html", {"request": request, 'products': promo_pd_catalog_dict.get_products(), 'email':''})

@app.get("/{email}/monthly-promotion", response_class=HTMLResponse)
async def view_promotion_email(request: Request, email: str):
  return templates.TemplateResponse("promotion.html", {"request": request, 'products': promo_pd_catalog_dict.get_products(), 'email': email})

@app.post("/{email}/get-coupon")
async def get_coupon(request: Request, data: dict):
  email = data['email']
  id = data['id']
  user = my_system.search_user_by_email(email)
  return user.add_user_coupon(id, my_system.get_coupon_catalog().get_coupons())

@app.get("/{email}/account/profile",tags=["account"])
async def read_user_infor(request:Request,email:str):
    id = my_system.search_user_by_email(email)
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
async def read_user_shipping_address_infor(email:str):
    shipping_address_dict = {}
    id = my_system.search_user_by_email(email)
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
    
@app.get('/login-page', response_class=HTMLResponse)
async def view_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get('/register-page', response_class=HTMLResponse)
async def view_login_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get('/address-page', response_class=HTMLResponse)
async def view_login_page(request: Request):
    return templates.TemplateResponse("address.html", {"request": request})

@app.get('/profile-page', response_class=HTMLResponse)
async def view_login_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.post("/login",tags=["account"])
async def  login(data:dict):
     email = data["email"]
     password = data["password"]
     x = my_system.login(email,password)
     if x != False:
         print(x)
         if x=="Admin":
            
            return {'result':"Admin"}
         return {'result': "success"}
     else:
         return {'result': "failed"}

@app.post('/logout')
async def logout(data:dict):
    email = data["email"]
    id = my_system.search_user_by_email(email)
    if id!= False:
      my_system.logout(id)
      return {'result':'success'}
    return {'result':'failed'}
        
@app.post("/register")
async def register(request: Request, data:dict):
    email = data["email"]
    password = data["password"]
    x = my_system.create_account(email,password)
    if x == True :
         return {'request': "success", 'result': "success"}
    else :
        return {'request': "failed", 'result': "failed"}

@app.post("/{email}/account/add_shipping_address" , tags=["account"])
async def add_shipping_address(email:str,data:dict):
    name_surname = data["new_name_surname"]
    phone_number = data["new_phone_number"]
    address = data["new_address"]
    sub_district = data["new_sub_district"]
    district = data["new_district"]
    province = data["new_province"] 
    postal_code = data["new_postal_code"]
    id =my_system.search_user_by_email(email)
    if id !=False:
        id.add_address(name_surname, phone_number, address, sub_district, district, province, postal_code)
        return {"result":f"success"}
    else:
        return {"Failed":"Email Not found"}

@app.put("/{email}/account/{address_id}/delete_shipping_address",tags=["account"])
async def delete_shipping_address(email:str,address_id:int):
    id = my_system.search_user_by_email(email)
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
async def edit_shipping_address(email:str,address_id:int,data:dict):
        address_id = address_id-1
        new_name_surname = data["new_name_surname"]
        new_phone_number = data["new_phone_number"]
        new_address = data["new_address"]
        new_sub_district = data["new_sub_district"]
        new_district = data["new_district"]
        new_province = data["new_province"] 
        new_postal_code = data["new_postal_code"]
        id = my_system.search_user_by_email(email)
        if id!=False:
            if address_id < len(id.get_address()) and address_id>=0:
                id.get_address()[address_id].edit_shipping_address(new_name_surname,new_phone_number,new_address,new_sub_district,new_district,new_province,new_postal_code)
                return {"result":"success"}
            else:
                return {"failed":f"Address_id not found"}
        else:
            return {"failed":f"Email not found"}

@app.put("/{email}/account/edit_username",tags=["account"])
async def edit_username(email:str,data:dict):
    new_username = data["new_username"]
    id = my_system.search_user_by_email(email)
    if id!= False:
        if id.edit_username(new_username):
            return {"result":"success"}
        else:
            return {"result":"Something but i dont know"}
    else:
        return {"result":"email not found"}

@app.put("/{email}/account/edit_phonenumber",tags=["account"])
async def edit_phonenumber(email:str,data:dict):
    new_phone_number = data["new_phone_number"]
    id = my_system.search_user_by_email(email)
    if id!=False:
        if id.edit_phone_number(new_phone_number):
            return {"result":f"success"}
        else:
            return{"result":f"failed"}
    else:
        return{"Failed":"Email not found"}

@app.post("/{email}/account/add_coupon",tags=["account"])
async def add_coupon(email:str,data:dict):
    new_coupon = data["new_coupon"]
    id = my_system.search_user_by_email(email)
    if id!=False:
        response = id.add_user_coupon(new_coupon,my_system.get_coupon_catalog().get_coupons())
        if response == True:
            return {"result":"success"}
        else:
            return {"result":response}
    else:
        return {"result":f"Email not found"}

@app.get("/{email}/account/view_user_coupon",tags=["account"],name="/account")
async def view_user_coupon(request:Request,email:str):

    id = my_system.search_user_by_email(email)
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
        return templates.TemplateResponse('user_coupon.html',{"request":request,"user_coupon_dict": user_coupon_dict})
    else:
        return {"Failed":"Email Not Found"}
    
@app.post("/{email}/admin/add_system_coupon")
async def  add_system_product(data:dict):
    print(data)
    data = data["data"]
    email = data["email"]
    due_date = data["due_date"]
    minimum_price = data["minimum_price"]
    discount = data["discount"]
    max_discount = data["max_discount"]
    description = data["description"]
    title = data["title"]
    quantity = data["quantity"]
    ban_types = data["ban_types"]
    ban_products = data["ban_products"]
    type = data["type"]
    brand = data["brand"]
    coupon_type = data["coupon_type"]
    quantity = data["quantity"]
    discount_type = data["discount_type"]
    id = my_system.search_user_by_email(email)
    if id != False:
        if isinstance(id, Admin):
                if discount_type == "flat":
                       new_coupon = FlatCoupon(due_date,minimum_price,discount,quantity,coupon_type,title,description,ban_products,ban_types,type,brand)
                elif discount_type == "percentage":
                       new_coupon = PercentageCoupon(due_date,minimum_price,discount,max_discount,quantity,coupon_type,title,description,ban_products,ban_types,type,brand)

                if id.add_coupon_to_coupon_catalog(new_coupon,my_system.get_coupon_catalog())==True:
                    return f"Success to add coupon {new_coupon.get_id()}"
                else:
                    return "Failed to add"
        else:
                return "you are not admin"
    else:
        return "Email Not Found"
    
@app.post("/{email}/admin/del_coupon_in_coupon_catalog",tags=["account"])
async def del_item_in_product_catalog(email:str,data:dict):
    try:
        coupon_id = data["coupon_id"]
        id = my_system.search_user_by_email(email)
        if id != False:
            if isinstance(id,Admin):
                if id.del_coupon_in_coupon_catalog(coupon_id,my_system.get_coupon_catalog())==True:    
                    return "del coupon success"
                else:
                    return "Failed"
            else:
                return "you are not admin"
        else:
            return "Email Not Found"
    except:
        return None

@app.put("/{email}/account/user_used_coupon",tags=["account"])
async def  user_used_coupon(email:str,data:dict):
    used_coupon_id = data["used_coupon_id"]
    id = my_system.search_user_by_email(email)
    if id != False:
        used_coupon = my_system.search_coupon_by_coupon_id(used_coupon_id)
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
async def view_order(request:Request,email:str):
    id = my_system.search_user_by_email(email)
    if id!=False:
        response = id.get_order_history().get_order_info()
        return templates.TemplateResponse('order.html',{"request":request,"Order":response})
    else:
        return {"Failed":"Email Not Found"}