from getpass import getpass
uname = "Orolfojm08"
pwd = "ingreso08"

user = input("Create your User name :")
passw = getpass("Enter password :" )
if user == uname.lower() and passw == pwd:
	print("Access granted")
	print("Welcome to the Program")
else:

	print("Access denied")
