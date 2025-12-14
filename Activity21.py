#While loop

notFull = True
while notFull == True:
    more=input('Do you want to add more ? (yes or no) :').lower()
    if more == 'yes':
        print("Keep Pouring")
        continue
    elif more == 'no':
        print("Stopping...")
        print("Drink Done." \
        "")
        break
    else:
        print("Invalid")
        continue

