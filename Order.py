class Order:
      def __init__(self, order_date = "", delivery_expect_date = "", payment_method = "", tracking_number = "", total_price = 0, order_id = "", status = ""):
        self.__order_date = order_date
        self.__delivery_expect_date = delivery_expect_date
        self.__payment_method = payment_method
        self.__tracking_number = tracking_number
        self.__total_price = total_price
        self.__order_id = order_id
        self.__status = status
        
      def get_order_info(self):
         order_info = (f"order_date: {self.__order_date}\n"
                        f"delivery_expect_date: {self.__delivery_expect_date}\n"
                        f"payment_method: {self.__payment_method}\n"
                        f"tracking_number: {self.__tracking_number}\n"
                        f"total_price: {self.__total_price}\n"
                        f"order_id: {self.__order_id}\n"
                        f"status: {self.__status}\n")
         return order_info