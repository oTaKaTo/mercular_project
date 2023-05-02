from order import Order

class OrderHistory:
     def __init__(self, orders = []):
          self.__orders = orders # list for store Orders
     
     def get_order_info(self):
          result = ""
          for order in self.__orders:
               result += f"{order.get_order()}" + '\n'
          result = result[:-1]
          return result
     
     def add_order_history(self, orders: list):
          for order in orders:
               if(isinstance(order, Order)):
                    self.__orders.append(order)