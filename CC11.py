def CC11():
  print("\t\t *")
  for i in range(2, 10, 1):
    for u in range(10, i, -1):
      print(" ", end=" ")
    for o in range(1, i, 1):
      print("*", end=" ")
    for a in range(1, i, 1):
      print ("*", end=" ")
    print()

  for i in range (1, 10, 1):
    for u in range(1, i, 1):
      print(" ", end=" ")
    for o in range(10, i, -1):
      print("*", end=" ")
    for a in range(10, i, -1):
      print("*", end=" ")
    print ()

  print("\t\t *")
