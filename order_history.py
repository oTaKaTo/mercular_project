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
     
     def get_order_by_id(self, id: int):
          if id > len(self.__orders):
               return None
          print(self.__orders[id - 1])
          return self.__orders[id - 1]
     
     def add_order(self, order: Order):
          if(isinstance(order, Order)):
               self.__orders.append(order)