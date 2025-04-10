x1 = int(input("enter number1: "))
x2 = int(input("enter number2: "))
if x2 > x1:
    for x1 in range(x1,x2+1):
        print(x1)
elif x1 > x2:
    for x2 in range(x2,x1+1):
        print(x2)