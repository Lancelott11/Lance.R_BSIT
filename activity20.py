from getpass import getpass

isLogin = False
while isLogin == False :
    username = input("Enter your user: ")
    password = getpass("Enter your pass: ")

    if username == "Sei" and password == "SEII":
        print("LUPET SANGGALA")
        isLogin = True
    else :
        print("HACKER HACKER, BADAP KAAA")