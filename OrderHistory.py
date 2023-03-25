from Order import Order

class OrderHistory:
     def __init__(self, orders = []):
          self.__orders = orders # list for store Orders
     
     def get_order(self):
          for order in self.__orders:
               print(f"{order.get_order_info()}")
          return 0
     
     def add_order_history(self, orders):
          if(isinstance(orders, list)):
               for order in orders:
                    if(isinstance(order, Order)):
                         self.__orders.append(order)
          elif(isinstance(orders, Order)):
               self.__orders.append(orders)
          return 0