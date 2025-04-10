x = 1
while x!= 0:
    x1 = int(input("enter number or 0 to quit: "))
    x = x1
    if x1 == 0:
        print("0 cant split")
    elif x1 % 7 == 0:
        print("the number can split in 7")
    else:
        print("no")