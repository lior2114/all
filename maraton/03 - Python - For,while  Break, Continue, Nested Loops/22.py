x = 1
while x > 0:
    number = int(input("enter number: "))
    x = number
    if number == 0 or number < 0:
        break
    else:
        for i in range(number,0,-1):
            print(i,end = " ")
        print()