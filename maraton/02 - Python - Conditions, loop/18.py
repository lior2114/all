x = 1
while x > 0 or x == 0:
    x1 = int(input("enter number or -num to quit: "))
    x = x1
    if x1 < 0:
        break
    else:
        print(x1**3)
