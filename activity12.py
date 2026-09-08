import getpass

username = 'seito'
password = 'undertaker'

u = input("Enter Username -->   ")
p = getpass.getpass("Enter password -->   ")
#p = getpass("Enter Password -->   ")
if username == u and password == p :
	print("Good job")
else:
	print("LOL nice try:D")
