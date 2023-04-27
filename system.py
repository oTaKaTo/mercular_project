from Account import *
from promotion import *
from fastapi.exceptions import HTTPException

class System:
    def __init__(self):
        self.__user_lst = []
        self.__coupon_catalog = CouponCatalog()
        self.__product_catalog = ProductCatalog()

    def get_user_lst(self):
        return self.__user_lst
    
    def get_coupon_catalog(self):
        return self.__coupon_catalog
    
    def get_product_catalog(self):
        return self.__product_catalog
        
    def create_account(self,username, password, email, phone_number=None):
            if self.check_exists_account(email) != False:
                return "already has account using this email"
            else:
                self.__user_lst.append(User(username,password,email,phone_number))
                self.login(email,password)
                return "Create account successfully"
            
    def check_exists_account(self, email):
            for ID in self.__user_lst:
                if ID.get_Email() == email:
                    return ID
            raise HTTPException(status_code=404, detail="User not found")

    def login(self,email,password):
        ID = self.check_id_password(email,password)
        if ID != False:
            ID.set_online_status(True)
            return f"online statue = {ID.get_online_status()}"
        return "email or password invaild"

    def check_id_password(self, email, password):
            for ID in self.__user_lst:
                if ID.get_Email()==email and ID.get_password() == password:
                    return ID
            return False
    
    def logout(self, ID):
            ID.set_online_status(False)
            return True
