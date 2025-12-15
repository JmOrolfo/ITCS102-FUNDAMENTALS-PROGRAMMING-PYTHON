#Number guessing
def Activity22():
    import random

    num = random.randint(1,11)

    tries = 0
    guess = True

    while guess == True:
        g = int(input("What's your guess from 1-10 ? : "))
        tries += 1
        
        if g == num:
            print("CONGRATULATIONS!!!")
            print(f"The answer is {num}")
            print(f"You only took {tries} tries")
            break
        
        else:
            print("Wrong Guess")
            stop = input("R - Retry\nS - Stop\nEnter here: ").upper()
            if stop == 'R':
                print("Try Again")
                continue

            else:
                print(f"The answer is {num}")
                print("Thank you for playing")
                break
