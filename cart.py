from Product import Item

class CartManager:
  def add_item(items, items_list: list):
    items_list.pop(items)
      
  def delete_item(items, items_list: list) -> str:
    if(len(items_list) != 0):
      items_list.pop(items)
    else:
      return "Cart is empty"
    return "Success"
  
  def edit_amount_item(items: Item, quantity):
    items.set_quantity(quantity)


class Cart:
  def __init__(self, items = [], coupon = None):
    self.__items = items # List for store Item object 
    self.__total_price = 0
    self.__coupon = coupon # Coupon object (use a coupon for discount)
    self.__total_item = 0
    self.__selected_item = []
    self.__cart_manager = CartManager()
    
  def add_item(self, items):
    self.__cart_manager.add_item(items, self.__item)
      
  def delete_item(self, items) -> str:
    return self.__cart_manager.delete_item(items, self.__item)
  
  def edit_amount_item(self, items, quantity):
    self.__cart_manager.edit_amount_item(items, quantity)
    
  def __update_cart(self, items): #update_total_item(self)
    item_quantity = [item.get_quantity() for item in self.__selected_item]
    self.__total_item = sum(item_quantity)
    self.__total_price = 0
    for item in self.__selected_item:
      price = items.get_price()
      self.__total_price += price
  
  def __get_item(self) -> str:
    items_info = ""
    for item in self.__items:
        items_info += item.get_item() + '\n'
    items_info[:-1] = ''
    return items_info
  
  def get_item_in_cart(self) -> str:
    if(len(self.__items) != 0):
      result = self.__get_item()
    else:
      result = "Cart is empty"
    return result
  
  def select_item(self, item: Item):
    self.__selected_item.append(item)
    self.__update_cart()
    
  def get_selected_item(self, selected_item: list):
    result = []
    if(len(self.__item) != 0):
        for item in selected_item:
          if((item in self.__selected_item) and (isinstance(selected_item, item))):
            result.append(item)
    else:
      return "Cart is empty" 
    return result

  def get_total_price(self) -> float:
    return self.__total_price

  def cal_discount_price(self, coupon): # def update_total_price(self, coupon):
    self.__total_price -= coupon.get_discount(self.__total_price)