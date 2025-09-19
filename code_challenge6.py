x = eval(input("The Factorial of : "))
result = 1
for y in range( x ,0 ,-1):
    result *= y
    print(result, "*", y, "=" , result)
print("The total of the Factorial of", x, "is" , result) 