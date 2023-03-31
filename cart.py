from Product import Item

class Cart:
  def __init__(self, items = [], coupon = None):
    self.__items = items # List for store Item object 
    self.__total_price = 0
    self.__coupon = coupon # Coupon object (use a coupon for discount)
    self.__total_item = 0
    self.__selected_item = []
    
  def add_item(self, items):
      self.__items.append(items)
      self.__total_item += items.get_quantity()
      
  def delete_item(self, items: Item) -> str:
    if(len(self.__items) != 0):
      self.__total_item -= items.get_quantity()
      self.__items.remove(items)
    else:
      return "Cart is empty"
    return "Success"
  
  def edit_amount_item(self, items: Item, quantity):
    items.set_quantity(quantity)
    
    
  def __update_total_price(self): #update_total_item(self)
    self.__total_price = 0
    for item in self.__selected_item:
      price = item.get_price()
      self.__total_price += price
  
  def __get_item(self) -> str:
    items_info = ""
    for item in self.__items:
        items_info += item.get_item() + '\n'
    items_info = items_info[:-1]
    return items_info
  
  def get_items_in_cart(self) -> str:
    if(len(self.__items) != 0):
      result = self.__get_item()
    else:
      result = "Cart is empty"
    return result
  
  def select_items(self, item: Item):
    self.__selected_item.append(item)
    self.__update_total_price()
    
  def get_selected_item(self):
    if(len(self.__item) != 0):
        return self.__selected_item
    else:
      return "Cart is empty" 

  def get_total_price(self) -> float:
    return self.__total_price

  def cal_discount_price(self, coupon): # def update_total_price(self, coupon):
    self.__total_price -= coupon.get_discount(self.__total_price)