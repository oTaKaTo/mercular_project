from Account import *
user_lst = []
def Register(email,username,password):
        for ID in user_lst:
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


