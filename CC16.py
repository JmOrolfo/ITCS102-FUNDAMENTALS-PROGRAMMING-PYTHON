#SIS 

import os 

S_Record = {}

true = True

print('Welcome Student!')

while True:
    print("SELECT FROM THE OPTION BELOW : \nA - Add Information \nB - Search Records \nC - Modify Record \nD - Delete record \nS - Show Records \nE - Exit ")

    choice = input ("Your Choice : ").upper()
    os.system('cls')

#Student Information
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

#Search Record
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
        os.system('cls')
        

    elif choice =='C':
        os.system('cls')
        for id in S_Record.keys():
            print
        continue
    
    elif choice =='D':
        os.system('cls')
        print('Select Existing Record')
        srch = input('Enter Student Number: ').lower()

        for id in S_Record.keys():
            if srch in S_Record.keys():
                print (f"Student ID{id} in Student Record {record}")

                for i in S_Record[srch]:
                    print(f'-- {i}')
            else:
                print('Record not found')
        continue
    
    elif choice =='S':
        os.system('cls')
        print("Loading Records... ")
        for id , record in S_Record.keys():
            print(f"Student ID{id} in Student Record {record}")
        continue
    
    elif choice =='E':
        pass
        break
        
                                                                                                                                  
