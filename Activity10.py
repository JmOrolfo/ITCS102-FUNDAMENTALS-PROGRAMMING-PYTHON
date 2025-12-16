#Discount Calculation using 'if/else'
# def Activity10():
print("---------------------------")
print("--WELCOME to Item Counter--")
print("---------------------------")

name = input("Enter name: ")
item = input("Item: ")
no = eval(input("Quantity: "))
prc = eval(input("Price Each: "))
pwd = input("are you PWD or Senior(Yes/No): ")
subtot = no * prc
disc = 0

if pwd.lower() == "yes":
	disc_am = subtot * 0.05
	total_with_disc = subtot - disc_am
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",no,"\nPrice each: ",prc,"\nTotal: ",subtot ,"\nDiscount:",disc_am,"\nTotal w/discount: ", total_with_disc)
else:
	total_with_disc = subtot 
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",no,"\nPrice each: ",prc,"\nTotal: ",subtot ,"\nDiscount:","\nTotal w/discount: ", total_with_disc)
