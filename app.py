from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
import uvicorn

from typing import Optional
from Product import Item
from order import Order, OrderStatus
from promotion import Coupon
from main import system, product_catalog



origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173"
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
app.mount("/mercular_frontend/src/styles/", StaticFiles(directory="mercular_frontend/src/styles"), name="styles")

templates = Jinja2Templates(directory = 'mercular_frontend\src\\templates')

@app.get('/', tags=["Page"], response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "email": "65010244@gmail.com"})

@app.get('/{email}/checkout', tags=["Page"], response_class=HTMLResponse)
async def index(request: Request, email: str):
    user = system.check_exists_account(email)
    user = system.check_exists_account(email)
    user_cart = user.get_user_cart()
    return templates.TemplateResponse("checkout.html", {"request": request,
                                                        "email": email,
                                                        "shipping_address": user.get_address(),
                                                        "total_price": user_cart.get_total_price(),
                                                        "discount_price": user_cart.get_discounted_price(None)
                                                        })

@app.get('/{email}/cart', tags=["Page"], response_class=HTMLResponse)
async def cart(email: str, request: Request):
        items_info = {}
        selected_info = {}
        user = system.check_exists_account(email)
        user_cart = user.get_user_cart()
        dict_price = {  "total_price": user_cart.get_total_price(),
                        "discount_price": user_cart.get_discounted_price(None)}
        items = user_cart.get_items_in_cart()
        selected_item = user_cart.get_selected_items()
        for selected in selected_item:
            selected_info.update(selected.get_item())   
        print("===============")
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
                                                        "selected_info": selected_info
                                                        })

@app.get('/{email}/cart/current_selected_items' , tags = ["View Cart"])
async def get_selected_items(email:str, request:Request):
    user = system.check_exists_account(email)
    user_cart = user.get_user_cart()
    return {"selected_item": user_cart.get_selected_items()}
        
@app.put("/{email}/cart/select_item_handler", tags = ["View Cart"])
async def select_item(email: str, data: dict):
    user = system.check_exists_account(email)
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
    user = system.check_exists_account(email)
    user_cart = user.get_user_cart()
    cart_items = user_cart.get_items_in_cart()
    if(data["selected_item_idx"] > len(cart_items)):
        return 0
    
    edit_item = cart_items[data["selected_item_idx"]]
    new_amount = data["new_amount"]
    user_cart.edit_amount_item(edit_item, new_amount)

@app.put("/{email}/cart/deleting_item", tags = ["View Cart"])
async def delete_item(email:str, data: dict):
    try:    
        user = system.check_exists_account(email)
        user_cart = user.get_user_cart()
        cart_items = user_cart.get_items_in_cart()
        
        user_cart.delete_item(cart_items[data['deleteing_index']])
        return {"status": "success"}
    except:
        return {"status": "fail"}

@app.put("/{email}/checkout/create_order", tags = ["Checkout"])
async def create_order(email: str, data: dict):
        try:
            user = system.check_exists_account(email)
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
        user = system.check_exists_account(email)
        user_cart = user.get_user_cart()
        return {"status": user_cart.checkout()}
    except:
        return {"status": False}


        


@app.put("/{email}/add_item_to_cart", tags = ["View Product"])
def add_item(email: str, product_id: str, quantity: int):
    user = system.check_exists_account(email)
    product = product_catalog.search_by_id(product_id) 
    item = Item(product, quantity)
    user.add__item_to_cart(item)
    
if __name__=="__main__":
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)