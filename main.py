from Product import Product
from System import System
from Account import User

my_product = Product("123", "321", "keyboardRGB", "keyboard", "razor", 920, 20)
my_second_product = Product("12341", "4123", "mouseRGB", "mouse", "stellseries", 200, 10)
my_system = System()
my_user = User("admin", "password", "1234@gmail.com", "0123456789", "คนสักคน")

my_cart = my_user.get_user_cart()
my_user.add_item_to_cart(my_product, 2)

print(my_product)
print(my_user.add_item_to_cart(my_second_product, 2))

print(my_cart.get_items_in_cart())
print(my_cart.get_total_price())

# my_cart.delete_item(my_cart.get_items_in_cart()[0])
print(my_cart.get_items_in_cart())


