#Finals Project - Importing all activities and CCs

from Activity1 import Activity1
from Activity2 import Activity2
from Activity3 import Activity3
from Activity4 import Activity4
from Activity5 import Activity5
from Activity6 import Activity6
from Activity7 import Activity7
from Activity8 import Activity8
from Activity9 import Activity9
from Activity10 import Activity10
from Activity11 import Activity11
from Activity12 import Activity12
from Activity13 import Activity13
from Activity14 import Activity14
from Activity15 import Activity15
from Activity16 import Activity16
from Activity17 import Activity17
from Activity18 import Activity18
from Activity19 import Activity19
from Activity20 import Activity20
from Activity21 import Activity21
from Activity22 import Activity22
from Activity23 import Activity23
from Activity24_1 import Activity24_1
from Activity24 import Activity24
from Activity25 import Activity25
from Activity25_1 import Activity25_1
from Activity25_2 import Activity25_2
from Activity26 import Activity26
from Activity27 import Activity27
from Activity28 import Activity28
from CC1 import CC1
from CC2 import CC2
from CC3 import CC3
from CC4 import CC4 
from CC5 import CC5
from CC6 import CC6
from CC7 import CC7
from CC8 import CC8
from CC9 import CC9
from CC10 import CC10
from CC11 import CC11
from CC12 import CC12
from CC13 import CC13
from CC14 import CC14
from CC15 import CC15
from CC16 import CC16
def Finals():
    import os
    while True:
        print("\n===============================================")
        print("Welcome to Python Fundamentals Interactive Menu")
        print("===============================================")
        print("1. Print Statements")
        print("2. Variables and Operators")
        print("3. Conditionals")
        print("4. Loops")
        print("5. Lists")
        print("6. Functions")
        print("7. Exit Program")
        print("===============================================")
        choice = input("Select an option from (1-7):\n===============================================\nEnter choice: ")
        os.system('cls')

    #PRINT STATEMENTS
        if choice == '1':
            print("\n=======================")
            q1 = input("What do you want to see?\n=======================\na- activities\nb - challenges\nEnter choice: ").lower()
            os.system('cls')
            if q1 == 'a':
                print("\n===============================================")
                q2 = input("Do you want to see the activities? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q2 == 'yes':
                    print("\n===============================================")
                    print("Here are the activities!")
                    print("List of Activities using Print Statements:\n")
                    print("===============================================")
                    print("Choose from options below:")
                    print("===============================================")
                    print("1. Activity 1, Basic Personal Info")
                    print("2. Activity 2, Interactive Greetings")
                    print("3. Activity 3, Name Leght using len()")
                    print("4. Activity 4, Type Checker")
                    print("5. Activity 15, String Formatting")
                    print("===============================================")
                    choi = input("Select an option from (1-4):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        Activity1()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        Activity2()
                        print("\n===============================================")
                        continue
                    elif choi == '3':
                        print("\n===============================================")
                        Activity3()
                        print("\n===============================================")
                        continue
                    elif choi == '4':
                        print("\n===============================================")
                        Activity4()
                        print("\n===============================================")
                        continue
                    elif choi == '5':
                        print("\n===============================================")
                        Activity15()
                        print("\n===============================================")
                        continue
                        
                    else:
                        print("\n========================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n========================================")
                        continue
                elif q2 == 'no':
                    print("============================")
                    print("Okay, skipping activities.")          
                    print("============================")
                    continue
                else:
                    print("\n========================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n========================================")
                    continue

            elif q1 == 'b':
                print("\n===============================================")
                q3 = input("Do you want to see the challenges? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q3 == 'yes':
                    print("\n===============================================")
                    print("Here are the challenges!")
                    print("List of Challenges using Print Statements:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. CC1, ")
                    print("\n===============================================")
                    choi = input("Select an option from (1):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        CC1()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                elif q3 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping challenges.")
                    print("\n===============================================")
                    continue                       
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue
                
    #VARIABLES AND OPERATORS        
        elif choice == '2':
            print("\n=======================")
            q1 = input("What do you want to see?\n=======================\na- activities\nb - challenges\nEnter choice: ").lower()
            os.system('cls')
            if q1 == 'a':
                print("\n===============================================")
                q2 = input("Do you want to see the activities? (yes or no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q2 == 'yes':
                    print("\n===============================================")
                    print("Here are the activities!")
                    print("List of Activities using Variables and Operators:\n")
                    print("===============================================")
                    print("Choose from options below:")
                    print("===============================================")
                    print("1. Activity 5, Evaluating using Arithmetic Operators")
                    print("2. Activity 6, Arithmetic Operation Demo")
                    print("3. Activity 7, Compound Assignment Operators")
                    print("4. Activity 8, Numbers and Strings")
                    print("5. Activity 9, Logical 'and' Operator for string matches")
                    print("===============================================")
                    choi = input("Select an option from (1-5):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        Activity5()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        Activity6()
                        print("\n===============================================")
                        continue
                    elif choi == '3':
                        print("\n===============================================")
                        Activity7()
                        print("\n===============================================")
                        continue
                    elif choi == '4':
                        print("\n===============================================")
                        Activity8()
                        print("\n===============================================")
                        continue
                    elif choi == '5':
                        print("\n===============================================")
                        Activity9()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                elif q2 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping activities.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue
                
            elif q1 == 'b':
                print("\n===============================================")
                q3 = input("Do you want to see the challenges? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q3 == 'yes':
                    print("\n===============================================")
                    print("Here are the challenges!")
                    print("List of Challenges using Variables and Operators:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. CC2, Deposit Calculator")
                    print("2. CC7, SUMMATION OF ALL ODD NUMBERS")
                    print("\n===============================================")
                    choi = input("Select an option from (1-2):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        CC2()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        CC7()
                        print("\n===============================================")
                        continue    
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                elif q3 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping challenges.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue  
                            
    #CONDITIONALS   
        elif choice == '3':
            print("\n=======================")
            q1 = input("What do you want to see?\n=======================\na- activities\nb - challenges\nEnter choice: ").lower()
            os.system('cls')
            if q1 == 'a':
                print("\n===============================================")
                q2 = input("Do you want to see the activities? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q2 == 'yes':
                    print("\n===============================================")
                    print("Here are the activities!")
                    print("List of Activities using Conditionals:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. Activity 10, Discount Calculation using if/else")
                    print("2. Activity 11, Temperature Analyzer using if/else")
                    print("\n===============================================")
                    choi = input("Select an option from (1-2):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        Activity10()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        Activity11()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                elif q2 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping activities.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue
                
            elif q1 == 'b':
                print("\n===============================================")
                q3 = input("Do you want to see the challenges? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q3 == 'yes':
                    print("\n===============================================")
                    print("Here are the challenges!")
                    print("List of Challenges using Conditionals:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. CC3, Using getpass to hide password input")
                    print("2. CC4, Odd or Even")
                    print("3. CC5, Anime and Manga Recommendation")
                    print("\n===============================================")
                    choi = input("Select an option from (1-3):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        CC3()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        CC4()
                        print("\n===============================================")
                        continue
                    elif choi == '3':
                        print("\n===============================================")
                        CC5()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                elif q3 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping challenges.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue
                
    #LOOPS   
        elif choice == '4':
            print("\n=======================")
            q1 = input("What do you want to see?\n=======================\na- activities\nb - challenges\nEnter choice: ").lower()
            os.system('cls')
            if q1 == 'a':
                print("\n===============================================")
                q2 = input("Do you want to see the activities? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q2 == 'yes':
                    print("\n===============================================")
                    print("Here are the activities!")
                    print("List of Activities using Loops:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. Activity 12, Basic Looping")
                    print("2. Activity 13, String Accomudation Using Loop")
                    print("3. Activity 14, Reverse Counting using for loop")
                    print("4. Activity 16, Printing Horizontaly using for loop")
                    print("5. Activity 17, Simple Nested Loop")
                    print("6. Activity 18, Printing Half Pyramid using for loop")
                    print("7. Activity 19, Half Pyramid Pattern")
                    print("8. Activity 20, Looping")
                    print("9. Activity 21, Using While loop")
                    print("10. Activity 22, Number Guessing Game using while loop")  
                    print("\n===============================================") 
                    choi = input("Select an option from (1-10):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        Activity12()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        Activity13()
                        print("\n===============================================")
                        continue
                    elif choi == '3':
                        print("\n===============================================")
                        Activity14()
                        print("\n===============================================")
                        continue
                    elif choi == '4':
                        print("\n===============================================")
                        Activity16()
                        print("\n===============================================")
                        continue
                    elif choi == '5':
                        print("\n===============================================")
                        Activity17()
                        print("\n===============================================")
                        continue
                    elif choi == '6':
                        print("\n===============================================")
                        Activity18()
                        print("\n===============================================")
                        continue
                    elif choi == '7':
                        print("\n===============================================")
                        Activity19()
                        print("\n===============================================")
                        continue
                    elif choi == '8':
                        print("\n===============================================")
                        Activity20()
                        print("\n===============================================")
                        continue
                    elif choi == '9':
                        print("\n===============================================")
                        Activity21()
                        print("\n===============================================")
                        continue
                    elif choi == '10':
                        print("\n===============================================")
                        Activity22()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                elif q2 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping activities.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue

            elif q1 == 'b':
                print("\n===============================================")
                q3 = input("Do you want to see the challenges? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q3 == 'yes':
                    print("\n===============================================")
                    print("Here are the challenges!")
                    print("List of Challenges using Loops:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. CC6, Multiplication Table using for loop")
                    print("2. CC8, Factorial Calculation")
                    print("3. CC9, Summation of All Odd Numbers")
                    print("4. CC10, Printing Pyramid Pattern")
                    print("5. CC11, Printing Diamond Pattern")
                    print("6. CC12, Palindrome Number Pyramid Pattern")
                    print("7. CC13, Printing Christmas Tree Pattern")
                    print("8. CC14, Sum of Odd Numbers with Input Validation")
                    print("\n===============================================")
                    choi = input("Select an option from (1-8):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        CC6()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        CC8()
                        print("\n===============================================")
                        continue
                    elif choi == '3':
                        print("\n===============================================")
                        CC9()
                        print("\n===============================================")
                        continue
                    elif choi == '4':
                        print("\n===============================================")
                        CC10()
                        print("\n===============================================")
                        continue
                    elif choi == '5':
                        print("\n===============================================")
                        CC11()
                        print("\n===============================================")
                        continue
                    elif choi == '6':
                        print("\n===============================================")
                        CC12()
                        print("\n===============================================")
                        continue
                    elif choi == '7':
                        print("\n===============================================")
                        CC13()
                        print("\n===============================================")
                        continue
                    elif choi == '8':
                        print("\n===============================================")
                        CC14()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                    
                elif q3 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping challenges.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue
                
    #LISTS   
        elif choice == '5':
            print("\n=======================")
            q1 = input("What do you want to see?\n=======================\na- activities\nb - challenges\nEnter choice: ").lower()
            os.system('cls')
            if q1 == 'a':
                print("\n===============================================")
                q2 = input("Do you want to see the activities? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q2 == 'yes':
                    print("\n===============================================")
                    print("Here are the activities!")
                    print("List of Activities using Lists:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. Activity 23, List Fundamentals and Iteration")
                    print("2. Activity 26, Dictionary Basics")
                    print("\n===============================================")
                    choi = input("Select an option from (1-2):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        Activity23()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        Activity26()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                    
                elif q2 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping activities.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue
                
            elif q1 == 'b':
                print("\n===============================================")
                q3 = input("Do you want to see the challenges? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q3 == 'yes':
                    print("\n===============================================")
                    print("Here are the challenges!")
                    print("List of Challenges using Lists:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. CC15, AniWantchlist")
                    print("\n===============================================")
                    choi = input("Select an option from (1):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        CC15()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                    
                elif q3 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping challenges.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue
                
    #FUNCTIONS   
        elif choice == '6':
            print("\n=======================")
            q1 = input("What do you want to see?\n=======================\na- activities\nb - challenges\nEnter choice: ").lower()
            os.system('cls')
            if q1 == 'a':
                print("\n===============================================")
                q2 = input("Do you want to see the activities? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q2 == 'yes':
                    print("\n===============================================")
                    print("Here are the activities!")
                    print("List of Activities using Functions:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. Activity 24, Function Def and Reuse")
                    print("2. Activity 24_1, Importing Functions")
                    print("3. Activity 25, Program Menu")
                    print("4. Activity 25_1, Simple Input/Output Menu")
                    print("5. Activity 25_2, Creating Main Menu ")
                    print("6. Activity 27, Anime Watch List")
                    print("7. Activity 28, Snake GAME")
                    print("\n===============================================")
                    choi = input("Select an option from (1-7):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        Activity24()
                        print("\n===============================================")
                        continue
                    elif choi == '2':
                        print("\n===============================================")
                        Activity24_1()
                        print("\n===============================================")
                        continue
                    elif choi == '3':
                        print("\n===============================================")
                        Activity25()
                        print("\n===============================================")
                        continue
                    elif choi == '4':
                        print("\n===============================================")
                        Activity25_1()
                        print("\n===============================================")
                        continue
                    elif choi == '5':
                        print("\n===============================================")
                        Activity25_2()
                        print("\n===============================================")
                        continue
                    elif choi == '6':
                        print("\n===============================================")
                        Activity27()
                        print("\n===============================================")
                        continue                        
                    elif choi == '7':
                        print("\n===============================================")
                        Activity28()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue                  
                elif q2 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping activities.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue

            elif q1 == 'b':
                print("\n===============================================")
                q3 = input("Do you want to see the challenges? (yes/no):\n===============================================\nEnter choice: ").lower()
                os.system('cls')
                if q3 == 'yes':
                    print("\n===============================================")
                    print("Here are the challenges!")
                    print("List of Challenges using Functions:\n")
                    print("\n===============================================")
                    print("Choose from options below:")
                    print("\n===============================================")
                    print("1. CC16, Student Info System")
                    print("\n===============================================")
                    choi = input("Select an option from (1):\n===============================================\nEnter choice: ")
                    os.system('cls')
                    if choi == '1':
                        print("\n===============================================")
                        CC16()
                        print("\n===============================================")
                        continue
                    else:
                        print("\n===============================================")
                        print("Invalid input. Returning to main menu.")
                        print("\n===============================================")
                        continue
                elif q3 == 'no':
                    print("\n===============================================")
                    print("Okay, skipping challenges.")
                    print("\n===============================================")
                    continue
                else:
                    print("\n===============================================")
                    print("Invalid input. Returning to main menu.")
                    print("\n===============================================")
                    continue

    #EXIT PROGRAM
        elif choice == '7':
            print("\n===============================================")
            q1 = input("Are you sure you want to exit?\n===============================================\nEnter (yes/no): ").lower()
            os.system('cls')
            if q1 == 'yes':
                print("\n===============================================")
                print("===============================================")
                print("Thank you for using my Menu. Goodbye!\n===============================================\n===============================================")
                break
            elif q1 == 'no':
                print("\n===============================================")
                print("Returning to main menu.")
                print("\n===============================================")
                continue
            else:
                print("\n===============================================")
                print("Invalid input. Returning to main menu.")
                print("\n===============================================")
                continue
    
        else:
            print("\n===============================================")
            print("Invalid choice. Please select a valid option from (1-7):\n===============================================\nEnter choice: ")
            continue
        
if __name__ == "__main__":
    Finals()