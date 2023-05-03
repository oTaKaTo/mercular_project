from order import Order

class OrderHistory:
     def __init__(self, orders: list = []):
          self.__orders = orders # list for store Orders
     
     def get_order_info(self):
          result = {}
          for i in self.__orders:
               order_info = i.get_order()
               result.update({order_info["order_id"]: order_info})
          return result
          
     
     def add_order(self, order: Order):
          if(isinstance(order, Order)):
               self.__orders.append(order)