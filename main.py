from Account import User
from system import System
from Product import Product, ProductCatalog, Item
from shipping_address import ShippingAddress
from order import Order, OrderStatus
from promotion import PercentageCoupon, FlatCoupon



system = System()
system_user_lst = system.get_user_lst()
product_catalog = system.get_product_catalog()
coupoun_catalog = system.get_coupon_catalog()

coupon1 = PercentageCoupon('23-5-2023', 100, 10, 20, 100, description="oasijfoasifj")
coupoun_catalog.add_coupon(coupon1)
system_user_lst.append(User("momo","1234","65010244@gmail.com"))
momo = system.check_exists_account("65010244@gmail.com")

momo.add_address("ที่อยู่แรก","168","Sda123123d","ASda1111sdsa","asdasdsa","asdasdsa","Adsadsa")
momo.add_address("Address2","225","SAdasd","asdsad","sada","ASDASDS","asdasdsad")
momo_cart = momo.get_user_cart()
product_1st = Product("123", "321", "keyboardRGB", "keyboard", "razor", 920, 20)
product_2nd = Product("1234w", "4123", "mousRGB", "mouse", "stellseries", 200, 10)
product_3nd = Product("12341qweqw", "412ww3", "mseRGB", "mouse", "stellseries", 200, 10)
product_4nd = Product("12341eee", "412ww3", "mouseB", "mouse", "stellseries", 200, 10)
product_5nd = Product("12341ee", "412ww3", "mouseRG", "mouse", "stellseries", 200, 10)
product_6nd = Product("1241eee", "412ww3", "mousG", "mouse", "stellseries", 200, 10)
product_7nd = Product("2341eee", "412ww3", "ouseRG", "mouse", "stellseries", 200, 10)

product_catalog.add_product(product_1st)
product_catalog.add_product(product_2nd)



item_1 = Item(product_1st, 5)
item_2 = Item(product_2nd, 10)


momo.add_item_to_cart(Item(product_3nd, 2))
momo.add_item_to_cart(Item(product_4nd, 10))
momo.add_item_to_cart(Item(product_5nd, 5))
momo.add_item_to_cart(Item(product_6nd, 7))
momo.add_item_to_cart(Item(product_7nd, 8))

for i in momo_cart.get_items_in_cart():
    print(i.get_item())

momo_cart.select_items(momo_cart.get_items_in_cart()[0])
momo_cart.select_items(momo_cart.get_items_in_cart()[1])
print(momo_cart.get_total_price())

"""    items = momo_cart.get_items_in_cart()
    print(items)
    print(momo_cart.get_total_price())
    
    items1 = items[0]
    items2 = items[1]
    print("============Delete test===========\n")
    print("============ Before  ===========")
    print([x.get_item() for x in items])
    momo_cart.delete_item(items1)
    print("============ After  ===========")
    print([x.get_item() for x in items])
    
    print("\n============Selected test===========")
    momo_cart.select_items(items2)
    print([x.get_item() for x in items])
    print(momo_cart.get_total_price())
"""

"""@app.get("/{email}/cart", tags = ["View Cart"])
def view_cart(email:str):
    try:
         response = {}
         user = system.check_exists_account(email)
         user_cart = user.get_user_cart()
         items = user_cart.get_items_in_cart()
         for item in items:
            response.update(item.get_item())
         return response
    except AccountNotFoundException:
        return {"status": AccountNotFoundException.msg}
    except CartErrorException as error:
        return {"status": error.msg}"""
