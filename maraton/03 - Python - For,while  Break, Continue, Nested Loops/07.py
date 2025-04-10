x = 1 
while x >= 0:
    num = int(input("enter number or -number to stop: "))
    x = num
    if num == 0 : 
        print("the number is 0")
    elif num > 0:
        print(f"the number is True and its power 3 is {num**3}")
    elif num < 0:
        print(f"the number is negative and its power 3 is {num**3}")