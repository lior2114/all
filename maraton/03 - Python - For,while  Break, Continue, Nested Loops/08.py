x = 1 
while x % 7 != 0:
    num = int(input("enter number or -number to stop: "))
    x = num
    if num == 0 : 
        print("the number is 0")
    elif num > 0:
        print("the number is True")
    elif num < 0:
        print("the number is negative")