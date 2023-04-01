from Account import *
from promotion import *
from Product import *
from fastapi import FastAPI
from typing import Union
class System:
    def __init__(self):
        self.__user_lst = {} 
        self.__coupon_catalog = CouponCatalog()
        self.__product_catalog = ProductCatalog()

    def get_user_lst(self):
        return self.__user_lst
    
    def get_coupon_catalog(self):
        return self.__coupon_catalog
        
    def create_account(self,username, password, email, phone_number=None):
            if self.check_exists_account(email)!=False:
                return "already has account using this email"
            else:
                self.__user_lst[email] = User(username,password,email,phone_number)
                self.login(email,password)
                return "Create account successfully"
    
    def get_product_catalog(self):
        return self.__product_catalog        
    
    def check_exists_account(self,email):
            if email in self.__user_lst:
                return True
            return False
    
    def login(self,email,password):
        
        ID = self.check_id_password(email,password)
        
        if ID != False:
            ID.set_online_status(True)
            return f"online statue = {ID.get_online_status()}"
        return "email or password invaild"
    
    def check_id_password(self,email, password):
            if email in self.__user_lst:
                if self.__user_lst[email].get_password() == password:
                    return self.__user_lst[email]
            return False
    
    def logout(self,ID):
            ID.set_online_status(False)
            return True

mySystem = System()
mySystem.create_account("momo","1234","MOMO@gmail.com")
"""price= 300
my_coupon = FlatCoupon("26-4-2023", 100, 50, 1)
my_pc_coupon = PercentageCoupon("23-4-2023", 100, 20, 10, 1)
mySystem.get_coupon_catalog().add_coupon(my_coupon)
mySystem.get_coupon_catalog().add_coupon(my_pc_coupon)
print(mySystem.get_coupon_catalog().get_coupon())
mySystem.get_user_lst()["MOMO@gmail.com"].add_user_coupon("2",mySystem.get_coupon_catalog().get_coupon())
mySystem.get_user_lst()["MOMO@gmail.com"].get_user_coupon()
print(mySystem.get_user_lst()) 
print(mySystem.create_account("momo","1234","MOMO@gmail.com"))
print(mySystem.create_account("momo","1234","MOMO@gmail.com"))
print(mySystem.login("MOMO@gmail.com","1234"))
print(mySystem.login("MOMO3@gmail.com","1234"))
print(mySystem.login("MOMO@gmail.com","12345678"))
account_list = mySystem.get_user_lst()
print(account_list["MOMO@gmail.com"].get_online_status())
mySystem.logout(mySystem.get_user_lst()["MOMO@gmail.com"])
print(account_list["MOMO@gmail.com"].get_online_status())"""

"""  
    def Register(email,username,password):
            for ID in self.user_lst:
                if ID.get_Email() == email:
                    print ("Email is already use")
                    break;
            else:
                    user_lst.append(User(username,password,email))

    def Login(email,password):
            for ID in user_lst:
                if (ID.get_Email() == email)  and ID.get_password()==password:
                    print("Login success")
                    break;
            else:
                    print("invail Email or password")
    def Logout():
            print("Logout Confirm\nY/N")
            while(True):
                Input = input()
                if  Input=="Y":
                    print("Logout Success")
                    break;
                elif Input=="N":
                    print("Continue Login")
                    break;
                else:
                    print("Error!!!!\nPlease Enter Y or N")
Register("momo@gmail.com","momo","1234")
Register("momo@gmail.com","momo","1234")
Login("momo@gmail.com","1234")
"""
#test coupon
"""
#test admin class
price= 300
my_coupon = FlatCoupon("26-4-2023", 100, 50, 1)
my_pc_coupon = PercentageCoupon("23-4-2023", 100, 20, 10, 1)
my_coupon_catalog = CouponCatalog()
my_coupon_catalog.add_coupon(my_coupon)
my_coupon_catalog.add_coupon(my_pc_coupon)
mySystem.get_user_lst()[0].add_user_coupon("2",my_coupon_catalog.get_coupon())
print(mySystem.get_user_lst()[0].add_user_coupon("2",my_coupon_catalog.get_coupon()))
print(mySystem.get_user_lst()[0].get_user_coupon()[0].get_id())
print(mySystem.get_user_lst()[0].user_used_coupon(mySystem.get_user_lst()[0].get_user_coupon()[0]))
print(mySystem.get_user_lst()[0].get_used_user_coupons())
mySystem.get_user_lst().append(Admin("Admin","Admin","Admin@gmail.com"))
"""
"""
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World My friend"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "Hi"):
    return {"item_id": item_id, "q": q}

@app.get("/account/profile")
def read_user_infor():
    return {mySystem.get_user_lst()[0]}

"""