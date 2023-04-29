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
async def index(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request, "email": "65010244@gmail.com"})

@app.get('/{email}/cart', tags=["Page"], response_class=HTMLResponse)
async def cart(email: str, request: Request):
        items_info = {}
        selected_info = {}
        user = system.check_exists_account(email)
        user_cart = user.get_user_cart()
        dict_price = {   "total_price": user_cart.get_total_price(),
                        "discount_price": user_cart.get_discounted_price(None)}
        items = user_cart.get_items_in_cart()
        selected_item = user_cart.get_selected_items()
        for selected in selected_item:
            selected_info.update(selected.get_item())
            
        for item in items:
            items_info.update(item.get_item())
        return templates.TemplateResponse("cart.html", {"request": request, 
                                                        "items_info": items_info, 
                                                        "list": list,
                                                        "email": user.get_Email(), 
                                                        "dict_price": dict_price, 
                                                        "selected_info": selected_info})


@app.put("/{email}/cart/selecting_item_and_coupon", tags = ["View Cart"])
async def select_item(email: str, selected_item_idx: int, selected_coupon: Optional[str] = None):
    user = system.check_exists_account(email)
    user_cart = user.get_user_cart()
    cart_items = user_cart.get_items_in_cart()
    if(selected_item_idx < len(cart_items)):
        user_cart.select_items(cart_items[selected_item_idx])
    
    
@app.get("/{email}/checkout/make_payment", tags = ["Checkout"])
async def make_payment(email: str, selected_info: dict) -> dict:
        user = system.check_exists_account(email)
        user_cart = user.get_user_cart()
        selected_info = user_cart.get_items_in_cart()

@app.get("/{email}/checkout/pre_checkout", tags = ["Checkout"])
async def summarize(email: str) -> dict:
    response = {}
    user = system.check_exists_account(email)
    user_cart = user.get_user_cart()
    selected_info = user_cart.get_selected_info()
    if(isinstance(selected_info, list)):
        for item in selected_info:
            response.update(item.get_item())
        response.update({
                        "total_price": user_cart.get_total_price(),
                        "discounted_price": user_cart.get_discounted_price(None)
                        })
        return response
                
@app.post("/{email}/checkout/creating_order", tags = ["Checkout"])
async def create_order(email: str, data: dict):
    status = OrderStatus.pending_payment
    user = system.check_exists_account(email)
    user_order_history = user.get_order_history()
    payment_method = data["payment_method"]
    tracking_number = data["tracking_number"]
    total_price = data["total_price"]
    discounted_price = data["discounted_price"]
    order_id = data["order_id"]
    items_list = data["item_list"]
    user_order_history.add_order(Order(payment_method, tracking_number,
                            total_price, discounted_price,
                            order_id, status, items_list))
    return user_order_history


@app.put("/{email}/add_item_to_cart", tags = ["View Product"])
def add_item(email: str, product_id: str, quantity: int):
    user = system.check_exists_account(email)
    product = product_catalog.search_by_id(product_id) 
    item = Item(product, quantity)
    user.add__item_to_cart(item)
    
if __name__=="__main__":
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)