counter = int(input("enter number for loop: "))
for i in range(counter):
    num1 = int(input("enter number 1: "))
    num2 = int(input("enter number 2: "))
    num3 = int(input("enter number 3: "))
    if num1 >= num2 and num1 >= num3:
        print(f"max number is: {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"max number is: {num2}")
    else:
        print(f"max number is: {num3}")