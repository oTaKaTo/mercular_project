user_dic = {}
def Register(email,password):
    for name in user_dic:
        if name == email:
            print ("Email is already use")
            break;
    else:
        user_dic[email] = password

def Login(email,password):
    for name in user_dic:
        if name == email and user_dic[name]==password:
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

Register("momo@gmail.com","1234")
Register("2321231@gmail.com","5678")
Register("uhkjhjkjh@gmail.com","91011")
Register("momo@gmail.com","126534")
print(user_dic)
Login("momo@gmail.com","1234")
Login("momo123@gmail.com","1234")
Login("momo@gmail.com","12345")
Logout()