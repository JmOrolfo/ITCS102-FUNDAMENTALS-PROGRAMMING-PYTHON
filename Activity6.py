#Arithmetic Operation Demonstration

x = eval(input("First Number -> "))
y = eval(input("Second Number -> "))

s = x + y
d = x - y
p = x * y 
q = x / y

#solution = ((x / y) * 25 - 8 ) // 120
print("\n The sum of" ,x, "and" ,y, "is", s)
print("\n The diffirence of" ,x, "and"  ,y, "is", d)
print("\n The product of" ,x, "and" ,y, "is", p)
print("\n The qoutient of" ,x, "and" ,y, "is", q)
print(x, "exponent be" ,y, "is" ,x**y )
print("The remainder of" ,x, "and" ,y, "is" ,x % y)
print("The floor division of" ,x, "and" ,y, "is" ,x//y)

