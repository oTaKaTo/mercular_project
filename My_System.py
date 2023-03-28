from Account import *
class System:
    def __init__(self):
        self.__user_lst = []

    def get_user_lst(self):
        return self.__user_lst
        
    def create_account(self,username, password, email, phone_number=None):
            if self.check_exists_account(email)==True:
                return "already has account using this email"
            else:
                self.__user_lst.append(User(username,password,email,phone_number))
                self.login(email,password)
                return "Create account successfully"
            
    def check_exists_account(self,email):
            for ID in self.__user_lst:
                if ID.get_Email() == email:
                    return True
            return False
   
    def login(self,email,password):
        ID = self.check_id_password(email,password)
        if ID != False:
            ID.set_online_status(True)
            return f"online statue = {ID.get_online_status()}"
        return "email or password invaild"
   
    def check_id_password(self,email, password):
            for ID in self.__user_lst:
               if ID.get_Email()==email and ID.get_password() == password:
                   return ID
            return False
    
    def logout(self,ID):
            ID.set_online_status(False)
            return True
            
mySystem = System()
#create Account
mySystem.create_account("momo","1234","MOMO@gmail.com")
#print(mySystem.get_user_lst())
#print(mySystem.create_account("momo","1234","MOMO@gmail.com"))
#login
#print(mySystem.create_account("momo","1234","MOMO@gmail.com"))
#print(mySystem.login("MOMO@gmail.com","1234"))
#print(mySystem.login("MOMO3@gmail.com","1234"))
#print(mySystem.login("MOMO@gmail.com","12345678"))
#logout
account_list = mySystem.get_user_lst()
print(account_list[0].get_online_status())
mySystem.logout(mySystem.get_user_lst()[0])
print(account_list[0].get_online_status())
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