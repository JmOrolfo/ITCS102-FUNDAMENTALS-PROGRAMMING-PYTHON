#SIS 

import os 
import json
S_Record = {}

true = True

print ('STUDENT ACCOUNT')

while True:
    print("SELECT FROM THE OPTION BELOW : \nA - Add Information \nB - Search Records \nC - Modify Record \nD - Delete record \nS - Show Records \nE - Exit ")

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
        print('Select Existing Record')
        srch = input('Enter Student Number: ').lower()

        for id in S_Record.keys():
            if srch in S_Record.keys():
                print (f"Student ID{id} in Student Record {S_Record}")

                for i in S_Record[srch]:
                    print(f'-- {i}')
            else:
                print('Record not found')
        continue
    
    elif choice =='E':
        os.system('cls')
        print("Loading Records... ")

        for id in S_Record.keys():
            print(f"Student ID{id} in Student Record {S_Record}")
        continue

    elif choice == 'F':
        os.system('cls')
        print('IMPORT RECORD')  #pang save

        with open ('STUDENT_RECORD.json', 'r') as new_file:
            student_json = json.load(new_file)

        S_Record = student_json
        print('RECORD IMPORTED')

    elif choice == 'G':
        os.system('cls')
        print('EXPORT RECORD') #pang awan 

        with open ('STUDENT_RECORD.json', 'w') as new_file:
            student_json = json.load(new_file)

        S_Record = student_json
        print('RECORD EXPORTED')

    elif choice =='X':

        pass
        break
        
                                                                                                                                  
