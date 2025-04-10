x = 1 
while x > 0 or x < 0:
    num = int(input("enter number or 0 to stop: "))
    x = num
    if num == 0 : 
        print("the number is 0")
    elif num > 0:
        print("the number is True")
    elif num < 0:
        print("the number is negative")