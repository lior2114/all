x1 = int(input("enter numer1: "))
x2 = int(input("enter numer2: "))

if x1>= x2:
    for x2 in range (x2,x1+1):
        print(x2)
else:
    for x1 in range(x1,x2+1):
        print(x1)