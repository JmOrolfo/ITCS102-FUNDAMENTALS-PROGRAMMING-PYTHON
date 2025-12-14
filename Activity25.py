#Program Menu

from Activity_1 import *

name = input("Enter your name : ")
print("Please Select a Program")
print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activity4\nE - Exit")

run = input("Enter which program you want to run : ").lower()

if run = "a":
  activity1()
  continue

elif run = "b":
  activity2()
  continue
  
elif run = "c":
  activity3()
  continue

elif run = "d":
  activity4()
  continue

elif run = "e":
  print("Exiting...")
  print("Thankyou :)")
  break

else:
  print("Invalid Input")



             
