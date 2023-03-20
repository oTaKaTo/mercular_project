from Product import ProductCatalog
import System

def main():
    product_catalog = ProductCatalog()
    web_marketplace_system = System(product_catalog)
    
if __name__ == "__main__":
    main()