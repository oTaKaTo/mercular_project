import Order

class OrderHistory:
     def __init__(self, orders):
          self.__orders = [] # list for store Orders

     def add_order_history(self, orders):
          if(isinstance(orders, Order)):
            self.__orders.append(orders)
          
     def get_order_history(self):
          return self.__orders