for i in range(1,11):
  for u in range(11, i, -1):
    print(" ", end=" ")
  for o in range(i, 0, -1):
    print(o, end=" ")
  for a in range(2, i + 1):
    print(a, end=" ")
  print()
  
