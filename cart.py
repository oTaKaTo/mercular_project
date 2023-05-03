from product import Item
from fastapi.exceptions import HTTPException

class Cart:
  def __init__(self):
    self.__items = [] # List for store Item object 
    self.__selected_item = []
    self.__total_price = 0
    self.__total_items = 0
    self.__discounted_price = 0
    
  def add_item(self, items: Item):
    items_quantity = items.get_quantity()
    if(items not in self.__items):
      self.__items.append(items)
    else:
      exisited_item_no = self.__items.index(items)
      exisited_item = self.__items[exisited_item_no]
      exisited_item_quantity = exisited_item.get_quantity()
      exisited_item.set_quantity(exisited_item_quantity + items_quantity)
    self.__total_items += items_quantity
      
  def delete_item(self, items: Item) -> str:
    if(len(self.__items) != 0):
      self.__total_items -= items.get_quantity()
      self.__items.remove(items)
    else:
      raise HTTPException(status_code=204, detail="Cart is empty")
  
  def edit_amount_item(self, items: Item, quantity):
    if(len(self.__items) > 0):
      delta_quantity = quantity - items.get_quantity()
      self.__total_items += delta_quantity
      items.set_quantity(quantity)
      self.__update_total_price()
    else:
      raise HTTPException(status_code=204, detail="Cart is empty")
    
  def __update_total_price(self): #update_total_item(self)
    self.__total_price = 0
    for item in self.__selected_item:
      price = item.get_price() * item.get_quantity()
      self.__total_price += price
    self.cal_discount_price()
    
  def get_items_in_cart(self):
      return self.__items
  
  def select_items(self, items: Item):
    if(len(self.__items) != 0):
      self.__selected_item.append(items)
      self.__update_total_price()
    else:
      raise HTTPException(status_code=204, detail="Cart is empty")
  
  def deselect_items(self, items: Item):
    if(len(self.__items) != 0):
      self.__selected_item.remove(items)
      self.__update_total_price()
    else:
      raise HTTPException(status_code=204, detail="Cart is empty")

  def get_selected_items(self):
    return self.__selected_item

  def get_total_price(self) -> float:
    return self.__total_price
  
  def get_discounted_price(self, coupon) -> float:
    return self.__discounted_price

  def cal_discount_price(self): # def update_total_price(self, coupon):
    price = self.get_total_price()
    try:
      for item in self.get_selected_item():
        if not self.__coupon.is_available(price, item.get_type_brand_id()):
          return self.__total_price
      self.__discounted_price = self.__total_price - self.__coupon.get_discount(self.__total_price)
      return self.__discounted_price
    except:
      return self.__total_price

  def checkout(self, coupon = False, product_catalog = None, coupon_catalog = None):
    try:
      price = self.__total_price
  
      for items in self.__selected_item:
        product = items.get_product() 
        if (coupon and not coupon.is_available(price, product.get_type_brand_id())) or items.get_quantity() > product.get_quantity():
          return False
      
      for items in self.__selected_item:  
        items_quantity = items.get_quantity()
        items_id = items.get_product().get_product_id()
        product_catalog.checkout_product(items_id, items_quantity)
        self.delete_item(items)
        
      self.__selected_item.clear()  
      self.__update_total_price()    
      if(coupon):
        coupon_catalog.delete_coupon(coupon.get_id())
      
      return True
    except:
      return False

  
  def select_coupon(self, coupon):
    self.__coupon = coupon
    self.__update_total_price()
    return True