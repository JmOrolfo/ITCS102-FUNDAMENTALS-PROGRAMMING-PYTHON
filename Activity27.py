print('Adding anime in watchlist')

li = {}

true = True

def Print_Anime():
    for i,j in li.items():
        print(f'for Anime {j}, the key is {i}')

def Search_Anime(key):
    print('Searching...')
    print(f"result shows {li[key]} is in your watchlist.")

while true == True:
    key = input('Input anime keys :')
    tt = input('Enter anime name :')

    li[key] = tt

    choice = input('Would you like to continue adding? \nY - Yes\nN - No\nP - Print\nS - Search\nENTER: ').lower()

    if choice == 'y':
        print('has been added to your watchlist.')
        print('continuing...')
        continue

    elif choice == 'n':
        print('Exiting...')
        print('Buh-bye.')
        break
    
    elif choice == 'p':
        print('Printing.....')
        Print_Anime()
        continue
    
    elif choice == 's':
        code = input('Input the anime key.').lower()
        Search_Anime(key)
        continue
    
    else:
        print('Error')
        break
