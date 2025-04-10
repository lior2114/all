x = True
while x:
    num1 = int(input("enter number 1: "))
    num2 = int(input("enter number 2: "))
    if num1 > num2:
        print(f"number {num1} is bigger")
    elif num2 > num1:
        print(f"number {num2} is bigger")
    if num1 == num2:
        print(f"both equal, max number is: {num1}")
        x = False