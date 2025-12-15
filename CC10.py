def CC10():
    print("\t\t   *", end=" ")
    for u in range(1, 11, 1):
        for e in range(11, u,-1):
            print(" ", end=" ")
        for o in range(1,u,1):
                print("*" ,end=" ")
        for i in range(1, u,1):
            print("*", end=" ")

        print()
