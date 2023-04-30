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


pd_catalog_dict = ProductCatalog()

for i in productdata.data["data"]:
    promo_handle = None
    promo = i["promotion"]
    print(promo)
    
    if bool(promo) == True:
        promo_handle = Promotion(promo["date"],promo["price"],promo["title"],promo["description"])

    x = Product(i["product_id"],i["object_id"],i["name"],i["type"],i["brand"],i["price"],i["quantity"],i["detail"],i["image"],i["option"],promo_handle)
    print(i["product_id"])
    pd_catalog_dict.add_product(x)

print(pd_catalog_dict.get_object_products())

def handle_products_page_request(brand=""):
    list = []
    cnt = 0
    inner_list = []
    if brand == "":
        for i in pd_catalog_dict.get_object_products():
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    else:
        for i in pd_catalog_dict.get_product_by_brand(brand):
            if cnt == 4:
                list.append(inner_list)  
                inner_list = []
                cnt = 0 
            inner_list.append(i)
            cnt += 1
        list.append(inner_list)
    
    return list

print(pd_catalog_dict.get_option("89698"))


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


template = Jinja2Templates(directory="htmldirectory")
app = FastAPI()
app.mount('/htmldirectory', StaticFiles(directory='htmldirectory'), name='htmldirectory')



@app.get("/",response_class=HTMLResponse)
async def get_products(request: Request):
    return template.TemplateResponse("index.html",{"request":request,"products": handle_products_page_request()})

@app.get("/products/{brand}",response_class=HTMLResponse)
async def get_brand(request: Request, brand:str):
    return template.TemplateResponse("productbrand.html",{"request":request, "products":handle_products_page_request(brand),"brand": brand})

@app.get("/{object_id}",response_class=HTMLResponse)
async def get_product(request: Request, object_id:str):
    print(pd_catalog_dict.get_option(object_id))
    return template.TemplateResponse("product.html",{"request":request, "product": pd_catalog_dict.get_product_info(object_id),"option": pd_catalog_dict.get_option(object_id)})

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


@app.post("/search",tags=["search"])
async def search(keyword:str):
    search = []
    for i in pd_catalog_dict.get_products():
        if keyword.lower() == i.get_product_id():
            return i
        
        elif keyword.lower() in (i.get_name()).lower():
            x = {}
            x["product_id"] = i.get_product_id()
            x["name"] = i.get_name()
            x["price"] = i.get_price()
            search.append(x)
            continue

        elif keyword.lower() in i.get_type_brand_id():
            x = {}
            x["product_id"] = i.get_product_id()
            x["name"] = i.get_name()
            x["price"] = i.get_price()
            search.append(x)
            continue

        for j in i.get_type():
            if keyword.lower() in j.lower():
                x = {}
                x["product_id"] = i.get_product_id()
                x["name"] = i.get_name()
                x["price"] = i.get_price()
                search.append(x)
                continue       
    return search
