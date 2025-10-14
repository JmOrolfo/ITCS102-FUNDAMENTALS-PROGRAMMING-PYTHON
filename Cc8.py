#Multiplication Table using for loop
print("Multiplication Table")
num = eval(input("Enter a Number: "))
print("Multiplication Table For: ",num)
for u in range(1 ,11):
  total = num * u
  print(num,"x",u,"=", total)