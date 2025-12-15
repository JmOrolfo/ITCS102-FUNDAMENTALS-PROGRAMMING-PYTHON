#SUMMATION OF ALL ODD NUMBERS
def CC7():
    i = 0
    for x in range(1, 11,1): 
        y = eval(input("Enter a Number: "))
        if y % 2:
            i += y
    print("The Sum of all odd number is",i) 
