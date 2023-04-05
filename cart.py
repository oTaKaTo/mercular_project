from Product import Item
from exception import CartEmptyException, ItemNotFoundException

class Cart:
  def __init__(self):
    self.__items = [] # List for store Item object 
    self.__selected_item = []
    self.__total_price = 0
    self.__total_item = 0
    self.__discounted_price = 0
    
  def add_item(self, items: Item):
      self.__items.append(items)
      self.__total_item += items.get_quantity()
      
  def delete_item(self, items: Item) -> str:
    if(len(self.__items) != 0):
      self.__total_item -= items.get_quantity()
      self.__items.remove(items)
    else:
      raise CartEmptyException
  
  def edit_amount_item(self, items: Item, quantity):
    if(self.__items > 1):
      delta_quantity = quantity - items.get_quantity()
      self.__total_item += delta_quantity
      items.set_quantity(quantity)
    else:
      raise CartEmptyException
    
  def __update_total_price(self): #update_total_item(self)
    self.__total_price = 0
    for item in self.__selected_item:
      price = item.get_price()
      self.__total_price += price
    self.cal_discount_price()
    
  def get_items_in_cart(self):
    if(len(self.__items) != 0):
      return self.__items
    raise CartEmptyException
  
  def select_items(self, items: Item):
    if(len(self.__items) != 0):
      self.__selected_item.append(items)
      self.__update_total_price()
    else:
      raise CartEmptyException
  
  def deselect_items(self, items: Item):
    if(len(self.__items) != 0):
      self.__selected_item.remove(items)
      self.__update_total_price()
    else:
      raise CartEmptyException
   
  def get_selected_item(self):
    if(len(self.__selected_item) != 0):
        return self.__selected_item
    raise ItemNotFoundException

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

  def checkout(self):
    price = self.get_total_price()
    try:
      for item in self.get_selected_item():
        if (not self.__coupon.is_available(price, item.get_type_brand_id())) or item.get_quantity() > item.get_amount():
          return False
      return True
    except:
      return False
  
  def select_coupon(self, coupon):
    self.__coupon = coupon
    self.__update_total_price()
    return True