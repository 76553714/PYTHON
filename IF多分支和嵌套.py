s = int(input("pls input the weight"))
if s > 300 :print("you are so fat")
elif s > 200 : print ("you are a little fat")
else : print ("OK")

username = input("input user name") ##输入完用户名会提示
if username == "admin" : 
    print("user name correct, then input the password")
    password = input ("pls input password")
    if password == "123":print("login successfully")
    else: print("PWD not correct")
else : print("username not exist")

username = input("input user name") ##用户名和密码要一次性输入
password = input("pls input password")
if username == "admin" : 
    print("user name correct")
    if password == "123":print("login successfully")
    else: print("PWD not correct")
else : print("username not exist")