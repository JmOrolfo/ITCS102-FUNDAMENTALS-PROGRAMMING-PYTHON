#Program Menu
def Activity25():
  from Activity1 import Activity1 
  from Activity2 import Activity2
  from Activity3 import Activity3
  from Activity4 import Activity4

  name = input("Enter your name : ")
  print(f"Welcome  {name}")
  print("Please Select a Program")
  print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activity4\nE - Exit")

  run = input("Enter which program you want to run : ").upper()

  if run == "A":
    Activity1()
    
  elif run == "B":
    Activity2()
    
  elif run == "C":
    Activity3() 

  elif run == "D":
    Activity4()

  elif run == "E":
    print("Exiting...")
    print("Thankyou :)")

  else:
    print("Invalid Input")
    print("-------------")
    



             
