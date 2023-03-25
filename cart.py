class Cart:
  def __init__(self, items = [], total_price = 0, coupon = None):
    self.__items = items # List for store Item object 
    self.__total_price = total_price
    self.__coupon = coupon # Coupon object (use a coupon for discount)
  
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
  
  def get_is_selected_item():
    pass
  
  def add_item_to_cart(self, item):
    self.__items.append(item)
    self.__total_price += item.get_price()
  
  def update_total_item():
    pass

  def get_total_price(self):
    return self.__total_price

  def update_total_price(self, coupon):
    pass