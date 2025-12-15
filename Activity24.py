#Function Def and Reuse
def Activity24():
    import greeter
    def greeter(name):
        print(f"Hello {name}, How are you ? ")

    def summation(num):
        sum = 0
        for j in range(num, 0, -1):
            sum += j 
        print(f" The summation of {num} is {sum}")

    greeter("Axel")
    greeter("Christian")
    greeter("Axel")

    summation(24)
    summation(8)
    summation(11)
    print('----------------------------------------------')



