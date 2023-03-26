class Cart:
  def __init__(self, items = [], total_price = 0, coupon = None, selected_item = []):
    self.__items = items # List for store Item object 
    self.__total_price = total_price
    self.__coupon = coupon # Coupon object (use a coupon for discount)
    self.__total_item = 0
    self.__selected_total_price = 0
    self.__selected_item = selected_item
  
  def get_item_in_cart(self):
    result = ""
    if(len(self.__items) != 0):
      for item in self.__items:
        result += item.get_item() + '\n'
      result = result[:-1]
    else:
      result = "Cart is empty"
    return result
  
  def delete_item_in_cart(self, item):
    if(len(self.__items) != 0):
      self.__items.pop(item)
    else:
      return "Cart is empty"
    return "Success"
  
  def select_item(self, item):
    self.__selected_item.append(item)
    self.__selected_total_price += item.get_price()
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
    self.__total_price += item.get_price()
    return 0
  
  def update_total_item(self): #update_cart(self)
    self.__total_item = len(self.__items)
    self.__total_price = 0
    for item in self.__items:
      self.__total_price += item.get_price()
    return 0

  def get_total_price(self):
    return self.__total_price

  def update_total_price(self, coupon):
    self.__selected_total_price -= coupon.get_discount(self.__total_price)
    return 0