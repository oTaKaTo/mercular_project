from datetime import date, timedelta
from enum import Enum

class OrderStatus(str, Enum):
    pending_payment = "Pending Payment"
    preparing_order = "Preparing Order"
    on_route = "On Route"
    cancelled_refunded = "Cancelled/Refunded"
    
class Order:
      def __init__(self, payment_method = "", tracking_number = "", total_price = 0, discounted_price = 0, order_id = "", status = ""):
        self.__order_date = date.today()
        self.__delivery_expect_date = self.__order_date + timedelta(days = 4)
        self.__payment_method = payment_method
        self.__tracking_number = tracking_number
        self.__total_price = total_price
        self.__discounted_price = discounted_price
        self.__order_id = order_id
        self.__status = status
          
      def get_order(self):
         return {"order_date": self.__order_date,
                  "delivery_expect_date": self.__delivery_expect_date,
                  "payment_method": self.__payment_method,
                  "tracking_number": self.__tracking_number,
                  "total_price": self.__total_price,
                  "discounted_price": self.__discounted_price,
                  "order_id": self.__order_id,
                  "status": self.__status
                  }