
print("---------------------------")
print("--WELCOME to Item Counter--")
print("---------------------------")

name = input("What is your Name? :")
item = input("What item are you buying? (COFFEE/MILK) : ")
no = eval(input("How many(1-10): "))
prc = eval(input("How much? "))
pwd = input("are you PWD or Senior(Yes/No): ")
total = many * prc * .05
tot = no * prc
disc = man - equal

print("---------------------------")
print("---------------------------")
if pwd.lower() == "yes":
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",no,"\nPrice each: ",prc,"\nTotal: ",tot ,"\nDiscount:",total,"\nTotal w/discount: ",disc)
else:
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",no,"\nPrice each: ",prc,"\nTotal: ",tot ,"\nDiscount:","\nTotal w/discount: ",tot)
