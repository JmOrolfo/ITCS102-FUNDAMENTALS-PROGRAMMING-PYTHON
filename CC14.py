#def CC14():
name = input("Enter your name: ")
print("Input 0 to stop program")

odd = 0
num = ""
yes = True

while yes == True:
    nom = eval(input("Put a number: "))
    if nom % 2 == 1:
        print("ODD number detected")
        odd += nom
        num += str(nom) + ","
    elif nom == 0:
        print("End")
        break
    else:
        print("EVEN number detected!")
        print("Skipping...")
        continue
print(f"Total of all ODD numbers: {odd}")
print(f"All ODD numbers: {num}")

