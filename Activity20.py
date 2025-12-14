#Looping

for i in range(1,11):
  for u in range(1, i, 1):
    print("*", end="")
  for o in range(11, i, -1):
    print("x", end="")
  print()
