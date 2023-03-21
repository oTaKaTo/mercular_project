class Cart:
  def __init__(self, items=[], total_price=0, coupon=None):
    self.__items = items # List for store Item object 
    self.__total_price = total_price
    self.__coupon = coupon # Coupon object (use a coupon for discount)
  
  def get_cart():
    pass
  
  def get_is_selected_item():
    pass
  
  def add_item_to_cart(self, item):
    self.__items.append(item)
  
  def update_total_item():
    pass

  def update_total_price(coupon):
    pass