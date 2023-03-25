from Order import Order
import OrderHistory
from Account import User

def main():
    order_1 = Order("25/3/2023", "30/3/2023", "QrCode Payment", "3123123123", 2000, "1213231", "ยังส่งไม่ถึงครับ")
    order_2 = Order("25/3/2023", "30/3/2023", "QrCode Payment", "3123123123", 200, "1213231", "ส่งถึงครับ")
    order_3 = Order("25/3/2023", "30/3/2023", "QrCode Payment", "3123", 900, "1213231", "ยังครับ")
    
    User_1 = User("userครับ", "password", "1234@gmail.com", "0123456789", "คนสักคน")
    User_1_order_history = User_1.get_user_order_history()
    User_1_order_history.add_order_history([order_1, order_2, order_3])
    User_1_order_history.get_order()
    return 0
    
if __name__ == "__main__":
    main()