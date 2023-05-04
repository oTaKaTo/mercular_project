from order import Order

class OrderHistory:
     def __init__(self):
          self.__orders = [] # list for store Orders
     
     def get_order_info(self):
          result = {}
          for i in self.__orders:
               order_info = i.get_order()
               result.update({order_info["order_id"]: order_info})
               
          return result
     
     def get_order_by_id(self, id: int, system_orders_container):
          if id > len(system_orders_container):
               return None
          return system_orders_container[id - 1]
     
     def add_order(self, order: Order):
          if(isinstance(order, Order)):
               self.__orders.append(order)