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
from database import *
from promotion import FlatCoupon, PercentageCoupon, CouponCatalog,PercentageDiscount
from account import Admin,User
from order import Order,OrderStatus

template = Jinja2Templates(directory="templates")
templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount('/styles', StaticFiles(directory='styles'), name='styles')



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
    return template.TemplateResponse("allproduct_noemail.html",{"request":request,"products": handle_products_page_request()})
@app.get("/{email}/",response_class=HTMLResponse)
async def get_products(request: Request,email:str):
    return template.TemplateResponse("allproduct.html",{"request":request,"products": handle_products_page_request(),"email":email})


@app.get("/{email}/products/type/{product_type}",response_class=HTMLResponse)
async def get_products(request: Request, product_type:str,email:str):
    return template.TemplateResponse("product_type.html",{"request":request,"products":handle_products_page_request(type = product_type),"type":product_type,"email":email})

@app.get("/products/type/{product_type}",response_class=HTMLResponse)
async def get_products(request: Request, product_type:str):
    return template.TemplateResponse("product_type_noemail.html",{"request":request,"products":handle_products_page_request(type = product_type),"type":product_type})


@app.get("/products/brand/{brand}",response_class=HTMLResponse)
async def get_brand(request: Request, brand:str):
    return template.TemplateResponse("product_brand_noemail.html",{"request":request, "products":handle_products_page_request(brand = brand),"brand": brand})

@app.get("/{email}/products/brand/{brand}",response_class=HTMLResponse)
async def get_brand(request: Request, brand:str,email:str):
    return template.TemplateResponse("product_brand.html",{"request":request, "products":handle_products_page_request(brand = brand),"brand": brand,"email":email})

@app.get("/{email}/product/{object_id}",response_class=HTMLResponse)
async def get_product(request: Request, object_id:str,email:str):
    print(pd_catalog_dict.get_option(object_id))
    return template.TemplateResponse("product.html",{"request":request, "product": pd_catalog_dict.get_product_info(object_id),"option": pd_catalog_dict.get_option(object_id),"email":email})

@app.get("/product/{object_id}",response_class=HTMLResponse)
async def get_product(request: Request, object_id:str):
    return template.TemplateResponse("product_noemail.html",{"request":request, "product": pd_catalog_dict.get_product_info(object_id),"option": pd_catalog_dict.get_option(object_id)})



# Cart and Checkout API

@app.put("/{email}/add_item_to_cart", tags = ["View Product"])
def add_item(data:dict, email:str):
    id = data['product_id']
    quantity = data['quantity']
    user = my_system.search_user_by_email(email)
    print(id)
    product = pd_catalog_dict.search_by_id(id)
    print(product,quantity) 
    item = Item(product, quantity)
    print(product)
    user.add_item_to_cart(item)
    return {"add_item":"success"}

@app.get('/{email}/checkout', tags=["Page"], response_class=HTMLResponse)
async def index(request: Request, email: str, data: dict):
    user = my_system.search_user_by_email(email)
    user = my_system.search_user_by_email(email)
    user_cart = user.get_user_cart()
    if(data["is_buynow"]):
        total_price = 0
        discount_price = 0
    else:
        total_price = user_cart.get_total_price()
        discount_price = user_cart.get_discounted_price(None)
    
    return templates.TemplateResponse("checkout.html", {"request": request,
                                                        "email": email,
                                                        "shipping_address": user.get_address(),
                                                        "total_price": float(total_price),
                                                        "discount_price": float(discount_price),
                                                        "user_coupons": user.get_user_coupon(),
                                                        })

@app.get('/{email}/cart', tags=["Page"], response_class=HTMLResponse)
async def cart(email: str, request: Request):
        items_info = {}
        selected_info = {}
        user = my_system.search_user_by_email(email)
        user_cart = user.get_user_cart()
        dict_price = {  "total_price": user_cart.get_total_price(),
                        "discount_price": user_cart.get_discounted_price(None)}
        items = user_cart.get_items_in_cart()
        selected_item = user_cart.get_selected_items()
        for selected in selected_item:
            selected_info.update(selected.get_item())   
            
        for item in items:
            price = item.get_price() * item.get_quantity()
            temp_info = item.get_item()
            temp_info[item.get_product().get_name()].update({"price": price})
            items_info.update(temp_info)
            
            
        return templates.TemplateResponse("cart.html", {"request": request, 
                                                        "items_info": items_info, 
                                                        "list": list,
                                                        "email": email, 
                                                        "dict_price": dict_price, 
                                                        "selected_info": selected_info,
                                                        "user_coupons": user.get_user_coupon()
                                                        })

@app.get('/{email}/cart/current_selected_items' , tags = ["View Cart"])
async def get_selected_items(email:str, request:Request):
    user = my_system.search_user_by_email(email)
    user_cart = user.get_user_cart()
    return {"selected_item": user_cart.get_selected_items()}
        
@app.put("/{email}/cart/select_item_handler", tags = ["View Cart"])
async def select_item(email: str, data: dict):
    user = my_system.search_user_by_email(email)
    user_cart = user.get_user_cart()
    cart_items = user_cart.get_items_in_cart()
    if(data["selected_item_idx"] > len(cart_items)):
        return 0
    
    if(data["option"] == 0):
        user_cart.select_items(cart_items[data["selected_item_idx"]])
    elif(data["option"] == 1):
        user_cart.deselect_items(cart_items[data["selected_item_idx"]])

@app.put("/{email}/cart/edit_amount_item", tags = ["View Cart"])
async def select_item(email: str, data: dict):
    user = my_system.search_user_by_email(email)
    user_cart = user.get_user_cart()
    cart_items = user_cart.get_items_in_cart()
    if(data["selected_item_idx"] > len(cart_items)):
        return 0
    
    edit_item = cart_items[data["selected_item_idx"]]
    new_amount = data["new_amount"]
    user_cart.edit_amount_item(edit_item, int(new_amount))

@app.put("/{email}/cart/deleting_item", tags = ["View Cart"])
async def delete_item(email:str, data: dict):
    try:    
        user = my_system.search_user_by_email(email)
        user_cart = user.get_user_cart()
        cart_items = user_cart.get_items_in_cart()
        
        user_cart.delete_item(cart_items[data['deleteing_index']])
        return {"status": "success"}
    except:
        return {"status": "fail"}

@app.put("/{email}/checkout/create_order", tags = ["Checkout"])
async def create_order(email: str, data: dict):
        try:
            user = my_system.search_user_by_email(email)
            user_order_history = user.get_order_history()
            payment_method = data["payment_method"]
            total_price = data["total_price"]
            discounted_price = data["discounted_price"]
            status = OrderStatus(int(data["status"])).name
            selected_shipping_address =  data["shipping_address"]
            items_list = user.get_user_cart().get_selected_items()
            
            user_order_history.add_order(Order(payment_method, 
                                            total_price,
                                            discounted_price,
                                            status,
                                            items_list,
                                            selected_shipping_address))
            return {"status": "success"}
        except:
            return {"status": "failed"}

@app.put("/{email}/checkout/update", tags = ["Checkout"])
async def create_order(email: str, data: dict):
    try:
        user = my_system.search_user_by_email(email)
        user_cart = user.get_user_cart()
        return {"status": user_cart.checkout(my_system.get_product_catalog(), my_system.get_coupon_catalog())}
    except:
        return {"status": False}



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
  return templates.TemplateResponse("coupon_no_email.html", {"request": request, 'coupons': coupons})

@app.get("/{email}/coupon-special", response_class=HTMLResponse)
async def view_coupon_email(request: Request, email: str):
  email
  coupons = my_system.get_coupon_catalog().get_coupons_sorted_by_coupon_type()
  return templates.TemplateResponse("coupon.html", {"request": request, 'coupons': coupons, 'email': email})

@app.get("/monthly-promotion", response_class=HTMLResponse)
async def view_promotion(request: Request):
  return templates.TemplateResponse("promotion_no_email.html", {"request": request, 'products': promo_pd_catalog_dict.get_products(), 'email': None})

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
def read_user_infor(request:Request,email:str):
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
def read_user_shipping_address_infor(email:str):
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
    return templates.TemplateResponse("address.html", {"request": request, "email": None})

@app.get('/profile-page', response_class=HTMLResponse)
async def view_login_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request, "email": None})

@app.post("/login",tags=["account"])
def  login(data:dict):
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
def logout(data:dict):
    email = data["email"]
    id = my_system.search_user_by_email(email)
    if id!= False:
      my_system.logout(id)
      return {'result':'success'}
    return {'result':'failed'}
        
@app.post("/register")
def register(request: Request, data:dict):
    email = data["email"]
    password = data["password"]
    x = my_system.create_account(email,password)
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
    id =my_system.search_user_by_email(email)
    if id !=False:
        id.add_address(name_surname, phone_number, address, sub_district, district, province, postal_code)
        return {"result":f"success"}
    else:
        return {"Failed":"Email Not found"}

@app.put("/{email}/account/{address_id}/delete_shipping_address",tags=["account"])
def delete_shipping_address(email:str,address_id:int):
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
def edit_shipping_address(email:str,address_id:int,data:dict):
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
def edit_username(email:str,data:dict):
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
def edit_phonenumber(email:str,data:dict):
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
def add_coupon(email:str,data:dict):
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
        return templates.TemplateResponse('user_coupon.html',{"request":request,"user_coupon_dict": user_coupon_dict, 'email': email})
    else:
        return {"Failed":"Email Not Found"}
    
@app.post("/{email}/admin/add_my_system_coupon")
async def  add_my_system_product(data:dict):
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
def del_item_in_product_catalog(email:str,data:dict):
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
def  user_used_coupon(email:str,data:dict):
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
def view_order(request:Request,email:str):
    id = my_system.search_user_by_email(email)
    if id!=False:
        response = id.get_order_history().get_order_info()
        return templates.TemplateResponse('order.html',{"request":request,"Order":response, 'email': email})
    else:
        return {"Failed":"Email Not Found"}