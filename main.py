from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from promotion import FlatCoupon, PercentageCoupon, CouponCatalog
from account import Admin
import productdata
from product import *
from system import System
from promotion import PercentageDiscount
from database import *

app = FastAPI()
app.mount('/styles', StaticFiles(directory='styles'), name='styles')

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def view_home_page(request: Request):
    return templates.TemplateResponse("index_no_email.html", {"request": request, 'email': ''})

@app.get('/{email}/', response_class=HTMLResponse)
async def view_home_page_email(request: Request, email:str):
    return templates.TemplateResponse("index.html", {"request": request, 'email': email})

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
    return templates.TemplateResponse("address.html", {"request": request})

@app.get('/profile-page', response_class=HTMLResponse)
async def view_login_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

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
        return templates.TemplateResponse('order.html',{"request":request,"Order":response})
    else:
        return {"Failed":"Email Not Found"}



  
