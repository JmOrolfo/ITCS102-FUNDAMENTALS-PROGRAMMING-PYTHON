import random

num = random.randint(1,10)

tries = 0
guess = True

while guess == True:
    g = int(input("What's your guess from ? : "))
    tries += 1
    
    if guess == num:
        print("CONGRATULATIONS!!!")
        print(f"The answer is {num}")
        print(f"You only took {tries} tries")
        break
    else:
        print("Wrong Guess")
        print("Try Again")
        continue
    
