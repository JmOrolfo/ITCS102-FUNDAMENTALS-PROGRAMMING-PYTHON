import os 
import json
S_Record = {}

true = True

print ('STUDENT ACCOUNT')

while True:
    print("SELECT FROM THE OPTION BELOW : \nA - Add Information \nB - Search Records \nC - Modify Record \nD - Delete record \nE - Show Records \nF - Import Record \nG - Export Record \nX - Exit ")

    choice = input ("Your Choice : ").upper()
    os.system('cls')

#CREATING ACCOUNT
    if choice == 'A':
        print('ADDING STUDENT INFORMATION')
        print("-------------------------------")

        S_num = input('Please Input your Student Number: ')

        f_name = input('Enter your First Name: ').upper()
        l_name = input('Enter your Last Name: ').upper()
        course = input('Enter your Course: ').upper()
        email = input("Enter your Email Address: ")

        S_Record[S_num] = [f_name, l_name, course, email]
        print('INFORMATION SAVED')

        os.system('cls')
        continue

#SEARCHING RECORD
    elif choice == 'B':
        os.system('cls')
        srch = input('Enter Student Number: ').lower()

        for id in S_Record.items():
            if srch in S_Record.keys():
                print('RECORD FOUND')

                for i in S_Record[srch]:
                    print(f'-- {i}')

            else:
                print('Record not found')
        continue

# MODIFY / EDIT RECORD
    elif choice =='C':
        os.system('cls')
        srch = input('Enter Student Number: ').lower()

        for id in S_Record.items():
            if srch in S_Record.keys():
                print('RECORD FOUND')

                for i in S_Record[srch]:
                    print(f'-- {i}')
                    
                f_name = input('Enter NEW First Name: ').upper()
                l_name = input('Enter NEW Last Name: ').upper()
                course = input('Enter NEW Course: ').upper()
                email = input("Enter NEW Email Address: ")

                S_Record[srch][0] = f_name
                S_Record[srch][1] = l_name
                S_Record[srch][2] = course
                S_Record[srch][3] = email

            else:
                print('Record not found')
        continue

#DELETING RECORD
    elif choice =='D':  
        
        os.system('cls')
        print("Delete existing record")
        srch = input("key of the information: ")
        if  srch in S_Record.keys(): 
            print("Record deleted")
            print("--------------------------")
            for i in S_Record[srch]:
                    print(f": {i}")

            S_Record.pop(srch)
            print("Record deleted")
        else:
            print("Information cannot found") 
        continue

#Show/Print Record
    elif choice =='E':
        os.system('cls')
        for a,b in S_Record.items(): 
            print(f"STUDENTS ID {a}: STUDENT RECORD {b}")
#Import Record
    elif choice == 'F':
        ("IMPORTING RECORD...")
        os.system('cls')
        try:
            with open('S_Record.json','r') as new_file:
                S_Record = json.load(new_file)

                print("Data Imported Successfully")
        except FileNotFoundError:
            print("Error: 'S_Record.json' not found. Please Export a record first.")
        continue
#Export Record
    elif choice == 'G':
        os.system('cls')
        print("EXPORTING RECORD...")
        with open('S_Record.json', 'w') as new_file:
            json.dump(S_Record, new_file , indent=4)
            print("Data Exported")
            continue

    elif choice =='X':
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
        continue
                                                                                                                                

            
                                                                                                                                    

