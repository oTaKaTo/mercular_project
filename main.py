from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from promotion import FlatCoupon, PercentageCoupon, CouponCatalog
from account import Admin
import productdata
from product import *
from database import *
from promotion import PercentageDiscount
from database import *
from fastapi import HTTPException
from typing import Optional
from order import Order, OrderStatus
from payment import QRCodeTransaction, CreditCardTransaction, CashOnDeliveryTransaction
from datetime import timedelta, date
from itertools import count

import uvicorn

transaction_id_gen = count()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5173"
]

async def not_found_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('404.html', {'request': request}, status_code=404)


async def internal_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('500.html', {'request': request}, status_code=500)

exception_handlers = {
    404: not_found_error,
    500: internal_error
}

app = FastAPI(exception_handlers = exception_handlers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/styles', StaticFiles(directory='styles'), name='styles')

templates = Jinja2Templates(directory="templates")

def handle_products_page_request(brand="",type="",search="",promo =False):
    list = []
    cnt = 0
    inner_list = []
    if promo:
        for i in promo_pd_catalog_dict.get_object_products():
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    elif search != "":
        for i in my_system.get_product_catalog().search(search):
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    elif type != "":
        for i in my_system.get_product_catalog().get_object_products_by_type(type):
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    elif brand != "":
        for i in my_system.get_product_catalog().get_object_products_by_brand(brand):
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    else:
        for i in my_system.get_product_catalog().get_object_products():
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    return list

@app.post('/get-product-information')
async def get_product_information(request: Request, data: dict):
    id = data['id']
    product = my_system.get_product_catalog().search_by_id(id)
    return product

@app.post('/get-product-information')
async def get_product_information(request: Request, data: dict):
    id = data['id']
    product = my_system.get_product_catalog().search_by_id(id)
    return product

@app.post('/add-promotion')
async def add_promotion(request: Request, data: dict):
    data = data['data']
    id = data['id']
    email = data['email']
    discount_type = data['discount_type']
    due_date = data['due_date']
    minimum_price = int(data['minimum_price'])
    max_discount = int(data['max_discount'])
    discount = int(data['discount'])
    title = data['title']
    description = data['description']
    promotion = None
    admin = my_system.search_user_by_email(email)
    if admin != False:
        if isinstance(admin, Admin):
                if discount_type == 'flat':
                    promotion = FlatDiscount(due_date, minimum_price, discount, title, description)
                elif discount_type == 'percentage':
                    promotion = PercentageDiscount(due_date, minimum_price, discount, max_discount, title, description)
                my_system.get_product_catalog().search_by_id(id).add_promotion(promotion)
                return "Success"
        else:
                return "you are not admin"
    else:
        return "Email Not Found"

@app.post("/edit_system_coupon")
async def  edit_system_coupon(data:dict):
    coupon_id = data['coupon_id']
    data = data["data"]
    email = data["email"]
    due_date = data["due_date"]
    minimum_price = int(data["minimum_price"])
    discount = int(data["discount"])
    max_discount = int(data["max_discount"])
    description = data["description"]
    title = data["title"]
    quantity = int(data["quantity"])
    ban_types = data["ban_types"]
    ban_products = data["ban_products"]
    type = data["type"]
    brand = data["brand"]
    coupon_type = data["coupon_type"]
    discount_type = data["discount_type"]
    id = my_system.search_user_by_email(email)
    if id != False:
        if isinstance(id, Admin):
                if discount_type == "flat":
                       new_coupon = FlatCoupon(due_date,minimum_price,discount,quantity,coupon_type,title,description,ban_products,ban_types,type,brand)
                elif discount_type == "percentage":
                       new_coupon = PercentageCoupon(due_date,minimum_price,discount,max_discount,quantity,coupon_type,title,description,ban_products,ban_types,type,brand)

                if my_system.get_coupon_catalog().edit_coupon(coupon_id, new_coupon)==True:
                    return f"Success to edit coupon {new_coupon.get_id()}"
                else:
                    return "Failed to add"
        else:
                return "you are not admin"
    else:
        return "Email Not Found"

@app.post("/{email}/admin/add_system_coupon")
async def  add_my_system_product(data:dict):
    data = data["data"]
    email = data["email"]
    due_date = data["due_date"]
    minimum_price = int(data["minimum_price"])
    discount = int(data["discount"])
    max_discount = int(data["max_discount"])
    description = data["description"]
    title = data["title"]
    quantity = int(data["quantity"])
    ban_types = data["ban_types"]
    ban_products = data["ban_products"]
    type = data["type"]
    brand = data["brand"]
    coupon_type = data["coupon_type"]
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
    
@app.get("/search/{keyword}", tags=["Page"], response_class=HTMLResponse)
async def get_product(request: Request, keyword:str):
    return templates.TemplateResponse("product_search_noemail.html",{"request":request,"products":handle_products_page_request(search=keyword),"email":None,"keyword":keyword})

@app.get("/{email}/search/{keyword}", tags=["Page"], response_class=HTMLResponse)
async def get_product(request: Request, keyword:str, email:str):
    return templates.TemplateResponse("product_search.html",{"request":request,"products":handle_products_page_request(search=keyword),"email":email,"keyword":keyword})

@app.get('/{email}/{is_buynow}/checkout', tags=["Page"], response_class=HTMLResponse)
async def index(request: Request, email: str, is_buynow: str):
    selected_items_info = {}
    user = my_system.search_user_by_email(email)
    user = my_system.search_user_by_email(email)
    user_cart = user.get_user_cart()
    selected_items = user_cart.get_selected_items()
    
    for item in selected_items:
        price = item.get_price() * item.get_quantity()
        temp_info = item.get_item()
        
        items_product = item.get_product()
        
        product_image = items_product.get_image()[0]
        items_name = items_product.get_name()
        items_id = items_product.get_product_id()
        
        temp_info[items_id].update({"price": price})
        temp_info[items_id].update({"image": product_image})
        temp_info[items_id].update({"name": items_name})
            
        selected_items_info.update(temp_info)
    
    return templates.TemplateResponse("checkout.html", {"request": request,
                                                        "email": email,
                                                        "shipping_address": user.get_address(),
                                                        "total_price": user_cart.get_total_price(),
                                                        "discount_price": user_cart.get_discounted_price(None),
                                                        "user_coupons": user.get_user_coupon(),
                                                        "selected_items": selected_items_info,
                                                        "list": list,
                                                        "is_buynow": is_buynow
                                                        })

@app.put('/{email}/{product_id}/buynow', tags=["Page"], response_class=HTMLResponse)
async def buynow(email: str, data: dict):
        user = my_system.search_user_by_email(email)
        user = my_system.search_user_by_email(email)
        user_cart = user.get_user_cart()
        
        product = my_system.get_product_catalog().search_by_id(data['product_id']) 
        items = Item(product, int(data['quantity']))
        
        user_cart.get_selected_items().clear()
        user_cart.select_items(items)

@app.get('/{email}/cart', tags=["Page"], response_class=HTMLResponse)
async def cart(email: str, request: Request):
        items_info = {}
        selected_info = {}
        user = my_system.search_user_by_email(email)
        user_cart = user.get_user_cart()
        user_coupon = user.get_user_coupon()
        
        dict_price = {  "total_price": user_cart.get_total_price(),
                        "discount_price": user_cart.get_discounted_price(None)}
        items = user_cart.get_items_in_cart()
        selected_item = user_cart.get_selected_items()
        
        for selected in selected_item:
            selected_info.update(selected.get_item())   
            
        for item in items:
            print(item.get_product().get_product_id(), end = "")
            price = item.get_price() * item.get_quantity()
            temp_info = item.get_item()
            
            item_product = item.get_product()
            product_image = item_product.get_image()[0]
            items_id = item_product.get_product_id()
            item_name = item_product.get_name()
            
            temp_info[items_id].update({"price": price})
            temp_info[items_id].update({"image": product_image})
            temp_info[items_id].update({"name": item_name})
            
            
            items_info.update(temp_info)
            
  
        return templates.TemplateResponse("cart.html", {"request": request, 
                                                        "items_info": items_info, 
                                                        "list": list,
                                                        "email": email, 
                                                        "dict_price": dict_price, 
                                                        "selected_info": selected_info,
                                                        "user_coupons": user_coupon,
                                                        })

@app.get("/",response_class=HTMLResponse)
async def get_products(request: Request):
    return templates.TemplateResponse("allproduct_noemail.html",{"request":request,"products": handle_products_page_request(), "email":None})

@app.get("/{email}/",response_class=HTMLResponse)
async def get_products(request: Request,email:str):
    return templates.TemplateResponse("allproduct.html",{"request":request,"products": handle_products_page_request(),"email":email})

@app.get("/products/type/{product_type}",response_class=HTMLResponse)
async def get_products(request: Request, product_type:str):
    return templates.TemplateResponse("product_type.html",{"request":request,"products":handle_products_page_request(type = product_type),"type":product_type, "email":None})


@app.get("/products/brand/{brand}",response_class=HTMLResponse)
async def get_brand(request: Request, brand:str):
    return templates.TemplateResponse("product_brand_noemail.html",{"request":request, "products":handle_products_page_request(brand = brand),"brand": brand, "email":None})

@app.get("/{email}/products/brand/{brand}",response_class=HTMLResponse)
async def get_brand(request: Request, brand:str,email:str):
    return templates.TemplateResponse("product_brand.html",{"request":request, "products":handle_products_page_request(brand = brand),"brand": brand,"email":email})

@app.get("/{email}/product/{object_id}",response_class=HTMLResponse)
async def get_product(request: Request, object_id:str,email:str):
    return templates.TemplateResponse("product.html",{"request":request, "product": my_system.get_product_catalog().get_product_info(object_id),"option": my_system.get_product_catalog().get_option(object_id),"email":email,"pd_catalog":my_system.get_product_catalog()})

@app.get("/product/{object_id}",response_class=HTMLResponse)
async def get_product(request: Request, object_id:str):
    return templates.TemplateResponse("product_noemail.html",{"request":request, 
                                                            "product": my_system.get_product_catalog().get_product_info(object_id),
                                                            "option": my_system.get_product_catalog().get_option(object_id), 
                                                            "email":None,
                                                            "pd_catalog":my_system.get_product_catalog()})

@app.put("/{email}/cart/clear_select", tags= ["View Cart"])
async def clear_selected_items(email: str):
        user = my_system.search_user_by_email(email)
        user_cart = user.get_user_cart()
        selected_items = user_cart.get_selected_items()
        
        for item in selected_items:
            user_cart.deselect_items(item)
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
    if(data["selected_item_idx"] >=   len(cart_items)):
        return 0
    
    edit_item = cart_items[data["selected_item_idx"]]
    new_amount = data["new_amount"]
    user_cart.edit_amount_item(edit_item, new_amount)
    
@app.put("/{email}/checkout/create_order", tags = ["Checkout"])
async def create_order(email: str, data: dict):
        try:
            user = my_system.search_user_by_email(email)
            system_order_container = my_system.get_order_container()
            
            payment_method = data["payment_method"]
            total_price = data["total_price"]
            discounted_price = data["discounted_price"]
            status = OrderStatus(int(data["status"])).name
            selected_shipping_address =  data["shipping_address"]
            
            new_order = user.create_order(payment_method, 
                            total_price,
                            discounted_price,
                            status,
                            selected_shipping_address,
                            system_order_container)
            
            return {"status": "success",
                    'created_order_id': new_order.get_order_id()}
        except:
            return {"status": "failed"}

@app.put("/{email}/checkout/update_stock", tags = ["Checkout"])
async def create_order(email: str, data: dict):
    try:
        user = my_system.search_user_by_email(email)
        user_cart = user.get_user_cart()

        return {"status": user_cart.checkout(None, my_system.get_product_catalog(), my_system.get_coupon_catalog(), data['is_buynow'])}
    except:
        return {"status": 'fail'}

    

@app.put("/{email}/add_item_to_cart", tags = ["View Product"])
def add_item(email: str, data: dict):
    try:
        id = data['product_id']
        quantity = int(data['quantity'])
        
        user = my_system.search_user_by_email(email)
        product = my_system.get_product_catalog().search_by_id(id) 
        
        item = Item(product, quantity)
        user.add_item_to_cart(item)
    
        return {'status': 'success'}
    except:
        return {'status': 'fail'}


@app.get("/{email}/admin", response_class=HTMLResponse)
async def view_admin_page(request: Request, email:str):
    return templates.TemplateResponse("admin.html", {"request": request, 'email': email})

@app.post("/{email}/admin/search_coupon_infor_by_id")
async def search_coupon_infor_by_id(data:dict):
    try:
        id = str(data["id"])
        for coupon in my_system.get_coupon_catalog().get_coupons():
            if coupon != None and coupon.get_id()==id:
                return coupon
        return "ID Invaild"
    except:
        return None

@app.get("/coupon-special", response_class=HTMLResponse)
async def view_coupon(request: Request):
  coupons = my_system.get_coupon_catalog().get_coupons_sorted_by_coupon_type()
  return templates.TemplateResponse("coupon.html", {"request": request, 
                                                    'coupons': coupons, 
                                                    'email': None})

@app.get("/monthly-promotion", response_class=HTMLResponse)
async def view_promotion(request: Request):
  print(handle_products_page_request(promo=True))
  return templates.TemplateResponse("promotion.html", {"request": request, 
                                                                'products': handle_products_page_request(promo=True), 
                                                                'email':None})


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
async def view_user_coupon(request:Request, email:str):
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
        return templates.TemplateResponse('user_coupon.html',{"request":request,
                                                            "user_coupon_dict": 
                                                            user_coupon_dict,
                                                            'email': email})
    else:
        return {"Failed":"Email Not Found"}
    
@app.post("/{email}/admin/add_system_coupon")
async def  add_system_coupon(data:dict):
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

def update_order_status(email, order_id):
    user = my_system.search_user_by_email(email)
    user_order_history = user.get_order_history()
    system_order_container = my_system.get_order_container()
    
    select_order = user_order_history.get_order_by_id(int(order_id), system_order_container)
    
    select_order.update_status(1)

@app.get("/{email}/account/view_order",tags=["account"])
def view_order(request:Request, email:str):
    id = my_system.search_user_by_email(email)
    if id != False:
        response = id.get_order_history().get_order_info()
        
        return templates.TemplateResponse('order.html',{"request":request, "Order":response, "email": email})
    else:
        return {"Failed":"Email Not Found"}

@app.post("/requestQRpayment")
async def request_QRcode(request: Request, data:dict):
    try:
        qrcode = QRCodeTransaction(next(transaction_id_gen), "In progress", date.today())
        email = data['email']
        address = data['address']
        u = my_system.search_user_by_email(email)
        cart = u.get_user_cart()
        
        if not qrcode.process():
            print('qrcode')
            return False
        
        update_order_status(email, data['created_order_id'])
        
        return True
    except:
        return False

@app.post("/requestCOD")
async def request_COD(request: Request, data:dict):
  try:
    email = data['email']
    address = data['address']
    cod = CashOnDeliveryTransaction(next(transaction_id_gen), "In progress", date.today())
    u = my_system.search_user_by_email(email)
    cart = u.get_user_cart()
    if not cod.process():
      print('cod')
      return False
    
    o = Order(date.today(), date.today() + timedelta(days=4), "COD", "asdlqnwie", cart.get_discounted_price(), "123", "preparing")
    
    update_order_status(email, data['created_order_id'])
    
    return o.dict()
  except:
    return False

@app.post("/requestcreditdebit")
async def request_credit_debit(request: Request, data:dict):
  try:
    name_on_card = data['name_on_card']
    card_id = data['card_id']
    CVC = data['CVC']
    due_date = data['due_date']
    email = data['email']
    address = data['address']
    cd = CreditCardTransaction(next(transaction_id_gen), "In progress", date.today(), name_on_card, card_id, CVC, due_date)
    u = my_system.search_user_by_email(email)
    cart = u.get_user_cart()
    if not cd.process():
      return False
    
    o = Order(date.today(), date.today() + timedelta(days=4), "credit/debit", "asdlqnwie", cart.get_discounted_price(), "123", "preparing")
    
    update_order_status(email, data['created_order_id'])
    
    return o.dict()
  except:
    return False

if __name__=="__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
