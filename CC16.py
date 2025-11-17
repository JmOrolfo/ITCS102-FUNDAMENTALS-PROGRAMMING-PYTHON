import os 

dic = {}

true = True

print('Welcome Student!')

while True:
    print("SELECT FROM THE OPTION BELOW : \nA - Add Information \nB - Search Records \nC - Modify Record \nD - Delete record \nE - Exit ")

    choice = input ("Your Choice :").upper()

    if choice == 'a':
        print('Adding Student Information')
        print("-------------------------------")

        S_num = input ('Please Input your Student Number: ')

        f_name = input('Enter your First Name: ').upper()
        l_name = input('Enter your Last Name: ').upper()
        course = input('Enter your Course: ').upper()
        email = input("Enter your Email Address: ")
        isSingle = input('Are you single? (Yes or No):').upper()

        dic = {S_num: [f_name, l_name, course, email, isSingle]}
        print('INFORMATION SAVED')

        os.system('cls')
        continue
#search
    elif choice == 'b':
        os.system('cls')
        srch = input('Enter Student Number: ')

        if srch in dic.keys():
                print('Record Found')

                for i in dic[srch]:
                    print(i)
        else:
             print('Record not found')
        
    elif choice =='c':
         pass
         continue
    os.system('cls')
