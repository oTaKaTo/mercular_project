from Account import *
class System:
    def __init__(self):
        self.__user_lst = []
    def create_account(self,username, password, email, phone_number=None):
            if self.check_exists_account(email):
                return False
            else:
                self.__user_lst.append(User(username,password,email,phone_number))
                return True
            
    def check_exists_account(self,email):
            for ID in self.__user_lst:
                if ID.get_Email() == email:
                    return True
            return False
    
    def check_id_password(self,email, password):
            for ID in self.__user_lst:
               if ID.get_Email==email and ID.get_password == password:
                   return True
            return False
    
    def Logout(self,ID):
            pass
        
mySystem = System()
print(mySystem.create_account("momo","1234","MOmo@gmail.com"))
print(mySystem.create_account("momo","1234","MOmo@gmail.com"))
print(mySystem.check_exists_account("MOmo@gmail.com"))
print(mySystem.check_exists_account("MOmo@gmaisl.com"))      
print(mySystem.check_id_password("MOmo@gmail.com","1234"))    
print(mySystem.check_id_password("MOmo@gmail.com","123s4"))   
print(mySystem.check_id_password("MOmsdasado@gmail.com","123s4")) 

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