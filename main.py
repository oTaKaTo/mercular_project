from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from promotion import FlatCoupon, PercentageCoupon, CouponCatalog
import productdata
from product import *
from system import System
from promotion import PercentageDiscount

my_system = System()
my_system.create_account(email='qwer', password='1234')

my_promotion = PercentageDiscount("6-6-2023", 200, 12, 300)

my_coupon_catalog = CouponCatalog()
coupon1 = FlatCoupon("15-4-2024", 100, 50, 3, "exclusive", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
coupon2 = PercentageCoupon("15-4-2024", 100, 5, 20, 3, "exclusive", title="คอมพิวเตอร์ ลดเพิ่ม 600.-", description="คูปองอันใดอันหนึ่งอันนั้น")
coupon3 = PercentageCoupon("15-4-2024", 100, 10, 20, 3, "exclusive", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon4 = PercentageCoupon("15-4-2024", 100, 15, 20, 3, "exclusive", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon5 = PercentageCoupon("15-4-2024", 100, 20, 20, 3, "exclusive", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon6 = PercentageCoupon("15-4-2024", 100, 20, 20, 3, "table", title="จัดโต๊ะคอม ลดเพิ่ม 200.-", description="คูปองซักอัน")
coupon7 = FlatCoupon("15-4-2024", 100, 50, 3, "gaming", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
coupon8 = FlatCoupon("15-4-2024", 100, 50, 3, "computer", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
coupon9 = FlatCoupon("15-4-2024", 100, 50, 3, "speaker", title="เล่นเกม ลดเพิ่ม 100.-", description="คูปองลดหนักลดแรง")
my_coupon_catalog.add_coupon(coupon1)
my_coupon_catalog.add_coupon(coupon2)
my_coupon_catalog.add_coupon(coupon3)
my_coupon_catalog.add_coupon(coupon4)
my_coupon_catalog.add_coupon(coupon5)
my_coupon_catalog.add_coupon(coupon6)
my_coupon_catalog.add_coupon(coupon6)
my_coupon_catalog.add_coupon(coupon6)
my_coupon_catalog.add_coupon(coupon7)
my_coupon_catalog.add_coupon(coupon8)
my_coupon_catalog.add_coupon(coupon9)
# print(coupon5.get_due_date_str())

pd_catalog_dict = ProductCatalog()
promo_pd_catalog_dict = ProductCatalog()

for i in productdata.data["data"]:
  promo_handle = None
  promo = i["promotion"]
  
  if bool(promo) == True:
    promo_handle = my_promotion

  x = Product(i["product_id"],i["object_id"],i["name"],i["type"],i["brand"],i["price"],i["quantity"],i["detail"],i["image"],i["option"],promo_handle)
  pd_catalog_dict.add_product(x)
  if bool(promo):
    promo_pd_catalog_dict.add_product(x)


app = FastAPI()
app.mount('/styles', StaticFiles(directory='styles'), name='styles')

templates = Jinja2Templates(directory="templates")

@app.get("/coupon-special", response_class=HTMLResponse)
async def view_coupon(request: Request):
  coupons = my_coupon_catalog.get_coupons_sorted_by_coupon_type()
  return templates.TemplateResponse("coupon_no_email.html", {"request": request, 'coupons': coupons})

@app.get("/{email}/coupon-special", response_class=HTMLResponse)
async def view_coupon_email(request: Request, email: str):
  email
  coupons = my_coupon_catalog.get_coupons_sorted_by_coupon_type()
  return templates.TemplateResponse("coupon.html", {"request": request, 'coupons': coupons, 'email': email})

@app.get("/monthly-promotion", response_class=HTMLResponse)
async def view_promotion(request: Request):
  return templates.TemplateResponse("promotion_no_email.html", {"request": request, 'products': promo_pd_catalog_dict.get_products()})

@app.get("/{email}/monthly-promotion", response_class=HTMLResponse)
async def view_promotion_email(request: Request, email: str):
  return templates.TemplateResponse("promotion.html", {"request": request, 'products': promo_pd_catalog_dict.get_products(), 'email': email})

@app.post("/{email}/get-coupon")
async def get_coupon(request: Request, data: dict):
  email = data['email']
  id = data['id']
  user = my_system.search_user_by_email(email)
  return user.add_user_coupon(id, my_coupon_catalog.get_coupons())



  