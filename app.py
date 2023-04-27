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

templates = Jinja2Templates(directory = 'mercular_frontend\src\pages')

@app.get('/', tags=["Page"], response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "email": "65010244@gmail.com"})

@app.get('/{email}/cart', tags=["Page"], response_class=HTMLResponse)
async def cart(email: str, request: Request):
        response = {}
        user = system.check_exists_account(email)
        user_cart = user.get_user_cart()
        items = user_cart.get_items_in_cart()
        for item in items:
            response.update(item.get_item())
        return templates.TemplateResponse("cart.html", {"request": request, "items_info": response, "list": list})


@app.put("/{email}/cart/selecting_item_and_coupon", tags = ["View Cart"])
async def select_item(email: str, selected_item_idx: list, selected_coupon: Optional[str] = None):
    user = system.check_exists_account(email)
    user_cart = user.get_user_cart()
    cart_items = user_cart.get_items_in_cart()
    if(len(cart_items) >= max(selected_item_idx)):
        for idx in selected_item_idx:
            user_cart.select_items(cart_items[idx])
    
    
@app.get("/{email}/checkout/make_payment", tags = ["Checkout"])
async def make_payment(email: str, selected_items: dict) -> dict:
        user = system.check_exists_account(email)
        user_cart = user.get_user_cart()
        selected_items = user_cart.get_items_in_cart()

@app.get("/{email}/checkout/pre_checkout", tags = ["Checkout"])
async def summarize(email: str) -> dict:
    response = {}
    user = system.check_exists_account(email)
    user_cart = user.get_user_cart()
    selected_items = user_cart.get_selected_item()
    if(isinstance(selected_items, list)):
        for item in selected_items:
            response.update(item.get_item())
        response.update({
                        "total_price": user_cart.get_total_price(),
                        "discounted_price": user_cart.get_discounted_price(None)
                        })
        return response
                
@app.post("/{email}/checkout/creating_order", tags = ["Checkout"])
async def create_order(email: str, data: list):
    status = OrderStatus.pending_payment
    user = system.check_exists_account(email)
    user_order_history = user.get_order_history()
    order_list = []
    for item_data in data:
        payment_method = item_data["payment_method"]
        tracking_number = item_data["tracking_number"]
        total_price = item_data["total_price"]
        discounted_price = item_data["discounted_price"]
        order_id = item_data["order_id"]
        order_list.append(Order(payment_method, tracking_number,
                                total_price, discounted_price,
                                order_id, status))
    user_order_history.insert(0, order_list)
    return user_order_history


@app.put("/{email}/add_item_to_cart", tags = ["View Product"])
def add_item(email: str, product_id: str, quantity: int):
    user = system.check_exists_account(email)
    product = product_catalog.search_by_id(product_id) 
    item = Item(product, quantity)
    user.add__item_to_cart(item)
    
if __name__=="__main__":
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)