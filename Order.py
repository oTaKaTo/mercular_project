class Order:
     def __init__(self, order_date, delivery_expect_date, payment_method, tracking_number, total_price, order_id, status):
        self.__order_date = order_date
        self.__delivery_expect_date = delivery_expect_date
        self.__payment_method = payment_method
        self.__tracking_number = tracking_number
        self.__total_price = total_price
        self.__order_id = order_id
        self.__status = status