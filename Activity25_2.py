#Final Program
#def Activity25_2():
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

print("Hello, Welcome to Matrix AI")
name = input ("What should I call you? : ")
print(f"Nice to meet you, {name}")
true = True 
while true == True:
    print("Please choose from the option list below")
    print("A - ACTIVITIES\nB - CHALLANGES\n C - Exit")
    choi = input("Enter your choice: ").upper()
    
    if choi == 'A':
        print("Welcome to Activity List")
        print("ACTIVITY LIST")
        print("1 - ACTIVITIES(1-5)\n2 - ACTIVITIES(6-10)\n3 - ACTIVITIES(11-15)\n4 - ACTIVITIES(16-20)\n5 - ACTIVITIES(21-25)")
        act = input("Enter your choice: ")
        
        if act == '1':
            print("Welcome to ACTIVITIES(1-5)")
            print("1 - ACTIVITY(1)\n2 - ACTIVITY(2)\n3 - ACTIVITY(3)\n4 - ACTIVITY(4)\n5 - ACTIVITY(5)")
            act1 = input("Enter your choice: ")
            
            if act1 == '1':
                

                print('My basic personal info')
                print(f"You choose {act1}")
                print(f"Running Activity {act1}")
                Activity1()
                continue
        
            elif act1 == '2':
                print('Interactive greeting program')
                print(f"You choose {act1}")
                print(f"Running Activity {act1}")
                Activity2()
                continue
        
            elif act1 == '3':
                print(f"You choose {act1}")
                print(f"Running Activity {act1}")
                Activity3()
                continue
        
            elif act1 == '4':
                print(f"You choose {act1}")
                print(f"Running Activity {act1}")
                Activity4()
                continue
            
            elif act1 == '5':
                print(f"You choose {act1}")
                print(f"Running Activity {act1}")
                Activity5()
                continue
        
        elif act == '2':
            print("Welcome to ACTIVITIES(6-10)")
            print("6 - ACTIVITY(6)\n7 - ACTIVITY(7)\n8 - ACTIVITY(8)\n9 - ACTIVITY(9)\n5 - ACTIVITY(10)")
            act2 = input("Enter your choice: ")
            
            if act2 == '6':
                print(f"You choose {act2}")
                print(f"Running Activity {act2}")
                Activity6()
                continue
            
            elif act2 == '7':
                print(f"You choose {act2}")
                print(f"Running Activity {act2}")
                Activity7()
                continue
            
            elif act2 == '8':
                print(f"You choose {act2}")
                print(f"Running Activity {act2}")
                Activity8()
                continue
            
            elif act2 == '9':
                print(f"You choose {act2}")
                print(f"Running Activity {act2}")
                Activity9()
                continue
            
            elif act2 == '10':
                print(f"You choose {act2}")
                print(f"Running Activity {act2}")
                Activity10()
                continue
        
        elif act == '3':
            print("Welcome to ACTIVITIES(11-15)")
            print("11 - ACTIVITY(11)\n12 - ACTIVITY(12)\n13 - ACTIVITY(13)\n14 - ACTIVITY(14)\n15 - ACTIVITY(15)")
            act3 = input("Enter your choice: ")
            
            if act3 == '11':
                print(f"You choose {act3}")
                print(f"Running Activity {act3}")
                Activity11()
                continue
            
            elif act3 == '12':
                print(f"You choose {act3}")
                print(f"Running Activity {act3}")
                Activity12()
                continue
            
            elif act3 == '13':
                print(f"You choose {act3}")
                print(f"Running Activity {act3}")
                Activity13()
                continue
            
            elif act3 == '14':
                print(f"You choose {act3}")
                print(f"Running Activity {act3}")
                Activity14()
                continue
            
            elif act3 == '15':
                print(f"You choose {act3}")
                print(f"Running Activity {act3}")
                Activity15()
                continue
            
        elif act == '4':
            print("Welcome to ACTIVITIES(16-20)")
            print("16 - ACTIVITY(16)\n17 - ACTIVITY(17)\n18 - ACTIVITY(18)\n19 - ACTIVITY(19)\n20 - ACTIVITY(20)")
            act4 = input("Enter your choice: ")
            
            if act4 == '16':
                print(f"You choose {act4}")
                print(f"Running Activity {act4}")
                Activity16()
                continue
            
            elif act4 == '17':
                print(f"You choose {act4}")
                print(f"Running Activity {act4}")
                Activity17()
                continue
            
            elif act4 == '18':
                print(f"You choose {act4}")
                print(f"Running Activity {act4}")
                Activity18()
                continue
            
            elif act4 == '19':
                print(f"You choose {act4}")
                print(f"Running Activity {act4}")
                Activity19()
                continue
            
            elif act4 == '20':
                print(f"You choose {act4}")
                print(f"Running Activity {act4}")
                Activity20()
                continue
            
        elif act == '5':
            print("Welcome to ACTIVITIES(21-25)")
            print("21 - ACTIVITY(21)\n22 - ACTIVITY(22)\n23 - ACTIVITY(23)\n24 - ACTIVITY(24)\n24.1 - ACTIVITY(24_1)\n25 - ACTIVITY(25)\n25.1 - ACTIVITY(25_1)")
            act5 = input("Enter your choice: ")
            
            if act5 == '21':
                print(f"You choose {act5}")
                print(f"Running Activity {act5}")
                Activity16()
                continue
            
            elif act5 == '22':
                print(f"You choose {act5}")
                print(f"Running Activity {act5}")
                Activity22()
                continue
            
            elif act5 == '23':
                print(f"You choose {act5}")
                print(f"Running Activity {act5}")
                Activity23()
                continue
            
            elif act5 == '24':
                print(f"You choose {act5}")
                print(f"Running Activity {act5}")
                Activity24()
                continue
            
            elif act5 == '24.1':
                print(f"You choose {act5}")
                print(f"Running Activity {act5}")
                Activity24_1()
                continue
            
            elif act5 == '25':
                print(f"You choose {act5}")
                print(f"Running Activity {act5}")
                Activity25()
                continue
            
            elif act5 == '25.1':
                print(f"You choose {act5}")
                print(f"Running Activity {act5}")
                Activity25_1()
                continue
            
    elif choi == 'B':
        print("Welcome to Code Challange List")
        print("CODE CHALLANGE LIST")
        print("-------------------------------------------------------------------------")
        print("1 - CODECHALLANGE(1-5)\n2 - CODECHALLANGE(6-10)\n3 - CODECHALLANGE(11-15)")
        cc = input("Enter your choice: ")
        
        if cc == '1':
            print("Welcome to CODE CHALLANGE(1-5)")
            print("1 - CODECHALLENGE(1)\n2 - CODECHALLENGE(2)\n3 - CODECHALLENGE(3)\n4 - CODECHALLENGE(4)\n5 - CODECHALLENGE(5)")
            cc1 = input("Enter your choice: ")
            
            if cc1 == '1':
                print(f"You choose {cc1}")
                print(f"Running Code challenge {cc1}")
                CC1()
                continue
            
            elif cc1 == '2':
                print(f"You choose {cc1}")
                print(f"Running Code challenge {cc1}")
                CC2()
                continue
            
            elif cc1 == '3':
                print(f"You choose {cc1}")
                print(f"Running Code challenge {cc1}")
                CC3()
                continue
                        
            elif cc1 == '4':
                print(f"You choose {cc1}")
                print(f"Running Code challenge {cc1}")
                CC4()
                continue
            
            elif cc1 == '5':
                print(f"You choose {cc1}")
                print(f"Running Code challenge {cc1}")
                CC5()
                continue
                
        elif cc == '2':
            print("Welcome to CODE CHALLANGE(6-10)")
            print("6 - CODECHALLENGE(6)\n7 - CODECHALLENGE(7)\n8 - CODECHALLENGE(8)\n9 - CODECHALLENGE(9)\n10 - CODECHALLENGE(10)")
            cc2 = input("Enter your choice: ")
            
            if cc2 == '6':
                print(f"You choose {cc2}")
                print(f"Running Code challenge {cc2}")
                CC6()
                continue
            
            elif cc1 == '7':
                print(f"You choose {cc2}")
                print(f"Running Code challenge {cc2}")
                CC7()
                continue
            
            elif cc2 == '8':
                print(f"You choose {cc2}")
                print(f"Running Code challenge {cc2}")
                CC8()
                continue
                        
            elif cc2 == '9':
                print(f"You choose {cc2}")
                print(f"Running Code challenge {cc2}")
                CC9()
                continue
            
            elif cc2 == '10':
                print(f"You choose {cc2}")
                print(f"Running Code challenge {cc2}")
                CC10()
                continue
            
        elif cc == '3':
            print("Welcome to CODE CHALLANGE(11-15)")
            print("11 - CODECHALLENGE(11)\n12 - CODECHALLENGE(12)\n13 - CODECHALLENGE(13)\n14 - CODECHALLENGE(14)\n15 - CODECHALLENGE(15)")
            cc3 = input("Enter your choice: ")
            
            if cc3 == '11':
                print(f"You choose {cc3}")
                print(f"Running Code challenge {cc3}")
                CC11()
                continue
            
            elif cc3 == '12':
                print(f"You choose {cc3}")
                print(f"Running Code challenge {cc3}")
                CC12()
                continue
            
            elif cc3 == '13':
                print(f"You choose {cc3}")
                print(f"Running Code challenge {cc3}")
                CC13()
                continue
                        
            elif cc3 == '14':
                print(f"You choose {cc3}")
                print(f"Running Code challenge {cc3}")
                CC14()
                continue
            
            elif cc3 == '15':
                print(f"You choose {cc3}")
                print(f"Running Code challenge {cc3}")
                CC15()
                continue
            
        continue
    elif choi == "C":
        print("Would you like to continue? :")
        x = input("Y - YES\nN - NO\nEnter Choice: ").upper()
        if x == 'Y':
            print("Continuing...")
            continue
        
        elif x == 'N':
            print('Thanks for using my program, Buhbyee!')
            break
        
        else:
            print("Invalid Choice")
            print("Try Again...")
            continue
