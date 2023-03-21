# from Product import ProductCatalog
# import System

# def main():
#     product_catalog = ProductCatalog()
#     web_marketplace_system = System(product_catalog)
    
# if __name__ == "__main__":
#     main()
from Product import Product
from System import System

my_product = Product("123", "321", "keyboardRGB", "keyboard", "razor", 920, 20)
my_system = System()

print(my_product)


print(my_system.addtocart(my_product, 2))

