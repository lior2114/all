x1 = int(input("enter number1: "))

if x1 == 0:
    print("zero")
elif x1 < 0:
    print("its a negative number")
elif x1 <= 100 and x1 > 0: 
    print("number is between 1-100 ")
elif x1 <= 1000 and x1 >= 101: 
    print("number is between 101-1000 ")
elif x1 > 1000:
    print("number is bigger then 1000")
