x1 = int(input("enter number1: "))
x2 = int(input("enter number2: "))
x3 = int(input("enter number3: "))

if x1 >= x2 and x1 >= x3:
    print(x1)
elif x2 >= x1 and x2 >= x3:
    print(x2)
else:
    print(x3)