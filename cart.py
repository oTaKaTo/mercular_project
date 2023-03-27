class Cart:
  def __init__(self, items = [], coupon = None):
    self.__items = items # List for store Item object 
    self.__total_price = 0
    self.__coupon = coupon # Coupon object (use a coupon for discount)
    self.__total_item = 0
    self.__selected_item = []
  
  def get_item_in_cart(self) -> str:
    if(len(self.__items) != 0):
      result = self.__get_item()
    else:
      result = "Cart is empty"
    return result
  
  def __get_item(self) -> str:
    items_info = ""
    for item in self.__items:
        items_info += item.get_item() + '\n'
    items_info[:-1] = ''
    return items_info
    
  def delete_item_in_cart(self, item) -> str:
    if(len(self.__items) != 0):
      self.__items.pop(item)
    else:
      return "Cart is empty"
    return "Success"
  
  def select_item(self, item) -> int:
    self.__selected_item.append(item)
    self.__update_cart()
    return 0
    
  def get_selected_item(self, selected_item):
    result = []
    if(len(self.__item) != 0):
      if(isinstance(selected_item, list)):
        for item in selected_item:
          if((item in self.__selected_item) and (isinstance(selected_item, item))):
            result.append(item)
      elif(isinstance(selected_item, item) and (item in self.__selected_item)):
            result = item
    else:
      return "Cart is empty" 
    return result
  
  def add_item_to_cart(self, item):
    self.__items.append(item)
    return 0
  
  def __update_cart(self): #update_total_item(self)
    item_quantity = [item.get_quantity() for item in self.__selected_item]
    self.__total_item = sum(item_quantity)
    self.__total_price = 0
    for item in self.__selected_item:
      price = item.get_price()
      self.__total_price += price
      
    return 0

  def get_total_price(self):
    return self.__total_price

  def update_total_price(self, coupon):
    self.__total_price -= coupon.get_discount(self.__total_price)
    return 0