from datetime import date, timedelta
from enum import Enum
from shipping_address import ShippingAddress

class OrderStatus(Enum):
    pending_payment = 0
    preparing_order = 1
    on_route = 2
    cancelled_refunded = 3
    
class Order:
      order_id_counter = 0
      tracking_number_counter = 0
      
      def __init__(self, payment_method = "", total_price = 0, discounted_price = 0, status: str = "", items: list = [], shipping_address: ShippingAddress = None):
        self.__order_date = date.today()
        self.__delivery_expect_date = self.__order_date + timedelta(days = 4)
        self.__payment_method = payment_method
        self.__total_price = total_price
        self.__discounted_price = discounted_price
        self.__status = status
        self.__items_list = items
        self.__shipping_address = shipping_address
        
        Order.order_id_counter += 1
        Order.tracking_number_counter += 1
        self.__tracking_number = Order.tracking_number_counter
        self.__order_id = Order.order_id_counter
          
      def get_order(self):
          return {"order_date": self.__order_date,
                  "delivery_expect_date": self.__delivery_expect_date,
                  "payment_method": self.__payment_method,
                  "tracking_number": str(self.__tracking_number),
                  "total_price": self.__total_price,
                  "discounted_price": self.__discounted_price,
                  "order_id": str(self.__order_id),
                  "status": self.__status,
                  "items_list": self.__items_list,
                  "shipping_address": self.__shipping_address
                  }